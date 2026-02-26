---
title: "Core Data Model"
module: core
---

## Tables

### Organization Unit

The **Organization Unit** table represents organizational structure entities such as departments, divisions, programs, teams, offices, or external partner organizations. Each record includes a name, organization unit type assignment for categorization (e.g., Division, Office, Program), parent organization unit references for hierarchy modeling, and contact information including primary contact person, phone, email, and website. Additional fields support descriptions, notes, organizational codes, and status tracking to manage the complete organizational structure from headquarters through field offices and partner entities.

### Organization Unit Type

The **Organization Unit Type** table categorizes organization units into standard types (e.g., Headquarters, Regional Office, Division, Bureau, Program Office, External Partner) with type names, descriptions, and type codes for consistent organizational taxonomy and reporting segmentation.

### Account

The **Account** table (from Dataverse Account entity) represents external organizations including partners, vendors, contractors, member organizations, or counterparty entities. Standard Dataverse account fields support organization names, addresses, contact information, account numbers, and relationship management, enabling modules to reference external entities in agreements, procurement, partnerships, and external engagement scenarios.

### Person

The **Person** table (from Dataverse Contact entity) represents individuals throughout the enterprise including employees, contractors, partners, constituents, or external participants. Standard Dataverse contact fields provide name, contact information, demographic data, and relationship context. The only custom field is Custom Page State for UI state persistence, with other person-related data captured through related tables like Personal Information, Credential Assignments, and module-specific references.

### Personal Information

The **Personal Information** table extends person records with structured sensitive data elements categorized by information type (e.g., SSN, Passport Number, Emergency Contact, Medical Information, Dietary Restrictions). Each record links to a person and personal information type, captures the information value, includes effective and expiration dates for time-bound information, security classification, verification tracking (is verified, verified by, verified date), and name/description fields. This maintains privacy-protected personal data with controlled access and verification audit trails.

### Personal Information Type

The **Personal Information Type** table defines categories of personal information with type names, descriptions, type codes, general category classification, sensitivity indicators (is sensitive flag), and verification requirement indicators to establish personal information taxonomy and handling requirements.

### Organization Initiative

The **Organization Initiative** table documents strategic initiatives, programs, campaigns, or organizational priorities with initiative names, descriptions, start and end dates, initiative status tracking, responsible organization units, executive sponsors, parent initiative hierarchies for nested initiative structures, and outcome descriptions. This enables initiative portfolio management, strategic alignment tracking, and cross-module initiative references.

### Location

The **Location** table captures physical places including sites, buildings, floors, rooms, storage areas, or geographic coordinates with location names, descriptions, full addresses (street, city, state/province, postal code, country references), location types, parent location hierarchies for site-building-room nesting, GPS coordinates (latitude/longitude), and status indicators. This supports asset placement, position assignments, meeting locations, telework sites, and facility management across all modules.

### Country

The **Country** table provides country reference data with country names and standard abbreviations for address standardization and geographic categorization.

### State or Province

The **State or Province** table maintains state and province reference data with full names, abbreviations, and country associations for address validation and geographic reporting.

### Judicial District

The **Judicial District** table supports government and legal scenarios with judicial district names, district codes, jurisdiction levels (federal, state, county, municipal), presiding judge assignments, state/province context, parent judicial district hierarchies, and descriptions for geographic legal jurisdiction management.

### Personnel Type

The **Personnel Type** table categorizes workforce segments with type names, descriptions, type codes, and associated employment types (full-time, part-time, temporary, contract, volunteer) to support differentiated policies, benefits, compensation structures, and reporting requirements across employment categories.

### Job Series

The **Job Series** table groups related occupations into occupational families (e.g., Information Technology, Legal, Administrative, Medical) with series names, descriptions, and series codes for classification systems, career progression planning, and workforce analytics.

### Pay Grade

The **Pay Grade** table establishes salary grade structures with grade names, minimum/midpoint/maximum salary values (with currency support), and exchange rates to define compensation ranges for positions, job classifications, and employment actions.

### Grade-Rank

The **Grade-Rank** table combines grade and rank identifiers for organizations using hierarchical workforce structures (military, uniformed services, grade-based career ladders) with grade-rank names, associated pay grades, descriptions, and identifiers, enabling grade and rank-based compensation and advancement frameworks.

### Clearance Level

The **Clearance Level** table defines security clearance requirements with clearance names, clearance codes, security level numeric indicators for comparison ordering, and descriptions to support position clearance requirements and personnel security eligibility tracking in sensitive environments.

### Competency

The **Competency** table documents skills, knowledge areas, abilities, or behavioral competencies with competency names, codes, descriptions, general category classification, and parent competency hierarchies to build competency frameworks for workforce development, position requirements, training planning, and performance management.

### Credential Type

The **Credential Type** table categorizes certifications, licenses, qualifications, or accreditations with type names, descriptions, credential type codes, issuing organizations, validity periods (days), renewal requirement indicators, general category classification, competency linkages for skill mapping, and parent credential type hierarchies. This standardizes credential tracking and supports certification management, professional licensing, and qualification validation.

### Credential Assignment

The **Credential Assignment** table links persons to credential types documenting individual certification or licensure status. Records capture credential numbers, issue/expiration/renewal dates, certification status (active, expired, suspended, revoked), person and credential type references, supporting documents for verification, and names/descriptions. This maintains workforce credential inventories, tracks expiration for renewal planning, and supports qualification verification.

### Agreement

The **Agreement** table documents formal commitments, contracts, MOUs, inter-agency agreements, partnership arrangements, or service level agreements. Records include agreement numbers, names, agreement types and status, effective and expiration dates, primary and counterparty organizations, primary contacts, organization unit ownership, descriptions and key terms, total value with currency support, parent agreement references for master agreements with amendments or task orders, and supporting document linkages. This provides enterprise agreement inventory, commitment tracking, and partnership coordination.

### Formal Decision

The **Formal Decision** table captures official decisions made through governance processes with decision names, decision types (policy, strategic, operational, budgetary, personnel), decision dates, effective dates, decision makers, decision authority organizations, decision rationales, decision status, approval status, related organization initiatives for strategic alignment, and supporting documents. This maintains governance decision records for transparency, accountability, and audit compliance.

### Discussion Item

The **Discussion Item** table manages meeting agenda items, policy discussion topics, or deliberation points with item names, descriptions, discussion types, discussion dates, discussion status, parent discussion item threading for sub-topics, formal decision linkages when discussions result in decisions, submitter and assigned to references, priority indicators, and notes. This supports structured meeting management and discussion-to-decision workflows.

### After Action Report

The **After Action Report** table documents event retrospectives or lessons learned with report numbers, names, event and report dates, report authors, reporting organization units, executive summaries, "what went well" and "areas for improvement" narratives, recommendations, overall assessments (successful, mixed, needs improvement), general category classification, related initiative linkages, and supporting documents. This enables organizational learning, continuous improvement, and best practice sharing.

### Legal Authority

The **Legal Authority** table captures statutes, regulations, executive orders, policies, directives, legal opinions, or governing legal instruments with authority names, citations, document numbers, authority types and status, jurisdiction levels (federal, state, local, international), issuing authority and body references, enactment/effective/expiration dates, full text URLs, summaries, disposition notes for amendments or repeal tracking, parent legal authority hierarchies, and supporting document linkages. This provides legal authority inventory, citation management, and regulatory compliance foundation.

### Legal Amendment

The **Legal Amendment** table tracks changes to legal authorities with amendment names, numbers, and dates, effective dates, changes summaries, legal authority impact indicators (major, minor, clarification, repeal), original authority references, descriptions, and supporting documents to maintain amendment history and legal authority version control.

### Legal Cross-Reference

The **Legal Cross-Reference** table documents relationships between legal authorities (implements, modifies, supersedes, references, contradicts) with cross-reference names, primary and related authority references, relationship types via general category classification, impact indicators, and descriptions to map legal authority networks and dependency analysis.

### Compliance Framework

The **Compliance Framework** table defines regulatory, policy, or standard frameworks (FISMA, NIST Cybersecurity Framework, ISO 27001, HIPAA, SOX, Privacy Shield) with framework names, codes, categories, versions, issuing organizations, publication status, effective dates, scope descriptions, parent framework hierarchies for framework families or versions, and supporting documents. This establishes compliance program structure and regulatory mapping foundation.

### Compliance Framework Category

The **Compliance Framework Category** table organizes compliance frameworks into taxonomic groupings (cybersecurity, privacy, financial, safety, quality) with category names, codes, descriptions, and parent category hierarchies to support framework classification and reporting segmentation.

### Compliance Requirement

The **Compliance Requirement** table details specific compliance obligations or controls with requirement names, numbers, compliance frameworks and categories, legal authority references establishing the requirement basis, control objectives, descriptions, compliance status, priority, responsible organization units, general category classification, parent requirement hierarchies for multi-level control frameworks, and supporting documents. This maps regulatory requirements to organizational accountability for compliance management and audit preparation.

### Risk Item

The **Risk Item** table documents threats, vulnerabilities, uncertainties, or risk events with risk names, numbers, descriptions, general category classification, likelihood and severity assessments, overall risk level calculations, identified by and identified date attribution, impact descriptions, mitigation strategies, action status tracking, analysis linkages for risk assessments, owning organization units, and parent risk hierarchies for risk breakdown structures. This enables enterprise risk management, risk registers, and risk-informed decision making.

### Impact

The **Impact** table captures consequences, effects, or outcomes with impact names, descriptions, impact types, severity levels, status tracking, affected parties, risk item associations, analysis references, and general category classification to document impacts from risks, decisions, projects, or events for impact assessment and evaluation.

### Analysis

The **Analysis** table documents analytical studies, research, assessments, or evaluations with analysis names, numbers, dates, conducted by attributions, findings and recommendations narratives, action status, general category classification, owning organization units, and supporting documents. Analysis records maintain bidirectional linkages to associated risk items and impacts, enabling evidence-based findings to inform risk and impact management, and supporting analytical rigor in decision support.

### Document

The **Document** table provides centralized document repository functionality with document names, numbers, titles, versions, document types via general category, publication status, effective dates, security classifications, visibility controls, descriptions, file attachments, and notes. Documents can be referenced from legal authorities, agreements, compliance frameworks, analyses, credentials, decisions, and other entities requiring document evidence or supporting materials for comprehensive document management.

### Content Template

The **Content Template** table maintains reusable content patterns or boilerplate text with template names, template content (HTML or markdown), versions, effective dates, general category categorization, and descriptions for standardized document generation, automated communications, or content consistency.

### Privacy Consent

The **Privacy Consent** table documents individual consent for data processing with consent names, types via general category, consent status, consent and expiration dates, purpose and scope narratives, person references, revoked by and revoked date tracking for consent withdrawal, supporting consent documents, and user references for consent collector attribution. This supports GDPR Article 6 lawful basis, CCPA consent requirements, and privacy regulation compliance.

### Product

The **Product** table represents goods, services, or standard items with product names, numbers, codes, descriptions, specifications, general category classification, manufacturers, URLs, unit prices with currency support, unit of issue indicators (each, box, case, hour, etc.), and parent product hierarchies for product families, variants, or assemblies. Products can be referenced by procurement, asset management, inventory, catalog, or service delivery modules for standardized product data.

### Fiscal Period

The **Fiscal Period** table represents budgetary timeframes including fiscal years, quarters, or months with period names, start and end dates, and parent fiscal period hierarchies for multi-level fiscal calendars (year containing quarters containing months), supporting financial planning, budget cycles, and fiscal reporting.

### Action Item

The **Action Item** table provides general-purpose task tracking capability for items requiring follow-up action. While the ERD doesn't show this entity (not enough relationships to appear in filtered diagram), it's a foundational task management entity available for modules to reference or extend for action tracking, tasking, and to-do management functionality.