# ERD Documentation Generator

This script generates ERD (Entity Relationship Diagram) documentation for industry solution modules by reading Dataverse solution files from the sibling `industry-apps` repository.

## Prerequisites

- The `industry-apps` repository should be located as a sibling to this repository
- Python 3.x with xml.etree.ElementTree support (standard library)

## Repository Structure Expected

```
parent-folder/
├── industry-solutions/      (this repository)
│   ├── scripts/
│   │   └── create_erd.py
│   ├── .temp/               (output location)
│   ├── _modules/            (module overview pages)
│   └── _tables/             (data model descriptions)
└── industry-apps/           (sibling repository)
    ├── operations/          (operations category)
    │   ├── asset-management/
    │   ├── facilities-management/
    │   └── ...
    ├── administrative/      (administrative category)
    ├── financial/           (financial category)
    ├── compliance-security/ (compliance & security category)
    └── workforce/           (workforce category)
```

## Usage

### Command Line Mode

Generate ERD documentation for a specific module:

```bash
python scripts/create_erd.py <module-name>
```

Examples:
```bash
python scripts/create_erd.py asset-management
python scripts/create_erd.py facilities-management  
python scripts/create_erd.py case-management
```

### Interactive Mode

Run without arguments for an interactive selection process:

```bash
python scripts/create_erd.py
```

The interactive mode provides:
1. **Category Selection**: Choose between Operations, Administrative, Financial, Workforce, etc.
2. **Module Selection**: Browse modules within the selected category
3. **Navigation**: Go back to category selection or exit at any time

## Output

The script generates markdown files in the `.temp/` directory with the naming pattern `erd-{module-name}.md`. Each file includes:

- Entity Relationship Diagram (Mermaid format)
- Detailed entity documentation with fields and metadata

## Features

- **Automatic Discovery**: Scans all category folders in the industry-apps repository
- **Interactive Selection**: Two-stage selection (category, then specific module)
- **Error Handling**: Gracefully handles missing files and parsing errors
- **Cross-Repository**: Reads from sibling repo, outputs to current repo's .temp folder
- **Flexible Naming**: Handles various module naming conventions
- **Safe Output**: Generates files in .temp directory for review before updating module documentation

## Error Handling

The script includes robust error handling for:
- Missing sibling repository
- Missing module folders
- Corrupted XML files
- Missing entity or relationship files

Warnings and errors are displayed to help diagnose issues.

## Workflow

1. **Generate ERD**: Run the script to create ERD documentation in the `.temp/` folder
2. **Review Output**: Check the generated Mermaid diagram and entity list in `.temp/erd-{module-name}.md`
3. **Update Module**: Copy the ERD diagram to `_modules/{module-name}.md`
4. **Update Data Model**: Manually maintain table descriptions in `_tables/{module-name}.md`
5. **Clean Up**: Remove files from `.temp/` once incorporated

This workflow ensures you maintain control over what gets updated in your module documentation files while using the script to generate accurate ERD diagrams from the solution metadata.

## Related Documentation

For guidance on creating or updating complete module documentation, see [.github/instructions/update-module-documentation.md](../.github/instructions/update-module-documentation.md).
