---
title: "Gamification Data Model"
module: gamification
---

The **Gamification** module provides a structured way to encourage, track, and recognize desired behaviors across programs, teams, and initiatives. It allows organizations to define Games (time-bound or ongoing initiatives), configure Activities that represent measurable actions, and establish Achievements that participants can earn based on participation or performance. Participants (individuals or teams) generate Activity records through their actions, and when criteria are met, Achievement records are granted and tracked. This module can be used to reinforce training completion, safety compliance, case resolution timeliness, volunteer engagement, productivity milestones, wellness initiatives, community participation, or internal innovation efforts—making it a flexible behavioral reinforcement layer that can operate alongside workforce, compliance, training, service delivery, or operational modules across public or commercial environments.


## Tables

### Game
Represents a structured gamification initiative or campaign. A Game defines the scope, timeframe, participation model, and overall purpose of the engagement effort (e.g., training challenge, performance drive, volunteer campaign).

### Game Activity
Defines the types of actions that are tracked within a Game. Activities represent measurable behaviors such as completing training, closing a case, attending an event, or submitting a task. These are definitional and not transactional.

### Game Achievement
Defines the achievements that can be earned within a Game. These may represent badges, levels, milestones, point thresholds, or titles. This table stores the criteria and configuration for what participants can earn.

### Game Participant
Represents an individual or team enrolled in a specific Game. This table tracks participation status, enrollment, and contextual role within the Game (participant, admin, etc.), separate from the core person or team record.

### Game Participant Activity
Logs instances of Participants performing defined Game Activities. This table captures the behavioral history used to evaluate achievement criteria and calculate performance metrics.

### Game Participant Achievement
Records when a Participant earns a specific Game Achievement. This is the transactional recognition record, including when it was granted, its status, and any related activity or approval.

### Game Type
- Training Challenge
- Performance Drive
- Compliance Campaign
- Wellness Initiative
- Safety Program
- Volunteer Campaign
- Innovation Challenge
- Service Excellence
- Onboarding Program
- Community Engagement

### Game Status
- Planning
- Open for Enrollment
- Active
- Paused
- Completed
- Archived
- Cancelled

### Participation Model
- Individual
- Team
- Department
- Organization Wide
- Invitation Only
- Tiered

### Activity Type
- Training Completion
- Task Completion
- Event Attendance
- Case Resolution
- Time Logged
- Certification Earned
- Feedback Submitted
- Survey Completion
- Mentor Session
- Safety Report
- Innovation Submission
- Volunteer Hours

### Achievement Type
- Badge
- Level
- Tier
- Milestone
- Certificate
- Title
- Rank
- Recognition
- Reward

### Award Criteria Type
- Points Threshold
- Activity Count
- Activity Streak
- Time Based
- Performance Based
- Combination

### Participant Type
- Individual Participant
- Team Member
- Team Lead
- Game Administrator
- Observer

### Participation Status
- Invited
- Enrolled
- Active
- Inactive
- Completed
- Withdrawn
- Disqualified

### Activity Record Status
- Pending
- Verified
- Rejected
- Expired
- Voided

### Verification Status
- Not Required
- Pending Verification
- Verified
- Rejected
- Needs Information

### Achievement Record Status
- Earned
- Awarded
- Pending Approval
- Revoked
- Expired

### Recognition Status
- Not Recognized
- Pending
- Recognized
- Public
- Private
