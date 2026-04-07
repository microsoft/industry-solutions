---
layout: post
title: "New Release: HR Recruiting Module (v1.1.0.0)"
date: 2026-04-07
categories: [modules, workforce]
tags: [hr-recruiting, recruiting, hiring, workforce, data-model]
---

We're excited to announce the initial data model release of the **HR Recruiting module** (v1.1.0.0), enabling organizations to manage the complete hiring lifecycle from workforce planning through candidate selection and offer management.

The HR Recruiting module provides structured workflows for requisition management, candidate tracking, evaluation, and selection. It supports merit-based civil service hiring, corporate recruiting, campus hiring, internal mobility, and high-volume talent acquisition across public sector, corporate, and regulated environments.

## Key Capabilities

- **Workforce Planning**: Create workforce requests to justify new or replacement positions before initiating formal recruitment
- **Requisition Management**: Track authorized recruitment efforts with detailed hiring requirements, salary ranges, and approval workflows
- **Multi-Channel Posting**: Advertise positions across internal job boards, external career sites, and specialized platforms with versioned content
- **Candidate Profiles**: Maintain persistent recruiting profiles with contact information and application history across multiple opportunities
- **Application Tracking**: Monitor candidate submissions through evaluation lifecycle with status progression and decision tracking
- **Structured Evaluation**: Assess candidates against weighted qualification criteria using skill assessments tied to requisition requirements
- **Interview Coordination**: Schedule and track interviews with support for phone, panel, virtual, and in-person formats
- **Evaluator Scoring**: Capture individual reviewer assessments with rubric-based scoring and competency ratings
- **Selection Decisions**: Document formal hiring decisions with selected candidate identification, ranking, and approval justification
- **Offer Management**: Extend employment offers with compensation details, terms, negotiation tracking, and acceptance workflow
- **Pre-Hire Requirements**: Track conditional requirements such as background checks, credential verification, and security clearance
- **Defensible Selection**: Leverage shared competency frameworks and documented evaluation criteria for merit-based decisions
- **Compliance Support**: Link selection decisions to legal authorities and formal decision records when required

## What's Included

This release includes the **HR Recruiting data model** (v1.1.0.0) with 13 custom tables:

- HR Workforce Request
- HR Requisition
- HR Requisition Posting
- HR Requisition Requirement
- HR Candidate
- HR Application
- HR Application Skill Assessment
- HR Application Evaluation
- HR Interview
- HR Evaluation
- HR Selection Decision
- HR Offer
- HR Pre-Hire Requirement

Forms, views, and additional user interface components will be included in a future release.

This module integrates with the **Core module** for shared entities including Person, Organization Unit, Location, Job Series, Pay Grade, Clearance Level, Competency, Credential, Document, Legal Authority, and Privacy Consent.

## Getting Started

To use the HR Recruiting module in your environment:

1. Review the [HR Recruiting module documentation]({{ site.baseurl }}{% link _modules/hr-recruiting.md %})
2. Explore the [data model reference]({{ site.baseurl }}{% link _tables/hr-recruiting.md %})
3. Download the solution from the [industry-apps repository](https://github.com/jeremyhorgan/industry-apps)
4. Import the HR Recruiting solution into your Power Platform environment
5. Configure requisition workflows, posting channels, and evaluation criteria to match your hiring processes

We look forward to your feedback as you begin using the HR Recruiting module!
