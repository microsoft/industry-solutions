---
title: "Court Case Management Data Model"
module: court-case-management
---

The **Court Case Management** module provides a structured system for tracking legal matters through the court system, from case filing through final disposition. It manages core case information including parties, filings, hearings, orders, and decisions, while maintaining chronological docket entries for full case history. The module supports representation tracking, work item assignment, and court session scheduling. Typical use cases include civil litigation management, criminal case processing, administrative hearings, probate matters, family court proceedings, and appellate case tracking. It provides both operational case management and scheduling capabilities while ensuring comprehensive audit trails for all case activities.

## Tables

### Court Case

The primary record representing a legal matter before the court.
Tracks case number, type, jurisdiction, status, assigned judge, and overall lifecycle of the matter.

### Court Case Decision

Records a judicial ruling or determination made in a case.
Captures the decision type, date, deciding official, and links to related hearings or filings. May represent interim or final decisions.

### Court Case Docket Entry

The official chronological log entry for activity in a case.
Provides an audit-friendly record of filings, hearings, orders, and other significant case events.

### Court Case Filing

Represents a document or submission formally entered into the case record.
Includes motions and other filings submitted by parties or external entities, along with filing date and status.

### Court Case Hearing

Represents a scheduled case appearance or proceeding.
May be associated with a Court Session and records hearing type, scheduling details, and results.

### Court Case Order

Represents a formal directive issued by the court.
Often generated from a decision, and may include effective dates, status (draft/issued), and compliance implications.

### Court Case Party

Links a person or organization to a case in a defined role.
Used to track plaintiffs, defendants, petitioners, respondents, and other involved parties.

### Court Case Representation

Tracks representation relationships within a case.
Identifies which party is represented by which attorney, guardian, or agent, including effective dates.

### Court Case Work Item

Represents internal court staff tasks related to advancing a case.
Includes assignments, due dates, status, and links to related filings, hearings, or orders.

### Court Session

Represents a scheduled sitting of the court.
Defines the date, location, presiding official, and status of a court calendar block during which one or more case hearings may occur.
