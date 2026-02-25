---
title: "Training and Certification Data Model"
module: training-and-certification
---

The **Training and Certification** module provides a comprehensive framework for managing learning delivery, academic programs, credentialing, and eligibility requirements across higher education, workforce development, and regulated industries. It supports defining training courses and sessions (classes), organizing structured curricula through learning paths and academic programs, tracking enrollments, attendance, and completions, and awarding certificates with lifecycle management including renewals and expiration tracking. The module also enables configurable qualification requirements that can be applied to roles, access privileges, programs, or operational activities, ensuring individuals meet required training, credential, or competency standards. Common use cases include university course and degree management, corporate learning and development, professional certification programs, compliance-driven training environments, apprenticeship models, and readiness or eligibility enforcement across enterprise operations.


## Tables

### Training Course
Represents a catalog entry for a learning offering, including description, objectives, credit value, and prerequisites.

### Training Course Requirement
Represents prerequisite conditions required before enrolling in or completing a Training Course.

### Training Objective
Represents a learning objective or outcome associated with a Training Course.

### Training Instructor
Represents an individual authorized to deliver Training Sessions.

### Academic Term
Represents a defined academic period (e.g., Fall 2026, Spring 2027) used to organize and schedule Training Sessions.

### Training Session
Represents a scheduled offering of a Training Course within a specific Academic Term, often referred to as a "class" or "section."

### Training Enrollment
Represents an individual's registration in a specific Training Session.

### Training Session Attendance
Represents an individual's attendance status for a specific Training Session (and optionally per meeting occurrence).

### Training Completion
Represents an individual's successful or attempted completion of a Training Course, including result, score, and completion date.

### Learning Path
Represents an ordered or curated sequence of Training Courses intended to guide learners toward a specific outcome or skill set.

### Learning Path Course
Represents the association between a Learning Path and its component Training Courses, including sequence order and requirement status.

### Training Certificate
Represents a credential that may be awarded upon meeting defined requirements. Includes issuing authority, validity period, and renewal rules.

### Training Certificate Requirement
Represents the criteria required to earn a Training Certificate, such as completion of specific courses or paths.

### Training Certificate Achievement
Represents a specific instance of a Training Certificate awarded to an individual, including issue date, expiration date, and current status.

### Training Certificate Renewal
Represents a renewal event for a Training Certificate Achievement, including renewal date and updated expiration details.

### Academic Program
Represents a structured curriculum such as a degree, diploma, or formal certificate program. Contains overall program metadata, credit requirements, and governance information.

### Academic Program Requirement
Represents the specific course, path, credit, or rule requirements that must be met to complete an Academic Program.

### Academic Program Completion
Represents an individual's completion status for an Academic Program, including completion date, final standing, and honors if applicable.

### Qualification Requirement
Represents a reusable eligibility rule set that specifies what an individual must possess (courses, certificates, competencies) to perform a role, access a resource, or participate in an activity.

### Qualification Requirement Item
Represents an individual requirement within a Qualification Requirement, such as a required course, certificate, or competency level.

### Person *(Core)*
Learners, instructors, course owners, program directors, advisors.

### Organization Unit *(Core)*
Departments, training divisions, program ownership.

### Credential *(Core)*
Professional credentials required or linked to certificates.

### Competency *(Core)*
Skills and competencies linked to courses, certificates, and qualifications.

### Clearance Level *(Core)*
Security clearances required in qualification requirements.

### Compliance Framework *(Core)*
Regulatory frameworks for training and certification requirements.

### Legal Authority *(Core)*
Regulatory basis for training, certification, and qualification requirements.

### Event *(Core)*
Commencement ceremonies, graduation events.

### Document *(Core)*
Course materials, syllabi, certificates, transcripts, diplomas, supporting documentation.

### Course Type
- Instructor Led
- Online
- Hybrid
- Self Paced
- Workshop
- Seminar
- Lab
- Practicum
- Capstone

### Course Category
- Technical
- Professional Development
- Leadership
- Compliance
- Safety
- Operational
- Administrative
- Elective
- Core

### Course Level
- Introductory
- Intermediate
- Advanced
- Expert
- Refresher

### Delivery Method
- In Person
- Virtual
- Hybrid
- Self Paced
- Blended
- Asynchronous
- Synchronous

### Training Requirement Type
- Course Completion
- Certificate Held
- Credential Held
- Competency Level
- Experience
- Assessment
- Approval

### Objective Type
- Knowledge
- Skill
- Ability
- Behavior
- Performance

### Blooms Level
- Remember
- Understand
- Apply
- Analyze
- Evaluate
- Create

### Instructor Status
- Active
- Inactive
- Pending Approval
- Suspended
- Retired

### Instructor Type
- Full Time
- Adjunct
- Guest
- Subject Matter Expert
- Contractor
- Volunteer

### Term Type
- Fall
- Spring
- Summer
- Winter
- Quarter 1
- Quarter 2
- Quarter 3
- Quarter 4
- Intersession

### Term Status
- Planning
- Active
- Completed
- Archived

### Session Status
- Scheduled
- Open for Registration
- Registration Closed
- In Progress
- Completed
- Cancelled
- Postponed

### Session Type
- Regular
- Accelerated
- Intensive
- Weekend
- Evening
- Online
- Hybrid

### Enrollment Status
- Registered
- Confirmed
- Waitlisted
- Enrolled
- In Progress
- Completed
- Withdrawn
- Dropped
- No Show
- Cancelled

### Attendance Status
- Present
- Absent
- Tardy
- Excused
- Partial
- Remote

### Attendance Method
- In Person
- Virtual
- Remote
- Self Reported

### Pass Fail
- Pass
- Fail
- Incomplete
- Withdrawn

### Payment Status
- Not Required
- Pending
- Partial
- Paid
- Overdue
- Waived
- Refunded

### Completion Method
- In Person
- Online
- Hybrid
- Challenge Exam
- Transfer Credit
- Prior Learning Assessment

### Learning Path Type
- Career Path
- Skill Development
- Compliance Path
- Onboarding
- Professional Development
- Certification Prep

### Difficulty Level
- Beginner
- Intermediate
- Advanced
- Expert

### Certificate Type
- Professional Certification
- Compliance Certification
- License
- Credential
- Badge
- Award
- Recognition

### Recognition Level
- Internal
- Industry
- Regional
- National
- International

### Achievement Status
- Active
- Expired
- Suspended
- Revoked
- Pending Renewal
- Renewed

### Renewal Status
- Not Required
- Upcoming
- Submitted
- Under Review
- Approved
- Denied
- Completed
- Expired

### Renewal Method
- Continuing Education
- Re Examination
- Professional Development
- Work Experience
- Combination

### Academic Program Type
- Degree Program
- Certificate Program
- Diploma Program
- Credential Program
- Professional Program

### Academic Program Level
- Associate
- Bachelor
- Master
- Doctoral
- Post Doctoral
- Professional
- Certificate
- Diploma

### Program Requirement Type
- Core Course
- Elective Course
- Concentration Course
- Capstone
- Thesis
- Dissertation
- Practicum
- Internship
- Credit Hours

### Program Completion Status
- Prospective
- Admitted
- Enrolled
- Active
- On Leave
- Completed
- Graduated
- Withdrawn
- Dismissed

### Academic Standing
- Good Standing
- Academic Probation
- Academic Warning
- Dean's List
- Honor Roll
- Dismissed

### Academic Honors
- Summa Cum Laude
- Magna Cum Laude
- Cum Laude
- With Distinction
- With High Distinction
- With Highest Distinction

### Conferral Status
- Pending
- Conferred
- Deferred
- Withheld

### Qualification Requirement Type
- Role Qualification
- Access Qualification
- Operational Qualification
- Certification Requirement
- Licensing Requirement
- Safety Requirement

### Qualification Item Type
- Course Completion
- Learning Path Completion
- Certificate
- Credential
- Competency
- Clearance
- Assessment
- Experience

### Validation Frequency
- One Time
- Annual
- Biennial
- Triennial
- Quarterly
- On Demand
- Event Driven

### Enforcement Level
- Required
- Recommended
- Optional
- Advisory
