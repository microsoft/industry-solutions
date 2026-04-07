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
