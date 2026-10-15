import os
import sys
import json
import time
import base64
import asyncio
import tempfile
import threading
import subprocess
import http.server
import socketserver
from pathlib import Path
import requests
import websockets

sys.stdout.reconfigure(line_buffering=True)

WORKSPACE = Path(r"C:\Users\Krushna\Documents\Projects\Invoice Generator")
OUTPUT_DIR = WORKSPACE / "Project Diagrams"
SCRATCH_DIR = WORKSPACE / "scratch_test"
HTTP_PORT = 8999

# Clear, beautifully styled Mermaid diagrams formatted for readability
DIAGRAMS = [
    {
        "filename": "01_system_architecture",
        "title": "High-Level System Architecture",
        "code": """flowchart TD
    subgraph Client[" CLIENT APPLICATION RUNTIME (Vanilla JS Single Page App)"]
        direction TB

        subgraph UI["1. PRESENTATION LAYER"]
            direction LR
            HTML["index.html<br/><b>SPA Root & Toast Notifications</b>"]
            CSS["style.css<br/><b>Design Tokens & Print Layout</b>"]
            Theme["Theme Engine<br/><b>Light / Dark Mode State</b>"]
        end

        subgraph Core["2. ROUTING & CONTROLLER LAYER"]
            direction LR
            Router["Router & Navigation Guard<br/><b>Hash Routing (#/path) + Auth Guard</b>"]
            Views["View Controllers<br/><b>Dashboard | Create | Preview | History<br/>Customers | Enterprise | Profile</b>"]
        end

        subgraph Logic["3. PROCESSING & BUSINESS LOGIC SERVICES"]
            direction LR
            Calc["Calculation Engine<br/><b>Subtotal, Discount, Tax, Grand Total</b>"]
            Sig["Signature Engine<br/><b>HTML5 Canvas 2D Vector Path</b>"]
            QR["Payment QR Helper<br/><b>UPI Deep-Link & Hosted URL</b>"]
            Val["Validation Rules<br/><b>Email & Required Field Validation</b>"]
        end

        subgraph DB["4. CLIENT STORAGE (Browser localStorage)"]
            direction LR
            D1[("ig_users<br/><b>User Accounts</b>")]
            D2[("ig_session<br/><b>Active Session</b>")]
            D3[("ig_invoices<br/><b>Invoice Ledger</b>")]
            D4[("ig_customers<br/><b>Customer Profiles</b>")]
            D5[("ig_enterprises<br/><b>Enterprise Profiles</b>")]
        end
    end

    subgraph Ext[" EXTERNAL INTEGRATIONS & SUBSYSTEMS"]
        direction LR
        API1["api.qrserver.com<br/><b>Dynamic QR Code Generator</b>"]
        API2["mailto: Protocol<br/><b>Native Mail Client Handler</b>"]
        API3["window.print()<br/><b>Browser PDF / Print Subsystem</b>"]
    end

    UI --> Core
    Core --> Logic
    Logic --> DB
    Core --> DB
    Logic --> Ext
    Core --> Ext"""
    },
    {
        "filename": "02_entity_relationship_diagram",
        "title": "Entity-Relationship Diagram (ERD)",
        "code": """erDiagram
    USER ||--o{ ENTERPRISE_PROFILE : owns
    USER ||--o{ CUSTOMER : manages
    USER ||--o{ INVOICE : creates
    USER ||--o| SESSION : has
    INVOICE ||--|{ INVOICE_ITEM : contains

    USER {
        string id PK "u_admin, uid('u')"
        string name "Full Name"
        string email "Unique Login Email"
        string password "Plaintext / Hash"
        string businessName "Default Business Name"
        string phone "Phone Number"
        string address "Business Postal Address"
        string upiId "Default UPI VPA"
        string taxId "Default GSTIN / Tax ID"
        string signature "Base64 Signature String"
    }

    SESSION {
        string userId FK "References USER.id"
        boolean remember "Persistent session flag"
    }

    ENTERPRISE_PROFILE {
        string id PK "ent_default, uid('ent')"
        string userId FK "References USER.id"
        boolean isDefault "Default seller profile flag"
        string name "Business / Legal Entity Name"
        string tagline "Company Motto or Tagline"
        string email "Official Billing Email"
        string phone "Business Contact Phone"
        string address "Registered Office Address"
        string taxId "GSTIN / VAT / Tax ID"
        string currency "INR, USD, EUR, GBP"
        string currencySymbol "₹, $, €, £"
        string upiId "UPI ID for QR Code"
        string bankName "Banking Institution"
        string accountNumber "Bank Account Number"
        string ifscCode "IFSC / SWIFT Code"
        string paymentUrl "Custom Checkout URL"
        string notes "Default Invoice Terms"
    }

    CUSTOMER {
        string id PK "cust_sample_1, uid('cust')"
        string userId FK "References USER.id"
        string name "Company or Customer Name"
        string contactPerson "Primary Contact Individual"
        string email "Billing Email"
        string phone "Contact Phone"
        string address "Billing Address"
        string taxId "GSTIN / Tax ID"
        string terms "Payment Terms (Net 15, Due on Receipt)"
    }

    INVOICE {
        string id PK "uid('inv')"
        string userId FK "References USER.id"
        string invoiceNumber "INV-YYYY-XXX"
        date invoiceDate "YYYY-MM-DD"
        date dueDate "YYYY-MM-DD"
        string currencySymbol "₹, $, €, £"
        json seller "Seller Profile Snapshot"
        json customer "Customer Profile Snapshot"
        number discountPct "Discount Rate %"
        number taxPct "Tax Rate %"
        number subtotal "Line Items Sum"
        number discount "Calculated Discount Amount"
        number tax "Calculated Tax Amount"
        number grandTotal "Net Payable Amount"
        string paymentTerms "Terms & Conditions"
        string notes "Remarks / Instructions"
        string status "Draft | Generated | Pending | Paid"
        date paidAt "Settlement Date"
        string paymentMethod "UPI, Bank Transfer, Card, Cash..."
        string transactionRef "UTR / Reference Number"
        string paidMessage "Receipt Acknowledgement Note"
        string signature "Base64 Drawn Signature"
        number createdAt "Timestamp"
    }

    INVOICE_ITEM {
        string id PK "uid('it')"
        string name "Product / Service Title"
        string description "Scope / Specifications"
        number qty "Quantity"
        number price "Unit Price"
    }"""
    },
    {
        "filename": "03_navigation_state_machine",
        "title": "Application State & Route Navigation State Machine",
        "code": """flowchart TD
    Start([ User Opens App]) --> AuthCheck{Active Session Found?}

    subgraph Public[" Public Authentication Views"]
        Login["<b>#/login</b><br/>User Login View<br/>Email & Password Verification"]
        Register["<b>#/register</b><br/>User Signup View<br/>Account Registration & Auto-Login"]
        Login <-->|"Switch Form"| Register
    end

    subgraph Guarded[" Guarded Application Shell (appShell)"]
        Dashboard["<b>#/dashboard</b><br/>Main Dashboard<br/>KPI Cards & Recent Invoices"]
        Create["<b>#/create</b><br/>Invoice Builder<br/>Live Math, Autofill & Signature"]
        Edit["<b>#/edit?id={id}</b><br/>Edit Invoice<br/>Modify Existing Invoice"]
        Preview["<b>#/preview?id={id}</b><br/>Invoice Preview & Sheet<br/>Payment QR, PAID Watermark, Receipt"]
        History["<b>#/history</b><br/>Invoices Ledger<br/>Search, Status & Date Filter"]
        Customers["<b>#/customers</b><br/>Customer Directory<br/>Client Profiles CRUD"]
        Enterprise["<b>#/enterprise</b><br/>Enterprise Profiles<br/>Multi-Business & Banking Setup"]
        Profile["<b>#/profile</b><br/>User Profile<br/>Account Settings & Signatures"]

        Dashboard -->|"+ Create New Invoice"| Create
        Dashboard -->|"View All Invoices"| History
        Dashboard -->|"Click Recent Row"| Preview

        Create -->|"Save & Preview / Generate"| Preview
        Create -->|"Save Draft"| History

        Edit -->|"Update & Preview"| Preview
        Preview -->|"Edit Details"| Edit
        Preview -->|"Back to List"| History

        Customers -->|"Bill Customer"| Create
        Enterprise -->|"Use Profile"| Create
    end

    AuthCheck -->|No Session / Expired| Login
    AuthCheck -->|Session Valid| Dashboard
    Login -->|"Authentication Success"| Dashboard
    Register -->|"Registration Success"| Dashboard
    Guarded -->|"Logout (clearSession)"| Login"""
    },
    {
        "filename": "04_invoice_lifecycle_state_machine",
        "title": "Invoice Lifecycle State Machine",
        "code": """stateDiagram-v2
    [*] --> Draft: Save as Draft
    [*] --> Generated: Save & Generate

    Draft --> Generated: Finalize Line Items & Assign Number
    Draft --> Draft: Edit & Re-save

    Generated --> Pending: Dispatched / Awaiting Settlement
    Generated --> Paid: Immediate Payment Received
    Generated --> Draft: Revert to Draft

    Pending --> Paid: Record Payment via Modal
    Pending --> Pending: Resend Invoice / Re-scan QR

    Paid --> Pending: Reopen Invoice (status change)
    Paid --> Draft: Reset Status

    state Paid {
        [*] --> WatermarkActive: Apply Embossed 'PAID' Watermark
        WatermarkActive --> ReceiptBannerActive: Render Green Settled Receipt Banner
        ReceiptBannerActive --> EmailReceiptReady: Enable 'Email Receipt' Template
    }

    Paid --> [*]: Final Settlement & Archival"""
    },
    {
        "filename": "05_sequence_auth_and_session",
        "title": "Sequence Diagram: Authentication & Session Flow",
        "code": """sequenceDiagram
    autonumber
    actor User as Business User
    participant Browser as Browser Window
    participant Router as Hash Router and Route Guard
    participant AuthView as Login and Register View
    participant DB as LocalStorage [ig_users, ig_session]
    participant Dashboard as Main Dashboard View

    User->>Browser: Opens Application URL
    Browser->>Router: hashchange or DOMContentLoaded
    Router->>DB: getSession() and currentUser()
    alt No valid session found
        DB-->>Router: null
        Router->>AuthView: renderLogin()
        AuthView-->>User: Displays Login Interface
        User->>AuthView: Inputs Email and Password
        AuthView->>DB: Query ig_users matching email
        alt Valid Credentials
            AuthView->>DB: setSession(userId, remember)
            AuthView->>Browser: Update location.hash to dashboard
            Browser->>Router: hashchange event triggers
            Router->>Dashboard: renderDashboard()
            Dashboard-->>User: Displays Dashboard KPI Cards & Action CTA
        else Invalid Credentials
            AuthView-->>User: Displays 'Invalid email or password' error
        end
    else Active session found
        DB-->>Router: Authenticated User Object
        Router->>Dashboard: renderDashboard()
        Dashboard-->>User: Renders Dashboard
    end"""
    },
    {
        "filename": "06_sequence_invoice_builder_and_signature",
        "title": "Sequence Diagram: Invoice Creation, Calculation & Signature",
        "code": """sequenceDiagram
    autonumber
    actor User as Business Owner
    participant Builder as Invoice Builder View [Create Route]
    participant Calc as computeTotals Calculation Engine
    participant Canvas as Signature Pad Canvas Pad
    participant Storage as LocalStorage [ig_invoices]
    participant Preview as Invoice Preview View [Preview Route]

    User->>Builder: Selects Saved Customer or Enterprise Profile
    Builder->>Builder: Autofills Seller & Customer Details
    User->>Builder: Adds or Modifies Line Items [Qty, Unit Price]
    Builder->>Calc: computeTotals(items, discountPct, taxPct)
    Note over Calc: subtotal = Σ(qty * price)<br/>discount = subtotal * discountPct / 100<br/>taxable = subtotal - discount<br/>tax = taxable * taxPct / 100<br/>grandTotal = taxable + tax
    Calc-->>Builder: Updates Subtotal, Discount, Tax & Grand Total
    User->>Canvas: Draws Signature with Mouse or Touch
    Canvas->>Canvas: Records 2D Vector Path Coordinates
    User->>Builder: Clicks 'Save & Preview'
    Builder->>Canvas: canvas.toDataURL('image/png')
    Canvas-->>Builder: Base64 Signature Image String
    Builder->>Builder: Validates Customer Name & Line Items
    Builder->>Storage: Persist Invoice Object with Snapshot Data
    Storage-->>Builder: Confirmation OK
    Builder->>Preview: Route to /preview?id={newInvoiceId}
    Preview-->>User: Displays Formatted Invoice Sheet"""
    },
    {
        "filename": "07_sequence_payment_and_receipt",
        "title": "Sequence Diagram: Payment Recording, QR Generation & Receipt Dispatch",
        "code": """sequenceDiagram
    autonumber
    actor Merchant as Merchant or Client
    participant Preview as Invoice Preview View [Preview Route]
    participant QRHelper as Payment QR Helper Service
    participant QRServer as Dynamic QR Code API Server
    participant Modal as Payment Settlement Modal Form
    participant DB as LocalStorage [ig_invoices]
    participant Mail as Native Mail Client [mailto Protocol]

    Merchant->>Preview: Opens Invoice Preview
    Preview->>QRHelper: getPaymentQrTarget(invoice)
    alt Custom Checkout URL specified
        QRHelper-->>Preview: Returns paymentUrl
    else UPI ID configured
        QRHelper-->>Preview: Returns upi://pay?pa=...&pn=...&am=...&cu=INR
    end
    Preview->>QRServer: GET /v1/create-qr-code/?size=200x200&data={target}
    QRServer-->>Preview: Returns Dynamic QR Code Image Stream

    Merchant->>Preview: Clicks 'Record Payment / Mark Paid'
    Preview->>Modal: Opens Payment Modal
    Merchant->>Modal: Selects Date, Method [UPI, NEFT, Card], Enters UTR Ref & Note
    Merchant->>Modal: Submits Form ['Save & Display Receipt']
    Modal->>DB: Updates invoice.status='Paid', paidAt, paymentMethod, transactionRef
    DB-->>Modal: Updated Confirmation
    Modal->>Preview: Trigger Re-render
    Preview-->>Merchant: Renders Embossed PAID Watermark & Green Settlement Banner

    Merchant->>Preview: Clicks 'Email Receipt'
    Preview->>Preview: Builds Pre-filled Settlement Body Text
    Merchant->>Preview: Clicks 'Open Mail App'
    Preview->>Mail: Launches mailto:client@email.com?subject=...&body=..."""
    },
    {
        "filename": "08_dfd_level_0_context_diagram",
        "title": "Data Flow Diagram — Level 0 Context Diagram",
        "code": """flowchart LR
    User[" Business Owner / User"]
    System(("Ledgerly Invoice Generator System"))
    Client[" Customer / Client"]
    QRApi[" QR Code Generator API"]
    MailClient[" Native Mail Client"]

    User -->|"1. Credentials, Profiles, Line Items & Signature"| System
    System -->|"A. Dashboard Analytics & Invoices Ledger"| User
    System -->|"B. Rendered Invoice & Printable PDF"| User

    System -->|"2. Request Payment QR Code"| QRApi
    QRApi -->|"3. QR Code Image Stream"| System

    System -->|"4. Dispatch Pre-filled Email"| MailClient
    System -->|"5. Generated Invoice & Payment QR"| Client
    System -->|"6. Official Paid Receipt"| Client
    Client -.->|"Payment Settlement"| User"""
    },
    {
        "filename": "09_dfd_level_1_decomposition",
        "title": "Data Flow Diagram — Level 1 Functional Decomposition",
        "code": """flowchart TD
    User[" Business Owner / User"]

    subgraph Processes["System Core Processes"]
        P1(("1.0<br>Authentication &<br>Session Management"))
        P2(("2.0<br>Profile Directory<br>Management"))
        P3(("3.0<br>Invoice Builder &<br>Totals Engine"))
        P4(("4.0<br>Signature & QR<br>Generation"))
        P5(("5.0<br>Preview, Print &<br>Email Dispatcher"))
        P6(("6.0<br>Payment Settlement<br>& Receipt Generator"))
    end

    subgraph DataStores["Storage Repositories (localStorage)"]
        D1[("D1: ig_users")]
        D2[("D2: ig_session")]
        D3[("D3: ig_enterprises")]
        D4[("D4: ig_customers")]
        D5[("D5: ig_invoices")]
    end

    User -->|Credentials| P1
    P1 <-->|Verify / Store Account| D1
    P1 -->|Set Active Session| D2

    User -->|Customer & Enterprise Info| P2
    P2 <-->|Read / Write Enterprises| D3
    P2 <-->|Read / Write Customers| D4

    User -->|Line Items, Qty, Rates, Tax| P3
    D3 -->|Autofill Enterprise| P3
    D4 -->|Autofill Customer| P3
    P3 -->|Draft / Generated Invoice| D5

    User -->|Canvas Vector Signature| P4
    D3 -->|UPI ID / Payment URL| P4
    P4 -->|Signature Base64| D5
    P4 -->|Payment String| ExtQR[" api.qrserver.com"]
    ExtQR -->|QR Image Stream| P5

    D5 -->|Invoice Object| P5
    P5 -->|Print View / PDF Document| User
    P5 -->|Mail Subject & Body| ExtMail[" Mail Client (mailto:)"]

    User -->|Payment Date, Method, UTR Ref| P6
    P6 -->|Update Status: Paid + Settlement Meta| D5
    P6 -->|Render PAID Watermark & Receipt Banner| P5"""
    },
    {
        "filename": "10_component_ui_hierarchy",
        "title": "Component & UI Module Hierarchy",
        "code": """flowchart TD
    Root["Application Root (#app)"]

    subgraph Shell["Shared Shell (appShell)"]
        Sidebar["Sidebar Navigation\n- Ledgerly Logo & Branding\n- Nav Links (Dashboard, New, History, Customers, Enterprise, Profile)\n- User Info & Logout Button"]
        Topbar["Top Bar\n- Section Eyebrow & Title\n- Theme Switcher ( / )\n- Quick Action Trigger Button"]
        MainArea["Dynamic View Container"]
    end

    Root --> Shell

    MainArea --> V1["Dashboard View\n- KPI Stat Cards (Total, Billed, Paid, Pending)\n- Recent Invoices Table\n- Quick Action CTA Banner"]
    MainArea --> V2["Invoice Builder View\n- Seller / Enterprise Section (with Autofill)\n- Customer Section (with Autofill)\n- Dates & Terms Metadata\n- Dynamic Items Table with Live Math\n- HTML5 Canvas Signature Pad"]
    MainArea --> V3["Invoice Preview View\n- Action Toolbar (Edit, Status, Record Payment, Email, Print)\n- Invoice Sheet\n- Paid Receipt Banner\n- Bank & UPI QR Payment Box\n- Digital Signature Display"]
    MainArea --> V4["History View\n- Realtime Text Search\n- Status Dropdown Filter\n- Date Picker Filter\n- Invoices Ledger Table"]
    MainArea --> V5["Customers View\n- Search Filter\n- Customer Directory Grid\n- Add/Edit Customer Modal"]
    MainArea --> V6["Enterprise View\n- Search Filter\n- Multi-Enterprise Grid\n- Add/Edit Enterprise Modal (Bank/UPI Config)"]
    MainArea --> V7["Profile View\n- User Details Form\n- Password Change Form\n- Default Signature Canvas\n- Data Management (Reset DB)"]

    Root --> Toast["Floating Toast Notifications (#toast)"]"""
    },
    {
        "filename": "11_print_and_pdf_pipeline",
        "title": "Print & PDF Export Execution Pipeline",
        "code": """flowchart TD
    UserTrigger["User Clicks 'Print / Save as PDF'"] --> Exec["window.print() Executed"]
    Exec --> Evaluator{"Browser Evaluates @media print Rules"}

    subgraph SuppressedElements["Suppressed from Output (display: none !important)"]
        S1["Sidebar Navigation (.sidebar)"]
        S2["Top Bar (.topbar)"]
        S3["Preview Action Toolbar (.preview-toolbar)"]
        S4["Modals & Overlays (.modal-overlay)"]
        S5["Interactive Form Buttons (.btn)"]
        S6["Toast Notifications (#toast)"]
    end

    subgraph AppliedPrintStyles["Print Styling Applied"]
        A1["Page Sized to Standard A4 with 10mm Margins"]
        A2["Invoice Sheet Background Set to Pure Solid White"]
        A3["Drop Shadows, Rings & Screen Outlines Removed"]
        A4["PAID Watermark Opacity Optimized (0.15)"]
        A5["High-Contrast Typography & Table Borders"]
        A6["Payment QR Code Scaled at Crisp Print DPI"]
    end

    Evaluator --> SuppressedElements
    Evaluator --> AppliedPrintStyles
    SuppressedElements --> Output[" Spooler / PDF Engine (Save as PDF)"]
    AppliedPrintStyles --> Output"""
    },
    {
        "filename": "12_dfd_level_0_detailed_flow",
        "title": "DFD Level 0: Context Data Flow Diagram (from dfd_diagram.md)",
        "code": """flowchart TD
    User[" Business Owner / User"]
    System(("Ledgerly Invoice Generator System"))
    Client[" Customer / Client"]
    QRApi[" QR Code Generator API"]

    User -->|"1. Login / Registration Credentials"| System
    User -->|"2. Customer & Enterprise Profiles"| System
    User -->|"3. Line Items, Pricing, Discounts & Tax"| System
    User -->|"4. Authorised Digital Signature"| System
    User -->|"5. Payment Settlement Details & Paid Message"| System

    System -->|"A. Dashboard Analytics & Invoices History"| User
    System -->|"B. Invoice Preview & Printable PDF"| User

    System -->|"Request Payment QR (UPI / Pay URL)"| QRApi
    QRApi -->|"Rendered QR Code Image"| System

    System -->|"6. Generated Invoice / Payment QR"| Client
    System -->|"7. Official Paid Receipt & Settlement Notice"| Client
    Client -.->|"Payment via UPI / Bank Transfer"| User"""
    },
    {
        "filename": "13_dfd_level_1_detailed_processes",
        "title": "DFD Level 1: Detailed Data Flow Diagram (from dfd_diagram.md)",
        "code": """flowchart LR
    User[" Business Owner / User"]
    QRApi[" External QR Server API"]
    EmailClient[" Client Mail App (mailto:)"]

    subgraph DataStores["Data Stores"]
        D1[("D1: ig_users")]
        D2[("D2: ig_session")]
        D3[("D3: ig_enterprises")]
        D4[("D4: ig_customers")]
        D5[("D5: ig_invoices")]
    end

    P1(("1.0<br>Authentication &<br>Session Management"))
    P2(("2.0<br>Profile Directory<br>Management"))
    P3(("3.0<br>Invoice Builder &<br>Totals Engine"))
    P4(("4.0<br>Signature & QR<br>Generation"))
    P5(("5.0<br>Preview, Print &<br>Email Dispatcher"))
    P6(("6.0<br>Payment Settlement<br>& Receipt Generator"))

    User -->|"Credentials"| P1
    P1 <-->|"Verify / Store Account"| D1
    P1 -->|"Set Active Session"| D2

    User -->|"Customer / Enterprise Info"| P2
    P2 <-->|"Read / Write Enterprises"| D3
    P2 <-->|"Read / Write Customers"| D4

    User -->|"Items, Qty, Rates, Tax, Discounts"| P3
    D3 -->|"Autofill Enterprise"| P3
    D4 -->|"Autofill Customer"| P3
    P3 -->|"Draft / Generated Invoice"| D5

    User -->|"Canvas Touch/Mouse Signature"| P4
    P4 -->|"Base64 Signature Data"| D5
    D3 -->|"UPI ID / Payment URL"| P4
    P4 -->|"Encode Payment String"| QRApi
    QRApi -->|"QR Code Stream"| P5

    D5 -->|"Invoice Object"| P5
    P5 -->|"Print View / PDF Document"| User
    P5 -->|"Mail Template & Body"| EmailClient

    User -->|"Payment Date, Method, Txn ID, Paid Note"| P6
    P6 -->|"Update Status: 'Paid' + Settlement Meta"| D5
    P6 -->|"Render 'PAID' Stamp & Official Receipt"| P5"""
    },
    {
        "filename": "14_dfd_level_2_invoice_and_payment",
        "title": "DFD Level 2: Invoice Creation & Payment Settlement Process (from dfd_diagram.md)",
        "code": """flowchart TD
    subgraph Process3["Process 3.0: Invoice Construction & Calculation"]
        A[Start Invoice Creation] --> B{Select Existing or Enter New?}
        B -->|Select Profile| C[Autofill Seller / Customer Data]
        B -->|Enter New| D[Click 'Save Profile' -> Store in D3/D4]
        D --> C
        C --> E[Input Line Items: Qty * Unit Price]
        E --> F[Calculate Subtotal = Σ Item Totals]
        F --> G[Apply Discount: Subtotal - Discount Amt]
        G --> H[Apply Tax: Taxable Amt + Tax Amt]
        H --> I[Compute Grand Total]
        I --> J[Capture Digital Signature on Canvas Pad]
        J --> K[(Save to D5: ig_invoices)]
    end

    subgraph Process6["Process 6.0: Payment Recording & Receipt Generation"]
        K --> L[Open Invoice Preview #/preview]
        L --> M{Is Payment Received?}
        M -->|No| N[Display Payment QR Code & Bank Transfer Details]
        M -->|Yes| O[Click 'Record Payment / Mark Paid']
        O --> P[Enter Payment Date, Method, Txn/UTR ID, Custom Paid Msg]
        P --> Q[(Update Invoice in D5 with Status: Paid & Payment Meta)]
        Q --> R[Display 'PAID' Embossed Watermark]
        Q --> S[Display Official Green Payment Receipt Banner]
        Q --> T[Hide Payment QR / Convert to Settlement Proof]
        Q --> U[Generate Official Receipt Email & Printable PDF]
    end"""
    }
]

HTML_TEMPLATE = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Diagram Renderer</title>
<script src="http://127.0.0.1:{HTTP_PORT}/mermaid.min.js"></script>
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    background: #f8fafc;
    padding: 40px;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    display: inline-block;
  }}
  #card {{
    background: #ffffff;
    border: 2px solid #e2e8f0;
    border-radius: 16px;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.08);
    padding: 36px 44px 44px;
    display: inline-block;
  }}
  #card-header {{
    border-bottom: 2px solid #e2e8f0;
    padding-bottom: 18px;
    margin-bottom: 28px;
  }}
  #card-title {{
    font-size: 28px;
    font-weight: 800;
    color: #0f172a;
    letter-spacing: -0.02em;
  }}
  #card-subtitle {{
    font-size: 15px;
    color: #64748b;
    margin-top: 6px;
    font-weight: 500;
  }}
  #diagram-container {{
    display: block;
  }}
  /* DO NOT SHRINK SVG - ALLOW FULL NATURAL VECTOR SIZE */
  #diagram-container svg {{
    display: block;
    width: auto !important;
    height: auto !important;
    max-width: none !important;
  }}
  .node text, .node .label, .node span, text, tspan {{
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif !important;
    font-size: 19px !important;
    font-weight: 600 !important;
  }}
  .edgeLabel, .edgeLabel span {{
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif !important;
    font-size: 16px !important;
    font-weight: 700 !important;
    background-color: #ffffff !important;
    padding: 3px 8px !important;
    border-radius: 4px !important;
  }}
  .cluster-label text, .cluster-label span {{
    font-size: 22px !important;
    font-weight: 800 !important;
    fill: #0f172a !important;
  }}
</style>
</head>
<body>
  <div id="card">
    <div id="card-header">
      <div id="card-title"></div>
      <div id="card-subtitle">Ledgerly System Architecture &amp; Engineering Specification</div>
    </div>
    <div id="diagram-container"></div>
  </div>

  <script>
    mermaid.initialize({{
      startOnLoad: false,
      theme: 'default',
      securityLevel: 'loose',
      fontFamily: '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif',
      fontSize: 20,
      themeVariables: {{
        fontSize: '20px',
        primaryColor: '#e0f2fe',
        primaryTextColor: '#0369a1',
        primaryBorderColor: '#0284c7',
        lineColor: '#334155',
        secondaryColor: '#f0fdf4',
        tertiaryColor: '#f8fafc',
        fontFamily: '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif'
      }},
      flowchart: {{
        curve: 'basis',
        nodeSpacing: 60,
        rankSpacing: 70,
        padding: 24
      }},
      er: {{
        fontSize: 18
      }},
      sequence: {{
        fontSize: 18,
        actorFontSize: 18,
        messageFontSize: 18,
        boxMargin: 18
      }}
    }});

    window.renderDiagram = async function(title, code) {{
      document.getElementById('card-title').textContent = title;
      const container = document.getElementById('diagram-container');
      container.innerHTML = '';
      const id = 'svg_' + Math.random().toString(36).slice(2);
      try {{
        const res = await mermaid.render(id, code);
        container.innerHTML = res.svg;
        return {{ success: true, svg: res.svg }};
      }} catch (err) {{
        container.innerHTML = '<pre style="color:red;padding:20px;">' + err.toString() + '</pre>';
        return {{ success: false, error: err.toString() }};
      }}
    }};
  </script>
</body>
</html>
"""

class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(SCRATCH_DIR), **kwargs)
    def log_message(self, *args):
        pass

async def run():
    OUTPUT_DIR.mkdir(exist_ok=True)
    SCRATCH_DIR.mkdir(exist_ok=True)

    # Write render.html into SCRATCH_DIR
    render_html_path = SCRATCH_DIR / "render.html"
    with open(render_html_path, "w", encoding="utf-8") as f:
        f.write(HTML_TEMPLATE)

    # Start local HTTP server on HTTP_PORT
    socketserver.TCPServer.allow_reuse_address = True
    server = socketserver.TCPServer(("127.0.0.1", HTTP_PORT), QuietHandler)
    server_thread = threading.Thread(target=server.serve_forever, daemon=True)
    server_thread.start()
    print(f"Local HTTP server active on http://127.0.0.1:{HTTP_PORT}")

    temp_user_dir = tempfile.mkdtemp(prefix="chrome_diagram_")
    chrome_cmd = [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        "--headless=new",
        "--remote-debugging-port=9222",
        f"--user-data-dir={temp_user_dir}",
        "--disable-gpu",
        "--no-sandbox",
        "--window-size=3840,2400"
    ]
    print("Launching isolated headless Chrome (3840x2400)...")
    chrome_proc = subprocess.Popen(chrome_cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(1.8)

    try:
        tabs = requests.get("http://127.0.0.1:9222/json").json()
        page_tabs = [t for t in tabs if t.get("type") == "page"]
        ws_url = page_tabs[0]["webSocketDebuggerUrl"]

        async with websockets.connect(ws_url, max_size=100 * 1024 * 1024) as ws:
            req_id = 0

            async def cdp(method, params=None):
                nonlocal req_id
                req_id += 1
                curr_id = req_id
                payload = {"id": curr_id, "method": method}
                if params:
                    payload["params"] = params
                await ws.send(json.dumps(payload))
                while True:
                    raw = await ws.recv()
                    res = json.loads(raw)
                    if res.get("id") == curr_id:
                        if "error" in res:
                            print(f"CDP Error in {method}:", res["error"])
                        return res.get("result", {})

            await cdp("Page.enable")
            await cdp("Runtime.enable")
            await cdp("Emulation.setDeviceMetricsOverride", {
                "width": 3840,
                "height": 2400,
                "deviceScaleFactor": 2,
                "mobile": False
            })

            url = f"http://127.0.0.1:{HTTP_PORT}/render.html"
            print(f"Navigating to {url}")
            await cdp("Page.navigate", {"url": url})
            await asyncio.sleep(2.0)

            for idx, diag in enumerate(DIAGRAMS, 1):
                base_name = diag["filename"]
                title = diag["title"]
                code = diag["code"]
                print(f"[{idx}/{len(DIAGRAMS)}] Rendering {base_name}: {title}...")

                # Call window.renderDiagram
                js_code = f"window.renderDiagram({json.dumps(title)}, {json.dumps(code)})"
                render_res = await cdp("Runtime.evaluate", {
                    "expression": js_code,
                    "awaitPromise": True,
                    "returnByValue": True
                })

                res_val = render_res.get("result", {}).get("value", {})
                svg_data = res_val.get("svg", "")
                if svg_data:
                    # Save pure vector SVG as well!
                    svg_file = OUTPUT_DIR / f"{base_name}.svg"
                    with open(svg_file, "w", encoding="utf-8") as sf:
                        sf.write(svg_data)

                await asyncio.sleep(0.8)

                # Get bounding rect of #card
                rect_res = await cdp("Runtime.evaluate", {
                    "expression": """(() => {
                        const el = document.getElementById('card');
                        if (!el) return JSON.stringify({x: 0, y: 0, width: 1200, height: 800});
                        const r = el.getBoundingClientRect();
                        return JSON.stringify({
                            x: Math.max(0, Math.floor(r.x)),
                            y: Math.max(0, Math.floor(r.y)),
                            width: Math.max(300, Math.ceil(r.width)),
                            height: Math.max(150, Math.ceil(r.height))
                        });
                    })()""",
                    "returnByValue": True
                })

                val_str = rect_res.get("result", {}).get("value", "{}")
                rect = json.loads(val_str)
                card_w = rect.get("width", 1600)
                card_h = rect.get("height", 1200)

                # Ensure browser viewport fits the entire card so nothing is truncated
                target_viewport_w = max(3840, card_w + 200)
                target_viewport_h = max(2400, card_h + 200)
                await cdp("Emulation.setDeviceMetricsOverride", {
                    "width": target_viewport_w,
                    "height": target_viewport_h,
                    "deviceScaleFactor": 2,
                    "mobile": False
                })

                await asyncio.sleep(0.4)

                # Re-evaluate rect after viewport resize
                rect_res2 = await cdp("Runtime.evaluate", {
                    "expression": """(() => {
                        const el = document.getElementById('card');
                        const r = el.getBoundingClientRect();
                        return JSON.stringify({
                            x: Math.max(0, Math.floor(r.x)),
                            y: Math.max(0, Math.floor(r.y)),
                            width: Math.ceil(r.width),
                            height: Math.ceil(r.height)
                        });
                    })()""",
                    "returnByValue": True
                })
                rect = json.loads(rect_res2.get("result", {}).get("value", val_str))

                # Capture crisp high-res 2x PNG of card bounding box
                clip = {
                    "x": max(0, rect["x"] - 8),
                    "y": max(0, rect["y"] - 8),
                    "width": rect["width"] + 16,
                    "height": rect["height"] + 16,
                    "scale": 2
                }

                shot_res = await cdp("Page.captureScreenshot", {
                    "format": "png",
                    "clip": clip,
                    "fromSurface": True
                })

                img_bytes = base64.b64decode(shot_res["data"])
                png_file = OUTPUT_DIR / f"{base_name}.png"
                with open(png_file, "wb") as f:
                    f.write(img_bytes)

                print(f"    -> Saved {png_file.name} ({len(img_bytes) / 1024:.1f} KB, dimensions: {rect['width']*2}x{rect['height']*2}px) and {base_name}.svg")

        print(f"\nSUCCESS! All {len(DIAGRAMS)} diagrams rendered in Ultra-HD PNG & Lossless SVG into {OUTPUT_DIR}")
    finally:
        chrome_proc.terminate()
        server.shutdown()

if __name__ == "__main__":
    asyncio.run(run())
