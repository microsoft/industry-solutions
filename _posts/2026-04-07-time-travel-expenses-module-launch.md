---
layout: post
title: "Time, Travel, and Expenses Module Now Available"
date: 2026-04-07
tags: [modules, releases]
---

We're excited to announce the **Time, Travel, and Expenses** module — a unified framework for capturing time worked, planning personnel availability, authorizing travel, and submitting reimbursable expenses.

## What is the Time, Travel, and Expenses Module?

The Time, Travel, and Expenses module provides integrated tracking and reporting capabilities across time management, travel authorization, and expense reimbursement. It enables organizations to define time codes and reporting periods, record actual time worked with classification, plan future availability and commitments, authorize and manage travel requests with detailed itineraries, configure expense categories with policy controls, and submit expense reports with line-level expense items.

Key capabilities include:

- **Time Period Management** – Define reporting cycles such as weeks, pay periods, or months for grouping time entries and expense reports with fiscal alignment
- **Time Code Classification** – Establish hierarchical classification structures for categorizing time entries by investigations, operations, initiatives, or administrative activities
- **Time Entry Tracking** – Record actual time worked by persons with date, hours, time code classification, and time period grouping
- **Time Commitment Planning** – Plan future availability or obligations with defined date and time ranges for scheduling, duty assignments, or leave tracking
- **Travel Purpose Configuration** – Define standardized reasons for travel such as training, site visits, inspections, conferences, or official business
- **Travel Request Authorization** – Create primary authorization records for trips with traveler identification, purpose, dates, origin/destination, estimated costs, and approval workflows
- **Travel Segment Detailing** – Document individual trip components such as flights, lodging stays, rental cars, or ground transportation with itinerary details
- **Expense Category Configuration** – Define standardized expense classifications with reimbursement rules, maximum amounts, mileage calculation flags, and GL account assignments
- **Expense Report Submission** – Group multiple expense items for review and approval with time period alignment, travel request linkage, and status tracking
- **Expense Item Recording** – Capture individual expense transactions with dates, amounts, categories, receipt documentation, and travel segment associations
- **Policy Enforcement** – Configure maximum amounts per day or per trip for expense categories with policy compliance validation
- **Mileage Tracking** – Support mileage-based expense calculations with odometer or distance tracking for vehicle reimbursement
- **Strategic Alignment** – Link time codes and travel requests to organization initiatives for mission tracking and reporting
- **Approval Workflows** – Track submission, review, and approval stages for time entries, travel requests, and expense reports

## What's Included

This initial release (v1.1.0.0) provides the foundational data model:

- **10 entities** providing comprehensive time tracking, availability planning, travel authorization, itinerary management, and expense reimbursement capabilities
- **Integration with Core module** for persons, organization units, organization initiatives, countries, states/provinces, and documents

Forms and views for time entry submission, time commitment scheduling, travel request processing, itinerary planning, expense category administration, and expense report workflows will be available in an upcoming release. The module provides implementors with a baseline data structure that can be customized for operational time tracking, workforce scheduling, travel program management, and employee reimbursement processing across public sector, nonprofit, and commercial environments.

## Getting Started

The Time, Travel, and Expenses module is available in the [FAST Modules Repository](https://github.com/microsoft/industry-apps) under the MIT license. It requires the Core module as a foundation.

View the complete [Time, Travel, and Expenses module documentation]({{ '/modules/time-travel-expenses/' | relative_url }}) for entity descriptions, data model diagrams, and implementation guidance.
