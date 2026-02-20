---
title: "Asset Management Data Model"
module: asset-management
---

### Asset
Individual, accountable item instance. Stores identifying details, current status/condition, links to Product, Asset Type, ownership, assignment, and lifecycle records.

### Asset Type
Operational classification of assets (e.g., Laptop, Vehicle, Generator). Used for reporting, inspection requirements, and grouping.

### Asset Category
Higher-level grouping of Asset Types (e.g., IT Equipment, Fleet, Facilities Equipment). Useful for roll-up reporting and policy alignment.

### Product
Standardized product definition (manufacturer/model-level reference) that assets can reference for consistency across modules.

### Asset Acquisition
Represents the acquisition event for one or more assets (purchase, lease, donation, transfer-in). Captures supplier, acquisition type, funding, and financial context.

### Asset Cost Entry
Additional capital or operational costs associated with an asset (repairs, upgrades, improvements, reconditioning, etc.) for total cost tracking.

### Asset Owner
Tracks legal or financial ownership of the asset over time (e.g., owned, leased, externally owned). Supports ownership history with effective dates.

### Asset Assignment
Tracks custody or responsibility for the asset over time (assigned to a person, organization unit, or team). Includes start and end dates.

### Asset Custody Event
Timeline-based record of significant custody or control changes (assign, return, move, transfer, retire, dispose). Provides an auditable history of asset movement and responsibility.

### Location
Reference table for physical places where assets may reside (site, building, room, storage area, etc.).

### Organization Unit
Organizational structure entity (department, division, program, team) used for ownership, assignment, reporting, and accountability.

### Person
Individual record used for asset assignment, responsibility tracking, or audit verification.

### Asset Service Record
Lightweight maintenance/service log entry for an asset. Captures service date, service type, provider, cost, and notes.

### Asset Service Type
Reference list defining types of service events (Preventive, Repair, Inspection, Upgrade, Calibration, etc.).

### Asset Audit
Represents an audit cycle or inventory verification event (e.g., Annual Inventory Count). Defines scope, dates, and status.

### Asset Audit Item
Asset-level audit result within an Asset Audit. Records expected vs observed data, verification status, and findings.

### Asset Inspection Requirement
Defines recurring inspection rules that apply to an Asset Type or specific Asset. Includes frequency and regulatory reference.

### Asset Disposition
Captures retirement and disposal details for an asset, including retirement reason, disposal method, dates, approvals, and recipient (if applicable).
