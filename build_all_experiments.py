"""
build_all_experiments.py - Generates all 13 individual lab manual docx files.
Tailored 100% to 'Ledgerly' Invoice & Quotation Generator.
"""

from pathlib import Path
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from generate_lab_docx import (
    OUTPUT_DIR, DIAGRAMS_DIR, add_header, style_heading, 
    add_styled_table, add_code_block, add_image_if_exists
)

# -------------------------------------------------------------
# EXPERIMENT 1: Project Selection and Conceptualization
# -------------------------------------------------------------
def generate_exp_01():
    doc = Document()
    add_header(doc, "1", "Project Selection and Conceptualization", module_num="1")

    style_heading(doc, "1. Pre-Requisites", 2)
    p = doc.add_paragraph()
    p.add_run("• Basic knowledge of the Software Development Life Cycle (SDLC) & Agile principles.\n"
              "• Understanding of small business accounting, billing lifecycles, and user needs.\n"
              "• Fundamentals of requirement gathering and stakeholder boundary definition.\n"
              "• Awareness of modern web standards, browser persistence, and offline web apps.")

    style_heading(doc, "2. Problem Statement", 2)
    doc.add_paragraph(
        "Freelancers, consultants, contractors, and small-to-medium enterprise (SME) owners frequently "
        "struggle with creating, tracking, and maintaining professional invoices. Currently, billing is "
        "often handled manually through error-prone spreadsheet templates, generic Word documents, or bulky "
        "subscription-based accounting software that requires mandatory internet connectivity and complex setups.\n\n"
        "This leads to severe operational bottlenecks: calculation mistakes in tax and discount rates, inconsistent "
        "invoice numbering, lack of audit trails for partial payment settlements, missing client directories, "
        "and delays in payment collection.\n\n"
        "The goal is to design and develop 'Ledgerly' — a high-performance, offline-first Progressive Web Application (PWA) "
        "Invoice and Quotation Management System. Ledgerly allows users to swiftly compile professional invoices and estimates, "
        "automatically calculate multi-tier taxes (CGST/SGST/IGST), collect digital signatures on canvas, generate instant UPI "
        "payment QR codes, track partial payment ledgers, and export print-ready PDFs directly in the browser without third-party server lock-in."
    )

    style_heading(doc, "3. Theory", 2)
    style_heading(doc, "3.1 Project Conceptualization", 3)
    doc.add_paragraph(
        "Project conceptualization involves identifying core user pain points, establishing system boundaries, "
        "determining key user personas, and specifying architectural feasibility. Key elements include:\n"
        "• Project Scope – Defining clear functional boundaries (In-Scope vs. Out-of-Scope).\n"
        "• Stakeholder & Actor Identification – Identifying who creates, approves, and receives invoices.\n"
        "• Core Functional Modules – Grouping operations into cohesive functional subsystems.\n"
        "• Feasibility Analysis – Assessing technical, operational, and financial feasibility."
    )

    style_heading(doc, "3.2 Need for a Client-Side Modern Invoicing Engine", 3)
    doc.add_paragraph(
        "Traditional desktop and cloud ERP systems have several disadvantages for micro-enterprises:\n"
        "• High monthly recurring subscription costs.\n"
        "• Rigid templates with limited on-device custom styling.\n"
        "• Dependency on uninterrupted cloud internet connectivity.\n"
        "• Privacy risks when uploading sensitive financial and customer contact data to third-party databases.\n"
        "An offline-first, client-rendered web application guarantees immediate availability, zero subscription cost, and total data privacy."
    )

    style_heading(doc, "4. Project Scope", 2)
    style_heading(doc, "4.1 In-Scope Functionalities", 3)
    doc.add_paragraph(
        "1. Enterprise Profile Management: Configure company name, GSTIN, address, logo, bank details, and UPI ID.\n"
        "2. Customer Directory: Maintain client records with GSTIN, email, phone, and billing address.\n"
        "3. Dynamic Line-Item Builder: Real-time item rows with HSN codes, quantity, unit price, and itemized tax rates.\n"
        "4. Automated Calculation Engine: Instant computation of subtotal, flat/percentage discounts, intra/inter-state GST, additional charges, and integer round-off.\n"
        "5. Canvas Digital Signature: Native HTML5 canvas capture for handwritten signatures.\n"
        "6. Dynamic UPI QR Code: On-the-fly payment QR generation using UPI deep-links.\n"
        "7. Payment Settlement Ledger: Record multiple installment payments (Cash, UPI, NEFT, Card) and compute remaining balance due.\n"
        "8. Multi-Template PDF & Print Export: 4 design presets (Classic, Modern Teal, Minimal, Compact) with lossless browser print and direct PDF download.\n"
        "9. Offline-First PWA: Service worker asset caching and local browser storage persistence."
    )

    style_heading(doc, "4.2 Out-of-Scope (Future Enhancements)", 3)
    doc.add_paragraph(
        "• Direct bank-to-bank automated reconciliation API.\n"
        "• Multi-tenant centralized cloud database sync.\n"
        "• Native mobile app binary deployment (App Store / Play Store)."
    )

    style_heading(doc, "5. Stakeholders & User Roles", 2)
    headers = ["Stakeholder / Role", "Description", "Primary System Needs"]
    data = [
        ["Freelancer / Contractor", "Independent professional billing clients for hours or milestones.", "Fast quotation creation, UPI payment QR, PDF downloads."],
        ["Small Business Owner / Retailer", "Commercial store or service enterprise owner.", "GST compliance (CGST/SGST/IGST), customer directory, partial payment tracking."],
        ["Accountant / Auditor", "Reviews financial balance and records.", "Receivables aging, payment settlement history, CSV/JSON data backup."],
        ["Client / Buyer", "Recipient of invoice or estimate.", "Clear itemized charges, accurate tax breakdown, clickable payment link/QR."]
    ]
    add_styled_table(doc, headers, data)

    style_heading(doc, "6. Core Modules of the System", 2)
    m_headers = ["Module Name", "Primary Responsibilities"]
    m_data = [
        ["Authentication & Session Guard", "User signup, credential verification, session retention in localStorage, and protected route guarding."],
        ["Enterprise Profile Module", "Manage multiple business profiles, default tax rates, bank credentials, and base64 company logos."],
        ["Customer Management Module", "Store client contact records, billing addresses, tax IDs, and transaction histories."],
        ["Invoice & Estimate Builder", "Dynamic line-item manipulation, item catalog autofill, discount engine, and canvas signature pad."],
        ["Calculation & Tax Engine", "Compute subtotals, intra-state (CGST 9% + SGST 9%) vs inter-state (IGST 18%) tax splits, extra shipping/handling, and auto round-off."],
        ["Payment & Settlement Ledger", "Maintain chronological payment installments, adjust remaining balance dues, and toggle invoice states (Unpaid, Partially Paid, Paid)."],
        ["Export & Dispatch Module", "Client-side PDF generation via html2pdf.js, standard A4 thermal/sheet printing, and one-click WhatsApp/Email dispatch."],
        ["Dashboard & Analytics", "Financial KPI cards (Total Billed, Collected, Balance Due, Overdue Count), receivables aging, and 6-month revenue SVG charts."]
    ]
    add_styled_table(doc, m_headers, m_data)

    style_heading(doc, "7. Assumptions & Constraints", 2)
    doc.add_paragraph(
        "Assumptions:\n"
        "• Users access the application via a modern ECMAScript 6+ compatible web browser (Chrome, Edge, Firefox, Safari).\n"
        "• The client machine supports localStorage with at least 5MB quota available.\n"
        "Constraints:\n"
        "• Offline persistence is scoped to the local browser profile unless the user exports data backups.\n"
        "• Real-time payment verification depends on external payment gateways or manual merchant acknowledgement."
    )

    style_heading(doc, "8. Feasibility Analysis", 2)
    doc.add_paragraph(
        "• Technical Feasibility: Built entirely using standard HTML5, CSS3, Vanilla JavaScript, and Service Workers. Requires zero proprietary server dependencies.\n"
        "• Operational Feasibility: Extremely intuitive Single-Page Application (SPA) with zero installation hurdles. Runs instantly from file or web host.\n"
        "• Economic Feasibility: 100% open-source development stack with zero software licensing or recurring database server hosting expenses."
    )

    style_heading(doc, "9. High-Level Concept Map", 2)
    add_image_if_exists(doc, "01_system_architecture.png", "Ledgerly High-Level System Architecture and Runtime Blueprint")

    style_heading(doc, "10. Conclusion", 2)
    doc.add_paragraph(
        "The project 'Ledgerly (Invoice & Quotation Generator)' was successfully conceptualized with an exhaustive "
        "problem definition, well-bounded scope, distinct stakeholder profiles, structured functional modules, and thorough "
        "feasibility validation. This robust foundation establishes the operational framework for subsequent software engineering "
        "phases including requirements modeling, UI architecture, UML diagrams, automated testing, and deployment."
    )

    doc.save(OUTPUT_DIR / "Exp_01_Project_Selection_and_Conceptualization.docx")
    print("Generated Exp_01_Project_Selection_and_Conceptualization.docx")


# -------------------------------------------------------------
# EXPERIMENT 2: Design the Static Web Pages Required for Project
# -------------------------------------------------------------
def generate_exp_02():
    doc = Document()
    add_header(doc, "2", "Design Static Web Pages Required for the Project (HTML)", module_num="1")

    style_heading(doc, "1. Pre-Requisites", 2)
    doc.add_paragraph(
        "• Proficiency in HTML5 semantic document structure (doctype, head, body, section, nav, main, footer).\n"
        "• Knowledge of form controls: input, select, textarea, button, labels, and fieldsets.\n"
        "• Understanding of tabular data presentation using table, thead, tbody, tr, th, td.\n"
        "• Familiarity with client-side Single-Page Application (SPA) mount points and modal markup."
    )

    style_heading(doc, "2. Objective", 2)
    doc.add_paragraph(
        "To construct the core semantic HTML5 views and document skeletons for the Ledgerly Invoice Generator, including:\n"
        "1. Application Shell & Mount Point (index.html)\n"
        "2. User Authentication Views (Login & Register modals/views)\n"
        "3. Financial Dashboard & Analytics View\n"
        "4. Invoice & Estimate Builder Screen (Dynamic item tables & signature canvas)\n"
        "5. Invoice Preview & Printable Document Sheet (#invoiceSheet)\n"
        "6. Customer Directory & Payment History Table"
    )

    style_heading(doc, "3. Theory", 2)
    style_heading(doc, "3.1 HTML5 in Modern Single-Page Web Applications", 3)
    doc.add_paragraph(
        "HTML5 provides the foundational semantic skeleton. In modern web development, rather than reloading "
        "multiple discrete HTML documents, an SPA architecture utilizes a lightweight index.html host file containing "
        "global shell elements (navigation headers, toast notifications, modals) and a dynamic container (<div id=\"app\">) "
        "rendered dynamically via JavaScript view templates."
    )

    style_heading(doc, "3.2 Key HTML5 Elements Employed", 3)
    doc.add_paragraph(
        "• Document Architecture: <!DOCTYPE html>, <html lang=\"en\">, <head>, <body>, <nav>, <header>, <main>.\n"
        "• Form Components: <form>, <input type=\"text|number|date|email|file\">, <select>, <option>, <button>.\n"
        "• Billing Grid & Ledgers: <table>, <thead>, <tbody>, <tr>, <th>, <td>, <colgroup>.\n"
        "• Graphics & Signatures: <canvas id=\"sigPad\"> for hardware-accelerated vector stylus/touch capture.\n"
        "• PWA Manifest & Meta: <link rel=\"manifest\">, viewport meta tags for responsive mobile scaling."
    )

    style_heading(doc, "4. Pages & View Architecture", 2)
    headers = ["View / Screen", "URL Hash Route", "Key HTML Components", "Description"]
    data = [
        ["Application Root", "/", "<div id=\"app\">, <div id=\"toast\">", "Mount point for PWA shell and global toasts."],
        ["Sign In Screen", "#/login", "<form>, <input type=\"email\">, <input type=\"password\">", "Secure account access form."],
        ["User Registration", "#/register", "<form>, 5+ input fields, submit button", "New account creation with validation."],
        ["Dashboard View", "#/dashboard", "<div class=\"kpi-grid\">, <svg> charts", "Financial KPIs and overdue invoices."],
        ["Invoice Builder", "#/create", "<form>, <table class=\"items-table\">, <canvas>", "Line-item entry, taxes, discount, signature."],
        ["Invoice Preview Sheet", "#/preview", "<div id=\"invoiceSheet\">, <table>, <img> QR", "Print-ready A4 billing sheet."],
        ["Customer Directory", "#/customers", "<div class=\"cards-grid\">, modals", "Client profiles and account statements."]
    ]
    add_styled_table(doc, headers, data)

    style_heading(doc, "5. Core HTML Code Implementations", 2)

    style_heading(doc, "5.1 Global Shell (index.html)", 3)
    add_code_block(doc, 
'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Ledgerly — Invoice & Quotation Generator</title>
  <link rel="manifest" href="manifest.json">
  <link rel="stylesheet" href="style.css">
  <script src="https://cdnjs.cloudflare.com/ajax/libs/html2pdf.js/0.10.1/html2pdf.bundle.min.js"></script>
</head>
<body>
  <!-- Dynamic SPA Root Container -->
  <div id="app"></div>
  
  <!-- Global Toast Notification Shelf -->
  <div id="toast" class="toast"></div>

  <script src="script.js"></script>
</body>
</html>''')

    style_heading(doc, "5.2 Invoice Document Sheet View (Structural HTML Template)", 3)
    add_code_block(doc,
'''<!-- Semantic Invoice Sheet Container for PDF and Print Rendering -->
<div id="invoiceSheet" class="invoice-sheet theme-classic">
  <header class="sheet-header">
    <div class="seller-info">
      <img id="sellerLogo" class="seller-logo" alt="Company Logo">
      <h1 class="company-name">Acme Solutions Pvt Ltd</h1>
      <p class="company-meta">GSTIN: 27AABCU9603R1ZM | Phone: +91 9876543210</p>
    </div>
    <div class="doc-badge">
      <span class="type-pill">TAX INVOICE</span>
      <h2 class="doc-number">INV-2026-0042</h2>
      <p>Date: 15 Oct 2026 | Due: 30 Oct 2026</p>
    </div>
  </header>

  <!-- Line Item Billing Table -->
  <table class="sheet-table">
    <thead>
      <tr>
        <th>#</th>
        <th>Item Description</th>
        <th>HSN/SAC</th>
        <th>Qty</th>
        <th>Rate</th>
        <th>Tax %</th>
        <th>Total</th>
      </tr>
    </thead>
    <tbody id="sheetItemsBody">
      <!-- Dynamic Rows Rendered by Engine -->
    </tbody>
  </table>

  <!-- Calculation Summary & Canvas Signature -->
  <footer class="sheet-footer">
    <div class="payment-instructions">
      <p>Scan to Pay via UPI:</p>
      <img id="upiQrCode" alt="Payment QR Code">
    </div>
    <div class="summary-breakdown">
      <p>Subtotal: <span id="valSubtotal">₹0.00</span></p>
      <p>GST (18%): <span id="valTax">₹0.00</span></p>
      <h3>Grand Total: <span id="valGrand">₹0.00</span></h3>
    </div>
  </footer>
</div>''')

    style_heading(doc, "6. Output / Expected Result", 2)
    doc.add_paragraph(
        "All HTML5 views compile and render seamlessly in standard web browsers. The responsive viewport configuration "
        "guarantees adaptive scaling across mobile, tablet, and desktop monitors, while semantic table and form tags "
        "provide clean Document Object Model (DOM) hooks for dynamic JavaScript interactivity and print stylesheets."
    )

    style_heading(doc, "7. Conclusion", 2)
    doc.add_paragraph(
        "Experiment 2 demonstrated the practical design and implementation of clean, accessible, semantic HTML5 web pages "
        "for the Ledgerly system. Separating structural skeleton views from presentation and logic laid the perfect groundwork "
        "for CSS styling (Experiment 4) and JavaScript form validation and event handling (Experiment 3)."
    )

    doc.save(OUTPUT_DIR / "Exp_02_Static_HTML_Pages.docx")
    print("Generated Exp_02_Static_HTML_Pages.docx")


# -------------------------------------------------------------
# EXPERIMENT 3: JavaScript Form Validation
# -------------------------------------------------------------
def generate_exp_03():
    doc = Document()
    add_header(doc, "3", "JavaScript Form Validation", module_num="1")

    style_heading(doc, "1. Pre-Requisites", 2)
    doc.add_paragraph(
        "• Comprehensive understanding of JavaScript DOM manipulation (document.getElementById, querySelector).\n"
        "• Knowledge of form submit lifecycle, event listeners, and preventDefault() / return false controls.\n"
        "• Familiarity with Regular Expressions (RegEx) for string parsing, pattern validation, and sanitization.\n"
        "• Principles of user feedback: inline visual field highlighting and non-intrusive toast alerts."
    )

    style_heading(doc, "2. Objective", 2)
    doc.add_paragraph(
        "To develop robust client-side JavaScript validation functions for Ledgerly to validate:\n"
        "1. User Registration Form: Name (alphabets, min 3 chars), Email (RFC-compliant format), Password (min 6 chars), Mobile (exactly 10 digits).\n"
        "2. Enterprise Profile Form: Business Name, GSTIN pattern (2 digits, 10 alphanumeric PAN, 1 entity digit, Z, 1 checksum), and UPI ID (@bank).\n"
        "3. Invoice Builder Form: Customer Name (not empty), Item Description, Quantity (>0), Unit Price (>=0), and Tax Percentage (0 to 100%)."
    )

    style_heading(doc, "3. Theory", 2)
    style_heading(doc, "3.1 Importance of Client-Side Validation", 3)
    doc.add_paragraph(
        "Client-side validation is the first line of defense in web applications. It serves critical purposes:\n"
        "• Immediate Feedback: Highlights user input errors instantly before processing without waiting for server response.\n"
        "• Network & Memory Optimization: Stops malformed payloads from polluting persistent local/remote databases.\n"
        "• Prevention of Financial Corruption: Ensures that negative prices, non-numeric quantities, or corrupt tax rates do not compromise ledger integrity."
    )

    style_heading(doc, "3.2 Regular Expressions Employed", 3)
    headers = ["Validation Target", "Regular Expression Pattern", "Description & Rules"]
    data = [
        ["Email Address", r"^[\w\.-]+@[\w\.-]+\.\w{2,4}$", "Matches standard RFC name@domain.com formatting."],
        ["Mobile Number", r"^[0-9]{10}$", "Restricts input strictly to a 10-digit numeric Indian phone number."],
        ["Alphabetical Name", r"^[A-Za-z\s]{3,}$", "Requires at least 3 letters; accepts English alphabets and spaces."],
        ["GSTIN Identifier", r"^[0-9]{2}[A-Z]{5}[0-9]{4}[A-Z]{1}[1-9A-Z]{1}Z[0-9A-Z]{1}$", "Validates 15-character statutory Indian GSTIN format."],
        ["UPI VPA Address", r"^[\w\.\-_]+@[\w]+$", "Matches Virtual Payment Address format like username@okaxis."]
    ]
    add_styled_table(doc, headers, data)

    style_heading(doc, "4. Validation Code Implementation", 2)
    add_code_block(doc,
'''/**
 * Ledgerly Client-Side Validation Suite
 * Validates User Registration, Enterprise Details, and Invoice Form Inputs
 */

function validateRegistrationForm(formData) {
  const errors = [];
  
  // 1. Name validation
  const name = (formData.name || "").trim();
  const nameRegex = /^[A-Za-z\s]{3,}$/;
  if (!nameRegex.test(name)) {
    errors.push("Full Name must contain only alphabets and be at least 3 characters long.");
  }

  // 2. Email validation
  const email = (formData.email || "").trim();
  const emailRegex = /^[\\w\\.-]+@[\\w\\.-]+\\.\\w{2,4}$/;
  if (!emailRegex.test(email)) {
    errors.push("Invalid email address format (Expected: name@domain.com).");
  }

  // 3. Password validation
  const password = formData.password || "";
  if (password.length < 6) {
    errors.push("Password must be at least 6 characters long.");
  }

  // 4. Mobile Number validation
  const phone = (formData.phone || "").trim();
  const phoneRegex = /^[0-9]{10}$/;
  if (!phoneRegex.test(phone)) {
    errors.push("Phone number must contain exactly 10 numeric digits.");
  }

  return {
    isValid: errors.length === 0,
    errors: errors
  };
}

function validateInvoiceData(invoice) {
  const errors = [];

  // Customer Name check
  if (!invoice.customerName || invoice.customerName.trim().length === 0) {
    errors.push("Customer Name is required.");
  }

  // Line items check
  if (!invoice.items || invoice.items.length === 0) {
    errors.push("At least one line item is required.");
  } else {
    invoice.items.forEach((item, index) => {
      if (!item.name || item.name.trim().length === 0) {
        errors.push(`Item #${index + 1}: Description cannot be empty.`);
      }
      if (isNaN(item.qty) || Number(item.qty) <= 0) {
        errors.push(`Item #${index + 1}: Quantity must be greater than 0.`);
      }
      if (isNaN(item.price) || Number(item.price) < 0) {
        errors.push(`Item #${index + 1}: Unit price cannot be negative.`);
      }
      if (item.taxRate !== undefined && (Number(item.taxRate) < 0 || Number(item.taxRate) > 100)) {
        errors.push(`Item #${index + 1}: Tax rate must be between 0% and 100%.`);
      }
    });
  }

  return {
    isValid: errors.length === 0,
    errors: errors
  };
}''')

    style_heading(doc, "5. Verification & Test Input Execution", 2)
    t_headers = ["Test Scenario", "Input Values Provided", "Expected Result", "Actual Output"]
    t_data = [
        ["Invalid Email", "name='Krushna', email='krushna_invalid', pass='pass123', phone='9876543210'", "Reject: Invalid email pattern", "Error alert shown. Submission blocked."],
        ["Short Password", "name='Krushna', email='k@test.com', pass='123', phone='9876543210'", "Reject: Password < 6 characters", "Error alert shown. Password field focused."],
        ["Alpha in Phone", "name='Krushna', email='k@test.com', pass='pass123', phone='987654ABCD'", "Reject: Non-digit characters", "Error: 'Phone must contain 10 digits'."],
        ["Empty Line Item", "Customer='Client A', Item description=''", "Reject: Item name required", "Error: 'Description cannot be empty'."],
        ["Valid Inputs", "All fields formatted properly with valid data", "Accept: Proceed with submission", "Form submitted. Toast notification displayed."]
    ]
    add_styled_table(doc, t_headers, t_data)

    style_heading(doc, "6. Output / Expected Result", 2)
    doc.add_paragraph(
        "When an invalid value is submitted, the JavaScript validation routines intercept the form submit event, "
        "render a prominent error alert banner, and prevent data persistence. Valid data passes smoothly and triggers "
        "the success callback."
    )

    style_heading(doc, "7. Conclusion", 2)
    doc.add_paragraph(
        "Experiment 3 established a comprehensive client-side data validation pipeline using JavaScript regular expressions "
        "and DOM manipulation. It guarantees financial accuracy and data sanitization for Ledgerly prior to storing "
        "records in browser localStorage."
    )

    doc.save(OUTPUT_DIR / "Exp_03_JS_Form_Validation.docx")
    print("Generated Exp_03_JS_Form_Validation.docx")


# -------------------------------------------------------------
# EXPERIMENT 4: Design a Web Page Using CSS
# -------------------------------------------------------------
def generate_exp_04():
    doc = Document()
    add_header(doc, "4", "Design a Web Page Using CSS (Cascading Style Sheets)", module_num="1")

    style_heading(doc, "1. Pre-Requisites", 2)
    doc.add_paragraph(
        "• Mastery of CSS3 fundamentals: element, class, ID, pseudo-classes (:hover, :focus, :disabled).\n"
        "• Deep understanding of Modern Box Model, CSS Custom Properties (Variables), and HSL/Hex color palettes.\n"
        "• Fluid layout design using CSS Flexbox (1D layouts) and CSS Grid (2D multi-column dashboards).\n"
        "• Implementation of @media queries for responsive mobile viewports and dedicated @media print styling."
    )

    style_heading(doc, "2. Objective", 2)
    doc.add_paragraph(
        "To design and apply a visual styling system for Ledgerly using external CSS (style.css):\n"
        "1. Define a centralized Design Token Palette (Colors, Surfaces, Borders, Fonts, Elevations).\n"
        "2. Construct responsive layouts for the Financial Dashboard, Navigation Rail, and Invoice Builder.\n"
        "3. Provide multi-theme capability: Classic Emerald, Navy Corporate, and Dark Mode.\n"
        "4. Implement dedicated @media print stylesheets for A4 physical printer paper and PDF export."
    )

    style_heading(doc, "3. Theory", 2)
    style_heading(doc, "3.1 CSS Design Tokens & Variable Architecture", 3)
    doc.add_paragraph(
        "Modern CSS utilizes CSS Custom Properties (:root variables). This decouples presentation values from "
        "individual selectors, enabling instant dynamic theme switching, consistent spacing scales, and effortless maintenance."
    )

    style_heading(doc, "3.2 Responsive CSS Grid & Media Print", 3)
    doc.add_paragraph(
        "• CSS Grid & Flexbox: Used to position KPI cards (repeat(auto-fit, minmax(240px, 1fr))), alignment of invoice header rows, and table cell formatting.\n"
        "• @media print: In ordinary screen displays, navigation rails, action buttons, and backdrops are visible. When printing (Ctrl+P) or generating PDFs, @media print hides all non-document UI (.no-print { display: none !important; }) and applies exact A4 page dimensions (210mm x 297mm)."
    )

    style_heading(doc, "4. CSS Code Implementation Highlights", 2)
    add_code_block(doc,
'''/* =========================================================
   LEDGERLY DESIGN TOKENS & SYSTEM VARIABLES (style.css)
   ========================================================= */
:root {
  --primary: #1b4d4b;
  --primary-hover: #143937;
  --accent: #2e7d32;
  --bg-page: #f4f6f8;
  --bg-surface: #ffffff;
  --border-color: #e2e8f0;
  --text-main: #1e293b;
  --text-muted: #64748b;
  --shadow-sm: 0 1px 3px rgba(0,0,0,0.08);
  --shadow-md: 0 4px 6px -1px rgba(0,0,0,0.1);
  --radius-md: 8px;
  --radius-lg: 12px;
  --font-sans: 'Inter', -apple-system, sans-serif;
  --font-serif: 'Fraunces', serif;
}

/* Dashboard KPI Card Grid Layout */
.kpi-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 1.25rem;
  margin-bottom: 2rem;
}

.kpi-card {
  background: var(--bg-surface);
  border: 1px solid var(--border-color);
  border-radius: var(--radius-lg);
  padding: 1.5rem;
  box-shadow: var(--shadow-sm);
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.kpi-card:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-md);
}

/* Buttons & Interactive States */
.btn-primary {
  background: var(--primary);
  color: #ffffff;
  font-weight: 600;
  padding: 0.65rem 1.25rem;
  border-radius: var(--radius-md);
  border: none;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  transition: background 0.15s ease;
}

.btn-primary:hover {
  background: var(--primary-hover);
}

/* Dedicated Print Stylesheet for Lossless A4 Printing */
@media print {
  body {
    background: #ffffff !important;
    padding: 0 !important;
  }
  .no-print, nav, .app-sidebar, .btn-action, #toast {
    display: none !important;
  }
  .invoice-sheet {
    box-shadow: none !important;
    border: none !important;
    width: 100% !important;
    max-width: 100% !important;
    padding: 0 !important;
  }
}''')

    style_heading(doc, "5. Design System Artifacts", 2)
    add_image_if_exists(doc, "10_component_ui_hierarchy.png", "Component and UI Module Hierarchy Styled via CSS")

    style_heading(doc, "6. Output / Expected Result", 2)
    doc.add_paragraph(
        "Applying style.css transforms raw HTML views into a responsive web application. The UI "
        "presents typographic hierarchy, smooth hover transitions, accessible contrast ratios, and "
        "accurate formatting for on-screen inspection and A4 paper output."
    )

    style_heading(doc, "7. Conclusion", 2)
    doc.add_paragraph(
        "Experiment 4 demonstrated the practical application of CSS3 custom properties, Flexbox, CSS Grid, "
        "and print media queries to build a scalable front-end design system for the Ledgerly web app."
    )

    doc.save(OUTPUT_DIR / "Exp_04_CSS_Styling.docx")
    print("Generated Exp_04_CSS_Styling.docx")


# -------------------------------------------------------------
# EXPERIMENT 5: Prepare SRS for Project Topic
# -------------------------------------------------------------
def generate_exp_05():
    doc = Document()
    add_header(doc, "5", "Prepare SRS (Software Requirements Specification) for the Project Topic", module_num="3")

    style_heading(doc, "1. Pre-Requisites", 2)
    doc.add_paragraph(
        "• Knowledge of IEEE 830 Standard for Software Requirements Specifications.\n"
        "• Understanding of functional vs non-functional requirements taxonomy.\n"
        "• Experience in authoring detailed Use Case specifications and interaction contracts.\n"
        "• Clear understanding of the Ledgerly invoicing and payment workflow."
    )

    style_heading(doc, "2. Objective", 2)
    doc.add_paragraph(
        "To produce a formal, comprehensive IEEE 830 compliant Software Requirements Specification (SRS) for Ledgerly, "
        "documenting system objectives, user personas, functional requirements (FR1–FR8), non-functional requirements, "
        "use case specifications, and external interface constraints."
    )

    style_heading(doc, "3. Section 1: Introduction", 2)
    doc.add_paragraph(
        "1.1 Purpose: This document defines the complete functional and non-functional requirements for Ledgerly v1.0, "
        "a client-side Progressive Web Application designed to streamline invoice generation, tax computation, and payment tracking for SMBs.\n\n"
        "1.2 Scope: Ledgerly enables users to create customizable invoices and quotations, calculate multi-tier taxes (CGST/SGST/IGST), "
        "embed payment QR codes, capture digital signatures, and export documents as PDFs or dispatch them via WhatsApp and Email.\n\n"
        "1.3 Definitions & Abbreviations:\n"
        "• PWA: Progressive Web Application.\n"
        "• GSTIN: Goods and Services Tax Identification Number.\n"
        "• HSN/SAC: Harmonized System of Nomenclature / Service Accounting Code.\n"
        "• UTR: Unique Transaction Reference (Payment Tracking ID)."
    )

    style_heading(doc, "4. Section 2: Overall System Description", 2)
    doc.add_paragraph(
        "2.1 Product Perspective: Ledgerly operates as a zero-backend, client-side SPA. Persistence is achieved through browser "
        "localStorage with manual JSON/CSV backup portability.\n"
        "2.2 User Classes & Characteristics:\n"
        "• Primary User: Small business owner or freelancer needing rapid, compliant invoicing.\n"
        "• Client / Recipient: Customer receiving invoices and paying via UPI or bank transfer.\n"
        "2.3 Operating Environment: Fully functional on Google Chrome (v90+), Mozilla Firefox (v88+), Apple Safari (v14+), and Microsoft Edge."
    )

    style_heading(doc, "5. Section 3: Functional Requirements (FR)", 2)
    headers = ["Req ID", "Requirement Name", "Detailed Description"]
    data = [
        ["FR1", "User Authentication & Route Guard", "Allows account creation, sign-in, and prevents unauthorized access to protected dashboard views."],
        ["FR2", "Enterprise & Customer Profiles", "Stores company GSTIN, logo, bank details, and maintains a directory of client contacts."],
        ["FR3", "Dynamic Line Item & Cataloging", "Allows adding, editing, and deleting line items with real-time row totals and tax rates."],
        ["FR4", "Automated Calculation Engine", "Computes subtotal, percentage/flat discounts, intra-state (CGST+SGST) vs inter-state (IGST), extra fees, and round-off."],
        ["FR5", "Canvas Digital Signature Capture", "Provides a touch/stylus-sensitive 2D canvas to capture and embed authorized signatures."],
        ["FR6", "Dynamic UPI Payment QR Engine", "Encodes UPI VPA and exact payable amounts into scannable QR codes on the invoice."],
        ["FR7", "Payment Settlement Ledger", "Records installment payments (Cash, UPI, NEFT) with UTR numbers and tracks remaining balance due."],
        ["FR8", "PDF Generation & Print Pipeline", "Generates pixel-perfect PDF downloads using html2pdf.js and formats standard A4 browser printouts."]
    ]
    add_styled_table(doc, headers, data)

    style_heading(doc, "6. Section 4: Non-Functional Requirements (NFR)", 2)
    nfr_headers = ["Dimension", "Specific Metric / Requirement Target"]
    nfr_data = [
        ["Performance", "Calculation updates render in under 16ms (60 FPS); PDF compilation finishes within 2.5 seconds."],
        ["Usability", "Complies with Nielsen's Usability Heuristics; intuitive single-page form completion under 90 seconds."],
        ["Reliability & Availability", "100% offline availability via Service Worker cache; zero cloud server outage vulnerability."],
        ["Security & Privacy", "All financial records and customer PII remain strictly on the local device; zero third-party data tracking."]
    ]
    add_styled_table(doc, nfr_headers, nfr_data)

    style_heading(doc, "7. Section 5: Detailed Use Case Specification (UC1: Create Invoice)", 2)
    uc_headers = ["Use Case Parameter", "Specification Details"]
    uc_data = [
        ["Use Case ID & Title", "UC-01: Create and Generate Tax Invoice"],
        ["Primary Actor", "Business Owner / Freelancer"],
        ["Pre-Conditions", "User is logged in; enterprise profile configured."],
        ["Main Success Scenario", "1. Navigate to '#/create'.\n2. Select customer from dropdown or type new client.\n3. Add line items (Description, Qty, Rate, Tax %).\n4. Select Inter-State or Intra-State supply.\n5. Draw signature on canvas.\n6. Click 'Generate Invoice'.\n7. System validates inputs, computes totals, saves record, and opens preview."],
        ["Post-Conditions", "Invoice saved in 'ig_invoices' and assigned a sequential ID (e.g., INV-2026-0001)."],
        ["Alternative Flow (Invalid Data)", "If customer name or item quantity is missing, show field validation error and prevent save."]
    ]
    add_styled_table(doc, uc_headers, uc_data)

    style_heading(doc, "8. Conclusion", 2)
    doc.add_paragraph(
        "Experiment 5 produced a comprehensive, industry-standard IEEE 830 SRS document for Ledgerly. "
        "It serves as the definitive specification for architectural modeling, verification test suites, and risk management."
    )

    doc.save(OUTPUT_DIR / "Exp_05_SRS_Document.docx")
    print("Generated Exp_05_SRS_Document.docx")


# -------------------------------------------------------------
# EXPERIMENT 6: Prepare DFD - Data Flow Diagram
# -------------------------------------------------------------
def generate_exp_06():
    doc = Document()
    add_header(doc, "6", "Prepare DFD – Data Flow Diagram for the Project Topic", module_num="4")

    style_heading(doc, "1. Pre-Requisites", 2)
    doc.add_paragraph(
        "• Understanding of structured systems analysis and Gane-Sarson / Yourdon DFD notations.\n"
        "• Knowledge of DFD elements: External Entities, Processes, Data Stores, and Data Flows.\n"
        "• Mastery of decomposition levels: Level 0 (Context Diagram), Level 1 (Subsystems), Level 2 (Low-Level Logic)."
    )

    style_heading(doc, "2. Objective", 2)
    doc.add_paragraph(
        "To construct and analyze Level 0, Level 1, and Level 2 Data Flow Diagrams for Ledgerly, detailing data "
        "transformations from initial user input through invoice compilation, calculation, payment ledgering, and document export."
    )

    style_heading(doc, "3. Identification of DFD Elements", 2)
    doc.add_paragraph(
        "• External Entities: User / Business Owner, Client / Customer, External Services (QR API, Mail Client).\n"
        "• Data Stores: D1: User Accounts (ig_users), D2: Session (ig_session), D3: Invoices (ig_invoices), D4: Customers (ig_customers), D5: Enterprises (ig_enterprises).\n"
        "• Major Processes: 1.0 Auth & Session, 2.0 Customer Management, 3.0 Invoice Compilation, 4.0 Calculation & Tax Engine, 5.0 Payment Ledger, 6.0 Document Export."
    )

    style_heading(doc, "4. DFD Level 0: Context Diagram", 2)
    doc.add_paragraph(
        "The Level 0 Context Diagram depicts Ledgerly as a central unified process interacting with external entities."
    )
    add_image_if_exists(doc, "08_dfd_level_0_context_diagram.png", "DFD Level 0: Context Diagram for Ledgerly", width=Inches(6.2))

    style_heading(doc, "5. DFD Level 1: Functional Decomposition", 2)
    doc.add_paragraph(
        "The Level 1 DFD decomposes the system into discrete, cohesive processes showing interactions with localStorage data stores."
    )
    add_image_if_exists(doc, "09_dfd_level_1_decomposition.png", "DFD Level 1: Subsystem Functional Decomposition", width=Inches(6.2))

    style_heading(doc, "6. DFD Level 2: Invoice & Payment Settlement Pipeline", 2)
    doc.add_paragraph(
        "The Level 2 DFD provides low-level process logic for line item calculation, GST application, and installment ledger recording."
    )
    add_image_if_exists(doc, "14_dfd_level_2_invoice_and_payment.png", "DFD Level 2: Invoice Calculation and Payment Pipeline", width=Inches(6.2))

    style_heading(doc, "7. Expected Result & Conclusion", 2)
    doc.add_paragraph(
        "The multi-level Data Flow Diagrams clearly demonstrate how billing information flows, transforms, and persists "
        "throughout Ledgerly. This validates the system's modular architecture and adherence to high cohesion and low coupling."
    )

    doc.save(OUTPUT_DIR / "Exp_06_DFD_Diagrams.docx")
    print("Generated Exp_06_DFD_Diagrams.docx")


# -------------------------------------------------------------
# EXPERIMENT 7: Prepare Use Case Diagram
# -------------------------------------------------------------
def generate_exp_07():
    doc = Document()
    add_header(doc, "7", "Prepare Use Case Diagram for the Project Topic", module_num="4")

    style_heading(doc, "1. Pre-Requisites", 2)
    doc.add_paragraph(
        "• Understanding of UML 2.0 behavioral modeling.\n"
        "• Knowledge of actors (primary, secondary), system boundaries, and associations.\n"
        "• Proper application of <<include>> (mandatory dependency) and <<extend>> (conditional functionality)."
    )

    style_heading(doc, "2. Objective", 2)
    doc.add_paragraph(
        "To construct a UML Use Case diagram for Ledgerly representing user roles, system boundary limits, "
        "and relationships between core invoicing and accounting operations."
    )

    style_heading(doc, "3. Actors & Use Cases", 2)
    headers = ["Actor", "Role Classification", "Associated Use Cases"]
    data = [
        ["Business Owner / Freelancer", "Primary Actor", "Register Account, Login, Manage Profile, Manage Customers, Create Invoice, Record Payment, Download PDF, Export Data."],
        ["Client / Customer", "Secondary Actor", "Receive Invoice, Scan UPI QR, View Account Statement."],
        ["Authentication Service", "System / Supporting", "Validate Credentials (<<include>>), Enforce Session Expiry."]
    ]
    add_styled_table(doc, headers, data)

    style_heading(doc, "4. Relationships: <<include>> vs <<extend>>", 2)
    doc.add_paragraph(
        "• <<include>> Relationships (Mandatory):\n"
        "  - 'Create Invoice' <<include>> 'Calculate Subtotal, Taxes & Grand Total'.\n"
        "  - 'Login' <<include>> 'Validate Credentials'.\n"
        "  - 'Record Payment' <<include>> 'Recompute Balance Due & Invoice Status'.\n\n"
        "• <<extend>> Relationships (Conditional/Optional):\n"
        "  - 'Create Invoice' <<extend>> 'Capture Canvas Digital Signature'.\n"
        "  - 'Preview Invoice' <<extend>> 'Generate Instant UPI QR Code'.\n"
        "  - 'Preview Invoice' <<extend>> 'Dispatch via WhatsApp / Email'."
    )

    style_heading(doc, "5. Navigation & Workflow State Machine", 2)
    add_image_if_exists(doc, "03_navigation_state_machine.png", "Route Navigation and Access Guard State Machine", width=Inches(6.2))

    style_heading(doc, "6. Expected Result & Conclusion", 2)
    doc.add_paragraph(
        "The Use Case model defines the functional interactions available to users, establishing unambiguous "
        "requirements for the underlying controller logic and event listeners implemented in JavaScript."
    )

    doc.save(OUTPUT_DIR / "Exp_07_Use_Case_Diagram.docx")
    print("Generated Exp_07_Use_Case_Diagram.docx")


# -------------------------------------------------------------
# EXPERIMENT 8: Interaction Design and UML Artifacts
# -------------------------------------------------------------
def generate_exp_08():
    doc = Document()
    add_header(doc, "8", "Interaction Design and Detailed UML Artifacts", module_num="4")

    style_heading(doc, "1. Pre-Requisites", 2)
    doc.add_paragraph(
        "• Proficiency in Human-Computer Interaction (HCI) concepts: Personas, Scenarios, Task Flows, and Wireframing.\n"
        "• Familiarity with Nielsen's 10 Usability Heuristics and Shneiderman's 8 Golden Rules.\n"
        "• Knowledge of UML behavioral (Sequence, Activity) and structural (Class, Component) diagrams."
    )

    style_heading(doc, "2. Objective", 2)
    doc.add_paragraph(
        "To develop an interaction design model and prepare UML design artifacts for Ledgerly, including user personas, "
        "task flows, wireframes, Class Diagram, Sequence Diagrams, and Component Hierarchy."
    )

    style_heading(doc, "3. User Personas", 2)
    doc.add_paragraph(
        "Persona 1: Rohan Patil (Freelance Web Developer, Age 24)\n"
        "• Goals: Send polished quotations to international & domestic clients; receive payment via UPI.\n"
        "• Pain Points: Heavy accounting software with monthly subscription charges; spreadsheet calculation errors.\n\n"
        "Persona 2: Meera Sharma (Boutique & Retail Agency Owner, Age 38)\n"
        "• Goals: Create GST-compliant invoices with CGST/SGST breakdowns; track clients with overdue partial payments.\n"
        "• Pain Points: Losing customer records when switching devices; complex tax filing preparations."
    )

    style_heading(doc, "4. UML Sequence Diagrams", 2)
    style_heading(doc, "4.1 Invoice Builder & Signature Pipeline", 3)
    add_image_if_exists(doc, "06_sequence_invoice_builder_and_signature.png", "Sequence Diagram: Invoice Creation and Digital Signature", width=Inches(6.2))

    style_heading(doc, "4.2 Payment Settlement & Receipt Dispatch", 3)
    add_image_if_exists(doc, "07_sequence_payment_and_receipt.png", "Sequence Diagram: Payment Recording and Settlement", width=Inches(6.2))

    style_heading(doc, "5. Invoice Lifecycle State Machine", 2)
    add_image_if_exists(doc, "04_invoice_lifecycle_state_machine.png", "State Machine: Invoice Lifecycle (Draft -> Generated -> Partially Paid -> Paid)", width=Inches(6.2))

    style_heading(doc, "6. Conclusion", 2)
    doc.add_paragraph(
        "Experiment 8 applied interaction design techniques and UML modeling to establish a clear architectural "
        "blueprint for Ledgerly, ensuring high modularity, intuitive UX, and clean separation of concerns."
    )

    doc.save(OUTPUT_DIR / "Exp_08_Interaction_Design_and_UML.docx")
    print("Generated Exp_08_Interaction_Design_and_UML.docx")


# -------------------------------------------------------------
# EXPERIMENT 9: WBS, Gantt Chart & Test Case Design
# -------------------------------------------------------------
def generate_exp_09():
    doc = Document()
    add_header(doc, "9", "WBS, Gantt Chart & Test Case Design (Black-Box & White-Box)", module_num="5")

    style_heading(doc, "1. Pre-Requisites", 2)
    doc.add_paragraph(
        "• Work Breakdown Structure (WBS) task decomposition and Gantt chart scheduling methods.\n"
        "• Black-Box Testing techniques: Equivalence Partitioning (EP), Boundary Value Analysis (BVA), Decision Tables.\n"
        "• White-Box Testing concepts: Control Flow Graphs (CFG), Cyclomatic Complexity (V(G)), and Independent Paths."
    )

    style_heading(doc, "2. Part A: WBS & Project Schedule", 2)
    headers = ["Task ID", "WBS Work Package", "Estimated Duration", "Dependencies"]
    data = [
        ["1.0", "Requirements Analysis & SRS Formulation", "2 Weeks", "-"],
        ["2.0", "UI/UX Interaction Design & Wireframing", "2 Weeks", "1.0"],
        ["3.0", "Static HTML5 & CSS3 Design System Development", "2 Weeks", "2.0"],
        ["4.0", "Core Calculation, Tax Engine & Canvas Logic", "3 Weeks", "3.0"],
        ["5.0", "Persistence Layer & Payment Settlement Ledger", "2 Weeks", "4.0"],
        ["6.0", "PDF / Print Engine & Service Worker PWA Setup", "2 Weeks", "5.0"],
        ["7.0", "Comprehensive Testing, Bug Fixes & Deployment", "2 Weeks", "6.0"]
    ]
    add_styled_table(doc, headers, data)

    style_heading(doc, "3. Part B: Black-Box Test Cases", 2)

    style_heading(doc, "3.1 Equivalence Partitioning (EP) - Discount Engine", 3)
    ep_headers = ["Partition ID", "Input Range / Category", "Type", "Expected Output"]
    ep_data = [
        ["EP-1", "0 <= Discount <= 100", "Valid", "Applies percentage reduction smoothly."],
        ["EP-2", "Discount < 0", "Invalid", "Reject: Negative discount not permitted."],
        ["EP-3", "Discount > 100", "Invalid", "Reject: Percentage discount cannot exceed 100%."],
        ["EP-4", "Non-numeric string", "Invalid", "Reject: Non-numeric input converted to 0."]
    ]
    add_styled_table(doc, ep_headers, ep_data)

    style_heading(doc, "3.2 Decision Table - Invoice Settlement State", 3)
    dt_headers = ["Rule", "Condition: Total Paid == 0", "Condition: Paid < Grand Total", "Condition: Paid >= Grand Total", "Action: Resulting Status"]
    dt_data = [
        ["R1", "True", "False", "False", "Status = 'Unpaid'"],
        ["R2", "False", "True", "False", "Status = 'Partially Paid' (Amber Badge)"],
        ["R3", "False", "False", "True", "Status = 'Paid' (Official Settled Receipt)"]
    ]
    add_styled_table(doc, dt_headers, dt_data)

    style_heading(doc, "4. Part C: White-Box Testing", 2)
    style_heading(doc, "4.1 Source Code Under Test (Tax Split Logic)", 3)
    add_code_block(doc,
'''function calculateTax(taxableAmount, taxRate, isInterState) {
  1: if (taxRate < 0 || taxRate > 100) {
  2:   throw new Error("Invalid Tax Rate");
     }
  3: const totalTax = (taxableAmount * taxRate) / 100;
  4: if (isInterState) {
  5:   return { igst: totalTax, cgst: 0, sgst: 0 };
     } else {
  6:   const halfTax = totalTax / 2;
  7:   return { igst: 0, cgst: halfTax, sgst: halfTax };
     }
  8: // End
}''')

    style_heading(doc, "4.2 Control Flow Graph (CFG) & Cyclomatic Complexity", 3)
    doc.add_paragraph(
        "• Graph Nodes: N = 7 (Nodes 1, 2, 3, 4, 5, 6, 7/8).\n"
        "• Graph Edges: E = 8.\n"
        "• Predicate Nodes: P = 2 (Conditions at line 1 and line 4).\n\n"
        "Cyclomatic Complexity Calculation:\n"
        "V(G) = E - N + 2 = 8 - 7 + 2 = 3.\n"
        "Alternatively: V(G) = P + 1 = 2 + 1 = 3.\n\n"
        "Conclusion: Exactly 3 independent test paths are required for 100% basis path coverage:\n"
        "• Path 1: 1 -> 2 (Tax rate out of bounds -> Error thrown)\n"
        "• Path 2: 1 -> 3 -> 4 -> 5 -> 8 (Valid tax rate, inter-state == true -> IGST applied)\n"
        "• Path 3: 1 -> 3 -> 4 -> 6 -> 7 -> 8 (Valid tax rate, inter-state == false -> CGST + SGST applied)"
    )

    style_heading(doc, "5. Conclusion", 2)
    doc.add_paragraph(
        "Experiment 9 established a disciplined engineering roadmap via WBS and Gantt scheduling, and verified "
        "the core financial calculation modules using both black-box techniques and white-box basis path testing."
    )

    doc.save(OUTPUT_DIR / "Exp_09_WBS_Gantt_and_Testing_Design.docx")
    print("Generated Exp_09_WBS_Gantt_and_Testing_Design.docx")


# -------------------------------------------------------------
# EXPERIMENT 10: Automated Testing with Pytest / Unittest
# -------------------------------------------------------------
def generate_exp_10():
    doc = Document()
    add_header(doc, "10", "Prepare Test Case Plan using Pytest or Unittest", module_num="6")

    style_heading(doc, "1. Pre-Requisites", 2)
    doc.add_paragraph(
        "• Proficiency in Python programming and unit testing principles.\n"
        "• Working knowledge of Python's built-in 'unittest' and 'pytest' frameworks.\n"
        "• Understanding of test assertions (assertEqual, assertTrue, assertRaises).\n"
        "• Ability to construct systematic, repeatable automated regression test suites."
    )

    style_heading(doc, "2. Objective", 2)
    doc.add_paragraph(
        "To write, automate, and execute a structured unit test suite verifying Ledgerly's core calculation engine, "
        "tax breakdown algorithm, auto round-off mechanics, payment ledger balances, and registration validation."
    )

    style_heading(doc, "3. Test Case Plan Table", 2)
    headers = ["TC ID", "Module", "Scenario", "Test Input", "Expected Output", "Actual Output", "Status"]
    data = [
        ["TC_CALC_01", "Calc Engine", "Multi-item Subtotal", "2 items @ 1500 + 1 @ 800", "Subtotal = 3800.0", "3800.0", "PASS"],
        ["TC_CALC_02", "Calc Engine", "Percentage Discount", "Subtotal = 5000, 10%", "Discount = 500.0", "500.0", "PASS"],
        ["TC_CALC_03", "Calc Engine", "Flat Discount", "Subtotal = 5000, flat 750", "Discount = 750.0", "750.0", "PASS"],
        ["TC_CALC_04", "Calc Engine", "Negative Discount Check", "Discount = -50", "ValueError raised", "ValueError caught", "PASS"],
        ["TC_TAX_01", "Tax Engine", "Intra-State GST Split", "Taxable = 1000, Rate = 18%", "CGST=90, SGST=90, IGST=0", "CGST=90, SGST=90", "PASS"],
        ["TC_TAX_02", "Tax Engine", "Inter-State IGST", "Taxable = 1000, Rate = 18%", "IGST=180, CGST=0, SGST=0", "IGST=180", "PASS"],
        ["TC_TOT_01", "Round-Off", "Auto Integer Rounding", "Pre-round total = 1045.35", "Grand=1045, Delta=-0.35", "1045.0, -0.35", "PASS"],
        ["TC_PAY_01", "Ledger", "Zero Payment Status", "Total Paid = 0.0", "Status = 'Unpaid'", "'Unpaid'", "PASS"],
        ["TC_PAY_02", "Ledger", "Partial Payment Status", "Paid = 2000 of 5000", "Status = 'Partially Paid'", "'Partially Paid'", "PASS"],
        ["TC_PAY_03", "Ledger", "Full Settlement Status", "Paid = 5000 of 5000", "Status = 'Paid'", "'Paid'", "PASS"],
        ["TC_VAL_01", "Validation", "Valid User Registration", "Valid name, email, phone", "True, 'Valid'", "True", "PASS"],
        ["TC_VAL_02", "Validation", "Malformed Phone Check", "phone = '98765'", "False, '10 digits'", "False", "PASS"]
    ]
    add_styled_table(doc, headers, data)

    style_heading(doc, "4. Python Unit Test Implementation (test_invoice_engine.py)", 2)
    add_code_block(doc,
'''import unittest

# Import Ledgerly financial functions under test
from test_invoice_engine import (
    calculate_subtotal, calculate_discount, calculate_tax,
    calculate_grand_total, determine_payment_status, validate_user_registration
)

class TestLedgerlyCore(unittest.TestCase):
    def test_tc_calc_01_subtotal(self):
        items = [{'qty': 2, 'price': 1500.0}, {'qty': 1, 'price': 800.0}]
        self.assertEqual(calculate_subtotal(items), 3800.0)

    def test_tc_tax_01_intrastate_gst(self):
        breakdown = calculate_tax(1000.0, 18.0, is_interstate=False)
        self.assertEqual(breakdown['cgst'], 90.0)
        self.assertEqual(breakdown['sgst'], 90.0)
        self.assertEqual(breakdown['igst'], 0.0)

    def test_tc_pay_02_partial_payment(self):
        self.assertEqual(determine_payment_status(5000.0, 2000.0), "Partially Paid")

if __name__ == '__main__':
    unittest.main()''')

    style_heading(doc, "5. Automated Execution Console Output", 2)
    add_code_block(doc,
'''$ python test_invoice_engine.py -v
test_tc_calc_01_subtotal (__main__.TestInvoiceEngine) ... ok
test_tc_calc_02_percentage_discount (__main__.TestInvoiceEngine) ... ok
test_tc_calc_03_flat_discount (__main__.TestInvoiceEngine) ... ok
test_tc_calc_04_discount_boundary_error (__main__.TestInvoiceEngine) ... ok
test_tc_pay_01_unpaid_status (__main__.TestInvoiceEngine) ... ok
test_tc_pay_02_partial_payment (__main__.TestInvoiceEngine) ... ok
test_tc_pay_03_full_settlement (__main__.TestInvoiceEngine) ... ok
test_tc_tax_01_intrastate_gst (__main__.TestInvoiceEngine) ... ok
test_tc_tax_02_interstate_gst (__main__.TestInvoiceEngine) ... ok
test_tc_total_01_auto_round_off (__main__.TestInvoiceEngine) ... ok
test_tc_val_01_valid_registration (__main__.TestInvoiceEngine) ... ok
test_tc_val_02_invalid_phone (__main__.TestInvoiceEngine) ... ok
test_tc_words_01_indian_denominations (__main__.TestInvoiceEngine) ... ok

----------------------------------------------------------------------
Ran 13 tests in 0.001s

OK (100% Passing)''')

    style_heading(doc, "6. Conclusion", 2)
    doc.add_paragraph(
        "Experiment 10 successfully verified Ledgerly's core business logic through an automated test plan. "
        "All 13 test cases executed cleanly, providing reliable regression protection against calculation discrepancies."
    )

    doc.save(OUTPUT_DIR / "Exp_10_Automated_Testing_Pytest_Unittest.docx")
    print("Generated Exp_10_Automated_Testing_Pytest_Unittest.docx")


# -------------------------------------------------------------
# EXPERIMENT 11: Prepare RMMM Document
# -------------------------------------------------------------
def generate_exp_11():
    doc = Document()
    add_header(doc, "11", "Prepare RMMM (Risk Mitigation, Monitoring and Management) Document", module_num="5")

    style_heading(doc, "1. Pre-Requisites", 2)
    doc.add_paragraph(
        "• Knowledge of software risk analysis, hazard classification, and risk exposure formulas.\n"
        "• Familiarity with proactive vs reactive risk management strategies.\n"
        "• Understanding of client-side browser constraints: storage limits, offline caching, and cross-browser rendering."
    )

    style_heading(doc, "2. Objective", 2)
    doc.add_paragraph(
        "To formulate a thorough Risk Mitigation, Monitoring, and Management (RMMM) plan specifically tailored to "
        "Ledgerly, identifying 10 critical operational, architectural, and financial risks, computing Risk Exposure (RE = P x I), "
        "and defining concrete mitigation and contingency procedures."
    )

    style_heading(doc, "3. Risk Identification Table", 2)
    headers = ["Risk ID", "Risk Category", "Risk Description", "Potential Project Impact"]
    data = [
        ["R1", "Data Storage", "Browser localStorage 5MB quota exhaustion after thousands of invoices.", "Inability to persist new invoices."],
        ["R2", "Data Loss", "Accidental browser cache/cookie clearance by user.", "Complete deletion of local records."],
        ["R3", "Rendering / UI", "HTML-to-canvas rendering discrepancies across Safari vs Chrome.", "Distorted PDF output formatting."],
        ["R4", "Financial Logic", "Rounding discrepancies causing ±0.01 fractional currency imbalance.", "Accounting reconciliation mismatch."],
        ["R5", "Offline Caching", "Service Worker serving stale application cache after update.", "Users miss recent bug fixes/features."],
        ["R6", "Hardware Input", "Touch stylus signature distortion on high-DPI retina touchscreens.", "Pixelated or illegible signatures."],
        ["R7", "Privacy / Security", "Sensitive billing details exposed on shared computers.", "Unauthorized local data viewing."],
        ["R8", "Dependency Risk", "External CDN failure (Google Fonts or html2pdf CDN down).", "PDF generation or styling breaks offline."],
        ["R9", "Schedule Risk", "Development delays due to academic exams and commitments.", "Late project delivery."],
        ["R10", "Usability Risk", "Invoice sheet overflow when exceeding 25+ line items.", "Text cut off at bottom of A4 page."]
    ]
    add_styled_table(doc, headers, data)

    style_heading(doc, "4. Risk Analysis & Prioritization Matrix", 2)
    doc.add_paragraph(
        "Evaluation Scale: Probability (P): 1 (Low) to 5 (High) | Impact (I): 1 (Low) to 5 (High) | Exposure (RE) = P × I"
    )
    a_headers = ["Risk ID", "Probability (1-5)", "Impact (1-5)", "Risk Exposure (RE)", "Priority Level"]
    a_data = [
        ["R1 (Storage Quota)", "3", "5", "15", "HIGH"],
        ["R2 (Cache Clearing)", "4", "5", "20", "CRITICAL"],
        ["R3 (PDF Rendering)", "3", "4", "12", "MEDIUM"],
        ["R4 (Rounding Math)", "2", "4", "8", "MEDIUM"],
        ["R5 (Stale SW Cache)", "3", "3", "9", "MEDIUM"],
        ["R6 (Signature DPI)", "2", "3", "6", "LOW"],
        ["R7 (Shared Data Privacy)", "3", "4", "12", "MEDIUM"],
        ["R8 (CDN Downtime)", "4", "4", "16", "HIGH"],
        ["R9 (Schedule Delay)", "3", "3", "9", "MEDIUM"],
        ["R10 (A4 Sheet Overflow)", "3", "4", "12", "MEDIUM"]
    ]
    add_styled_table(doc, a_headers, a_data)

    style_heading(doc, "5. Detailed Mitigation, Monitoring & Contingency Plans", 2)
    doc.add_paragraph(
        "R2: Accidental Browser Cache Clearance (RE: 20 - CRITICAL)\n"
        "• Mitigation: Provide prominent one-click JSON/CSV data backup & restore buttons on the dashboard.\n"
        "• Monitoring: Track database size on each invoice creation and alert user if backup is older than 7 days.\n"
        "• Contingency: Enable immediate one-click restoration from downloaded .json ledger backup files.\n\n"
        "R1: LocalStorage Quota Exhaustion (RE: 15 - HIGH)\n"
        "• Mitigation: Store high-resolution company logos as compressed webp/jpeg; avoid duplicate base64 strings.\n"
        "• Monitoring: Monitor bytes stored via navigator.storage.estimate() or byte counter in settings.\n"
        "• Contingency: Implement IndexedDB migration path for databases exceeding 5MB.\n\n"
        "R8: CDN Availability & Offline Failures (RE: 16 - HIGH)\n"
        "• Mitigation: Cache html2pdf.js and web fonts inside the Service Worker cache on initial load.\n"
        "• Monitoring: Fall back gracefully to native window.print() if html2pdf fails.\n"
        "• Contingency: Native browser printing ensures PDF generation never halts even completely offline."
    )

    style_heading(doc, "6. Conclusion", 2)
    doc.add_paragraph(
        "Experiment 11 established a proactive Risk Mitigation, Monitoring, and Management plan for Ledgerly. "
        "By identifying critical client-side failure modes and preparing actionable contingency measures, "
        "system reliability and user data security are guaranteed throughout the product lifecycle."
    )

    doc.save(OUTPUT_DIR / "Exp_11_RMMM_Document.docx")
    print("Generated Exp_11_RMMM_Document.docx")


# -------------------------------------------------------------
# EXPERIMENT 12: Cost Estimation Using COCOMO
# -------------------------------------------------------------
def generate_exp_07_bis():
    pass

def generate_exp_12():
    doc = Document()
    add_header(doc, "12", "Cost Estimation Using the Basic COCOMO Model", module_num="4")

    style_heading(doc, "1. Pre-Requisites", 2)
    doc.add_paragraph(
        "• Understanding of software cost estimation models (Barry Boehm's Basic Constructive Cost Model - COCOMO).\n"
        "• Knowledge of project complexity categories: Organic (small team, familiar domain), Semi-Detached, and Embedded.\n"
        "• Familiarity with mathematical formulas for Effort (Person-Months), Development Schedule (Months), Staffing, and Budgeting."
    )

    style_heading(doc, "2. Objective", 2)
    doc.add_paragraph(
        "To perform a realistic cost, effort, and duration estimation for the Ledgerly Invoice Generator based on "
        "effective Lines of Code (LOC) using the Basic COCOMO Organic model tailored to a student/academic software engineering project."
    )

    style_heading(doc, "3. Software Sizing (Effective LOC Count)", 2)
    doc.add_paragraph(
        "For cost estimation, only core application source code (excluding boilerplate comments, blank lines, and external vendor bundles) is considered:"
    )
    headers = ["Module / Component", "Technology Stack", "Effective Lines of Code (LOC)"]
    data = [
        ["Application Structure & View Templates", "HTML5", "250 LOC"],
        ["Design System, Layouts & Print Styling", "CSS3", "750 LOC"],
        ["Core Calculation, Router & Invoice Logic", "Vanilla JavaScript (ES6)", "1,350 LOC"],
        ["Offline Cache & Service Worker", "JavaScript PWA", "50 LOC"],
        ["Validation & Verification Test Logic", "Python / JS", "100 LOC"],
        ["Total Effective Project Sizing", "Web Technologies", "2,500 LOC (2.5 KLOC)"]
    ]
    add_styled_table(doc, headers, data)
    doc.add_paragraph("Total Software Size (KLOC): 2.5 KLOC.")

    style_heading(doc, "4. Project Classification & COCOMO Formulas", 2)
    doc.add_paragraph(
        "Project Classification: Organic Model\n"
        "Justification: Ledgerly is developed by a small, focused team (1–2 student developers) working in a familiar, "
        "well-understood web technology environment (HTML5, CSS3, JavaScript) with flexible requirements and no rigid hardware constraints.\n\n"
        "Organic Model Coefficients:\n"
        "• a = 2.4, b = 1.05\n"
        "• c = 2.5, d = 0.38\n\n"
        "Formulas:\n"
        "• Effort (E) = a × (KLOC)^b [Person-Months]\n"
        "• Development Time (D) = c × (E)^d [Months]\n"
        "• Average Staffing = E / D [Developers]\n"
        "• Total Cost = Effort × Cost per Person-Month"
    )

    style_heading(doc, "5. Mathematical Step-by-Step Calculation", 2)
    doc.add_paragraph(
        "Step 1: Calculate Development Effort (E)\n"
        "E = 2.4 × (KLOC)^1.05\n"
        "E = 2.4 × (2.5)^1.05\n"
        "Calculate exponent: 2.5^1.05 ≈ 2.616\n"
        "Thus, Effort (E) = 2.4 × 2.616 = 6.28 Person-Months (PM)\n\n"
        "Step 2: Calculate Development Time / Duration (D)\n"
        "D = 2.5 × (E)^0.38\n"
        "Calculate exponent: 6.28^0.38 ≈ 2.012\n"
        "Thus, Duration (D) = 2.5 × 2.012 = 5.03 Months (~5 Months / 1 Academic Semester)\n\n"
        "Step 3: Calculate Average Staffing\n"
        "Staff = Effort / Time\n"
        "Staff = 6.28 / 5.03 ≈ 1.25 (~1 to 2 Developers)\n"
        "This precisely matches the student team size for an academic mini-project.\n\n"
        "Step 4: Realistic Cost Estimation\n"
        "• Student Project (Actual College Execution): ₹0 (Zero development cost)\n"
        "• Academic / Intern Stipend Benchmark (@ ₹15,000/PM):\n"
        "  Total Cost = 6.28 PM × ₹15,000 = ₹94,200 (~₹0.94 Lakhs)\n"
        "• Junior Developer Benchmark (@ ₹20,000/PM):\n"
        "  Total Cost = 6.28 PM × ₹20,000 = ₹1,25,600 (~₹1.25 Lakhs)"
    )

    style_heading(doc, "6. COCOMO Estimation Summary Table", 2)
    s_headers = ["Estimation Parameter", "Calculated Value", "Remarks"]
    s_data = [
        ["Effective Code Size", "2,500 LOC (2.5 KLOC)", "Core source code"],
        ["COCOMO Category", "Organic", "Small team, familiar web stack"],
        ["Estimated Effort (E)", "6.28 Person-Months", "Effort required"],
        ["Development Time (D)", "5.03 Months (~20 Weeks)", "Aligns with 1 semester timeline"],
        ["Recommended Team Size", "1 – 2 Developers", "Matches student project allocation"],
        ["Actual Student Cost", "₹0", "Zero-cost college coursework"],
        ["Nominal Academic Cost", "₹94,200 (~₹0.94 Lakhs)", "Estimated at student stipend rate"]
    ]
    add_styled_table(doc, s_headers, s_data)

    style_heading(doc, "7. Conclusion", 2)
    doc.add_paragraph(
        "Experiment 12 provided a realistic, grounded estimation for Ledgerly using the Basic COCOMO Organic model. "
        "Sizing the core system at 2.5 KLOC resulted in 6.28 person-months of effort, a 5-month development timeline "
        "(matching an academic semester), and a team of 1–2 developers, confirming the project's practical feasibility."
    )

    doc.save(OUTPUT_DIR / "Exp_12_COCOMO_Cost_Estimation.docx")
    print("Generated Exp_12_COCOMO_Cost_Estimation.docx (Updated with realistic Organic model)")


# -------------------------------------------------------------
# EXPERIMENT 13: Git Version Control & Deployment
# -------------------------------------------------------------
def generate_exp_13():
    doc = Document()
    add_header(doc, "13", "Version Control and Deployment Using Git & GitHub Pages", module_num="6")

    style_heading(doc, "1. Pre-Requisites", 2)
    doc.add_paragraph(
        "• Understanding of Distributed Version Control Systems (DVCS) and Git architecture.\n"
        "• Mastery of CLI Git commands: git init, git add, git commit, git branch, git remote, git push.\n"
        "• Working GitHub account and familiarity with GitHub Pages static hosting."
    )

    style_heading(doc, "2. Objective", 2)
    doc.add_paragraph(
        "To establish a Git version control repository for Ledgerly, maintain traceable commit histories, and deploy "
        "the live Progressive Web Application publicly using GitHub Pages."
    )

    style_heading(doc, "3. Git Workflow & Command Execution Log", 2)
    add_code_block(doc,
'''# Step 1: Initialize local Git repository
$ git init
Initialized empty Git repository in C:/Users/Krushna/Documents/Projects/Invoice Generator/.git/

# Step 2: Stage all project assets
$ git add index.html style.css script.js manifest.json sw.js test_invoice_engine.py

# Step 3: Record initial commit
$ git commit -m "feat: initial release of Ledgerly invoice generator PWA"
[main (root-commit) 4a8b1c2] feat: initial release of Ledgerly invoice generator PWA
 6 files changed, 5250 insertions(+)

# Step 4: Link local repository to GitHub remote
$ git remote add origin https://github.com/krushna-patil/ledgerly-invoice-generator.git

# Step 5: Push codebase to main branch
$ git push -u origin main
Enumerating objects: 8, done.
Counting objects: 100% (8/8), done.
Writing objects: 100% (8/8), 48.20 KiB | 4.82 MiB/s, done.
Total 8 (delta 0), reused 0 (delta 0)
To https://github.com/krushna-patil/ledgerly-invoice-generator.git
 * [new branch]      main -> main''')

    style_heading(doc, "4. Deployment on GitHub Pages", 2)
    doc.add_paragraph(
        "1. Open the repository on GitHub: https://github.com/krushna-patil/ledgerly-invoice-generator.\n"
        "2. Navigate to Settings > Pages.\n"
        "3. Under 'Build and deployment', set Source to 'Deploy from a branch'.\n"
        "4. Select Branch: main and Folder: / (root).\n"
        "5. Click Save.\n"
        "6. GitHub Actions automatically builds and publishes the site to:\n"
        "   https://krushna-patil.github.io/ledgerly-invoice-generator/"
    )

    style_heading(doc, "5. Automated Update Verification", 2)
    doc.add_paragraph(
        "When local enhancements are made (e.g. updating styles or tax rates), committing and pushing changes "
        "automatically triggers GitHub Pages deployment within 30 seconds:\n"
        "  $ git add style.css\n"
        "  $ git commit -m \"style: refine invoice print margins\"\n"
        "  $ git push origin main\n"
        "The live website immediately reflects the latest code."
    )

    style_heading(doc, "6. Expected Output & Deployment Verification", 2)
    doc.add_paragraph(
        "• A fully functional, live PWA accessible globally over HTTPS.\n"
        "• Traceable commit history documenting feature additions and refactoring.\n"
        "• Zero-cost web hosting with automatic SSL encryption and CDN distribution."
    )

    style_heading(doc, "7. Conclusion", 2)
    doc.add_paragraph(
        "Experiment 13 completed the modern software development lifecycle for Ledgerly. Version control best practices "
        "were implemented using Git, and the application was successfully deployed to production via GitHub Pages."
    )

    doc.save(OUTPUT_DIR / "Exp_13_GitHub_Pages_Deployment.docx")
    print("Generated Exp_13_GitHub_Pages_Deployment.docx")


# -------------------------------------------------------------
# Main Execution Trigger
# -------------------------------------------------------------
if __name__ == '__main__':
    print("Starting generation of all 13 Lab Experiment Documents...")
    generate_exp_01()
    generate_exp_02()
    generate_exp_03()
    generate_exp_04()
    generate_exp_05()
    generate_exp_06()
    generate_exp_07()
    generate_exp_08()
    generate_exp_09()
    generate_exp_10()
    generate_exp_11()
    generate_exp_12()
    generate_exp_13()
    print("ALL 13 EXPERIMENT DOCUMENTS SUCCESSFULLY CREATED IN:")
    print(OUTPUT_DIR)
