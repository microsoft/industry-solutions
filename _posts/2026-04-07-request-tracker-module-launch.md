---
layout: post
title: "Request Tracker Module Now Available"
date: 2026-04-07
tags: [modules, releases]
---

We're excited to announce the **Request Tracker** module — a lightweight, centralized system for intaking, triaging, assigning, and tracking cross-organizational or external requests.

## What is the Request Tracker Module?

The Request Tracker module provides teams and divisions with a flexible front door for handling incoming requests without the complexity of full case management systems. It enables organizations to intake and classify requests using configurable request types, assign work to appropriate teams or staff, track progress through standardized status workflows, monitor completion timelines and effort, capture requester feedback, and report on workload and turnaround metrics.

Key capabilities include:

- **Request Type Configuration** – Define classification categories that support routing, prioritization, and reporting with default routing rules, target completion timelines, and service level expectations
- **Hierarchical Type Taxonomy** – Organize request types using parent-child relationships for structured categorization and reporting
- **Request Intake** – Capture submitted requests with titles, detailed descriptions, requester identification, and contact information with contact preference tracking
- **Internal and External Tracking** – Distinguish between internal departmental requests and external partner or public inquiries
- **Confidentiality Controls** – Mark requests as confidential when handling sensitive information or restricted matters
- **Assignment Management** – Route requests to organization units and assigned staff with assignment date and assignment authority tracking
- **Approval Workflows** – Support approval requirements with approver identification, approval status, approval dates, and approval notes
- **Status Lifecycle** – Progress requests through submitted, assigned, in progress, completed, and closed statuses with stage tracking
- **Completion Tracking** – Document who completed work, completion dates, effort hours expended, and closure notes
- **Requester Feedback** – Capture feedback following request completion for quality monitoring and service improvement
- **Discussion Threading** – Link requests to discussion items for threaded communication and collaboration
- **Document Attachments** – Attach supporting documentation with attachment descriptions for context and reference
- **Due Date Management** – Track submission dates, due dates, and target completion timelines for service level monitoring

## What's Included

This initial release (v1.1.0.0) provides the foundational data model:

- **2 entities** providing lightweight request intake, classification, assignment, tracking, and completion capabilities
- **Integration with Core module** for persons, organization units, discussion items, and documents

Forms and views for request intake, request queue management, assignment coordination, and completion tracking will be available in an upcoming release. The module provides implementors with a baseline data structure that can be customized for data request handling, access coordination, policy question tracking, document review workflows, partner inquiry management, leadership tasking, service coordination, and general assistance requests.

## Getting Started

The Request Tracker module is available in the [FAST Modules Repository](https://github.com/microsoft/industry-apps) under the MIT license. It requires the Core module as a foundation.

View the complete [Request Tracker module documentation]({{ '/modules/request-tracker/' | relative_url }}) for entity descriptions, data model diagrams, and implementation guidance.
