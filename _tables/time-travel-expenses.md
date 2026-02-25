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

### Person *(Core)*
Travelers, time entry submitters, approvers, reviewers.

### Organization Unit *(Core)*
Cost centers, organizational ownership of time codes and expenses.

### Organization Initiative *(Core)*
Strategic initiatives linked to time entries and travel requests.

### Location *(Core)*
Work locations, travel origins, destinations, segment locations.

### Project *(Core)*
Projects linked to time entries, time codes, commitments, and travel.

### Project Work Item *(Core)*
Work items linked to time entries.

### Action Item *(Core)*
Tasks linked to time entries and commitments.

### Event *(Core)*
Events linked to travel requests (conferences, trainings).

### Document *(Core)*
Supporting documentation, receipts, trip reports, authorizations.

### Time Period Type
- Weekly
- Biweekly
- Semimonthly
- Monthly
- Quarterly
- Annual
- Custom

### Period Status
- Future
- Open
- Pending Approval
- Approved
- Locked
- Closed

### Time Code Category
- Operational
- Project
- Initiative
- Administrative
- Leave
- Training
- Travel
- Investigative
- Direct Work
- Indirect Work

### Entry Status
- Draft
- Submitted
- Under Review
- Approved
- Rejected
- Locked

### Commitment Type
- Work Assignment
- Duty Schedule
- Leave
- Training
- Travel
- Meeting
- On Call
- Unavailable
- Other

### Commitment Status
- Planned
- Requested
- Approved
- Active
- Completed
- Cancelled

### Travel Purpose Category
- Training
- Conference
- Site Visit
- Inspection
- Audit
- Investigation
- Meeting
- Consultation
- Operational Support
- Emergency Response
- Customer Visit
- Vendor Visit

### Travel Request Status
- Draft
- Submitted
- Under Review
- Approved
- Authorized
- In Progress
- Completed
- Cancelled
- Rejected

### Transportation Method
- Air
- Rail
- Personal Vehicle
- Rental Car
- Government Vehicle
- Taxi / Rideshare
- Public Transit
- Walking
- Other

### Travel Segment Type
- Flight
- Ground Transportation
- Lodging
- Rental Car
- Rail
- Other

### Segment Status
- Planned
- Booked
- Confirmed
- In Progress
- Completed
- Cancelled

### Expense Category Type
- Lodging
- Meals
- Transportation
- Mileage
- Airfare
- Ground Transportation
- Registration
- Supplies
- Equipment
- Communication
- Parking
- Tolls
- Per Diem
- Other

### Expense Report Type
- Travel Expense
- Operational Expense
- Training Expense
- Project Expense
- Reimbursement
- Blanket Expense

### Report Status
- Draft
- Submitted
- Under Review
- Approved
- Payment Pending
- Paid
- Rejected
- Cancelled

### Item Status
- Entered
- Submitted
- Approved
- Rejected
- Paid

### Payment Method
- Personal Card
- Corporate Card
- Cash
- Check
- Direct Deposit
- Wire Transfer
- Reimbursement
