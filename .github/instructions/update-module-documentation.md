# Update Module Documentation

This guide provides a complete workflow for creating or updating module documentation, including ERD diagrams, table definitions, and narrative sections.

## Context

- The module provides primarily data entry forms and views (not automation/workflows)
- Table definitions are available in `_tables/[module-name].md`
- The module overview and ERD diagram are already complete
- Use passive voice and "can" phrasing (e.g., "records can document...")

## Structure

Structure the narrative in 3-5 paragraphs following this pattern:

### 1. Foundational Reference Data (Paragraph 1)
Start with: "The module provides forms and views to capture [domain] information throughout the complete lifecycle from [start] through [end]. Foundational reference data is established using..."

Describe the reference tables that provide standardization:
- Categories and Types for classification
- Locations and Organization Units for placement
- Products or other standard reference data
- Any other lookup/classification tables

### 2. Core Records Creation (Paragraph 2)
Describe how primary records are created and what information they capture:
- Main acquisition/initiation records
- Core entity records (the central hub)
- Initial data capture and identification
- Links to reference data

### 3. Operational Tracking (Paragraphs 3-4)
Describe the ongoing operational data entry:
- Assignment and ownership tracking
- Status changes and custody events
- Service, maintenance, or activity records
- Related transactions or events

### 4. Specialized/Compliance Records (Final Paragraph)
Describe specialized tracking for compliance, verification, or lifecycle completion:
- Audit and inspection records
- Compliance requirements
- Additional cost or financial tracking
- Disposition/closure records

## Tone & Style Guidelines

- **Use passive constructions**: "can be captured," "can document," "provides visibility"
- **Bold table names** on first mention: **Asset**, **Asset Owner**
- **Focus on capabilities**, not step-by-step instructions
- **Emphasize**: data organization, audit trails, standardization, and visibility
- **Keep paragraphs flowing** naturally without numbered lists
- **Avoid**: "users create," "agencies enter," "the system does"
- **Prefer**: "records can document," "forms capture," "the module provides"

## Example: Asset Management Module

The module provides forms and views to capture asset information throughout the complete lifecycle from planning through disposal. Foundational reference data is established using **Asset Categories** and **Asset Types** to classify assets (e.g., IT Equipment > Laptops), **Products** to capture standard manufacturer and model information, and **Locations** and **Organization Units** to document where assets reside and which departments hold responsibility.

When assets are procured, **Asset Acquisition** records can document procurement details, supplier information, and funding context. Individual **Asset** records capture identifying details such as serial numbers, asset tags, condition status, and links to Product and Asset Type information, along with initial cost data.

The module provides separate forms to capture legal ownership and operational custody. **Asset Owner** records can document legal or financial ownership (owned, leased, borrowed), while **Asset Assignment** records track operational custody when assets are issued to individuals or organizational units, including expected return dates. **Asset Custody Events** can maintain an auditable timeline of custody changes, transfers, and movements.

Throughout the asset's operational life, **Asset Service Records** can build a service history by referencing predefined **Asset Service Types** (Preventive Maintenance, Repair, Inspection, Upgrade), supporting maintenance planning and operational decision-making. **Asset Inspection Requirements** can be defined to document recurring compliance requirements linked to Asset Types or specific assets.

The module supports periodic verification through **Asset Audit** records for inventory validation cycles, with **Asset Audit Items** documenting expected versus observed conditions at the asset level. Additional costs beyond initial acquisition—such as repairs, upgrades, or improvements—can be captured through **Asset Cost Entry** records for comprehensive total cost of ownership visibility.

When assets reach end-of-life, **Asset Disposition** records can document retirement reason, disposal method, required approvals, and recipient information, providing a complete audit trail from acquisition through disposal.

## Usage Prompt

When you need to generate or update documentation for a module (new or existing), use this prompt:

```
Please update the documentation for the [MODULE NAME] module following the template in .github/instructions/update-module-documentation.md.

This module [already exists in industry-solutions / is new and needs to be created].

Steps to complete:
0. If module is new, create initial structure using templates or create_module.py script
1. Run scripts/create_erd.py for [module-name] to generate the latest ERD and table information
2. Update _modules/[module-name].md with the latest ERD mermaid diagram
3. Compare the generated table list with _tables/[module-name].md and identify any new tables
4. Add descriptions for any new tables to _tables/[module-name].md
5. Write or update the "Using the Module" narrative section in _modules/[module-name].md

Follow the tone and style guidelines in the template, using passive voice and "can" phrasing throughout.
```

## Detailed Workflow for Agents

When asked to update module documentation, follow these steps:

### Step 0: Check if Module Exists in Documentation
1. Check if `_modules/[module-name].md` exists
2. Check if `_tables/[module-name].md` exists
3. If **either file is missing**, create the module structure first:
   - For new modules: Run `python scripts/create_module.py` interactively, OR
   - Manually create files from templates in `_modules/_template.md` and `_tables/_template.md`
   - Update front matter with appropriate values:
     - `title`: Proper title case (e.g., "Asset Management")
     - `description`: One-sentence summary of the module
     - `latest_release`: Set to "v1.0.0.0" or appropriate version
     - `thumbnail`: Set to `/assets/modules/[module-name].png`
     - `required_modules`: List any dependencies (usually includes "core")
     - `published`: Set to `false` until ready to publish
4. If **both files exist**, proceed to Step 1

#### Front Matter Cross-References

Module documentation uses several front matter fields to establish relationships with other content. These fields enable bidirectional navigation through the related-items.html include.

**Required Fields:**
- `required_modules`: List module dependencies (slug format, e.g., "core", "asset-management")
  - Most modules depend on "core" which provides foundational entities (Organization Unit, Location, Legal Authority, etc.)
  - Only the "core" module itself should omit this field
  - Example: `required_modules: - core`

- `required_data_models`: List the data model slug(s) for this module
  - Typically matches the module slug itself
  - Example: `required_data_models: - asset-management`

**Optional Relationship Fields:**
- `related_use_cases`: List relevant use case slugs from `_use_cases/` directory
  - Review available use cases: `_use_cases/` folder
  - Match module functionality to use case scenarios
  - Example: `related_use_cases: - asset-management`

- `related_personas`: List relevant persona slugs from `_personas/` directory
  - Review available personas: `_personas/` folder
  - Identify which roles would use this module
  - Example: `related_personas: - chief-information-officer`

- `related_modules`: List related non-dependency modules (complementary functionality)
  - Use for modules that integrate with but don't depend on each other
  - Example: `related_modules: - case-management`

- `related_portals`: List relevant portal slugs from `_portals/` directory
  - Use when the module is accessed through specific portals
  - Example: `related_portals: - core`

**How to Identify Relationships:**
1. Review `_use_cases/` directory to find matching scenarios
2. Review `_personas/` directory to identify relevant job roles
3. Consider the module's domain and who would use it
4. Add cross-references that enable useful navigation for readers

**Example Front Matter with Cross-References:**
```yaml
---
title: "Asset Management"
description: "Track, categorize, and manage organizational assets with a modern, reusable solution for accountability and lifecycle management."
latest_release: v1.0.0.4
thumbnail: /assets/use_cases/asset-management.png
required_modules:
 - core
required_data_models:
  - asset-management
related_use_cases:
  - asset-management
related_personas:
  - chief-information-officer
---
```

### Step 1: Generate Latest ERD and Table Information
Run the ERD generation script:
```bash
python scripts/create_erd.py [module-name]
```

This will create `.temp/erd-[module-name].md` with:
- Current ERD mermaid diagram
- Complete list of tables with their display names and fields

**Note**: The script searches industry-apps repository by module name across all categories (operations, administrative, financial, etc.). If the module isn't found, verify it exists in industry-apps first.

### Step 2: Update ERD Diagram in Module Overview
1. Read the mermaid diagram from `.temp/erd-[module-name].md`
2. Replace the existing mermaid diagram in `_modules/[module-name].md` with the updated version
3. Ensure the diagram is properly formatted with backticks

### Step 3: Identify New Tables
1. Extract the table list from `.temp/erd-[module-name].md` (look for "## [Table Name]" sections)
2. Read the existing table descriptions from `_tables/[module-name].md`
3. Compare the lists to identify:
   - New tables that need descriptions
   - Removed tables (if any)
   - Tables that already have descriptions

### Step 4: Update Tables Collection
For each new table identified:
1. Add a new `### [Table Name]` section to `_tables/[module-name].md`
2. Write a concise description (1-2 sentences) based on the table's fields and purpose
3. Maintain alphabetical or logical grouping order
4. Use the style: "Describes what the table tracks/manages/documents and its primary purpose."

### Step 5: Write or Update Module Narrative
Using the table information and following the structure guidelines:
1. Review all tables to understand the complete lifecycle
2. Identify the core hub (primary entity)
3. Group tables into categories: reference data, core records, operational tracking, compliance
4. **Present in chronological order**: From setup/reference data through transactional use to completion/disposal
5. **For new modules**: Write an introductory paragraph (before "Using the Module") that:
   - Describes what the module provides (structured way to...)
   - Lists key capabilities (capturing, maintaining, tracking...)
   - Includes typical use cases (2-5 examples)
6. Write 3-5 flowing paragraphs for the "Using the Module" section following the pattern described above
7. Bold table names on first mention
8. Use passive voice and "can" phrasing

### Step 6: Review and Finalize
1. Ensure the ERD diagram renders correctly
2. Verify all table descriptions are present and accurate
3. Check that the narrative flows naturally and covers all major table groups
4. Confirm tone and style match the guidelines

### Expected Outcome

After completing this workflow, the module should have:
- ✓ `_modules/[module-name].md` with:
  - Complete front matter
  - Introductory paragraph (what the module provides + use cases)
  - "Using the Module" section with flowing narrative
  - Current ERD mermaid diagram
- ✓ `_tables/[module-name].md` with:
  - Brief introduction to the data model
  - Description for every table (### heading format)
- ✓ `.temp/erd-[module-name].md` (can be deleted after review)

The documentation should be ready for review and publishing (set `published: true` when ready).
