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
