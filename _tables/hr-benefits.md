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
