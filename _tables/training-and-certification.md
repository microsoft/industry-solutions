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
