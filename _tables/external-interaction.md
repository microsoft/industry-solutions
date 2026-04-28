---
title: "External Interaction Data Model"
module: external-interaction
---

The External Interaction data model provides structured tracking of incoming communications and engagements from external parties across multiple contact channels. It supports reference data for topic categorization and source attribution, detailed contact information capture, internal routing and assignment workflows, progress tracking, and resolution management with integrated activity timelines.

## Tables

### External Interaction
Represents a single incoming communication or engagement from an external party. Captures reference numbers, received date and time, contact information (name, phones, emails, address), method of contact, topic and source classifications, interaction type, priority, action status, due dates (first response and resolution), detailed descriptions, progress notes, resolution notes, and relationships to Person, Queue, and related activities.

### External Interaction Topic
Categorizes external interactions by subject matter or inquiry type. Supports hierarchical parent-child topic relationships enabling detailed subject taxonomies for improved routing, reporting, and knowledge management.

### External Interaction Source
Documents originating channels, programs, referral organizations, or intake mechanisms that generate external interactions. Used for source attribution, trend analysis, and partnership tracking.

### Queue
Standard Dataverse entity representing team-based work queues for routing and distributing external interactions to specialized departments, subject matter experts, or geographic service teams.

### Queue Item
Standard Dataverse entity linking external interactions to specific queues for workload distribution and team-based assignment workflows.

### Person
Core module entity (Contact) representing individuals who submit external interactions. Enables persistent relationship tracking, contact history views, and constituent management when the submitter is a known contact.

### Country
Core module reference entity for standardizing country values in external interaction mailing addresses.

### State or Province
Core module reference entity for standardizing state or province values in external interaction mailing addresses, linked to countries.