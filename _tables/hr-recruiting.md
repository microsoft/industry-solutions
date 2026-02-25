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

### Person *(Core)*
Represents candidates (internally), hiring managers, recruiters, interviewers, evaluators, and approvers.

### Organization Unit *(Core)*
Hiring departments, divisions, and organizational structure for requisitions and offers.

### Location *(Core)*
Work locations for positions, interview locations, and office assignments.

### Job Series *(Core)*
Job family classifications for requisitions and workforce requests.

### Pay Grade *(Core)*
Salary grade structures for requisitions and offers.

### Clearance Level *(Core)*
Security clearance requirements for positions.

### Competency *(Core)*
Skills and competencies for requisition requirements and candidate assessments.

### Credential *(Core)*
Required certifications, licenses, and credentials for positions.

### Personnel Type *(Core)*
Employment categories for requisitions.

### Document *(Core)*
Resumes, cover letters, offer letters, background check results.

### Legal Authority *(Core)*
Regulatory basis for hiring decisions (merit systems, civil service rules, EEO regulations).

### Formal Decision *(Core)*
Links selection decisions to formal decision records when required.

### Privacy Consent *(Core)*
Candidate data privacy consent and opt-in tracking.

### Workforce Request Type
- New Position
- Replacement
- Temporary Backfill
- Seasonal
- Project Based
- Expansion

### Requisition Status
- Draft
- Pending Approval
- Approved
- Open
- On Hold
- Filled
- Cancelled
- Closed

### Posting Channel
- Company Website
- Job Board
- LinkedIn
- Indeed
- Government Jobs Portal
- Professional Association
- Internal Portal
- Campus Recruiting
- Agency
- Employee Referral

### Requirement Type
- Education
- Experience
- Competency
- Credential
- License
- Certification
- Language
- Technical Skill
- Physical Requirement
- Clearance

### Requirement Category
- Minimum Qualification
- Preferred Qualification
- Screening Criteria
- Evaluation Criteria

### Proficiency Level
- Beginner
- Intermediate
- Advanced
- Expert
- Subject Matter Expert

### Candidate Source
- Direct Application
- Employee Referral
- Agency
- LinkedIn
- Job Board
- Campus Recruiting
- Career Fair
- Social Media
- Internal Transfer
- Rehire

### Candidate Status
- Active
- Under Consideration
- Interviewing
- Selected
- Offered
- Hired
- Not Selected
- Withdrawn
- Inactive

### Education Level
- High School
- Associate Degree
- Bachelor Degree
- Master Degree
- Doctoral Degree
- Professional Degree
- Some College
- Trade Certification

### Application Status
- Submitted
- Under Review
- Screening
- Qualified
- Interviewing
- Finalist
- Selected
- Not Selected
- Withdrawn
- On Hold

### Application Stage
- Application Review
- Initial Screening
- Phone Screen
- First Interview
- Second Interview
- Panel Interview
- Final Interview
- Reference Check
- Offer Stage
- Pre-Hire

### Application Source
- Direct Application
- Employee Referral
- Agency Submission
- Internal Application
- Campus Recruiting
- Sourced by Recruiter

### Evaluation Type
- Initial Screening
- Phone Screen Evaluation
- Technical Assessment
- Behavioral Interview
- Panel Interview
- Final Assessment

### Overall Rating
- Excellent
- Above Average
- Average
- Below Average
- Poor
- Not Assessed

### Recommendation
- Strong Hire
- Hire
- Maybe
- Do Not Hire
- Advance to Next Stage
- Decline

### Interview Type
- Phone Screen
- Video Interview
- In Person
- Panel Interview
- Technical Interview
- Behavioral Interview
- Case Interview
- Presentation

### Interview Status
- Scheduled
- Confirmed
- Rescheduled
- Completed
- No Show
- Cancelled

### Attendance Status
- Attended
- No Show
- Cancelled by Candidate
- Cancelled by Employer
- Rescheduled

### Evaluation Category
- Technical Skills
- Communication
- Leadership
- Problem Solving
- Cultural Fit
- Experience
- Education
- Motivation

### Decision Status
- Pending
- Recommended
- Approved
- Declined
- On Hold

### Offer Status
- Draft
- Pending Approval
- Approved
- Extended
- Under Negotiation
- Accepted
- Declined
- Expired
- Withdrawn

### Salary Frequency
- Hourly
- Annual
- Bi-Weekly
- Monthly

### Offer Response
- Pending
- Accepted
- Declined
- Negotiating
- Expired

### Pre-Hire Requirement Type
- Background Check
- Drug Screening
- Medical Examination
- Reference Check
- Credential Verification
- Education Verification
- Employment Verification
- Security Clearance
- I-9 Verification
- Fingerprinting

### Requirement Status
- Not Started
- In Progress
- Completed
- Pending Review
- On Hold
- Cancelled
- Failed

### Requirement Result
- Cleared
- Cleared with Conditions
- Failed
- Incomplete
- Cancelled
- Pending
