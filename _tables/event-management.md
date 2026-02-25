---
title: "Event Management Data Model"
module: event-management
---

The **Event Management** module provides a structured system for planning, organizing, and executing events of all types and scales. It manages event definitions, participant registration and tracking, session scheduling, presentation and exhibition submissions, and sponsorship arrangements. The module supports detailed participant management including role assignments, check-in tracking, and certificate issuance. Sessions can be organized into tracks with scheduled time blocks, locations, and capacity management. The module accommodates submission workflows for presentations, posters, and exhibitions with review and approval processes. Typical use cases include conferences and symposiums, training events and workshops, public hearings and town halls, festivals and community events, board meetings and governance sessions, webinars and virtual events, and hybrid event formats combining in-person and virtual participation.

## Tables

### Event
The primary record representing a planned occurrence (conference, meeting, hearing, training, festival, etc.). Stores core details such as title, description, dates, location, status, and overall ownership.

### Event Type
A classification table defining categories of events (e.g., Conference, Training, Public Hearing, Webinar). Often used to drive default behaviors, templates, or required fields.

### Event Track
Represents a thematic or organizational grouping within an event (e.g., "Technology," "Policy," "Community Outreach"). Sessions and/or entries may be associated with a track.

### Event Request
Captures a proposed or requested event prior to formal approval or scheduling. Used for intake, evaluation, and approval workflows before an official Event record is created.

### Event Participant
Represents an individual or organization involved in the event. This can include attendees, speakers, staff, volunteers, exhibitors, VIPs, or panelists. Tracks participation status (invited, registered, confirmed, checked-in, etc.).

### Event Session Participant
Links participants to specific sessions. Used when attendance, roles, or responsibilities differ by session (e.g., a speaker in one session, attendee in another).

### Event Session
Represents a scheduled time block within an event (e.g., breakout session, hearing segment, workshop, keynote slot). Includes start/end time, location/room, capacity, and session-specific details.

### Event Entry
Represents an exhibition, presentation, booth, poster, demonstration, or other showcased submission within an event. Typically includes submission details, review/approval status, assigned session or track, and associated presenters.

### Event Sponsor
Represents an organization or entity providing financial or in-kind support for the event. May track sponsorship level, benefits, commitments, and related agreements.

### Event Status
- Draft
- Planning
- Open for Registration
- Registration Closed
- In Progress
- Completed
- Cancelled
- Postponed

### Event Format
- In Person
- Virtual
- Hybrid

### Participant Type
- Attendee
- Speaker
- Presenter
- Panelist
- Moderator
- Staff
- Volunteer
- Exhibitor
- Sponsor Representative
- VIP
- Media

### Participation Status
- Invited
- Tentative
- Registered
- Confirmed
- Waitlisted
- Checked In
- Attended
- No Show
- Cancelled
- Declined

### Payment Status
- Not Required
- Pending
- Partial
- Paid
- Refunded
- Waived
- Complimentary

### Session Role
- Presenter
- Co-Presenter
- Moderator
- Panelist
- Attendee
- Facilitator
- Note Taker

### Session Type
- Keynote
- Breakout Session
- Workshop
- Panel Discussion
- Roundtable
- Poster Session
- Networking
- Reception
- General Session
- Training

### Session Status
- Scheduled
- In Progress
- Completed
- Cancelled
- Rescheduled

### Entry Type
- Presentation
- Poster
- Exhibition Booth
- Demonstration
- Workshop
- Lightning Talk
- Video Submission
- Abstract Only

### Entry Status
- Submitted
- Under Review
- Accepted
- Rejected
- Waitlisted
- Withdrawn
- Confirmed

### Sponsorship Level
- Title Sponsor
- Platinum
- Gold
- Silver
- Bronze
- Supporting
- In Kind

### Sponsorship Type
- Financial
- In Kind
- Media Partner
- Venue Partner
- Technology Partner
- Community Partner
