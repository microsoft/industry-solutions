---
title: "Project Tracking Data Model"
module: project-tracking
---

The **Project Tracking** module supports the structured intake, planning, execution, and control of work across initiatives of any size. It enables organizations to capture proposed work through Project Requests, formally manage approved Projects, plan delivery using Backlogs and Iterations, and execute work through categorized Work Items aligned to defined Roles and Resource Assignments. Milestones provide timeline checkpoints, while Change Requests ensure formal governance over scope, schedule, and cost adjustments. This module can be used for IT system implementations, policy initiatives, construction efforts, product development, operational improvements, research programs, or any structured body of work requiring visibility, accountability, and controlled delivery from initiation through completion.


## Tables

### Project Request
Represents an intake record used to propose or initiate a new project. Captures initial business need, justification, high-level scope, and evaluation prior to formal project approval.

### Project
Represents the primary delivery record for a defined body of work with scope, objectives, schedule, ownership, and overall status. Serves as the parent container for backlog items, iterations, milestones, resources, and change requests.

### Project Role
Represents standardized roles used within projects (e.g., Project Manager, Business Lead, Technical Lead). Supports consistent staffing structures and reporting.

### Project Resource Assignment
Represents the assignment of a person or resource to a project (and optionally to specific work items), including role, allocation percentage, and assignment duration.

### Project Backlog
Represents a planning container that groups and prioritizes future work items for a project. Used to manage the queue of pending work before assignment to an iteration or execution phase.

### Project Iteration
Represents a defined timebox or execution cycle within a project (e.g., sprint, phase, increment). Used to organize and track work items scheduled for completion during that period.

### Project Work Item Type
Represents the configuration table defining categories of work items (e.g., Epic, Feature, Task, Defect). Controls classification, reporting, and workflow behavior for Project Work Items.

### Project Work Item
Represents the core execution record for a unit of work within a project. May represent an epic, feature, task, defect, or other work category as defined by its type.

### Project Milestone
Represents a significant event or checkpoint within a project timeline. Represents key delivery dates, approvals, or completion markers used for progress tracking and reporting.

### Project Change Request
Represents a formal proposal to modify approved project scope, schedule, cost, deliverables, or other baseline elements. Tracks impact analysis, review, approval decision, and implementation status.

### Person *(Core)*
Project managers, sponsors, business owners, technical leads, resource assignments, work item assignees.

### Organization Unit *(Core)*
Owning units, delivery units, requesting units.

### Organization Initiative *(Core)*
Strategic alignment for projects and requests.

### Account *(Core)*
Customer accounts, vendor accounts, partner organizations.

### Action Item *(Core)*
Tasks related to projects, milestones, and work items.

### Risk Item *(Core)*
Project risks linked to work items and change requests.

### Agreement *(Core)*
Master agreements, contracts, SOWs for projects.

### Legal Authority *(Core)*
Regulatory requirements for projects.

### Document *(Core)*
Project charters, plans, deliverables, supporting documentation.

### Project Type
- IT Implementation
- Infrastructure Project
- Policy Initiative
- Process Improvement
- Product Development
- Construction Project
- Research Project
- Organizational Change
- System Integration
- Maintenance Project
- Compliance Project

### Project Status
- Proposed
- Approved
- Planning
- In Progress
- On Hold
- At Risk
- Completed
- Cancelled
- Closed

### Project Health
- Healthy
- At Risk
- Off Track
- Critical
- On Hold
- Unknown

### Request Priority
- Critical
- High
- Medium
- Low
- Future Consideration

### Backlog Status
- Planning
- Ready
- Active
- Archived
- Closed

### Backlog Type
- Product Backlog
- Sprint Backlog
- Release Backlog
- Feature Backlog
- Maintenance Backlog

### Iteration Status
- Planned
- Active
- Completed
- Cancelled

### Work Item Category
- Epic
- Feature
- User Story
- Task
- Defect
- Spike
- Technical Debt
- Documentation

### Work Item Status
- New
- Proposed
- Approved
- In Progress
- In Review
- In Testing
- Blocked
- Completed
- Cancelled
- Deferred

### Work Item Priority
- Critical
- High
- Medium
- Low

### Work Item Resolution
- Completed
- Fixed
- Verified
- Duplicate
- Won't Fix
- Cannot Reproduce
- By Design
- Deferred

### Milestone Status
- Planned
- On Track
- At Risk
- Achieved
- Missed
- Cancelled

### Milestone Type
- Project Start
- Project End
- Phase Gate
- Delivery
- Review
- Approval
- Go Live
- Customer Acceptance

### Milestone Category
- Schedule
- Deliverable
- Decision Point
- Funding
- Regulatory
- Contractual

### Resource Assignment Status
- Proposed
- Confirmed
- Active
- On Leave
- Completed
- Withdrawn
- Cancelled

### Role Category
- Management
- Leadership
- Technical
- Business
- Support
- Quality
- Subject Matter Expert

### Change Request Type
- Scope Change
- Schedule Change
- Budget Change
- Resource Change
- Quality Change
- Risk Response
- Requirement Change
- Technical Change
- Process Change

### Change Impact Level
- Minor
- Moderate
- Significant
- Major
- Critical
