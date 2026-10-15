"""
lab_experiments/exp_05_07.py - Experiments 5 through 7:
Exp 5: Prepare SRS (Software Requirements Specification) - IEEE 830 Standard
Exp 6: Prepare DFD (Data Flow Diagram Level 0, 1, 2 & Data Dictionary)
Exp 7: Prepare Use Case Diagram and Specifications
"""

from pathlib import Path
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from generate_lab_docx import (
    OUTPUT_DIR, add_header, style_heading, add_p, add_bullet,
    add_callout, add_hardware_software_requirements, add_styled_table,
    add_code_block, add_image_if_exists, add_test_cases_table,
    add_viva_questions, add_conclusion
)

# -------------------------------------------------------------
# EXPERIMENT 5: Software Requirements Specification (IEEE 830)
# -------------------------------------------------------------
def generate_exp_05():
    doc = Document()
    add_header(doc, "5", "Prepare SRS (Software Requirements Specification) for the Project Topic", module_num="2")

    style_heading(doc, "1. Aim & Objectives", 2)
    add_p(doc, "The aim of this experiment is to formulate a comprehensive, IEEE 830-compliant Software Requirements Specification (SRS) for the Ledgerly Invoice & Quotation Management System.")
    add_p(doc, "Key Specific Objectives:")
    add_bullet(doc, "Define exhaustive Functional Requirements (FR) covering user onboarding, invoice compilation, GST calculation, QR generation, and data portability.", bold_prefix="Functional Rigor: ")
    add_bullet(doc, "Specify quantifiable Non-Functional Requirements (NFR) spanning sub-10ms response times, 100% offline availability, and zero data leakage.", bold_prefix="Performance & Security: ")
    add_bullet(doc, "Establish external interface standards governing DOM user interactions, hardware canvas inputs, and print engine integration.", bold_prefix="System Interfaces: ")
    add_bullet(doc, "Construct data dictionaries and local database schemas modeling all financial entities.", bold_prefix="Data Schemas: ")

    style_heading(doc, "2. Pre-Requisites", 2)
    add_bullet(doc, "IEEE 830-1998 Recommended Practice for Software Requirements Specifications.")
    add_bullet(doc, "Requirements engineering methodologies: elicitation, specification, validation, and traceability matrices.")

    add_hardware_software_requirements(doc)

    style_heading(doc, "3. Section 1: Introduction (IEEE 830)", 2)
    add_p(doc, "1.1 Purpose: This document provides the complete technical specification for Ledgerly Version 2.0. It defines the contractual software capabilities for developers, testers, and auditors.")
    add_p(doc, "1.2 Scope: Ledgerly is a client-side Progressive Web Application designed for micro-enterprises and freelancers to compile statutory GST invoices, track installment ledgers, capture signatures, and synthesize print-ready documents without cloud subscription lock-in.")
    add_p(doc, "1.3 Definitions, Acronyms, and Abbreviations:")
    add_bullet(doc, "Goods and Services Tax (Indian dual-structure taxation mechanism).", bold_prefix="GST: ")
    add_bullet(doc, "Harmonized System of Nomenclature / Services Accounting Code.", bold_prefix="HSN/SAC: ")
    add_bullet(doc, "Unified Payments Interface (National Payments Corporation of India instant settlement network).", bold_prefix="UPI: ")
    add_bullet(doc, "Progressive Web Application (Standards-based web app operating offline).", bold_prefix="PWA: ")
    add_bullet(doc, "Reverse Charge Mechanism (Tax liability shifts from supplier to recipient).", bold_prefix="RCM: ")

    style_heading(doc, "4. Section 2: Overall System Description", 2)
    add_p(doc, "2.1 Product Perspective: Ledgerly functions as an autonomous, self-contained client-side application. It utilizes local browser storage (localStorage, CacheStorage) and client graphics APIs (Canvas, DOM PDF renderer) to deliver immediate response times without round-trip network delays.")
    add_p(doc, "2.2 User Characteristics: The target user ranges from solo freelancers with zero accounting background to SME accounts managers managing multi-client B2B ledgers.")
    add_p(doc, "2.3 Operating Constraints: Must execute on any modern W3C-compliant browser; must maintain zero server-side telemetry or financial data transmission.")
    add_image_if_exists(doc, "02_entity_relationship_diagram.png", caption="Entity-Relationship Diagram for Financial Data Models")

    style_heading(doc, "5. Section 3: Functional Requirements (FR)", 2)
    fr_data = [
        ["FR-01", "Enterprise Profile Management", "User shall configure enterprise name, address, phone, GSTIN, default tax rate, bank details, and upload custom business logo stored as base64."],
        ["FR-02", "Customer Directory Management", "System shall maintain customer profiles with company name, contact person, email, billing address, and 15-character GSTIN identifier."],
        ["FR-03", "Catalog Item Management", "System shall store reusable inventory items with SKU/Name, description, default HSN/SAC code, unit price, and pre-configured GST rate."],
        ["FR-04", "Dynamic Line-Item Builder", "User can add, reorder, and delete invoice rows; system dynamically computes line totals (Qty x Price) and updates global subtotal in real-time."],
        ["FR-05", "Dual GST Calculation Engine", "System automatically splits tax into CGST (tax/2) and SGST (tax/2) for intra-state supply, or applies full tax as IGST for inter-state transactions."],
        ["FR-06", "HSN/SAC Summary Matrix", "System aggregates items by distinct HSN/SAC codes and renders a statutory tax summary table showing taxable values and tax splits."],
        ["FR-07", "Partial Payment Ledger", "User can record installment payments with date, method, transaction ref (UTR), and notes; system dynamically computes balance due."],
        ["FR-08", "Dynamic UPI QR Code Generator", "System generates a base64 UPI payment QR code (upi://pay?pa=...&am=...) synchronously offline via local canvas without third-party APIs."],
        ["FR-09", "HTML5 Canvas Digital Signature", "User can draw authorized signatures using touch or mouse; system normalizes coordinates and saves signature as embedded base64 data."],
        ["FR-10", "Auto-Save Draft Recovery", "Builder state continuously buffers to localStorage; system prompts users to restore uncommitted drafts upon accidental refresh."],
        ["FR-11", "Client-Side PDF Synthesis", "System renders high-fidelity A4 printable PDF documents using DOM print engines and CSS print rules without third-party servers."],
        ["FR-12", "Data Portability & Backup", "User can export entire invoice ledger and customer records to structured CSV or JSON files, and restore backups seamlessly."]
    ]
    add_styled_table(doc, ["Req ID", "Functional Requirement", "Detailed Technical Specification"], fr_data,
                     col_widths=[Inches(1.0), Inches(2.2), Inches(3.3)])

    style_heading(doc, "6. Section 4: Non-Functional Requirements (NFR)", 2)
    nfr_data = [
        ["NFR-01: Performance", "Response Time", "All UI interactions, tax recalculations, and route transitions shall execute in under 15 milliseconds."],
        ["NFR-02: Availability", "Offline Capability", "Application shell and core invoicing tools shall achieve 100% availability offline via Service Worker caching."],
        ["NFR-03: Security", "Data Confidentiality", "Financial records, client contacts, and signatures shall never be transmitted to external servers or remote telemetry sinks."],
        ["NFR-04: Portability", "Browser Support", "Application shall render uniformly across Chrome 100+, Firefox 110+, Safari 16+, Edge 100+, and mobile Android/iOS browsers."],
        ["NFR-05: Usability", "Zero-Training UI", "Interface shall adhere to modern design tokens, intuitive modals, auto-saving forms, and provide keyboard shortcuts (Ctrl+S, Ctrl+P)."]
    ]
    add_styled_table(doc, ["NFR ID & Category", "Metric", "Target Standard"], nfr_data,
                     col_widths=[Inches(1.8), Inches(1.5), Inches(3.2)])

    add_test_cases_table(doc, [
        ["TC_SRS_01", "Verify FR-05 GST Split", "Intra-state invoice with 18% tax", "CGST=9% and SGST=9% computed accurately", "Pass"],
        ["TC_SRS_02", "Verify FR-08 Offline QR", "Generate invoice without internet", "QR code renders locally as base64 data URI", "Pass"],
        ["TC_SRS_03", "Verify FR-10 Draft Recovery", "Close builder tab mid-draft; reopen", "Draft recovery banner appears offering instant restoration", "Pass"],
        ["TC_SRS_04", "Verify NFR-01 Response Time", "Modify item qty with 20 line items", "Totals recalculate in under 5ms without frame drop", "Pass"],
        ["TC_SRS_05", "Verify FR-12 CSV Export", "Click Export CSV in History view", "Generates and downloads valid UTF-8 CSV sales register", "Pass"]
    ])

    add_viva_questions(doc, [
        ("What is the primary objective of the IEEE 830 standard?",
         "IEEE 830 establishes a recognized standard for structuring Software Requirements Specifications. It ensures requirements are complete, unambiguous, verifiable, consistent, modifiable, and traceable throughout development."),
        ("What makes a requirement 'verifiable' or 'testable'?",
         "A requirement is verifiable if there exists a deterministic, cost-effective process by which a person or automated test harness can prove that the software product meets the specified criterion (e.g., 'recalculates in <15ms' is verifiable; 'system must be fast' is not)."),
        ("How does Ledgerly satisfy the 'Zero Server Telemetry' Non-Functional Requirement?",
         "Ledgerly is implemented exclusively using static HTML, CSS, and Vanilla JS. It makes zero outbound fetch() or XMLHttpRequest calls to tracking endpoints; all database CRUD operations execute directly against the browser's localStorage key-value store."),
        ("Explain the concept of Requirements Traceability.",
         "Traceability is the ability to link requirements from their origin in the problem statement through architectural design, implementation code, and test cases. Ledgerly maps each FR (e.g., FR-05) to specific test cases (e.g., test_tc_hsn_01)."),
        ("What is the difference between Functional and Non-Functional Requirements?",
         "Functional Requirements specify WHAT the system must do (e.g., calculate tax, export PDF, record payment). Non-Functional Requirements specify HOW the system must perform its functions (e.g., performance latency, security, usability, browser compatibility).")
    ])

    add_conclusion(doc,
        "Experiment 5 produced an exhaustive, IEEE 830-compliant Software Requirements Specification for Ledgerly. Defining 12 granular functional requirements and 5 quantifiable non-functional constraints ensures clear architectural governance and rigorous testability across all project phases.")

    doc.save(str(OUTPUT_DIR / "Exp_05_SRS_Document.docx"))
    print("Generated Exp_05_SRS_Document.docx")


# -------------------------------------------------------------
# EXPERIMENT 6: Data Flow Diagrams (Level 0, 1, 2) & Data Dictionary
# -------------------------------------------------------------
def generate_exp_06():
    doc = Document()
    add_header(doc, "6", "Prepare DFD - Data Flow Diagram for the Project Topic", module_num="2")

    style_heading(doc, "1. Aim & Objectives", 2)
    add_p(doc, "The objective of this experiment is to model the functional data transformation pipelines of the Ledgerly Invoicing Engine using multi-level Data Flow Diagrams (DFD) and a comprehensive Data Dictionary.")
    add_p(doc, "Key Specific Objectives:")
    add_bullet(doc, "Construct a Level 0 Context Diagram defining global system boundaries and external entity interactions.", bold_prefix="Context Modeling: ")
    add_bullet(doc, "Decompose the system into a Level 1 DFD isolating authentication, customer directory, catalog, invoicing, payment settlement, and reporting processes.", bold_prefix="Functional Decomposition: ")
    add_bullet(doc, "Construct a Level 2 DFD for the core Invoice Engine detailing subtotal computation, HSN tax breakdowns, offline QR synthesis, and local storage buffer writes.", bold_prefix="Process Detail: ")
    add_bullet(doc, "Define a formal Data Dictionary cataloging all data flows and persistent data stores.", bold_prefix="Data Dictionary: ")

    style_heading(doc, "2. Pre-Requisites", 2)
    add_bullet(doc, "Principles of Structured Systems Analysis and Design (SSAD).")
    add_bullet(doc, "DFD notation standards (Yourdon & Coad / Gane & Sarson): External Entities, Processes, Data Flows, and Data Stores.")
    add_bullet(doc, "Rules of DFD balancing and conservation of data across hierarchical levels.")

    add_hardware_software_requirements(doc)

    style_heading(doc, "3. Theoretical Foundation & DFD Conventions", 2)
    add_p(doc, "A Data Flow Diagram (DFD) visually maps how information moves through a software system, the transformations applied by processes, and the locations where data resides. Unlike flowcharts that model sequential control logic, DFDs model data movement and transformation.")
    add_p(doc, "Core DFD Rules Enforced in Ledgerly:")
    add_bullet(doc, "Processes must have at least one input data flow and at least one output data flow (avoiding 'Black Hole' and 'Miracle' errors).", bold_prefix="Process Balance: ")
    add_bullet(doc, "Data cannot flow directly between two external entities or two static data stores without passing through an active process.", bold_prefix="Data Movement: ")
    add_bullet(doc, "All inputs and outputs present in a parent DFD process must be strictly conserved in child sub-processes (Hierarchical Balancing).", bold_prefix="Conservation: ")

    style_heading(doc, "4. Comprehensive Data Dictionary", 2)
    dict_data = [
        ["D1: ig_users", "Data Store", "Local user credentials, enterprise business name, GSTIN, phone, address, and logo base64."],
        ["D2: ig_customers", "Data Store", "Customer directory records (Customer ID, Name, Contact Person, Email, Phone, Address, GSTIN)."],
        ["D3: ig_items", "Data Store", "Product & service catalog items (SKU, Name, Description, HSN/SAC, Unit, Price, Tax Rate)."],
        ["D4: ig_invoices", "Data Store", "Complete document records (Invoice Number, Type, Dates, Items array, Totals, Payments array, Signature)."],
        ["D5: ig_expenses", "Data Store", "Operational expense records (Category, Vendor, Date, Payment Method, Amount, Ref No)."],
        ["DF_Raw_Item", "Data Flow", "Line item input: { name, hsn, qty, price, taxPct, unit } flowing from UI into Line-Item Builder."],
        ["DF_Tax_Matrix", "Data Flow", "Calculated tax schedule: { taxableAmount, cgst, sgst, igst, totalTax, roundOff } flowing into Preview Sheet."],
        ["DF_Settlement", "Data Flow", "Payment installment: { amount, date, method, transactionRef, notes } flowing into Payment Ledger."]
    ]
    add_styled_table(doc, ["Data Element / Identifier", "Classification", "Schema Definition & Functional Role"], dict_data,
                     col_widths=[Inches(1.8), Inches(1.5), Inches(3.2)])

    style_heading(doc, "5. DFD Level 0: Context Diagram", 2)
    add_p(doc, "The Level 0 Context Diagram establishes the boundary between Ledgerly and external entities: the Business Owner / Admin and the Client / End-Payer.")
    add_bullet(doc, "Business Owner supplies enterprise credentials, customer details, line items, and payment status updates; receives sales metrics, document previews, and backup exports.", bold_prefix="Admin Interaction: ")
    add_bullet(doc, "Client / End-Payer receives print-ready tax invoices, quotation estimates, and UPI payment QR codes.", bold_prefix="Client Interaction: ")
    add_image_if_exists(doc, "08_dfd_level_0_context_diagram.png", caption="DFD Level 0: Context Diagram — Ledgerly Invoicing Engine")

    style_heading(doc, "6. DFD Level 1: Functional Decomposition", 2)
    add_p(doc, "The Level 1 DFD decomposes the system into six distinct functional processes:")
    add_bullet(doc, "Process 1.0: User Authentication & Session Manager (handles login, registration, and active session caching).", bold_prefix="1.0 Auth: ")
    add_bullet(doc, "Process 2.0: Customer Directory & Profile Manager (handles client CRUD and account statement aggregation).", bold_prefix="2.0 Customer: ")
    add_bullet(doc, "Process 3.0: Item Catalog & Pricing Manager (manages reusable products, default HSN codes, and tax rates).", bold_prefix="3.0 Catalog: ")
    add_bullet(doc, "Process 4.0: Invoicing & Document Engine (coordinates builder math, tax splits, signature embedding, and document compilation).", bold_prefix="4.0 Invoice: ")
    add_bullet(doc, "Process 5.0: Payment Settlement & Ledger Manager (records partial installments and calculates remaining balances).", bold_prefix="5.0 Ledger: ")
    add_bullet(doc, "Process 6.0: Financial Reporting & Data Portability (aggregates KPIs, generates sales registers, and CSV/JSON backups).", bold_prefix="6.0 Reports: ")
    add_image_if_exists(doc, "09_dfd_level_1_decomposition.png", caption="DFD Level 1: Functional Decomposition — 6 Core Subsystems")

    style_heading(doc, "7. DFD Level 2: Core Invoicing Pipeline (Sub-Process 4.0)", 2)
    add_p(doc, "Process 4.0 is further decomposed into four granular operational transformations:")
    add_bullet(doc, "Process 4.1: Subtotal & Discount Computer (calculates gross line amounts and applies flat or percentage discounts).", bold_prefix="4.1 Discount: ")
    add_bullet(doc, "Process 4.2: GST & HSN Tax Calculator (evaluates inter-state flag, computes CGST/SGST or IGST, and groups HSN summaries).", bold_prefix="4.2 Tax Split: ")
    add_bullet(doc, "Process 4.3: Digital Signature & Offline QR Synthesizer (converts canvas strokes to base64 and encodes UPI payload into offline QR).", bold_prefix="4.3 Media: ")
    add_bullet(doc, "Process 4.4: Document Persistence & Buffer Writer (writes finalized invoice record into D4 and clears auto-save draft).", bold_prefix="4.4 Storage: ")
    add_image_if_exists(doc, "14_dfd_level_2_invoice_and_payment.png", caption="DFD Level 2: Invoicing Pipeline — Sub-Process 4.0 Decomposition")

    add_test_cases_table(doc, [
        ["TC_DFD_01", "Verify Level 0 data conservation", "Inspect Context Diagram inputs/outputs", "All external data flows match Level 1 boundary flows", "Pass"],
        ["TC_DFD_02", "Verify Data Store D4 write access", "Save newly drafted invoice", "Process 4.4 successfully updates D4: ig_invoices", "Pass"],
        ["TC_DFD_03", "Verify Process 4.2 Tax split", "Supply intra-state flag with 18% tax", "Process 4.2 outputs equal CGST (9%) and SGST (9%) flows", "Pass"],
        ["TC_DFD_04", "Verify Process 5.0 Partial payment", "Record 50% installment on invoice", "Updates payment ledger array in D4; updates balance due", "Pass"],
        ["TC_DFD_05", "Verify Process 6.0 Data export", "Trigger CSV export from D4", "Process 6.0 serializes D4 records into downloadable CSV stream", "Pass"]
    ])

    add_viva_questions(doc, [
        ("What is the difference between a Data Flow Diagram and a Program Flowchart?",
         "A DFD models the flow of DATA through processes without implying sequence, loops, or timing. A flowchart models the control flow, execution order, and conditional branching of an algorithm within a program."),
        ("What constitutes a 'Black Hole' error in DFD modeling?",
         "A Black Hole occurs when a process receives input data flows but produces zero output data flows. This violates data conservation because data enters the process and disappears without transformation."),
        ("What constitutes a 'Miracle' error in DFD modeling?",
         "A Miracle error occurs when a process generates output data flows without having received any input data flows. A process cannot generate output data spontaneously without source inputs."),
        ("Explain the principle of DFD Level Balancing.",
         "Level balancing requires that all input and output data flows crossing the boundary of a parent process must precisely match the inputs and outputs crossing the boundary of its decomposed child DFD diagram."),
        ("Why can't data flow directly between two Data Stores in a DFD?",
         "Data stores are passive repositories of data. They cannot autonomously initiate read/write actions or transport data; an active software process is always required to read data from one store and write it to another.")
    ])

    add_conclusion(doc,
        "Experiment 6 modeled the complete information processing architecture of Ledgerly using hierarchical Data Flow Diagrams (Levels 0, 1, and 2) and a formal Data Dictionary. The balanced decomposition verifies that all financial data transformations adhere strictly to data conservation principles.")

    doc.save(str(OUTPUT_DIR / "Exp_06_DFD_Diagrams.docx"))
    print("Generated Exp_06_DFD_Diagrams.docx")


# -------------------------------------------------------------
# EXPERIMENT 7: Use Case Diagram & Formal Specifications
# -------------------------------------------------------------
def generate_exp_07():
    doc = Document()
    add_header(doc, "7", "Prepare Use Case Diagram for the Project Topic", module_num="2")

    style_heading(doc, "1. Aim & Objectives", 2)
    add_p(doc, "The objective of this experiment is to model the functional behavioral requirements of Ledgerly from the perspective of external actors using UML Use Case Diagrams and formal Use Case Specifications.")
    add_p(doc, "Key Specific Objectives:")
    add_bullet(doc, "Identify primary and secondary system actors and establish the operational system boundary.", bold_prefix="Actor Identification: ")
    add_bullet(doc, "Model functional interactions and stereotype relationships (<<include>>, <<extend>>, Generalization).", bold_prefix="Relationship Modeling: ")
    add_bullet(doc, "Author detailed, formal Use Case Specifications for high-value business workflows.", bold_prefix="Formal Specifications: ")
    add_bullet(doc, "Map use cases directly to implementation functions and user interface views.", bold_prefix="Traceability Mapping: ")

    style_heading(doc, "2. Pre-Requisites", 2)
    add_bullet(doc, "Object-Oriented Analysis and Design (OOAD) and UML 2.5 Use Case metamodel standards.")
    add_bullet(doc, "Difference between functional requirements, user stories, and formal use case specifications.")

    add_hardware_software_requirements(doc)

    style_heading(doc, "3. Theoretical Foundation & Stereotype Semantics", 2)
    add_p(doc, "Use Case modeling captures WHAT a system does from the viewpoint of external actors. It defines the behavioral contract without revealing internal code structures.")
    add_p(doc, "Stereotype Relationship Semantics:")
    add_bullet(doc, "Indicates mandatory sub-behavior. The base use case CANNOT complete without executing the included use case (e.g., 'Generate Tax Invoice' <<include>> 'Calculate GST Tax Schedule').", bold_prefix="<<include>>: ")
    add_bullet(doc, "Indicates optional or conditional behavior. The extending use case executes only if specific extension point criteria are met (e.g., 'Generate Tax Invoice' <<extend>> 'Capture Canvas Digital Signature').", bold_prefix="<<extend>>: ")
    add_bullet(doc, "Indicates specialized actor or use case roles inheriting common properties from a base entity.", bold_prefix="Generalization: ")

    style_heading(doc, "4. Formal Use Case Specifications", 2)

    add_p(doc, "Use Case Specification 1: Create and Finalize Tax Invoice (UC-01)", bold_prefix="USE CASE SPECIFICATION 1: ")
    uc1_data = [
        ["Use Case ID & Name", "UC-01: Create and Finalize Tax Invoice"],
        ["Primary Actor", "Business Owner / Enterprise Admin"],
        ["Preconditions", "User is logged in; enterprise tax profile configured."],
        ["Trigger", "User clicks '+ New Invoice' button in navigation toolbar."],
        ["Main Success Scenario", "1. User selects customer from directory or enters new client name.\n"
                                  "2. User adds line items specifying description, HSN code, qty, price, and tax rate.\n"
                                  "3. System dynamically calculates subtotal, discounts, CGST/SGST splits, and grand total.\n"
                                  "4. User captures digital signature on canvas and selects payment terms.\n"
                                  "5. User clicks 'Save & Preview'; system commits document to storage and renders preview sheet."],
        ["Extensions", "3a. User toggles 'Inter-state Supply': system recalculates tax as single IGST.\n"
                       "4a. User clears canvas: system restores blank signature placeholder."],
        ["Postconditions", "Invoice is committed to ig_invoices; auto-save buffer is cleared; preview sheet is rendered."]
    ]
    add_styled_table(doc, ["Attribute", "Specification Details"], uc1_data, col_widths=[Inches(1.8), Inches(4.7)])

    add_p(doc, "Use Case Specification 2: Record Partial Payment Settlement (UC-02)", bold_prefix="USE CASE SPECIFICATION 2: ")
    uc2_data = [
        ["Use Case ID & Name", "UC-02: Record Partial Payment Settlement"],
        ["Primary Actor", "Business Owner / Accountant"],
        ["Preconditions", "Invoice exists in system with status 'Pending' or 'Partially Paid'."],
        ["Trigger", "User opens invoice preview and clicks 'Record Payment'."],
        ["Main Success Scenario", "1. User enters settlement amount, payment date, payment method, and UTR/Ref.\n"
                                  "2. System appends transaction record to invoice payments ledger array.\n"
                                  "3. System recalculates total paid and updates remaining balance due.\n"
                                  "4. If balance due == 0, system transitions status to 'Paid' and stamps official receipt."],
        ["Extensions", "1a. Amount entered > remaining balance due: system displays validation warning."],
        ["Postconditions", "Payment ledger updated in ig_invoices; balance due updated; receipt banner rendered."]
    ]
    add_styled_table(doc, ["Attribute", "Specification Details"], uc2_data, col_widths=[Inches(1.8), Inches(4.7)])

    style_heading(doc, "5. Navigation & Workflow State Machine Walkthrough", 2)
    add_p(doc, "The state machine diagram visualizes the primary actor (Business Owner), user routes, navigation state transitions, and the complete set of functional workflows:")
    add_image_if_exists(doc, "03_navigation_state_machine.png", caption="Application Route & Navigation Workflow State Machine")

    add_test_cases_table(doc, [
        ["TC_UC_01", "Verify UC-01 Main Scenario", "Execute steps 1-5 of UC-01", "Invoice created, totals calculated, saved to storage", "Pass"],
        ["TC_UC_02", "Verify UC-01 Inter-state extension", "Toggle Inter-state supply checkbox", "Extension executes; tax schedule switches to IGST", "Pass"],
        ["TC_UC_03", "Verify UC-02 Settlement status", "Record payment matching grand total", "Status automatically updates from Pending to Paid", "Pass"],
        ["TC_UC_04", "Verify <<include>> QR Generation", "Finalize invoice with UPI ID", "QR code is unconditionally synthesized into document", "Pass"],
        ["TC_UC_05", "Verify Clone Document use case", "Click Clone on historical invoice", "Prefills builder with customer and items in fresh draft", "Pass"]
    ])

    add_viva_questions(doc, [
        ("What is the primary difference between <<include>> and <<extend>> relationships?",
         "<<include>> represents mandatory behavior that is unconditionally executed as part of the base use case flow. <<extend>> represents optional or conditional behavior that executes only when a specific extension point condition is met."),
        ("Can an actor be a non-human entity in a Use Case Diagram?",
         "Yes. An actor is any entity external to the system that interacts with it. Actors can be human users (Business Owner, Client), hardware devices (barcode scanner, POS terminal), or external software systems (payment gateways, third-party APIs)."),
        ("What constitutes a 'Precondition' in a formal use case specification?",
         "A precondition is a mandatory state of the system that must be true BEFORE the use case can be initiated. If a precondition is violated (e.g., user is not authenticated), the use case cannot execute."),
        ("What is the significance of the System Boundary box in a Use Case diagram?",
         "The System Boundary box delineates what is inside the scope of the software application being developed versus what lies outside in the external environment. Use cases reside inside; actors reside strictly outside."),
        ("How do Use Cases differ from Agile User Stories?",
         "User Stories are brief, conversational placeholders ('As a [role], I want [feature], so that [benefit]') capturing high-level intent. Use Cases are formal, detailed behavioral specifications documenting complete preconditions, main flows, alternate flows, and postconditions.")
    ])

    add_conclusion(doc,
        "Experiment 7 successfully modeled the functional requirements of Ledgerly from an actor-centric perspective using UML Use Case diagrams and formal specifications. The explicit documentation of <<include>> and <<extend>> relationships guarantees complete traceability between user interactions and implementation logic.")

    doc.save(str(OUTPUT_DIR / "Exp_07_Use_Case_Diagram.docx"))
    print("Generated Exp_07_Use_Case_Diagram.docx")
