---
title: "Request Tracker Data Model"
module: request-tracker
---

The **Request Tracker** module provides a lightweight, centralized way for teams or divisions to intake, triage, assign, and track cross-organizational or external requests from submission through completion. It serves as a flexible front door for handling items such as data pulls, access requests, policy questions, document reviews, partner inquiries, leadership taskings, service coordination requests, or general assistance requests. By standardizing Requests and Request Types, the module enables consistent routing, prioritization, ownership, and status tracking without the overhead of a full case management system. It is especially useful for smaller teams that need visibility, accountability, and basic reporting on workload and turnaround time, while retaining the ability to link requests to more specialized modules if the work expands in scope.


## Tables

### Request
Represents a single submitted request for work, information, approval, or action. This is the primary tracking record from intake through completion and closure.

### Request Type
Defines the classification of a request and supports routing, prioritization, and reporting. Provides default routing rules, target timelines, and workflow configuration.

### Person *(Core)*
Requestors, contacts, assigned handlers, reviewers, approvers.

### Account *(Core)*
Submitting organizations, external entities making requests.

### Organization Unit *(Core)*
Submitting units, assigned units, routing targets.

### Action Item *(Core)*
Related tasks spawned from requests.

### Discussion Item *(Core)*
Collaboration threads linked to requests.

### Document *(Core)*
Supporting documentation, attachments, response materials.

### Project Work Item *(Core)*
Work items created or linked as a result of requests.

### Request Type Category
- Information Request
- Data Request
- Access Request
- Document Review
- Policy Question
- Technical Support
- Service Request
- Leadership Tasking
- Partner Inquiry
- General Assistance
- Coordination Request
- Research Request
- Report Request
- Approval Request

### Request Urgency
- Immediate
- Urgent
- Standard
- Low
