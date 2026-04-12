---
title: "Time, Travel, and Expenses"
description: "Capture time worked, plan personnel availability, authorize travel, and submit reimbursable expenses with unified time tracking, travel management, and expense reporting."
latest_release: v1.2.0.0
thumbnail: "assets/use_cases/time-travel-expenses.png"
module_category: workforce
required_modules:
  - core
required_data_models:
  - workforce/time-travel-expenses
related_use_cases:
  - Time, Travel, and Expenses
related_personas:
  - hr-administrator
---

The **Time, Travel, and Expenses module** provides a unified structure for capturing time worked, planning personnel availability, authorizing travel, and submitting reimbursable expenses. It enables individuals to record time against standardized time codes, plan future availability, request and manage travel with detailed itineraries, and submit costs through categorized expense reports.

## Using the Module

Time tracking begins with defining **Time Periods** to establish reporting cycles such as weeks or pay periods, and **Time Codes** to create hierarchical classification structures for categorizing work types. Personnel can then record actual work through **Time Entries** that capture dates, hours worked, and time code classifications, while **Time Commitments** can be created to plan future availability or obligations for scheduling and duty assignments.

When travel is required, organizations can configure **Travel Purposes** for standardized trip reasons, then create **Travel Requests** to authorize and track trips with traveler identification, dates, destinations, estimated costs, and approval workflows. Detailed itineraries can be documented through **Travel Segments** representing individual trip components such as flights, lodging, or rental cars with departure/arrival details and cost estimates.

For expense management, **Expense Categories** can be defined with reimbursement rules, maximum amounts, and policy controls. Personnel submit **Expense Reports** grouping multiple **Expense Items** for review and approval. Expense items can reference categories, link to travel segments, attach receipts, and support mileage calculations. This integrated approach enables organizations to manage time tracking, travel authorization, and reimbursement processing within a unified framework.

```mermaid
graph TD
  appbase_Country(Country)
  appbase_Document(Document)
  appbase_ExpenseCategory(Expense Category)
  appbase_ExpenseItem(Expense Item)
  appbase_ExpenseReport(Expense Report)
  appbase_OrganizationInitiative(Organization Initiative)
  appbase_StateorProvince(State or Province)
  appbase_TimeCode(Time Code)
  appbase_TimeCommitment(Time Commitment)
  appbase_TimeEntry(Time Entry)
  appbase_TimePeriod(Time Period)
  appbase_TravelPurpose(Travel Purpose)
  appbase_TravelRequest(Travel Request)
  appbase_TravelSegment(Travel Segment)
  appbase_ExpenseItem --> appbase_Country
  appbase_TravelRequest --> appbase_Country
  appbase_TravelRequest --> appbase_Country
  appbase_TravelSegment --> appbase_Country
  appbase_TravelSegment --> appbase_Country
  appbase_ExpenseItem --> appbase_Document
  appbase_ExpenseReport --> appbase_Document
  appbase_TravelRequest --> appbase_Document
  appbase_ExpenseCategory --> appbase_ExpenseCategory
  appbase_ExpenseItem --> appbase_ExpenseCategory
  appbase_ExpenseItem --> appbase_ExpenseReport
  appbase_TimeCode --> appbase_OrganizationInitiative
  appbase_TravelRequest --> appbase_OrganizationInitiative
  appbase_ExpenseItem --> appbase_StateorProvince
  appbase_TravelRequest --> appbase_StateorProvince
  appbase_TravelRequest --> appbase_StateorProvince
  appbase_TravelSegment --> appbase_StateorProvince
  appbase_TravelSegment --> appbase_StateorProvince
  appbase_TimeCode --> appbase_TimeCode
  appbase_TimeCommitment --> appbase_TimeCode
  appbase_TimeEntry --> appbase_TimeCode
  appbase_ExpenseReport --> appbase_TimePeriod
  appbase_TimeEntry --> appbase_TimePeriod
  appbase_TravelRequest --> appbase_TravelPurpose
  appbase_ExpenseReport --> appbase_TravelRequest
  appbase_TimeCommitment --> appbase_TravelRequest
  appbase_TimeEntry --> appbase_TravelRequest
  appbase_TravelSegment --> appbase_TravelRequest
  appbase_ExpenseItem --> appbase_TravelSegment
```
