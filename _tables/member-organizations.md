---
title: "Member Organizations Data Model"
module: member-organizations
---

The **Member Organizations** module manages structured groups of people formed for a defined purpose, such as boards, councils, committees, panels, clubs, associations, and teams. It supports defining the organization itself, classifying its type, managing members and their roles, handling membership applications and fees, and organizing service terms. For governance-focused groups, it also enables formal decision-making through motions, votes, vote responses, and resolutions, providing a clear record of proposals and adopted outcomes. This module can be used for scenarios such as a board of directors approving resolutions, a city council recording votes, a professional association managing dues-paying members, a university committee tracking terms and roles, or a club reviewing membership applications and documenting decisions.


## Tables

### Organization
Represents a structured group of people formed for a defined purpose, such as a board, council, committee, club, association, or team. Supports hierarchical relationships to model parent and subordinate organizations.

### Organization Type
Classifies organizations by their structural or functional category (e.g., Board, Council, Committee, Club, Team).

### Organization Term
Defines a defined period of service or operational cycle for an organization (e.g., board term, fiscal year, season), used to structure membership tenure and governance activities.

### Organization Member
Represents an individual's membership in an organization, including status and participation details. Serves as the central record linking a person to a specific organization.

### Organization Member Type
Defines categories of membership within an organization (e.g., Regular, Student, Associate, Sponsor, Coach), used to classify members and determine eligibility or fee structures.

### Organization Member Role
Associates a member with a specific role within the organization (e.g., Chair, Treasurer, Captain), including effective dates when applicable.

### Organization Role
Defines reusable role types within organizations (e.g., Chair, Secretary, Member, Advisor), which can be assigned to organization members.

### Organization Member Application
Captures requests to join an organization, including applicant details, review status, approval decisions, and onboarding information.

### Organization Member Fee
Defines membership fees or dues associated with an organization or membership type, including amounts, frequency, and applicability rules.

### Organization Motion
Represents a formal proposal submitted for consideration within an organization's governance process. Motions may proceed to vote and result in resolutions.

### Organization Vote
Represents a formal voting event associated with a motion or decision, including voting method, quorum information, and outcome summary.

### Organization Vote Response
Captures an individual member's vote within a specific voting event (e.g., Yes, No, Abstain), providing detailed accountability and audit history.

### Organization Resolution
Represents an adopted decision or formal outcome of a motion or governance action. Serves as the official record of an organization's approved actions.
