---
title: "⏱️ Time, Travel, and Expenses Data Model"
module: ⏱️-time,-travel,-and-expenses
---

The **Time, Travel, and Expense** module provides a unified structure for capturing time worked, planning personnel availability, authorizing travel, and submitting reimbursable expenses within an organization. It enables individuals to record time against standardized **Time Codes**, plan future availability through **Time Commitments**, request and manage travel through **Travel Requests** and **Travel Segments**, and submit costs through **Expense Reports** and **Expense Items** categorized by defined **Expense Categories**. This module supports use cases such as operational time tracking (e.g., investigations, casework, internal initiatives), workforce planning and duty scheduling, travel authorization and itinerary management, reimbursement processing, and financial reporting alignment with organizational units or funding sources. It is designed to be reusable across public sector, nonprofit, and commercial environments, supporting both lightweight tracking needs and scalable financial governance.


## Tables

### Time Period
Represents a defined reporting cycle such as a week, pay period, or month used to group Time Entries and optionally Expense Reports for administrative or financial purposes.

### Time Code
Represents a hierarchical classification structure used to categorize Time Entries. Supports parent/child relationships for organizing work types such as investigations, operations, initiatives, or administrative activities.

### Time Entry
Represents the actual time worked by a person on a specific date, including hours and associated Time Code. Serves as the foundational operational record for time tracking and reporting.

### Time Commitment
Represents a planned availability or obligation for a person over a defined date and time range. Used for scheduling, duty assignments, leave tracking, or other forward-looking planning purposes.

### Travel Purpose
Represents standardized reasons for travel such as training, site visits, inspections, or conferences. Used to categorize and report on Travel Requests.

### Travel Request
Represents a planned or approved trip, including traveler details, purpose, dates, and estimated costs. Serves as the primary authorization and oversight record for organizational travel.

### Travel Segment
Represents an individual component of a trip, such as a flight, lodging stay, or rental car, under a Travel Request. Enables structured tracking of itinerary details and associated estimated costs.

### Expense Category
Represents standardized classifications for expenses such as lodging, meals, mileage, registration fees, and supplies. Used to categorize Expense Items for reporting, policy enforcement, and financial analysis.

### Expense Report
Represents a grouped submission of multiple Expense Items for review, approval, and reimbursement. Serves as the primary expense workflow record for an individual reporting period or trip.

### Expense Item
Represents an individual expense transaction recorded under an Expense Report. Captures details such as date, amount, category, and optional travel linkage for reimbursement and accounting purposes.
