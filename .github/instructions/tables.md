---
applyTo: '_tables/*.md'
---

# Overview

This overall project is a Jekyll documentation site for  Power Platform and Dynamics 365 Dataverse solutions designed for industry scenarios.

Tables are a Jekyll collection and are parented virtually by another Jekyll collection, Modules, through the parent key in the table's front matter.

Each table should have a front matter metadata of title, description, and parent. The description is a very brief teaser of what the table is for. The parent is the parent data model to which the table belongs.

Each table page has a markdown table of fields, including the Field Name, Type, and Schema Name.

For table front matter descriptions, be briefly describe the purpose and usage of each table. Format the description in quotes.