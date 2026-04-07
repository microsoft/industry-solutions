---
title: "IT Service Management Data Model"
module: it-service-management
---

The **IT Service Management (Lite) / IT System Catalog** module provides a structured framework for managing IT service offerings, access control, system inventory, technology standards, and compliance oversight in a unified model. It supports core operational use cases such as submitting and fulfilling service requests, processing access requests and entitlement assignments, publishing orderable IT catalog items, and tracking hosting environments. At the same time, it enables governance scenarios including documenting system components and technology stacks, managing compliance assessments and system accreditations, and tracking remediation activities through POAM items. The module is designed to balance day-to-day service delivery with architectural visibility and security oversight, making it suitable for both public sector and commercial organizations that need lightweight ITSM capabilities combined with structured system and technology governance.


## Tables

### IT Service Request
Represents a general service transaction submitted by a user for IT support, provisioning, hardware, software, or other service needs. Parent record for request items.

### IT Service Request Item
A line-level record under an IT Service Request that references a specific IT Catalog Item or fulfillment action.

### IT Access Request
Represents a request submitted to obtain, modify, or remove access to systems, applications, data, or other secured resources. Serves as the parent transaction record for access-related actions.

### IT Access Request Item
A line-level record under an IT Access Request specifying the individual entitlement, system, or role being requested. Allows a single request to contain multiple access changes.

### IT Entitlement
Defines a specific access right, permission set, license assignment, or role that can be granted to a user or system account.

### IT Entitlement Assignment
Represents the assignment of an IT Entitlement to a person, account, or system. Tracks who has what access and its lifecycle status.

### IT Catalog Item
Defines an orderable IT offering. Represents a published service, product package, provisioning action, or access offering that users can request.

### IT Catalog Item Technology
A junction table linking an IT Catalog Item to one or more IT Technologies. Identifies technologies that are required, delivered, approved, or restricted for that offering.

### IT System
Represents a logical or operational information system. Serves as the primary record for tracking ownership, purpose, lifecycle status, and governance attributes.

### IT System Component
Represents a structural part of an IT System, such as an application module, service, database, infrastructure element, or interface.

### IT System Component Type
Defines categories or classifications of system components (e.g., Application, Database, API, Infrastructure, Interface).

### IT System Technology
A junction table linking an IT System (or optionally a specific System Component) to the IT Technologies it uses. Tracks technology usage and version information.

### IT Technology
Represents a technology concept, platform, framework, protocol, runtime, standard, or tool used within IT systems.

### IT Technology Type
Defines classification categories for IT Technologies (e.g., Operating System, Database Engine, Framework, Protocol, Security Standard).

### IT Hosting Location
Represents the physical or logical hosting environment for a system or component, such as a data center, cloud region, or managed hosting facility.

### IT System Accreditation
Represents the formal authorization or approval status of an IT System to operate within defined security and compliance parameters.

### IT Compliance Assessment
Represents a formal evaluation of a system, component, or technology against defined standards, policies, or regulatory requirements. May generate findings or POAM items.

### IT POAM Item
Plan of Action and Milestones (POAM) record used to track remediation of identified compliance findings, vulnerabilities, or control gaps.
