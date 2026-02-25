---
title: "Programs and Services Data Model"
module: programs-and-services
---

The **Programs and Services** module provides a structured framework for defining what an organization offers, who is eligible, who is participating, and what officially occurred as a result of service delivery. It separates strategic structure (Program, Service, Service Offering), eligibility configuration (Service Eligibility Rule and related scoping), and operational execution (Service Participation, Service Activity, Service Result), allowing services to be consistently defined and delivered across contexts. This module supports public sector use cases such as benefits administration, grants management, community assistance programs, and workforce initiatives, as well as commercial scenarios such as customer onboarding, subscription services, vendor programs, and training offerings. By cleanly distinguishing between enrollment, operational activities, and auditable outcomes, the module enables reusable service design, lifecycle tracking, and integration with related domains like Claims Processing, Permits and Licensing, Case Management, and Financial Management.


## Tables

### Program
Represents a high-level initiative or policy area under which services are offered. A Program groups related Services and provides strategic, organizational, or funding context.

### Service
Represents a defined type of service provided under a Program. A Service describes what is offered in general terms and may have one or more Service Offerings over time.

### Service Category
Represents a classification used to group Services for reporting, organization, or navigation purposes. Categories help structure the service catalog without affecting delivery logic.

### Service Offering
Represents a specific version or configuration of a Service, typically bounded by time, geography, or policy parameters. A Service Offering defines the concrete instance of a Service that participants may enroll in.

### Service Eligibility Rule
Represents a reusable eligibility condition that may be applied to one or more Service Offerings. Eligibility Rules define qualification logic but are not scoped to a specific offering until linked.

### Service Offering Eligibility Rule
Represents the association between a Service Offering and a Service Eligibility Rule. This table defines which eligibility rules apply to a specific offering and may control rule behavior (e.g., required, optional, effective dates).

### Service Offering Geography
Represents geographic constraints or applicability for a Service Offering. This table defines where an offering is available or valid.

### Service Participation
Represents a person's or organization's enrollment or engagement in a specific Service Offering. This table anchors the lifecycle of participation, including status, dates, and eligibility determination.

### Service Activity
Represents an operational event or action performed during delivery of a Service to a specific Participation. Service Activities track the timeline of work or milestones related to service execution.

### Service Result
Represents an official, factual outcome that occurred for a specific Service Participation. Examples include approval, denial, issuance, adjustment, or completion. Service Results are auditable and historical.

### Service Result Type
Represents the predefined set of allowable result classifications that may be applied to Service Results. This table defines the controlled vocabulary of possible outcomes.

### Person *(Core)*
Represents participants, program managers, service owners, case managers, decision makers.

### Account *(Core)*
Represents participant organizations, service providers.

### Organization Unit *(Core)*
Administering units, owning units, provider units.

### Organization Initiative *(Core)*
Strategic initiatives that programs support.

### Location *(Core)*
Service delivery locations, geographic areas.

### Judicial District *(Core)*
Service area definitions for geographic scope.

### Action Item *(Core)*
Tasks linked to service activities and follow-ups.

### Agreement *(Core)*
Participation agreements, service agreements.

### Legal Authority *(Core)*
Regulatory basis for programs, services, and eligibility.

### Formal Decision *(Core)*
Official decisions linked to service results.

### Document *(Core)*
Policy documents, guides, supporting documentation, result documents.

### Privacy Consent *(Core)*
Participant consent tracking.

### Credential, Competency, Clearance Level *(Core)*
Used in eligibility rules.

### Program Type
- Benefits Program
- Grant Program
- Assistance Program
- Workforce Program
- Community Program
- Training Program
- Support Services
- Customer Program
- Vendor Program
- Subscription Program

### Service Type
- Direct Service
- Support Service
- Benefit Service
- Information Service
- Referral Service
- Assessment Service
- Training Service
- Consultation Service

### Delivery Method
- In Person
- Virtual
- Hybrid
- Self Service
- Phone
- Mail
- Mobile
- Home Visit

### Service Level
- Standard
- Priority
- Expedited
- Emergency
- Premium

### Offering Status
- Planning
- Open for Enrollment
- Enrollment Closed
- Active
- Completed
- Cancelled
- Suspended

### Eligibility Rule Type
- Age Based
- Income Based
- Residency Based
- Employment Based
- Credential Based
- Risk Based
- Need Based
- Asset Based

### Eligibility Rule Category
- Minimum Requirement
- Preferred Qualification
- Disqualifying Condition
- Priority Factor
- Scoring Criteria

### Geographic Scope
- National
- Regional
- State
- County
- City
- District
- Facility
- Multiple Locations

### Participation Status
- Prospective
- Pending Eligibility
- Eligible
- Enrolled
- Active
- Suspended
- Completed
- Terminated
- Waitlisted
- Ineligible
- Withdrawn

### Activity Type
- Enrollment
- Assessment
- Consultation
- Service Delivery
- Follow Up
- Review
- Monitoring
- Evaluation
- Communication
- Documentation
- Referral

### Result Status
- Pending
- Approved
- Denied
- Adjusted
- Appealed
- Reversed
- Expired
- Cancelled

### Result Category
- Approval
- Denial
- Certification
- Issuance
- Adjustment
- Renewal
- Termination
- Completion
- Referral
