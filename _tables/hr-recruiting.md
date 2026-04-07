---
title: "HR Recruiting Data Model"
module: hr-recruiting
---

The **HR Recruiting module** manages the end-to-end hiring lifecycle from workforce request through candidate selection and offer. It supports structured requisition management, configurable posting and qualification requirements, candidate and application tracking, interviews, evaluator scoring, and formal selection decisions. The module is designed to work across public sector, commercial, and regulated environments, enabling use cases such as merit-based civil service hiring, corporate recruiting, campus hiring, internal mobility, and high-volume talent acquisition. It integrates with configurable question-and-answer capabilities for screening and leverages shared skills/competencies for defensible evaluation. The module concludes with offer management and pre-hire requirements, providing a clean handoff to HR Administration for onboarding and employment processing.


## Tables

### HR Workforce Request
Represents the initial request or justification to create or fill a position. Typically used in workforce planning and budgeting prior to requisition approval.

### HR Requisition
Represents the authorized request to recruit for a position. Contains hiring details such as department, hiring manager, employment type, funding source, salary range, and approval status.

### HR Requisition Posting
Represents a specific publication or advertisement instance of a requisition. Tracks posting channel, posting dates, and versioned job description content.

### HR Requisition Requirement
Defines the required and preferred qualifications, competencies, or eligibility criteria associated with a requisition. May include weighting, proficiency levels, or minimum thresholds.

### HR Candidate
Represents the persistent recruiting profile of an individual across applications. Stores contact details, high-level background information, and historical application activity independent of any single requisition.

### HR Application
Represents a candidate's formal submission for a specific requisition or posting. Tracks the lifecycle status (submitted, under review, interviewed, selected, not selected, withdrawn) and serves as the central operational record for evaluating and processing applicants.

### HR Application Skill Assessment
Stores detailed scoring or rating of how well an applicant meets specific skills, competencies, or requisition requirements. Supports structured, defensible evaluation using weighted criteria.

### HR Application Evaluation
Provides the consolidated summary assessment of an application. Captures overall score, recommendation, decision rationale, and disposition outcome based on interviews, skill assessments, and reviewer input.

### HR Interview
Represents a scheduled interview event for an application. Tracks interview type (phone, panel, virtual, in-person), date/time, participants, and outcome notes.

### HR Evaluation
Captures an individual reviewer's structured assessment of a candidate, typically tied to an interview or evaluation stage. May include rubric-based scoring, comments, and competency ratings.

### HR Selection Decision
Documents the formal hiring decision for a requisition. Identifies the selected candidate, ranking (if applicable), approvals, and justification supporting the final selection.

### HR Offer
Documents the formal employment offer extended to a selected candidate. Captures compensation details, employment terms, start date, expiration, negotiation status, and final acceptance or decline.

### HR Pre-Hire Requirement
Tracks conditional requirements that must be completed prior to employment start. Examples include background checks, credential verification, medical screening, or security clearance initiation.
