# Module Narrative Generation Template

This template provides guidance for writing "Using the Module" narrative sections for module documentation.

## Context

- The module provides primarily data entry forms and views (not automation/workflows yet)
- Table definitions are available in `_tables/[module-name].md`
- The module overview and ERD diagram are already complete in the module overview file

## Instructions

1. Review the tables in the table definition file and generate a narrative that shows how the various tables are used by end end users, in rough chronological order - from setup to transactional use.
2. Focus on how admins and users would actually use the tables, assuming they are interacting with them through forms in the app. Use phrases like "Users can" or "Admins can".
2. Place this narrative into section called "What's Included" after the module overview and before the ERD.

## Tone & Style Guidelines

- **Bold table names** on first mention: **Asset**, **Asset Owner**
- **Focus on capabilities**, not step-by-step instructions
- **Keep paragraphs flowing** naturally without numbered lists