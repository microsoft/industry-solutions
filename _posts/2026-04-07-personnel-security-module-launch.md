---
layout: post
title: "Personnel Security Module Now Available"
date: 2026-04-07
tags: [modules, releases]
---

We're excited to announce the **Personnel Security** module — a comprehensive framework for managing trust-based access through security reviews, background investigations, adjudications, eligibility determinations, and ongoing monitoring.

## What is the Personnel Security Module?

The Personnel Security module provides structured lifecycle management for evaluating and granting trust-based access to individuals. It enables organizations to initiate and track security reviews, conduct formal background investigations, make adjudication decisions, issue security eligibility determinations, provision access credentials, enroll individuals in continuous evaluation programs, and track reportable events that may impact access status.

Key capabilities include:

- **Security Review Management** – Track initial reviews, renewals, upgrades, reciprocity evaluations, or incident-triggered reviews from initiation through final outcome with timeline and approval tracking
- **Background Investigation** – Conduct formal investigative efforts with investigation type, scope, provider tracking, and status management for records checks and vetting procedures
- **Adjudication Decisions** – Document formal determinations with outcome classification (favorable, unfavorable, conditional, deferred), decision authority, decision rationale, and investigation linkage
- **Security Eligibility** – Issue approved levels of trust, clearance, or access authorization with eligibility type, effective dates, expiration tracking, and reinvestigation requirements
- **Access Credential Management** – Provision physical or logical access artifacts such as badges, smart cards, mobile credentials, or tokens with issuance tracking, biometric enrollment, and status management
- **Continuous Evaluation** – Enroll individuals in ongoing monitoring or recurring vetting processes with automated record checks, privacy consent management, and risk indicator identification
- **Reportable Event Tracking** – Document foreign travel, foreign contacts, legal incidents, financial issues, security violations, or policy-defined reportable matters that may trigger reviews
- **Clearance Level Attribution** – Associate reviews, investigations, adjudications, eligibilities, and credentials with specific clearance or trust levels
- **Compliance Integration** – Link security reviews and eligibility determinations to compliance frameworks and legal authorities governing personnel security
- **Credential Lifecycle** – Track credential activation, suspension, revocation, expiration, replacement, and upgrade with access zone authorization and usage monitoring
- **Investigation Coordination** – Document investigation activities, provider coordination, completion status, and findings supporting adjudication decisions
- **Event-Triggered Reviews** – Initiate security reviews based on reportable events and continuous evaluation findings with incident linkage

## What's Included

This initial release (v1.1.0.0) provides the foundational data model:

- **7 entities** providing comprehensive personnel security vetting, eligibility management, credential administration, and continuous monitoring capabilities
- **Integration with Core module** for persons, clearance levels, compliance frameworks, legal authorities, formal decisions, privacy consent, countries, and documents

Forms and views for security review tracking, investigation coordination, adjudication processing, eligibility management, and credential administration will be available in an upcoming release. The module provides implementors with a baseline data structure that can be customized for government security programs, defense contractors, critical infrastructure operators, financial services institutions, healthcare organizations, and other regulated environments requiring formal personnel security vetting.

## Getting Started

The Personnel Security module is available in the [FAST Modules Repository](https://github.com/microsoft/industry-apps) under the MIT license. It requires the Core module as a foundation.

View the complete [Personnel Security module documentation]({{ '/modules/personnel-security/' | relative_url }}) for entity descriptions, data model diagrams, and implementation guidance.
