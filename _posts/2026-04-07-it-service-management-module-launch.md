---
layout: post
title: "IT Service Management Module Now Available"
date: 2026-04-07
tags: [modules, releases]
---

We're excited to announce the **IT Service Management** module — a lightweight ITSM framework for managing service delivery, access control, system inventory, technology standards, and compliance oversight.

## What is the IT Service Management Module?

The IT Service Management module provides a unified framework for managing IT operations, balancing day-to-day service delivery with architectural visibility and security governance. It enables organizations to process service and access requests through a structured catalog, maintain comprehensive system and technology inventories, track entitlement assignments and access lifecycles, manage compliance assessments and system accreditations, and document technology usage and hosting environments.

Key capabilities include:

- **Service Request Management** – Process IT service requests with line-level items linked to catalog offerings, track fulfillment status and completion
- **Service Catalog** – Publish orderable IT offerings including services, product packages, and provisioning actions
- **Access Request Processing** – Submit and fulfill requests to grant, modify, or remove access to secured resources with manager approval and security review workflows
- **Entitlement Management** – Define specific access rights, permission sets, licenses, and roles that can be assigned to users
- **Entitlement Assignments** – Track who has what access with lifecycle status, expiration management, and audit trails
- **System Inventory** – Maintain comprehensive records of IT systems with ownership, purpose, lifecycle status, and governance attributes
- **Component Tracking** – Decompose systems into structural components such as application modules, services, databases, infrastructure elements, and interfaces
- **Technology Standards** – Document and classify technologies, platforms, frameworks, protocols, runtimes, and tools used across systems
- **Technology Association** – Link systems and components to the technologies they use with version tracking and technology governance
- **Hosting Environment Management** – Track physical and logical hosting locations such as data centers, cloud regions, and managed hosting facilities
- **Compliance Assessments** – Evaluate systems, components, and technologies against regulatory requirements and policy standards
- **POAM Management** – Track remediation of compliance findings, vulnerabilities, and control gaps with milestones and completion tracking
- **System Accreditation** – Document formal authorization for systems to operate within defined security and compliance parameters
- **Technology Governance** – Associate catalog items with approved, required, or restricted technologies

## What's Included

This initial release (v1.1.0.0) provides the foundational data model:

- **18 entities** providing comprehensive IT service delivery, access management, system inventory, and compliance oversight capabilities
- **Integration with Core module** for persons, accounts, organization units, locations, action items, agreements, compliance frameworks, compliance requirements, legal authorities, risk items, and documents

Forms and views for service request tracking, access provisioning, system inventory management, and compliance assessment will be available in an upcoming release. The module provides implementors with a baseline data structure that can be customized for IT departments, CIO offices, security teams, and technology governance programs.

## Getting Started

The IT Service Management module is available in the [FAST Modules Repository](https://github.com/microsoft/industry-apps) under the MIT license. It requires the Core module as a foundation.

View the complete [IT Service Management module documentation]({{ '/modules/it-service-management/' | relative_url }}) for entity descriptions, data model diagrams, and implementation guidance.
