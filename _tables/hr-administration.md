---
title: "HR Administration Data Model"
module: hr-administration
---

## Tables

### HR Position

The **HR Position** table represents authorized positions within the organizational structure, distinct from the persons who occupy them. Each position record includes position number, name, job classification assignment, organizational placement (organization unit, location), employment type, full-time equivalent (FTE), position status (authorized, filled, frozen, abolished), and effective date ranges for position lifecycle management. Supervisory relationships are maintained through reports-to position references, while grade/rank, pay grade, job series, and personnel type assignments establish compensation and classification context. Positions can specify clearance requirements (requires clearance flag and required clearance level), management and supervisory indicators, position designation, bargaining unit, and budget codes for financial planning and workforce structure management.

### HR Job Classification

The **HR Job Classification** table defines standardized job categories used to classify positions with classification codes, names, descriptions, classification levels, and occupational references (job series, standard occupational codes). Each classification includes FLSA status (exempt, non-exempt), bargaining unit eligibility, default bargaining unit, default pay grade, and indicators for supervision (is supervisory), management (is management), and certification requirements. Active status tracking enables classification lifecycle management, supporting consistent position classification, pay administration, and regulatory compliance with fair labor standards and occupational coding frameworks.

### Job Series

The **Job Series** table provides broader occupational family groupings for job classifications and positions, enabling roll-up reporting and career progression planning within related occupational areas.

### Personnel Type

The **Personnel Type** table categorizes workforce segments (e.g., civilian, military, contractor, intern, volunteer) used by positions to support differentiated policies, benefits, and reporting requirements across employment categories.

### HR Action Type

The **HR Action Type** table standardizes employment action categories (hire, promotion, transfer, reassignment, salary adjustment, separation, retirement, conversion, detail, extension) with action category classification, descriptions, and approval requirement indicators. This ensures consistent categorization of personnel transactions and enables workflow routing based on action type requirements.

### HR Pay Grade

The **HR Pay Grade** table defines compensation grade structures used by positions, job classifications, and employment actions to establish pay ranges and salary administration frameworks.

### Grade Rank

The **Grade Rank** table provides combined grade and rank identifiers for organizations using hierarchical or uniformed workforce structures, enabling grade and rank-based pay and advancement systems.

### HR Rank

The **HR Rank** table categorizes rank designations within hierarchical workforce structures, supporting rank-based progression in uniformed services or structured career ladders.

### Pay Grade

The **Pay Grade** table from the core module establishes base pay grade structures referenced by HR job classifications and positions for salary range assignments.

### Clearance Level

The **Clearance Level** table from the core module defines security clearance requirements (e.g., Confidential, Secret, Top Secret) that can be assigned to positions requiring personnel security clearances.

### HR Position Description

The **HR Position Description** table maintains formal position documentation including position purpose, primary duties, key responsibilities, required and preferred qualifications, supervisory responsibilities, physical requirements, and working conditions. Each description references its associated HR position and includes version numbers, effective dates, approval workflow (approval status, approved by, approval date), description status, and supporting document attachments for official position documentation management and compliance with classification standards.

### HR Position Assignment

The **HR Position Assignment** table links persons to HR positions for defined periods, documenting assignment type (permanent, temporary, acting, detailed, concurrent), start and end dates, assignment status (active, pending, completed, cancelled), and FTE allocation for partial assignments. Records maintain primary assignment indicators, reporting relationships (reports to person and position), location and organization unit context, and descriptions to support multiple concurrent assignments, acting appointments, detailed assignments, and historical assignment tracking.

### HR Employment Action

The **HR Employment Action** table documents personnel transactions affecting employment status, position, compensation, or assignment. Each action is categorized by HR action type and includes action number, effective date, action status, and approval workflow (requested by, requested date, approved by, approval status, approval date, processed by, processed date). Before/after context is captured through from/to field pairs for position, location, organization unit, employment type, FTE, pay grade, grade/rank, and salary (with currency support), enabling proper tracking of changes. Justification, description, impact on employee narratives, and legal authority references provide supporting documentation for personnel action audit trails and compliance.

### HR Employment Milestone

The **HR Employment Milestone** table tracks significant lifecycle events for employees including probationary completion, service anniversaries, eligibility dates, awards, certification achievements, or tenure milestones. Each milestone includes milestone type and date, milestone status, years of service calculations, recognition provided indicators, notification tracking (notification date, notification sent), recorded by and recorded date attribution, and descriptions for workforce milestone visibility and employee recognition program administration.

### HR Request

The **HR Request** table provides a common request structure for various HR transactions including time off, telework, and workplace accommodations. Records capture request number, request type and status, priority, request date, requested start and end dates, requesting organization unit and person, approval workflow (approved by, approval status, approval date), denial reason, and descriptions. Specialized request types (time off, telework, accommodations) extend this base structure with type-specific details.

### HR Time Off Request

The **HR Time Off Request** table documents employee leave requests with leave type specification (annual, sick, administrative, compensatory, unpaid, other), start, end, and return dates, total hours requested/approved/taken for balance tracking, reason narratives, approval workflow, contact during leave and emergency contact information, supporting document references, and denial reason. Each request links to the base HR request for common request attributes and generates HR time off entry records for individual leave dates.

### HR Time Off Entry

The **HR Time Off Entry** table stores individual leave date entries for approved time off requests, documenting entry date, hours taken, leave type, approval status, and person for daily or partial-day leave tracking. Entries link to their parent HR time off request and provide granular leave detail for payroll integration and balance calculation.

### HR Leave Donation

The **HR Leave Donation** table facilitates leave sharing programs by documenting voluntary leave transfers between employees. Records capture donor and recipient persons, leave types donated and received (which may differ based on conversion rules), hours donated and hours received with conversion rates, donation date, donor and recipient balance before/after snapshots, approval workflow (approval status, approved by, approval date), processing status and processed date, justification, and notes. This supports leave bank programs, emergency leave sharing, and charitable leave donation with full accountability and balance adjustment tracking.

### HR Overtime Entry

The **HR Overtime Entry** table captures overtime work instances with work date, hours worked, overtime type (overtime, compensatory time, holiday pay), overtime rate multipliers, total pay calculation with currency support, pay period reference, person and organization unit assignment, project codes for cost allocation, approval workflow (approval status, approved by, approval date), justification, and notes. This enables overtime authorization, cost tracking, and compensation administration.

### HR Telework Request

The **HR Telework Request** table manages remote work arrangement requests with telework type (regular, situational, emergency) and frequency specifications, start and end dates, business justification, primary telework location and full address details, schedule descriptions, equipment needs, internet speed availability, safety checklist completion indicators, agreement signed status and date, approval workflow (approval status, approved by, approval date), supervisor reference, request status, and notes. Requests link to the base HR request structure for common request handling and workflow coordination.

### HR Workplace Accommodation

The **HR Workplace Accommodation** table supports reasonable accommodation processes documenting accommodation requests and implementation. Records capture accommodation type, need description, requested and approved accommodation details, medical documentation provided indicator, privacy consent references, temporary or permanent status, start and end dates for temporary accommodations, approval workflow (approval status, approved by, approval date), request status, implementation date and cost (with currency), effectiveness evaluation narratives, supporting document attachments, security classification for sensitive information, and denial reason when applicable. This supports ADA compliance, accommodation coordination, and privacy-protected documentation.

### HR Employee Declaration

The **HR Employee Declaration** table captures required employee attestations and disclosures such as financial disclosures, conflict of interest statements, ethics acknowledgments, policy certifications, or regulatory compliance affirmations. Each declaration includes declaration type and content, compliance framework and legal authority references establishing the requirement basis, attestation status and date, submission date, declaration status, requires review indicator, review workflow (reviewed by, review date, review comments), effective and expiration dates for renewal tracking, supporting documents, security classification, and notes. This maintains compliance with disclosure requirements, ethics programs, and regulatory mandates.

### HR Disciplinary Action

The **HR Disciplinary Action** table documents personnel conduct and performance matters with disciplinary action type (verbal warning, written reprimand, suspension, demotion, termination), incident date and description, violation type, action taken, issue date and issuing authority, effective and expiration dates, approval workflow, action status, employee response narrative, appeal tracking (appeal filed status, appeal date, appeal outcome), legal authority references, supporting documents, organization unit, person, security classification, and visibility controls. This maintains sensitive personnel matter documentation for due process, appeal procedures, and workforce accountability.

### Person *(Core)*
Represents employees throughout the module for assignments, actions, requests, and history.

### Organization Unit *(Core)*
Departmental and divisional structure for position placement and reporting hierarchy.

### Location *(Core)*
Work locations for positions, assignments, and telework arrangements.

### Pay Grade *(Core)*
Salary grade structures referenced by positions, classifications, and employment actions.

### Grade-Rank *(Core)*
Combined grade and rank structures for uniformed or hierarchical organizations.

### Job Series *(Core)*
Broader job family groupings for classifications and positions.

### Personnel Type *(Core)*
Classification of employment categories (civilian, uniformed, contractor, etc.).

### Clearance Level *(Core)*
Security clearance requirements for positions.

### Legal Authority *(Core)*
Used as HR Governing Authority for employment actions, disciplinary actions, and declarations.

### Compliance Framework *(Core)*
Referenced for regulatory compliance in declarations and accommodations.

### Privacy Consent *(Core)*
Required for sensitive accommodation requests and medical information.

### Document *(Core)*
Supporting documentation for requests, descriptions, actions, and declarations.

### Content Template *(Core)*
Templates for position descriptions, offers, and standardized documents.

### Position Status
- Authorized
- Filled
- Vacant
- Frozen
- Abolished
- Pending Authorization

### Assignment Type
- Permanent
- Temporary
- Acting
- Detail
- Rotational
- Interim

### Assignment Status
- Active
- Pending Start
- Completed
- Terminated
- Suspended

### FLSA Status
- Exempt
- Non-Exempt

### Action Category
- Appointment
- Promotion
- Reassignment
- Transfer
- Pay Adjustment
- Status Change
- Separation
- Return to Duty
- Position Change

### Milestone Type
- Hire Date Anniversary
- Probation Start
- Probation End
- Tenure Eligibility
- Retirement Eligibility
- Service Anniversary
- Contract Renewal
- Performance Review Due

### Milestone Status
- Upcoming
- Current
- Completed
- Acknowledged

### Disciplinary Action Type
- Verbal Warning
- Written Warning
- Written Reprimand
- Suspension
- Demotion
- Termination
- Performance Improvement Plan
- Final Warning

### HR Request Type
- Time Off
- Telework
- Overtime
- Workplace Accommodation
- Schedule Change
- Leave Donation
- Personnel Record Update

### Leave Type
- Annual Leave
- Sick Leave
- Personal Leave
- Bereavement Leave
- Military Leave
- Jury Duty
- FMLA
- Parental Leave
- Administrative Leave
- Leave Without Pay
- Compensatory Time
- Holiday

### Entry Status
- Pending
- Approved
- Denied
- Cancelled
- Processed

### Overtime Type
- Regular Overtime
- Holiday Overtime
- Emergency Overtime
- Compensatory Time Earned
- Compensatory Time Used
- Premium Pay

### Telework Type
- Regular Telework
- Ad Hoc Telework
- Situational Telework
- Full Time Remote
- Hybrid

### Telework Frequency
- Daily
- Weekly
- Bi-Weekly
- Monthly
- As Needed
- Specific Days

### Accommodation Type
- Physical Workspace Modification
- Assistive Technology
- Schedule Modification
- Policy Exception
- Equipment Provision
- Job Restructuring
- Leave Modification
- Communication Support

### Declaration Type
- Conflict of Interest
- Outside Employment
- Financial Disclosure
- Ethics Certification
- Gift Receipt
- Travel Declaration
- Relationship Disclosure
- Political Activity
