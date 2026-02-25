---
title: "HR Administration Data Model"
module: hr-administration
---

The **HR Administration module** manages the core employment structure, transactions, and workforce recordkeeping for an organization. It supports position and classification management (positions, job classifications, grades, and ranks), effective-dated employment actions (promotions, reassignments, pay changes, milestones), employee requests (time off, telework, overtime, workplace accommodations, declarations), and related compliance tracking through governing authorities and structured approvals. Typical use cases include maintaining authorized staffing structures, processing personnel actions, tracking leave and overtime activity, managing accommodation workflows, administering grade/rank frameworks in government or structured environments, and maintaining accurate historical employment records. The module serves as the operational system of record for the employee lifecycle while remaining distinct from recruiting, benefits, and performance management.


## Tables

### HR Position
Represents an authorized position within the organization (distinct from the person occupying it).

### HR Position Assignment
Links an employee to a position for a defined period, including reporting structure and assignment details.

### HR Position Description
Stores formal descriptions and responsibilities associated with a position, potentially version-controlled.

### HR Job Classification
Represents a defined job role or classification (title, exempt status, bargaining unit, etc.) used to categorize positions.

### HR Employment Action
Represents effective-dated personnel changes such as promotions, transfers, pay adjustments, or status changes.

### HR Action Type
Defines categories of employment actions (e.g., Promotion, Reassignment, Pay Adjustment, Conversion). Used to standardize and classify HR Employment Actions.

### HR Employment Milestone
Tracks key lifecycle events such as probation completion, service anniversaries, tenure milestones, or eligibility dates.

### HR Disciplinary Action
Records formal disciplinary measures taken against an employee, including type, basis, effective dates, and outcome. Typically restricted access.

### HR Request
Generic parent table for employee-submitted or HR-initiated requests (e.g., time off, telework, accommodations).

### HR Time Off Request
Represents the header record for employee leave requests, including leave type, period, and approval status.

### HR Time Off Entry
Stores individual leave date entries tied to a time off request (specific dates and hours).

### HR Overtime Entry
Captures individual overtime or compensatory time work entries, including date, hours, type, and rate.

### HR Telework Request
Captures employee requests for telework or remote work arrangements, including schedule and approval details.

### HR Workplace Accommodation
Tracks requests and fulfillment of workplace accommodations, including approval workflow and implementation details.

### HR Employee Declaration
Captures employee-submitted attestations or disclosures (e.g., conflict of interest, outside employment, ethics certifications).

### HR Leave Donation
Records voluntary transfer or donation of leave hours from one employee to another, including approval and balance impact.

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
