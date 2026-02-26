---
title: "Executive Coordination Data Model"
module: executive-coordination
---

## Tables

### Executive Action
The central entity for documenting high-level directives, taskers, and executive actions requiring coordinated organizational response. Captures action number, name, type, issuance details (issued by, issue date, issuing authority), accountability assignments (executive sponsor, accountable lead, lead organization unit), timeline (start date, target completion date, actual completion date), resource estimates (budget, effort hours), progress indicators (percent complete, action items counters, overall health), and strategic context (organization initiative, legal authority, agreement references). Includes lifecycle stage, priority, security classification, visibility controls, and compliance flags.

### Executive Action Type
Standardized classification system for categorizing executive actions (e.g., Executive Order, Policy Directive, Compliance Tasker, Strategic Initiative, Crisis Response). Each type includes name, description, default priority, and configuration flags indicating whether actions of this type typically require impact assessment, risk assessment, or legal authority documentation.

### Executive Action Dependency
Documents sequencing and coordination relationships between executive actions for portfolio-level planning and dependency management. Links predecessor action and successor action with dependency type (finish-to-start, start-to-start, finish-to-finish, start-to-finish), dependency status (pending, active, satisfied, blocked), critical path indicators, description, impact if not met narratives, and notes.

### Executive Status Update
Periodic progress reporting on executive actions capturing snapshots of execution health, accomplishments, challenges, and forward plans. Includes status date, reporting period, action status, overall health, percent complete, and structured narratives for key accomplishments, next steps, challenges and risks, decisions needed, and resource concerns. Timeline impact, budget impact, scope change requests, and escalation flags alert leadership to emerging issues.

### Executive Decision Log
Auditable record of significant decisions made during executive action execution. Documents decision date, decided by, decision authority, decision category, decision description, rationale, and impact assessments on timeline, budget, scope, and accountability. Can link to Formal Decision records when governance processes require structured decision documentation, with communicated date and implementation date tracked.

### Analysis
Linkage point to analytical studies, research, or assessments that inform or support executive actions. Enables traceability between executive decisions and underlying evidence, options analysis, or recommendations.

### Impact
Linkage point to impact assessment records documenting expected or observed consequences of executive actions. Supports comprehensive impact visibility by connecting actions to detailed impact analyses.

### Risk Item
Linkage point to risk management records associated with executive actions. Ensures actions are connected to systematic risk assessment and mitigation planning, supporting informed decision-making and proactive risk management.
