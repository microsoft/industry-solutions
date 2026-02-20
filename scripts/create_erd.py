import os
import xml.etree.ElementTree as ET
from collections import defaultdict
from urllib.parse import quote
import sys


def encode_url(url):
    return quote(url, safe=":/?&=")  # Keeping some characters safe from encoding


def parse_filename(filename):
    parts = filename.split(" - ")
    if len(parts) != 2:
        return None, None

    module_name = parts[0].replace("Gov-CDM-", "")
    version = parts[1].replace(".zip", "").replace("_managed", "")

    return module_name, version


def read_releases(folder_path: str):
    """Read all filenames from the folder and group by version"""
    if not os.path.exists(folder_path):
        return [], {}
    
    file_names = [f for f in os.listdir(folder_path) if f.endswith(".zip")]
    version_dict = defaultdict(list)

    for file_name in file_names:
        module_name, version = parse_filename(file_name)
        if module_name and version:
            version_dict[version].append(file_name)

    releases = sorted(version_dict.keys(), key=lambda x: list(map(int, x.split("."))), reverse=True)
    return releases, version_dict


def to_sentence_case(input_string):
    if not input_string:
        return ""
    return input_string[0].upper() + input_string[1:].lower()


def get_available_modules():
    """Get list of available modules from the industry-apps sibling repo"""
    modules = []
    
    # Get current script directory and navigate to sibling repo
    current_dir = os.path.dirname(os.path.abspath(__file__))
    sibling_repo = os.path.join(os.path.dirname(current_dir), "..", "industry-apps")
    
    if not os.path.exists(sibling_repo):
        return modules
    
    # Recursively search through category folders for modules
    # Skip special folders that start with . or are known non-category folders
    skip_folders = {'.config', '.design', '.git', '.gitignore', '.scripts', '.vscode', 
                    'bin', 'obj', 'deployment-ui', 'shared'}
    
    for category_name in os.listdir(sibling_repo):
        category_path = os.path.join(sibling_repo, category_name)
        
        # Skip if not a directory or in skip list
        if not os.path.isdir(category_path) or category_name in skip_folders:
            continue
        
        # Look for modules in this category folder
        for module_name in os.listdir(category_path):
            module_path = os.path.join(category_path, module_name)
            
            # Verify it's a valid module by checking for src/Entities folder
            if os.path.isdir(module_path):
                entities_path = os.path.join(module_path, "src", "Entities")
                if os.path.exists(entities_path):
                    # Store as (category/module_name, module_name) for easy lookup
                    relative_path = os.path.join(category_name, module_name)
                    modules.append((relative_path, module_name))
    
    return modules


def get_module_path(relative_path, module_name):
    """Get the full path to a module in the industry-apps repo
    
    Args:
        relative_path: The relative path from industry-apps root (e.g., 'operations/asset-management')
        module_name: The module name (kept for compatibility)
    """
    current_dir = os.path.dirname(os.path.abspath(__file__))
    sibling_repo = os.path.join(os.path.dirname(current_dir), "..", "industry-apps")
    return os.path.join(sibling_repo, relative_path)


def read_entities(relative_path: str, module_name: str):
    """Read entities from the specified module"""
    tables = []

    exclude_fields = [
        "CreatedBy",
        "CreatedOn",
        "CreatedOnBehalfBy",
        "ImportSequenceNumber",
        "ModifiedBy",
        "ModifiedOn",
        "ModifiedOnBehalfBy",
        "OverriddenCreatedOn",
        "OwnerId",
        "OwningBusinessUnit",
        "OwningTeam",
        "OwningUser",
        "statecode",
        "statuscode",
        "TimeZoneRuleVersionNumber",
        "UTCConversionTimeZoneCode",
    ]

    # Get path to the module in industry-apps repo
    module_path = get_module_path(relative_path, module_name)
    entities_folder = os.path.join(module_path, "src", "Entities")

    if not os.path.exists(entities_folder):
        print(f"Warning: Entities folder not found at {entities_folder}")
        return tables

    # Iterate through each entity folder in the Entities directory
    for entity_folder in os.listdir(entities_folder):
        table = {"schema_name": "", "fields": []}

        # Construct the path to the Entity.xml file within each entity folder
        entity_xml_path = os.path.join(entities_folder, entity_folder, "Entity.xml")

        # Make sure the file exists before trying to open it
        if not os.path.exists(entity_xml_path):
            continue

        try:
            with open(entity_xml_path, "r", encoding="utf-8") as file:
                entity_xml_content = file.read()

            # Parse the XML content
            root = ET.fromstring(entity_xml_content)

            # Find entity name
            entity_name_tag = root.find(".//Name")
            if entity_name_tag is not None:
                entity_display_name = entity_name_tag.get("LocalizedName")
                entity_name = entity_name_tag.text

                table["schema_name"] = entity_name
                table["display_name"] = entity_display_name

            fields = []
            # Iterate through all 'attribute' elements
            for attribute in root.findall(".//attribute"):
                field = {}

                physical_name = attribute.attrib.get("PhysicalName", "")

                if physical_name in exclude_fields:
                    continue

                field["schema_name"] = physical_name

                # Get the Type information
                type_element = attribute.find("./Type")
                if type_element is not None:
                    field_type = type_element.text

                    if field_type == "primarykey":
                        continue

                    field["dataverse_type"] = to_sentence_case(field_type)

                # Get the displayname description
                displayname_element = attribute.find("./displaynames/displayname")
                if displayname_element is not None:
                    description = displayname_element.attrib.get("description", "")
                    field["display_name"] = description

                # Add the field to the 'fields' list
                fields.append(field)

            table["fields"] = fields
            tables.append(table)

        except Exception as e:
            print(f"Error processing {entity_xml_path}: {e}")
            continue

    return tables


def read_relationships(entity_name, relationships_folder):
    """Function to read relationships for a given entity"""
    relationship_file_path = os.path.join(relationships_folder, f"{entity_name}.xml")

    relationships = []

    if not os.path.exists(relationship_file_path):
        return relationships

    try:
        tree = ET.parse(relationship_file_path)
        root = tree.getroot()

        for relationship in root.findall("EntityRelationship"):
            rel_type = relationship.find("EntityRelationshipType").text
            ref_entity = relationship.find("ReferencingEntityName").text
            refd_entity = relationship.find("ReferencedEntityName").text
            ref_attribute = relationship.find("ReferencingAttributeName").text

            relationships.append(
                {
                    "Type": rel_type,
                    "from": ref_entity,
                    "to": refd_entity,
                }
            )
    except Exception as e:
        print(f"Error processing relationship file {relationship_file_path}: {e}")

    return relationships


def read_all_relationships(relative_path: str, module_name: str):
    """Read all relationships for the specified module"""
    module_path = get_module_path(relative_path, module_name)
    source_folder = os.path.join(module_path, "src", "Other", "Relationships")

    all_relationships = []
    
    if not os.path.exists(source_folder):
        print(f"Warning: Relationships folder not found at {source_folder}")
        return all_relationships

    # Iterate through each XML file in the Relationships folder
    for entity_file in os.listdir(source_folder):
        if entity_file.endswith(".xml"):
            entity_name = os.path.splitext(entity_file)[0]  # Remove '.xml' extension
            relationships = read_relationships(entity_name, source_folder)
            all_relationships.extend(relationships)

    return all_relationships


def render_mermaid(tables: list, relationships: list):
    """Render Mermaid diagram from tables and relationships"""
    mermaid_str = "graph TD\n"

    # Add tables (nodes)
    for table in tables:
        schema_name = table["schema_name"]
        display_name = table["display_name"]
        mermaid_str += f"  {schema_name}({display_name})\n"

    render_relationships = [
        rel for rel in relationships if rel["to"] not in ["Owner", "SystemUser", "Team", "BusinessUnit"]
    ]

    # Add relationships (edges)
    for rel in render_relationships:
        source = rel["from"]
        target = rel["to"]
        mermaid_str += f"  {source} --> {target}\n"

    return mermaid_str


def get_output_path(module_name: str):
    """Get the output path for the markdown file in the .temp folder"""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.dirname(current_dir)
    
    # Convert module name to match the naming convention
    # Replace underscores and convert to lowercase with hyphens
    file_name = module_name.lower().replace("_", "-").replace(" ", "-")
    
    # Output to .temp folder for review before updating module documentation
    return os.path.join(repo_root, ".temp", f"erd-{file_name}.md")


def document_module(relative_path: str, module_name: str):
    """Generate documentation for the specified module"""
    print(f"Processing module: {module_name} (from {relative_path})")
    
    tables = read_entities(relative_path, module_name)
    relationships = read_all_relationships(relative_path, module_name)

    print(f"Found {len(tables)} entities and {len(relationships)} relationships")

    # Convert module name for display (replace hyphens with spaces and title case)
    display_name = module_name.replace("-", " ").title()
    
    markdown = f"# {display_name} - Entity Relationship Diagram\n"
    markdown += "---\n\n"

    markdown += "## Entity Relationship Diagram\n"
    markdown += "---\n\n"
    mermaid = render_mermaid(tables, relationships)
    markdown += f"```mermaid\n{mermaid}```\n\n"

    for table in tables:
        markdown += "\n"
        markdown += "## " + table["display_name"] + "\n"
        markdown += "---\n\n"
        markdown += "**Metadata**\n\n"
        markdown += "- Schema: " + table["schema_name"] + "\n\n"
        markdown += "**Custom Fields**\n\n"

        sorted_fields = sorted(table["fields"], key=lambda x: x.get("display_name", ""))
        for field in sorted_fields:
            markdown += "- " + field.get("display_name", "N/A") + "\n"
            markdown += "  - Type: " + field.get("dataverse_type", "N/A") + "\n"
            markdown += "  - Schema: " + field["schema_name"] + "\n"

    # Save to the .temp folder in industry-solutions repo
    output_path = get_output_path(module_name)
    
    # Ensure the directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(markdown)
        print(f"\n✓ Generated documentation saved to: {output_path}")
        print(f"Review the ERD diagram and use it to update the module's documentation in _modules/")


def get_modules_by_category(category_name):
    """Get modules from a specific category folder"""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    sibling_repo = os.path.join(os.path.dirname(current_dir), "..", "industry-apps")
    
    category_path = os.path.join(sibling_repo, category_name)
    modules = []
    
    if os.path.exists(category_path):
        for module_name in os.listdir(category_path):
            module_path = os.path.join(category_path, module_name)
            if os.path.isdir(module_path):
                # Verify it has the expected structure
                entities_path = os.path.join(module_path, "src", "Entities")
                if os.path.exists(entities_path):
                    modules.append((os.path.join(category_name, module_name), module_name))
    
    return sorted(modules, key=lambda x: x[1])


def main():
    """Main function to handle user input and module selection"""
    print("Industry Apps ERD Documentation Generator")
    print("=" * 55)
    
    # Get available modules
    available_modules = get_available_modules()
    
    if not available_modules:
        print("No modules found in the industry-apps repository.")
        print("Make sure the industry-apps repository exists as a sibling to this repository.")
        return
    
    # Check for command line argument
    if len(sys.argv) > 1:
        module_arg = sys.argv[1].lower().replace("_", "-").replace(" ", "-")
        
        # Find matching module
        for relative_path, module_name in available_modules:
            if module_name.lower().replace("_", "-").replace(" ", "-") == module_arg:
                document_module(relative_path, module_name)
                return
        
        print(f"Module '{sys.argv[1]}' not found.")
        print("Available modules:")
        for i, (relative_path, module_name) in enumerate(available_modules, 1):
            category = relative_path.split(os.sep)[0]
            print(f"  {i}. {module_name} (from {category})")
        return
    
    # Interactive mode - get all categories
    categories = {}
    for relative_path, module_name in available_modules:
        category = relative_path.split(os.sep)[0]
        if category not in categories:
            categories[category] = []
        categories[category].append((relative_path, module_name))
    
    category_list = sorted(categories.keys())
    
    # Show category selection
    print("\nSelect a category:")
    for i, category in enumerate(category_list, 1):
        count = len(categories[category])
        print(f"  {i}. {category.replace('-', ' ').title()} ({count} modules)")
    print("  0. Exit")
    
    while True:
        try:
            type_choice = input(f"\nSelect category (1-{len(category_list)}) or 0 to exit: ").strip()
            
            if type_choice == "0":
                print("Exiting...")
                return
            
            choice_num = int(type_choice)
            if 1 <= choice_num <= len(category_list):
                selected_category = category_list[choice_num - 1]
                break
            else:
                print(f"Please enter a number between 1 and {len(category_list)}, or 0 to exit.")
        except ValueError:
            print("Please enter a valid number.")
        except KeyboardInterrupt:
            print("\nExiting...")
            return
    
    # Get modules for selected category
    modules = categories[selected_category]
    
    # Show modules for selected category
    print(f"\nAvailable modules in {selected_category.replace('-', ' ').title()}:")
    for i, (relative_path, module_name) in enumerate(modules, 1):
        print(f"  {i}. {module_name}")
    
    print(f"  0. Back to category selection")
    
    while True:
        try:
            choice = input(f"\nSelect a module (1-{len(modules)}) or 0 to go back: ").strip()
            
            if choice == "0":
                # Restart the main function to go back to category selection
                main()
                return
            
            choice_num = int(choice)
            if 1 <= choice_num <= len(modules):
                relative_path, module_name = modules[choice_num - 1]
                document_module(relative_path, module_name)
                break
            else:
                print(f"Please enter a number between 1 and {len(modules)}, or 0 to go back.")
        
        except ValueError:
            print("Please enter a valid number.")
        except KeyboardInterrupt:
            print("\nExiting...")
            return


if __name__ == "__main__":
    main()
