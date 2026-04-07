---
layout: post
title: "Programs and Services Module Now Available"
date: 2026-04-07
tags: [modules, releases]
---

We're excited to announce the **Programs and Services** module — a comprehensive framework for defining organizational offerings, configuring eligibility, tracking participation, and documenting service delivery outcomes.

## What is the Programs and Services Module?

The Programs and Services module provides structured lifecycle management for what organizations offer and how those offerings are delivered. It enables organizations to define programs and services with hierarchical structure, configure reusable eligibility rules and geographic scope, create versioned service offerings, enroll participants with eligibility tracking, document operational service activities, and capture auditable service results. By separating strategic structure from eligibility configuration and operational execution, the module enables consistent service design and delivery across public sector benefits administration, grants management, community assistance, workforce programs, and commercial customer onboarding, subscription services, and training offerings.

Key capabilities include:

- **Program Management** – Define high-level initiatives or policy areas that group related services with strategic context, organization ownership, funding sources, and hierarchical program structures
- **Service Definition** – Represent specific types of service provided under programs with service categories, legal authority references, and lifecycle tracking
- **Service Categorization** – Organize services using hierarchical classification taxonomies for reporting, navigation, and catalog structure
- **Service Offerings** – Create specific versions or configurations of services bounded by time, geography, or policy parameters with versioning support
- **Eligibility Rule Configuration** – Define reusable eligibility conditions including age ranges, income thresholds, residency requirements, employment status, clearance levels, competencies, and credentials
- **Offering Eligibility Assignment** – Link eligibility rules to specific service offerings with required/optional control, effective dates, and evaluation sequencing
- **Geographic Scoping** – Define where service offerings are available or valid by linking to locations, judicial districts, or geographic service areas
- **Participation Management** – Track enrollment or engagement in service offerings with participation status, enrollment dates, eligibility determinations, case manager assignment, and privacy consent
- **Service Activity Tracking** – Document operational events or actions performed during service delivery including appointments, assessments, training sessions, consultations, and interventions
- **Service Result Documentation** – Capture official, factual outcomes such as approvals, denials, issuances, adjustments, or completions with result type classification and formal decision linkage
- **Strategic Alignment** – Connect programs to organization initiatives and legal authorities to establish policy basis and strategic context
- **Agreement Integration** – Link service participations to formal participation or service agreements

## What's Included

This initial release (v1.1.0.0) provides the foundational data model:

- **11 entities** providing comprehensive program structure, service definition, eligibility configuration, participation tracking, activity management, and result documentation capabilities
- **Integration with Core module** for persons, accounts, organization units, organization initiatives, locations, judicial districts, action items, agreements, legal authorities, formal decisions, documents, privacy consent, credentials, competencies, and clearance levels

Forms and views for program administration, service catalog management, eligibility configuration, participation enrollment, activity tracking, and result processing will be available in an upcoming release. The module provides implementors with a baseline data structure that can be customized for benefits programs, grant administration, community services, workforce development, customer programs, vendor management, subscription services, and training delivery.

## Getting Started

The Programs and Services module is available in the [FAST Modules Repository](https://github.com/microsoft/industry-apps) under the MIT license. It requires the Core module as a foundation.

View the complete [Programs and Services module documentation]({{ '/modules/programs-and-services/' | relative_url }}) for entity descriptions, data model diagrams, and implementation guidance.
