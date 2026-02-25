---
title: "Financial Management Data Model"
module: financial-management
---

Financial Management is an end-to-end module that supports the planning, acquisition, contractual oversight, and financial execution of goods and services. It enables organizations to define budgets and funding sources, validate availability of funds, manage procurement processes, formalize agreements through contracts and amendments, issue purchase orders, record financial commitments, and process payments. The module supports use cases such as departmental budget control, competitive sourcing and vendor selection, contract lifecycle management, project- or grant-funded spending, compliance-driven funds certification, and structured payment tracking. It provides traceability from initial request through contract award to final payment, ensuring financial accountability, operational transparency, and audit readiness across both public sector and commercial environments.


## Tables

### Budget
Represents an approved financial plan for a defined fiscal period and organizational scope. A Budget establishes the total planned spending authority and serves as the parent record for detailed allocations. It is used to monitor planned versus committed and expended amounts over time.

### Budget Line Item
Detailed allocation within a Budget tied to a specific Financial Funding Source, Financial Classification, and Financial Period. Budget Line Items define how funds are distributed across categories and are used during funds checks and commitment creation to ensure spending stays within approved limits.

### Financial Funding Source
Identifies the origin of funds used to finance expenditures, such as a grant, appropriation, cost center, project, or internal budget. Funding Sources are referenced by budgets, commitments, and transactions to maintain traceability and compliance.

### Financial Classification
A categorization structure used to classify financial transactions, such as expense type, revenue type, object class, or fee category. Financial Classifications support reporting, budget allocation, compliance, and accounting integration.

### Purchase Request
An internal request to procure goods or services, typically initiated by program or operational staff. Purchase Requests capture business justification, estimated cost, and required approvals prior to sourcing or issuing a purchase order.

### Purchase Request Item
Line-level detail associated with a Purchase Request, specifying requested goods or services, quantities, and estimated pricing. These items support evaluation, sourcing, and budget validation activities.

### Procurement Package
A container for a sourcing process, such as a Request for Quote (RFQ), Request for Proposal (RFP), or sole-source procurement. The Procurement Package tracks vendor responses, evaluations, approvals, and award decisions prior to contract execution.

### Contract
A formal agreement with an external organization defining scope of work, pricing structure, performance period, terms and conditions, and total authorized value. Contracts serve as the governing instrument under which purchase orders, deliverables, and payments are executed.

### Contract Amendment
A modification to an existing Contract that changes scope, funding amount, pricing, performance period, or contractual terms. Amendments maintain a structured history of changes and ensure traceability of contract evolution over time.

### Contract Line
A structured pricing or scope element within a Contract, such as a labor category, fixed-price item, or cost-reimbursable component. Contract Lines allow financial tracking and purchase orders to align with defined contract elements.

### Contract Deliverable
A specific output, service, or product required under a Contract. Deliverables typically include due dates, acceptance criteria, and status tracking to monitor contractual performance and compliance.

### Contract Milestone
A significant contractual event or date, such as kickoff, phase completion, renewal decision, or option exercise. Milestones help monitor contract lifecycle progress and key decision points.

### Financial Commitment
Represents funds that have been formally reserved or obligated for an approved financial action, such as issuing a purchase order. Commitments reduce available budget and provide forward visibility into planned spending prior to invoice and payment.

### Purchase Order
An authorized order issued to a supplier under a Contract or approved procurement action. A Purchase Order formally commits funds and defines the goods or services to be delivered, along with pricing and delivery terms.

### Purchase Order Line
Line-level detail within a Purchase Order specifying item or service description, quantity, unit price, and funding allocation. Purchase Order Lines enable detailed receiving, invoice matching, and financial tracking.

### Payment
Represents the disbursement of funds to a supplier or payee in satisfaction of an approved financial obligation. Payments may reference invoices, purchase orders, contracts, and funding sources, and support audit and reconciliation processes.

### Budget Status
- Draft
- Pending Approval
- Approved
- Active
- Amended
- Closed
- Cancelled

### Funding Source Type
- Appropriation
- Grant
- Contract Revenue
- Fee Revenue
- Cost Center
- Project Funding
- Capital Fund
- Operating Fund
- Reserve Fund

### Classification Type
- Expense Category
- Revenue Category
- Object Class
- Cost Element
- Account Code
- Program Code
- Function Code

### Procurement Method
- Competitive Bid
- Request for Proposal
- Request for Quote
- Sole Source
- Emergency Procurement
- Blanket Purchase Agreement
- Simplified Acquisition
- GSA Schedule
- Cooperative Agreement

### Item Type
- Goods
- Services
- Software
- Equipment
- Supplies
- Professional Services
- Construction

### Procurement Type
- Request for Proposal (RFP)
- Request for Quote (RFQ)
- Invitation for Bid (IFB)
- Sole Source
- Small Purchase
- Emergency

### Procurement Status
- Planning
- Solicitation Issued
- Responses Due
- Under Evaluation
- Awarded
- Cancelled
- Closed

### Contract Type
- Fixed Price
- Cost Reimbursable
- Time and Materials
- Indefinite Delivery Indefinite Quantity (IDIQ)
- Blanket Purchase Agreement (BPA)
- Task Order
- Delivery Order

### Pricing Structure
- Firm Fixed Price
- Fixed Price with Economic Adjustment
- Cost Plus Fixed Fee
- Cost Plus Award Fee
- Cost Plus Incentive Fee
- Time and Materials
- Labor Hour

### Amendment Type
- Funding Increase
- Funding Decrease
- Period Extension
- Scope Change
- Administrative Correction
- Termination
- Option Exercise

### Contract Line Type
- Fixed Price Item
- Labor Category
- Material
- Travel
- Other Direct Cost
- Subcontract

### Deliverable Type
- Report
- Software
- Data Set
- Training Material
- Documentation
- Presentation
- Physical Product
- Service Completion

### Deliverable Status
- Not Started
- In Progress
- Submitted
- Under Review
- Accepted
- Rejected
- Resubmitted

### Milestone Type
- Contract Award
- Kickoff
- Phase Start
- Phase Completion
- Deliverable Due
- Renewal Decision
- Option Exercise
- Contract Closeout

### Milestone Status
- Upcoming
- Due Soon
- Completed On Time
- Completed Late
- Missed
- Cancelled

### Commitment Type
- Purchase Order
- Contract Obligation
- Grant Award
- Reserved Funds
- Encumbrance

### Purchase Order Type
- Standard
- Blanket
- Standing
- Emergency
- Contract Release

### Purchase Order Status
- Draft
- Pending Approval
- Approved
- Issued
- Partially Received
- Fully Received
- Closed
- Cancelled

### Purchase Order Line Status
- Open
- Partially Received
- Fully Received
- Invoiced
- Closed
- Cancelled

### Payment Status
- Pending
- Approved
- Processed
- Paid
- Voided
- Returned

### Payment Method
- Check
- Electronic Funds Transfer
- Wire Transfer
- Credit Card
- Purchase Card
- ACH
