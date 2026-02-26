
import shutil
import os
import sys

def ensure_dir(path):
    os.makedirs(path, exist_ok=True)

def copy_and_replace(src, dst, replacements):
    if not os.path.exists(dst):
        shutil.copyfile(src, dst)
        # Replace placeholders in the copied file
        with open(dst, 'r', encoding='utf-8') as f:
            content = f.read()
        for key, value in replacements.items():
            content = content.replace(key, value)
        with open(dst, 'w', encoding='utf-8') as f:
            f.write(content)

def main():

    module = input("Enter the module name (use hyphens for spaces, e.g., 'asset-management'): ").strip()
    module_title = module.replace('-', ' ').title()
    version = "v1.0.0.0"

    # Template paths
    base_dir = os.path.dirname(os.path.abspath(__file__))
    module_template = os.path.join(base_dir, '../_modules/_template.md')
    table_template = os.path.join(base_dir, '../_tables/_template.md')

    # Output paths
    module_md = os.path.join(base_dir, f"../_modules/{module}.md")
    table_md = os.path.join(base_dir, f"../_tables/{module}.md")
    docs_dir = os.path.join(base_dir, f"../_docs/{module}")
    assets_module_dir = os.path.join(base_dir, f"../assets/modules/{module}")

    # Create Module overview
    thumbnail_path = f"/assets/use_cases/{module}.png"
    copy_and_replace(module_template, module_md, {
        '<Module Name>': module_title,
        '<Short description of the module>': f'Placeholder for {module_title} module.',
        '<version>': version,
        '<path-to-thumbnail>': thumbnail_path,
        '<module-slug>': module,
    })
    
    print(f"✓ Created module overview: _modules/{module}.md")

    # Create Data Model / Tables overview
    copy_and_replace(table_template, table_md, {
        '{Module Name}': module_title,
        'module-slug': module,
    })
    
    print(f"✓ Created data model file: _tables/{module}.md")

    # Create Docs and Assets directories
    ensure_dir(docs_dir)
    ensure_dir(assets_module_dir)
    
    print(f"✓ Created documentation directory: _docs/{module}/")
    print(f"✓ Created assets directory: assets/modules/{module}/")
    print(f"\n✓ Module '{module}' structure created successfully!")
    print(f"\nNext steps:")
    print(f"1. Update _modules/{module}.md with module description and ERD")
    print(f"2. Update _tables/{module}.md with table descriptions")
    print(f"3. Add module thumbnail to assets/use_cases/{module}.png")

if __name__ == "__main__":
    main()
