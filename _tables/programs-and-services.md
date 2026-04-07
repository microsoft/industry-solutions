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
