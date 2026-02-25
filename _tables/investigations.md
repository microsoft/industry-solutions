---
title: "Investigations Data Model"
module: investigations
---

The **Investigations module** supports the structured intake, management, analysis, and resolution of formal investigations across public sector and commercial environments. It enables organizations to document allegations, assign investigators, manage interviews and evidence with defensible chain-of-custody tracking, analyze issues against policies or standards, produce formal reports, and monitor corrective actions and recoveries through closure. The module supports use cases such as employee misconduct investigations, fraud inquiries, ethics hotline complaints, safety incidents, regulatory violations, data breach reviews, quality control investigations, inspector general cases, internal affairs reviews, and compliance examinations. It provides both operational case management and governance oversight, ensuring investigations are thorough, auditable, and aligned with organizational or statutory requirements.


## Tables

### Investigation
Primary case record. Tracks lifecycle status, ownership, classification, key dates, confidentiality, and overall disposition.

### Investigation Intake
Initial allegation or referral submission before or at case creation. Captures source, channel, summary, and screening details.

### Investigation Allegation
Specific claim or accusation being evaluated within a case. A case may contain multiple allegations.

### Investigative Issue
Structured question, policy element, or control area being examined. Often used to frame analysis and findings.

### Investigative Type
Primary investigation taxonomy (Fraud, Misconduct, Safety, Data Breach, Quality, etc.).

### Investigative Category
Secondary classification used for reporting (program area, risk domain, business unit, etc.).

### Investigation Related Cases
Links cases together (duplicate, predecessor, parallel, systemic connection).

### Investigation Party
Person or organization involved in the case (subject, reporter, witness, impacted party, etc.).

### Investigative Party Role
Defines allowable roles a party may have in a case.

### Investigation Location
Physical or virtual location relevant to the case (facility, site, region, system environment).

### Investigation Plan
Documents scope, objectives, methodology, milestones, and investigative strategy.

### Evidence Item
Any collected material (document, image, device, log file, physical object).

### Evidence Type
Classification of evidence (email, CCTV, financial record, system log, physical item, etc.).

### Evidence Link
Associates evidence to specific allegations, issues, interviews, findings, or tasks.

### Evidence Custody Record
Chain-of-custody entries documenting transfer, handling, and condition changes.

### Evidence Access Log
Audit log of who viewed, downloaded, or accessed an evidence item.

### Evidence Storage Location
Physical or digital storage location (locker, vault, secure repository, external archive).

### Investigation Interview
Scheduled or completed interview session related to the case.

### Investigation Interview Participant
Links participants to interviews and defines their role (interviewer, witness, observer, counsel).

### Investigation Finding
Formal conclusion regarding an allegation or issue (substantiated, unsubstantiated, inconclusive, etc.).

### Investigation Recommendation
Proposed corrective, preventive, or control improvement action arising from findings.

### Investigation Corrective Action
Action assigned to remediate findings, with owner, due date, and status tracking.

### Investigation Outcome
Overall case resolution summary and closure rationale.

### Investigation Recovery Record
Tracks recovered funds, assets, restitution, or other tangible recoveries resulting from the case.

### Investigation Report
Formal written report record (draft/final versions, approvals, publication metadata).

### Investigation Referral
Records referrals made to or received from internal or external entities.

### Investigative Referral Type
Defines referral categories (Internal, Legal, Law Enforcement, Regulator, HR, etc.).

### Person *(Core)*
Represents investigators, subjects, witnesses, reporters, custodians, and decision makers.

### Account *(Core)*
Represents organizations involved as subjects, reporters, or referral recipients.

### Organization Unit *(Core)*
Investigative units, reporting departments, subject departments.

### Location *(Core)*
Incident locations, interview locations, evidence storage, investigation sites.

### Judicial District *(Core)*
Jurisdiction for cases with legal implications.

### Action Item *(Core)*
Operational task tracking for investigation work, linked to findings and corrective actions.

### Legal Authority *(Core)*
Regulatory basis for investigations and findings.

### Compliance Framework *(Core)*
Compliance standards being investigated.

### Document *(Core)*
Evidence documents, reports, interview transcripts, supporting documentation.

### After Action Report *(Core)*
Can be linked for post-investigation reviews and lessons learned.

### Formal Decision *(Core)*
Can be linked to investigation outcomes requiring formal governance decisions.

### Investigation Status
- Intake
- Screening
- Open
- Active Investigation
- Analysis
- Report Writing
- Pending Review
- Pending Closure
- Closed
- Suspended
- Referred Out

### Intake Status
- Received
- Under Review
- Screened
- Assigned
- Converted to Investigation
- Declined
- Referred
- Duplicate

### Screening Status
- Pending Screening
- Under Review
- Approved for Investigation
- Declined
- Referred

### Intake Disposition
- Proceed with Investigation
- Decline - Insufficient Evidence
- Decline - Outside Scope
- Refer to Other Entity
- Duplicate Case
- Already Resolved
- Administrative Closure

### Allegation Type
- Fraud
- Theft
- Misuse of Resources
- Conflict of Interest
- Ethics Violation
- Safety Violation
- Security Breach
- Policy Violation
- Misconduct
- Discrimination
- Harassment
- Retaliation
- Quality Defect
- Environmental Violation

### Allegation Status
- Pending Investigation
- Under Investigation
- Substantiated
- Unsubstantiated
- Inconclusive
- Not Investigated
- Withdrawn

### Issue Type
- Policy Compliance
- Control Effectiveness
- Procedural Adherence
- Documentation Adequacy
- Authorization
- Accountability
- Transparency

### Issue Status
- Open
- Under Review
- Resolved
- Closed

### Case Relationship Type
- Duplicate
- Related
- Predecessor
- Successor
- Parallel Investigation
- Systemic Issue
- Similar Pattern

### Party Type
- Individual
- Organization
- Department
- External Entity

### Participation Status
- Identified
- Contacted
- Cooperative
- Uncooperative
- Unavailable
- Declined to Participate

### Investigation Location Type
- Incident Site
- Interview Location
- Evidence Location
- Subject Location
- Facility
- System Environment

### Plan Status
- Draft
- Under Review
- Approved
- Active
- Revised
- Completed

### Evidence Status
- Collected
- In Custody
- Under Analysis
- Released
- Archived
- Destroyed

### Evidence Category
- Documentary
- Physical
- Digital
- Testimonial
- Demonstrative

### Evidence Link Type
- Supports Allegation
- Contradicts Allegation
- Relevant to Issue
- Discussed in Interview
- Basis for Finding
- Referenced in Task

### Custody Event Type
- Initial Collection
- Transfer
- Analysis
- Viewing
- Copying
- Return
- Release
- Archival
- Destruction

### Access Type
- View
- Download
- Copy
- Analysis
- Administrative

### Storage Type
- Physical Locker
- Evidence Vault
- Secure Repository
- Cloud Storage
- External Archive
- Sealed Container

### Interview Type
- Subject Interview
- Witness Interview
- Expert Interview
- Follow Up Interview
- Recorded Statement

### Interview Status
- Scheduled
- Conducted
- Cancelled
- Rescheduled
- Declined

### Interview Participant Role
- Primary Interviewer
- Co-Interviewer
- Witness
- Subject
- Legal Counsel
- Observer
- Interpreter

### Finding Type
- Allegation Finding
- Policy Finding
- Control Finding
- Compliance Finding
- Systemic Finding

### Finding Status
- Draft
- Under Review
- Finalized
- Appealed
- Upheld
- Overturned

### Finding Result
- Substantiated
- Partially Substantiated
- Unsubstantiated
- Inconclusive
- No Finding
- Unable to Determine

### Recommendation Type
- Disciplinary Action
- Process Improvement
- Policy Change
- Control Enhancement
- Training
- System Modification
- Management Action

### Recommendation Status
- Proposed
- Under Review
- Accepted
- Rejected
- Modified
- Implemented
- Closed

### Corrective Action Type
- Immediate Correction
- Process Change
- Policy Update
- Training
- Disciplinary Action
- System Enhancement
- Monitoring

### Outcome Type
- Administrative Closure
- Investigative Completion
- Referral
- Settled
- Withdrawn

### Overall Disposition
- Substantiated
- Partially Substantiated
- Unsubstantiated
- Inconclusive
- Unfounded
- Referred
- Administrative Closure

### Recovery Type
- Monetary Recovery
- Asset Recovery
- Restitution
- Fee or Penalty
- Civil Settlement
- Cost Savings

### Recovery Status
- Identified
- Pending Collection
- Partial Recovery
- Fully Recovered
- Uncollectible
- Written Off

### Recovery Method
- Payment
- Payroll Deduction
- Asset Seizure
- Legal Settlement
- Insurance Claim
- Voluntary Return

### Report Type
- Investigation Report
- Interim Report
- Summary Report
- Statistical Report
- Public Report

### Report Status
- Draft
- Under Review
- Final
- Published
- Archived

### Referral Direction
- Outgoing
- Incoming

### Referral Category
- Internal Department
- Legal Counsel
- Law Enforcement
- Regulatory Agency
- Inspector General
- Human Resources
- External Auditor

### Referral Status
- Pending
- Submitted
- Acknowledged
- Under Review
- Completed
- Declined
