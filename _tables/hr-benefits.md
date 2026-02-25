---
title: "HR Benefits Data Model"
module: hr-benefits
---

The **HR Benefits module** manages the full lifecycle of employee benefit offerings, from plan design and eligibility configuration to enrollment, life event changes, and cost administration. It allows organizations to define benefit plans, options, coverage levels, providers, and contribution structures, while enforcing eligibility rules and waiting periods. HR staff can manage open enrollment cycles, process new hire enrollments, handle qualifying life events (such as marriage or birth), maintain beneficiary records, and track benefit-related claims or reimbursements. The module also supports payroll integration through deduction codes and contribution rates, and enables financial oversight through cost allocation tracking. It is designed to support both public sector and commercial organizations with effective dating, auditability, and structured benefit governance.


## Tables

### HR Benefit Plan
Defines a specific benefit offering provided by the organization (e.g., Medical Plan A, Pension Plan, Basic Life Insurance), including plan year and provider.

### HR Benefit Option
Defines selectable options within a benefit plan (e.g., PPO vs. HDHP, Basic vs. Premium coverage).

### HR Benefit Coverage Level
Defines coverage tiers available under benefit plans (e.g., Employee Only, Employee + Spouse, Family). Used to determine pricing and eligibility.

### HR Benefit Provider
Stores information about the external or internal organization administering the benefit plan (e.g., insurance carrier, retirement board, third-party administrator).

### HR Benefit Plan Document
Stores plan-related documentation such as summary plan descriptions, policy documents, regulatory filings, or internal guidelines.

### HR Benefit Eligibility Rule
Defines reusable eligibility conditions for benefit participation, such as employment type, grade/rank, bargaining unit, service duration, or location.

### HR Benefit Waiting Period
Defines waiting period rules before an employee becomes eligible for enrollment (e.g., 30 days after hire, first of month following eligibility).

### HR Benefit Enrollment Period
Defines enrollment windows such as Open Enrollment, New Hire Enrollment, or Special Enrollment periods, including start and end dates.

### HR Benefit Enrollment
Represents an individual's enrollment in a specific benefit plan, including selected option, coverage level, effective dates, and enrollment status.

### HR Benefit Election
Captures detailed selections made under a benefit enrollment, such as optional riders, add-ons, or sub-options within a plan.

### HR Benefit Beneficiary
Stores beneficiary designations for benefit plans that require them (e.g., life insurance, retirement). Includes allocation percentage, relationship, effective dates, and priority sequencing.

### HR Benefit Life Event
Records a reported qualifying life event for an individual (e.g., marriage, birth, divorce) that may trigger enrollment changes. Includes documentation and approval status.

### HR Benefit Life Event Change
Tracks specific benefit enrollment changes resulting from a life event, including affected plans, requested modifications, approval status, and effective dates.

### HR Benefit Contribution Rate
Defines employer and employee contribution structures for a benefit plan, option, and/or coverage level. Supports percentage-based or fixed-amount contributions with effective dating.

### HR Benefit Cost Allocation
Defines how employer benefit costs are allocated across funds, cost centers, grants, or departments. Supports split allocations and effective dating.

### HR Benefit Deduction Code
Maps benefit enrollments to payroll deduction identifiers. Supports integration with payroll systems and deduction tracking.

### HR Benefit Claim
Tracks internal benefit-related claims or reimbursement requests (e.g., tuition reimbursement, wellness reimbursement). Includes submission details, approval status, payment status, and associated enrollment.

### Person *(Core)*
Represents employees and beneficiaries throughout the benefit lifecycle.

### Organization Unit *(Core)*
Used for plan administration, eligibility rules, and cost allocation.

### Account *(Core)*
Represents benefit providers and carriers.

### Agreement *(Core)*
Service agreements with benefit providers.

### Legal Authority *(Core)*
Regulatory basis for benefit plans (ERISA, ACA, etc.).

### Compliance Framework *(Core)*
Compliance requirements for benefit administration.

### Document *(Core)*
Plan documents, SPDs, enrollment forms, claim documentation.

### Personnel Type *(Core)*
Used in eligibility rules and contribution rate structures.

### Pay Grade *(Core)*
Used in eligibility rules and tiered contribution structures.

### Benefit Category
- Medical
- Dental
- Vision
- Life Insurance
- Disability
- Retirement
- Health Savings Account
- Flexible Spending Account
- Wellness
- Tuition Assistance
- Employee Assistance Program
- Commuter Benefits
- Legal Services
- Pet Insurance

### Coverage Type
- Employee Only
- Employee Plus Spouse
- Employee Plus Dependents
- Employee Plus Family
- Retiree
- Continuation Coverage

### Provider Type
- Insurance Carrier
- Third Party Administrator
- Retirement Board
- Health Maintenance Organization
- Preferred Provider Organization
- Self-Insured
- Government Agency

### Benefit Document Type
- Summary Plan Description
- Policy Document
- Enrollment Form
- Evidence of Coverage
- Certificate of Insurance
- Regulatory Filing
- Plan Amendment
- Summary of Benefits and Coverage

### Eligibility Rule Type
- Employment Type
- Personnel Type
- Service Duration
- Full Time Equivalent
- Organization Unit
- Location
- Pay Grade
- Age Based
- Bargaining Unit
- Combination

### Waiting Period Type
- Days from Hire
- First of Month Following
- First Day of Month After Days
- Immediate
- Plan Year Start
- Custom

### Calculation Method
- Calendar Days
- Business Days
- From Start Date
- From Eligibility Date

### Enrollment Period Type
- Open Enrollment
- New Hire Enrollment
- Special Enrollment
- Life Event Enrollment
- Annual Enrollment
- Qualifying Event

### Period Status
- Upcoming
- Active
- Closed
- Cancelled

### Enrollment Status
- Active
- Pending
- Pending Approval
- Approved
- Declined
- Terminated
- Waived
- Cancelled
- Suspended

### Enrollment Type
- New Enrollment
- Re-Enrollment
- Change
- Termination
- Waiver

### Enrollment Source
- Open Enrollment
- New Hire
- Life Event
- Administrative
- Reinstatement

### Deduction Frequency
- Per Pay Period
- Monthly
- Quarterly
- Annually
- Semi-Monthly
- Bi-Weekly
- Weekly

### Election Type
- Optional Rider
- Supplemental Coverage
- Buy-Up Option
- Beneficiary Election
- Contribution Amount
- Coverage Amount

### Beneficiary Type
- Primary
- Contingent
- Secondary
- Estate

### Relationship Type
- Spouse
- Domestic Partner
- Child
- Parent
- Sibling
- Other Relative
- Estate
- Trust
- Other

### Life Event Type
- Marriage
- Domestic Partnership
- Birth
- Adoption
- Legal Guardianship
- Divorce
- Legal Separation
- Death of Dependent
- Loss of Other Coverage
- Gain of Other Coverage
- Change in Employment
- Change in Residence
- Medicare Eligibility
- Court Order

### Event Status
- Reported
- Pending Documentation
- Verified
- Processed
- Expired
- Cancelled

### Enrollment Change Type
- Add Coverage
- Drop Coverage
- Change Option
- Change Coverage Level
- Add Dependent
- Remove Dependent
- Change Contribution
- Terminate

### Rate Type
- Standard
- Tiered by Age
- Tiered by Salary
- Tiered by Service
- Composite

### Contribution Type
- Fixed Amount
- Percentage of Premium
- Percentage of Salary
- Tiered

### Deduction Type
- Pre-Tax
- Post-Tax
- Employer Paid
- Shared

### Claim Type
- Medical Claim
- Dental Claim
- Vision Claim
- Tuition Reimbursement
- Wellness Reimbursement
- Dependent Care
- Flexible Spending Account
- Health Savings Account
- Other Reimbursement

### Claim Status
- Submitted
- Under Review
- Approved
- Partially Approved
- Denied
- Paid
- Closed

### Payment Status
- Pending
- Approved
- Processed
- Paid
- Cancelled
- On Hold

### Verification Status
- Not Required
- Pending Verification
- Verified
- Rejected
- Needs Information
