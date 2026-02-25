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

### Person *(Core)*
Represents requesters, approvers, system owners, technical contacts, assessors.

### Account *(Core)*
Represents vendors, cloud providers, hosting providers.

### Organization Unit *(Core)*
Departments requesting services, owning systems, providing support.

### Location *(Core)*
Physical locations for systems, hosting facilities, data centers.

### Action Item *(Core)*
Operational tasks linked to service requests, access provisioning, POAM remediation.

### Agreement *(Core)*
Service level agreements, hosting agreements, vendor contracts.

### Compliance Framework *(Core)*
NIST, FedRAMP, ISO 27001, HIPAA, PCI-DSS frameworks.

### Compliance Requirement *(Core)*
Specific control requirements for systems and entitlements.

### Legal Authority *(Core)*
Regulatory basis for system operations and compliance.

### Risk Item *(Core)*
Risks identified during assessments linked to POAM items.

### Document *(Core)*
System documentation, assessment reports, accreditation packages.

### IT Request Type
- Service Request
- Hardware Request
- Software Request
- Access Request
- Support Request
- Change Request
- Provisioning Request

### Request Item Status
- Pending
- In Progress
- Fulfilled
- Cancelled
- On Hold
- Blocked

### Access Request Type
- New Access
- Modify Access
- Remove Access
- Temporary Access
- Emergency Access
- Transfer Access

### Access Action
- Grant
- Modify
- Revoke
- Extend
- Transfer

### Entitlement Type
- System Access
- Application Role
- Data Access
- Administrative Rights
- License
- Group Membership
- API Access

### Entitlement Category
- User Access
- Administrative Access
- Service Account
- Privileged Access
- Read Only
- Read Write
- Full Control

### Access Level
- None
- Read
- Write
- Modify
- Delete
- Administrator
- Full Control

### Assignment Status
- Active
- Pending Activation
- Suspended
- Expired
- Revoked
- Under Review

### Assignment Type
- Permanent
- Temporary
- Emergency
- Project Based
- Role Based

### Review Status
- Current
- Review Required
- Under Review
- Approved
- Revoked

### Fulfillment Status
- Not Started
- In Progress
- Partially Fulfilled
- Fulfilled
- Cancelled

### Catalog Item Category
- Hardware
- Software
- Access
- Licenses
- Services
- Infrastructure
- Cloud Resources
- Support

### Catalog Item Type
- Orderable Item
- Service Offering
- Access Entitlement
- Provisioning Package
- Consultation Service

### Technology Relationship
- Required Technology
- Delivered Technology
- Approved Technology
- Restricted Technology
- Alternative Technology

### System Type
- Business Application
- Infrastructure System
- Platform Service
- Data System
- Security System
- Communications System
- Development Tool
- Enterprise System

### Component Category
- Application
- Database
- API
- Interface
- Middleware
- Infrastructure
- Network
- Storage

### Technology Role
- Operating System
- Database Platform
- Application Framework
- Development Tool
- Runtime Environment
- Integration Tool
- Security Tool
- Monitoring Tool

### Technology Status
- Approved
- Evaluation
- Deprecated
- Restricted
- End of Life
- Not Approved

### License Type
- Commercial
- Open Source
- Proprietary
- Subscription
- Perpetual
- Freeware
- Government License

### Hosting Type
- On Premises
- Co-Location
- Public Cloud
- Private Cloud
- Hybrid Cloud
- Managed Hosting
- Software as a Service

### Environment Type
- Production
- Development
- Test
- Staging
- Quality Assurance
- Training
- Sandbox
- Disaster Recovery

### Accreditation Type
- Authority to Operate (ATO)
- Interim Authority to Operate
- Interim Authority to Test
- Provisional Authorization
- Certification
- Self Assessment

### Accreditation Status
- Not Started
- In Progress
- Accredited
- Conditionally Accredited
- Denied
- Expired
- Under Review

### Assessment Type
- Security Assessment
- Compliance Audit
- Vulnerability Assessment
- Penetration Test
- Architecture Review
- Code Review
- Configuration Review
- Annual Review

### Assessment Status
- Planned
- In Progress
- Completed
- Under Review
- Approved
- Remediation Required

### Finding Type
- Security Control Gap
- Policy Violation
- Configuration Issue
- Vulnerability
- Process Deficiency
- Documentation Gap
- Architecture Issue

### Mitigation Status
- Not Started
- In Progress
- Risk Accepted
- Completed
- Verified
- Cancelled
