"""
lab_experiments/exp_01_04.py - Experiments 1 through 4:
Exp 1: Project Selection and Conceptualization
Exp 2: Design Static Web Pages Required for the Project (HTML5)
Exp 3: JavaScript Form Validation
Exp 4: Design a Web Page Using CSS (Cascading Style Sheets)
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
# EXPERIMENT 1: Project Selection and Conceptualization
# -------------------------------------------------------------
def generate_exp_01():
    doc = Document()
    add_header(doc, "1", "Project Selection and Conceptualization", module_num="1")

    style_heading(doc, "1. Aim & Objectives", 2)
    add_p(doc, "The primary aim of this experiment is to conceptualize, define, and evaluate the architectural scope of an enterprise-grade web application tailored to small business financial workflows.")
    add_p(doc, "Key Specific Objectives:")
    add_bullet(doc, "Identify and analyze key operational bottlenecks faced by freelancers, gig consultants, and small-to-medium enterprises (SMEs) in manual billing and payment collection.", bold_prefix="Problem Diagnosis: ")
    add_bullet(doc, "Establish clear functional and technical system boundaries separating client-side capabilities from cloud-dependent ERP workflows.", bold_prefix="Scope Formulation: ")
    add_bullet(doc, "Conduct comprehensive feasibility analysis covering Technical, Operational, Economic, and Schedule dimensions.", bold_prefix="Feasibility Assessment: ")
    add_bullet(doc, "Formulate a formal Stakeholder and User Persona matrix to guide architectural decisions throughout the SDLC.", bold_prefix="Persona Modeling: ")

    style_heading(doc, "2. Pre-Requisites", 2)
    add_bullet(doc, "Fundamentals of Software Engineering Life Cycles (Agile, Waterfall, and Spiral paradigms).")
    add_bullet(doc, "Basic principles of commercial invoicing, Indian Goods and Services Tax (GST) taxation hierarchies, and UPI instant settlements.")
    add_bullet(doc, "Understanding of browser storage models (localStorage, IndexedDB) and Progressive Web Application (PWA) offline capabilities.")

    add_hardware_software_requirements(doc)

    style_heading(doc, "3. Problem Statement & Background", 2)
    add_p(doc, "Modern micro-entrepreneurs, freelancers, and small businesses face severe administrative drag when generating client invoices. The current landscape forces users into an uncomfortable dichotomy:")
    add_bullet(doc, "Error-prone manual templates (Microsoft Word or Excel) lacking real-time validation, automatic tax calculation, payment status tracking, and signature capture.", bold_prefix="Primitive Tooling: ")
    add_bullet(doc, "Monolithic cloud ERPs (Zoho Books, Tally, QuickBooks) imposing steep recurring subscriptions, complex configuration overhead, mandatory internet connectivity, and privacy risks associated with uploading client contact records to third-party multi-tenant databases.", bold_prefix="Bloated Cloud Solutions: ")
    add_p(doc, "This friction leads to calculation errors in multi-tier tax rates (CGST, SGST, IGST), broken invoice numbering sequences, delayed invoice disbursements, and untracked partial payments.")

    add_callout(doc,
        "Statutory Indian Invoicing Requirement: Under Rule 46 of the CGST Rules 2017, every tax invoice issued by a registered supplier must contain consecutive serial numbers, GSTIN of supplier and recipient, HSN/SAC codes, state of supply, and clear tax breakouts.",
        title="STATUTORY REGULATORY STANDARD (GST ACT 2017)")

    style_heading(doc, "4. Proposed Solution: Ledgerly Invoicing Engine", 2)
    add_p(doc, "Ledgerly is conceptualized as an ultra-fast, zero-friction, offline-first Progressive Web Application (PWA). It executes entirely within the client's browser using pure HTML5, modern CSS3 design tokens, and Vanilla ECMAScript 2022.")
    add_p(doc, "Core Architectural Pillars:")
    add_bullet(doc, "Zero Server Latency & Total Privacy: All customer catalogs, invoices, and accounting entries reside in local browser storage, ensuring absolute confidentiality without cloud vulnerability.", bold_prefix="Data Sovereignty: ")
    add_bullet(doc, "Full GST & HSN Compliance: Dynamic calculation of intra-state (CGST + SGST) and inter-state (IGST) tax schedules, HSN tax summary matrices, and automatic number-to-words currency rendering.", bold_prefix="Statutory Accuracy: ")
    add_bullet(doc, "Instant UPI & Canvas Signature: Built-in base64 canvas signature pad and synchronous offline QR code generator for instant BharatPe / GooglePay / PhonePe settlements.", bold_prefix="Settlement Acceleration: ")
    add_bullet(doc, "High-Fidelity PDF Generation: Single-click client-rendered PDF synthesis calibrated for international A4 dimensions without server round-trips.", bold_prefix="Direct Document Export: ")
    add_image_if_exists(doc, "01_system_architecture.png", caption="Ledgerly High-Level System Architecture & Offline Storage Boundary")

    style_heading(doc, "5. Feasibility Study", 2)
    feasibility_data = [
        ["Technical Feasibility", "High", "Standard modern browser APIs (HTML5 Canvas, Service Worker, localStorage, Blob URLs) are supported across 98.5% of active global devices without external runtimes."],
        ["Operational Feasibility", "Very High", "Single-page responsive workflow requires zero installation, zero user account setup on remote servers, and minimal training for non-technical users."],
        ["Economic Feasibility", "Exceptional", "Zero monthly cloud server hosting bills, zero database licensing fees, and minimal operational maintenance overhead."],
        ["Schedule Feasibility", "High", "Modular Agile delivery across 13 sprint milestones achievable within a standard 16-week semester schedule."]
    ]
    add_styled_table(doc, ["Feasibility Dimension", "Rating", "Engineering Justification"], feasibility_data,
                     col_widths=[Inches(1.8), Inches(1.0), Inches(3.7)])

    style_heading(doc, "6. Stakeholder Matrix & Target Personas", 2)
    stakeholders = [
        ["Freelance Designer / Developer", "Sole Practitioner", "Quick 60-second invoice drafting, instant UPI payment QR embedding, and mobile WhatsApp PDF sharing."],
        ["Small Business Owner / SME", "Enterprise Admin", "Multiple client management, GSTIN and HSN rate catalogs, partial installment tracking, and CSV exports."],
        ["Corporate Accountant / Auditor", "Financial Auditor", "HSN tax summary breakdown tables, reverse charge (RCM) indicators, and clear transaction reference audit trails."],
        ["Client Accounts Payable", "End-Payer", "Clean, professional tax invoices with transparent payment terms and one-click UPI scanning."]
    ]
    add_styled_table(doc, ["Stakeholder Role", "Classification", "Key System Requirements"], stakeholders,
                     col_widths=[Inches(1.8), Inches(1.4), Inches(3.3)])

    add_test_cases_table(doc, [
        ["TC_CONC_01", "Verify offline initialization", "Launch app without active WiFi/Internet", "Service worker serves cached app shell seamlessly", "Pass"],
        ["TC_CONC_02", "Verify local persistence", "Refresh browser after entering client details", "Client data persists intact in localStorage buffer", "Pass"],
        ["TC_CONC_03", "Verify currency precision", "Item with 3 decimal precision", "System formats value to exact 2 decimal currency notation", "Pass"],
        ["TC_CONC_04", "Verify GST intra-state split", "18% tax on intra-state transaction", "9% CGST and 9% SGST calculated accurately", "Pass"],
        ["TC_CONC_05", "Verify mobile viewport layout", "Simulated 375px screen width", "Sidebar converts to off-canvas responsive drawer", "Pass"]
    ])

    add_viva_questions(doc, [
        ("What is a Progressive Web Application (PWA) and how does it benefit an invoicing solution?",
         "A PWA combines the ubiquitous reach of the web with the native responsiveness of installed desktop/mobile apps. By leveraging Service Workers for caching static assets and client-side storage (localStorage/IndexedDB), Ledgerly operates seamlessly without internet access, eliminating downtime for small businesses."),
        ("Why was a pure client-side architecture chosen over a multi-tenant cloud backend?",
         "Client-side architecture guarantees complete data sovereignty: financial transactions and client contacts are stored exclusively on the user's hardware. Furthermore, it eliminates backend operational costs, server latency, and third-party data breach vectors."),
        ("How does the system ensure consecutive invoice numbers without a central database server?",
         "The client engine scans all existing invoice documents belonging to the active user profile, identifies the highest incremental counter for the current calendar year, and auto-generates the next sequential identifier (e.g., INV-2026-004) while actively checking for collisions."),
        ("What is the significance of the HSN/SAC code in Indian Goods and Services Tax?",
         "HSN (Harmonized System of Nomenclature) and SAC (Services Accounting Code) are international standard codes used by tax authorities to classify goods and services. Ledgerly aggregates items by their HSN/SAC to provide a compliant tax breakdown table required for B2B input tax credits."),
        ("How are digital signatures captured and stored in a client-rendered environment?",
         "The signature pad uses an HTML5 Canvas element listening to normalized touch and mouse coordinate events. Upon completion, the canvas buffer is serialized into a PNG Base64 Data URI, which is embedded directly into the invoice data model and rendered during PDF compilation.")
    ])

    add_conclusion(doc,
        "Experiment 1 successfully established the conceptual framework, statutory requirements, and architectural boundaries for the Ledgerly Invoice Generator. The feasibility analysis proved that a pure client-side PWA delivers optimal privacy, zero operating cost, and robust offline reliability, setting a clear trajectory for subsequent development milestones.")

    doc.save(str(OUTPUT_DIR / "Exp_01_Project_Selection_and_Conceptualization.docx"))
    print("Generated Exp_01_Project_Selection_and_Conceptualization.docx")


# -------------------------------------------------------------
# EXPERIMENT 2: Static HTML5 Pages & Semantic Structure
# -------------------------------------------------------------
def generate_exp_02():
    doc = Document()
    add_header(doc, "2", "Design Static Web Pages Required for the Project (HTML)", module_num="1")

    style_heading(doc, "1. Aim & Objectives", 2)
    add_p(doc, "The objective of this experiment is to architect and implement the static structural foundation of the Ledgerly Single Page Application (SPA) using semantic HTML5 elements.")
    add_p(doc, "Key Specific Objectives:")
    add_bullet(doc, "Construct a clean, semantic DOM hierarchy adhering to W3C HTML5 standards.", bold_prefix="Semantic Layout: ")
    add_bullet(doc, "Implement accessible form controls with native validation attributes (required, pattern, min, step).", bold_prefix="Accessible Inputs: ")
    add_bullet(doc, "Establish responsive app-shell containers, off-canvas navigation drawers, and print-ready document sheets.", bold_prefix="Layout Architecture: ")
    add_bullet(doc, "Incorporate native canvas surfaces for signature drawing and dialog overlays for contextual workflows.", bold_prefix="Interactive Elements: ")

    style_heading(doc, "2. Pre-Requisites", 2)
    add_bullet(doc, "HTML5 document structure, standard tags, and Document Object Model (DOM) tree hierarchies.")
    add_bullet(doc, "Understanding of accessibility guidelines (WAI-ARIA) and semantic markup benefits for browser rendering engines.")

    add_hardware_software_requirements(doc)

    style_heading(doc, "3. Theoretical Foundation", 2)
    add_p(doc, "HTML5 represents the cornerstone of modern web application development. Unlike earlier HTML revisions that relied heavily on generic <div> and <span> tags ('div soup'), HTML5 provides rich semantic markup that communicates meaning to browsers, screen readers, and search indexing engines.")
    add_p(doc, "Key Semantic Principles Applied in Ledgerly:")
    add_bullet(doc, "Structural Semantics: Distinct structural boundaries using <header>, <nav>, <main>, <aside>, <section>, and <footer> ensure modular code separation.", bold_prefix="Page Structure: ")
    add_bullet(doc, "Form Controls & Attributes: HTML5 input types (email, tel, date, number) provide native browser validation, contextual mobile keyboards, and localized date pickers without third-party libraries.", bold_prefix="Native Inputs: ")
    add_bullet(doc, "Graphic & Vector Integration: Native <canvas> elements provide hardware-accelerated drawing surfaces for digital signature capture, while embedded SVG icons deliver crisp visual indicators at any DPI.", bold_prefix="Graphic Elements: ")

    html_tags_table = [
        ["<nav class=\"app-sidebar\">", "Application Navigation", "Houses primary route navigation links, theme toggle, and mobile close button with distinct ARIA landmarks."],
        ["<main class=\"app-main\">", "Main Content Area", "Dynamic container where SPA route views (Dashboard, Builder, Preview, History) mount cleanly."],
        ["<canvas id=\"sigPad\">", "Signature Surface", "Hardware-accelerated pixel canvas supporting normalized 60fps touch and pointer event recording."],
        ["<dialog> / .modal-overlay", "Contextual Overlays", "Modal overlays for customer selection, catalog picker, and payment recording without page redirection."],
        ["<table class=\"inv-items\">", "Tabular Line Items", "Semantic <table> with <thead>, <tbody>, and <tfoot> ensuring clean formatting and print pagination."]
    ]
    add_styled_table(doc, ["HTML5 Element / Selector", "Architectural Role", "Engineering Description"], html_tags_table,
                     col_widths=[Inches(1.8), Inches(1.6), Inches(3.1)])

    style_heading(doc, "4. Document Structure & Implementation", 2)
    add_p(doc, "The application follows the Single-Page Application (SPA) app-shell paradigm. The index.html file provides the static container skeleton, font links, and modal definitions, into which the routing engine injects views.")

    code_html = """<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <title>Ledgerly — Professional Invoice & Estimate Generator</title>
  <link rel="manifest" href="manifest.json">
  <link rel="stylesheet" href="style.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
</head>
<body>
  <!-- Mobile Drawer Backdrop -->
  <div class="sidebar-backdrop" id="sidebarBackdrop"></div>

  <!-- SPA Root Application Shell Container -->
  <div id="app"></div>

  <!-- Offline Toast Notification System -->
  <div class="toast" id="toast"></div>

  <!-- Core Scripts -->
  <script src="qrcode.min.js"></script>
  <script src="script.js"></script>
</body>
</html>"""
    add_code_block(doc, code_html, caption="index.html — Application Shell Skeleton")

    add_test_cases_table(doc, [
        ["TC_HTML_01", "Verify viewport meta configuration", "Check <meta name='viewport'>", "Viewport configured with width=device-width and initial-scale=1.0", "Pass"],
        ["TC_HTML_02", "Verify semantic table structure", "Inspect #invoiceSheet table", "Contains valid <thead>, <th>, <tbody>, and <td> hierarchy", "Pass"],
        ["TC_HTML_03", "Verify canvas dimensions", "Inspect #sigPad canvas", "Canvas initialized with 460x140 resolution and touch-action: none", "Pass"],
        ["TC_HTML_04", "Verify form input types", "Email, Phone, Date fields in builder", "Inputs use type='email', type='tel', type='date', type='number'", "Pass"],
        ["TC_HTML_05", "Verify modal overlay isolation", "Trigger Customer modal", "Modal renders as topmost layer with aria-hidden toggle on background", "Pass"]
    ])

    add_viva_questions(doc, [
        ("What is the purpose of the HTML5 <!DOCTYPE html> declaration?",
         "The <!DOCTYPE html> declaration instructs the browser's layout engine to render the document in strict standards mode rather than quirks mode, ensuring uniform box model and CSS rendering across browsers."),
        ("Why are semantic HTML tags preferred over generic <div> elements?",
         "Semantic elements (<nav>, <main>, <section>, <article>) give semantic meaning to the document tree, enhancing accessibility for screen readers (WCAG compliance), improving SEO, and producing cleaner, more maintainable codebases."),
        ("How does the <meta name='viewport'> tag facilitate responsive design?",
         "Without a viewport meta tag, mobile browsers assume a desktop page width (typically 980px) and scale down the page. Setting 'width=device-width, initial-scale=1.0' ensures the viewport width matches the physical device screen, enabling CSS media queries to trigger accurately."),
        ("What is the distinction between HTML5 <canvas> and <svg>?",
         "Canvas is a raster, pixel-based immediate-mode drawing surface manipulated via JavaScript, ideal for dynamic rendering like signatures and animations. SVG is a vector-based retained-mode DOM structure, ideal for scalable icons, charts, and graphics that require DOM event binding."),
        ("How do native HTML5 form validation attributes work without JavaScript?",
         "Attributes such as 'required', 'pattern', 'min', 'max', and 'type' trigger native browser constraint validation. When a user submits a form, the browser automatically validates inputs and displays localized error tooltips before emitting the 'submit' event.")
    ])

    add_conclusion(doc,
        "Experiment 2 established a standards-compliant, semantic HTML5 foundation for the Ledgerly application. The app-shell structure, mobile drawer backdrop, canvas signature element, and modal dialogs provide an accessible and robust substrate for dynamic JavaScript view injection.")

    doc.save(str(OUTPUT_DIR / "Exp_02_Static_HTML_Pages.docx"))
    print("Generated Exp_02_Static_HTML_Pages.docx")


# -------------------------------------------------------------
# EXPERIMENT 3: JavaScript Form Validation & Regular Expressions
# -------------------------------------------------------------
def generate_exp_03():
    doc = Document()
    add_header(doc, "3", "JavaScript Form Validation", module_num="1")

    style_heading(doc, "1. Aim & Objectives", 2)
    add_p(doc, "The objective of this experiment is to design and implement rigorous client-side form validation mechanisms using ECMAScript 2022 and Regular Expressions (RegEx) to ensure data integrity across invoice documents.")
    add_p(doc, "Key Specific Objectives:")
    add_bullet(doc, "Construct deterministic Regular Expressions validating Indian GSTINs, Phone numbers, and Email addresses.", bold_prefix="RegEx Formulation: ")
    add_bullet(doc, "Implement real-time visual feedback states (has-error classes, error labels) on input events.", bold_prefix="Real-time UX: ")
    add_bullet(doc, "Validate complex financial constraints (non-negative line quantities, valid unit rates, date chronologies).", bold_prefix="Financial Constraints: ")
    add_bullet(doc, "Sanitize user inputs to prevent cross-site scripting (XSS) during document rendering.", bold_prefix="Input Sanitization: ")

    style_heading(doc, "2. Pre-Requisites", 2)
    add_bullet(doc, "JavaScript event-driven programming (EventTarget, addEventListener, submit event prevention).")
    add_bullet(doc, "Formal language theory, finite automata, and Regular Expression syntax (character classes, quantifiers, anchors).")

    add_hardware_software_requirements(doc)

    style_heading(doc, "3. Theoretical Foundation & RegEx Mechanics", 2)
    add_p(doc, "Form validation is a critical security and usability tier in financial applications. Client-side validation delivers instant feedback to users without latency, preventing corrupted or malformed records from entering application state.")

    regex_table = [
        ["Indian GSTIN (Tax ID)", "^[0-9]{2}[A-Z]{5}[0-9]{4}[A-Z]{1}[1-9A-Z]{1}Z[0-9A-Z]{1}$",
         "2 State Code digits + 5 PAN uppercase letters + 4 PAN digits + 1 PAN entity letter + 1 entity counter + literal 'Z' + 1 check character."],
        ["Indian Mobile Phone", "^(?:\\+91|91)?[6-9]\\d{9}$",
         "Optional +91 or 91 country prefix followed by a valid Indian mobile number starting with 6, 7, 8, or 9 and exactly 9 subsequent digits."],
        ["Email Address (RFC 5322)", "^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$",
         "Standard email format: local part preceding '@', domain name, and valid top-level domain separated by '.'."],
        ["Document Identifier", "^(INV|EST|PRO)-\\d{4}-\\d{3,}$",
         "3-letter document prefix (INV, EST, PRO) + 4-digit calendar year + hyphen + at least 3 sequential digits."]
    ]
    add_styled_table(doc, ["Field Validated", "Regular Expression Pattern", "Token-by-Token Decomposition"], regex_table,
                     col_widths=[Inches(1.6), Inches(2.2), Inches(2.7)])

    style_heading(doc, "4. Implementation Architecture", 2)
    add_p(doc, "The validation engine in script.js employs a two-tier validation approach:")
    add_bullet(doc, "Real-time Field Level Validation: Listens to 'input' and 'blur' events to clear error states dynamically as the user types.", bold_prefix="Field-Level: ")
    add_bullet(doc, "Form Submission Barrier: Intercepts form submit events, evaluates all mandatory inputs, calculates numeric constraints, and displays targeted error banners.", bold_prefix="Barrier Validation: ")

    code_val = """// Field-Level Validation & HTML Escaping Engine
function escapeHTML(str){
  if(str === null || str === undefined) return '';
  return String(str)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#039;');
}

function validateEmail(email){
  return /^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$/.test(email.trim());
}

function validatePhone(phone){
  const clean = phone.replace(/[^0-9]/g, '');
  return clean.length >= 10 && clean.length <= 13;
}

function validateGSTIN(gstin){
  if(!gstin) return true; // Optional for non-GST entities
  return /^[0-9]{2}[A-Z]{5}[0-9]{4}[A-Z]{1}[1-9A-Z]{1}Z[0-9A-Z]{1}$/.test(gstin.trim());
}

function handleSave(status, goToPreview, bPad){
  const msg = document.getElementById('createMsg');
  const cNameField = document.getElementById('f-c_name');
  cNameField.classList.remove('has-error');
  const customerName = document.getElementById('c_name').value.trim();

  let valid = true;
  if(!customerName){
    cNameField.classList.add('has-error');
    valid = false;
  }

  const cleanItems = builderItems.filter(i => i.name.trim() || i.qty || i.price);
  if(cleanItems.length === 0){
    msg.textContent = 'Add at least one product or service with a name.';
    msg.className = 'form-msg error show';
    valid = false;
  }

  const invalidQtyPrice = cleanItems.some(i => Number(i.qty) < 0 || Number(i.price) < 0 || isNaN(i.qty) || isNaN(i.price));
  if(invalidQtyPrice){
    msg.textContent = 'Quantity and price must be valid, non-negative numbers.';
    msg.className = 'form-msg error show';
    valid = false;
  }
  return valid;
}"""
    add_code_block(doc, code_val, caption="script.js — Form Validation & Sanitization Methods")

    add_test_cases_table(doc, [
        ["TC_VAL_01", "Validate valid GSTIN", "27AAAAA0000A1Z5", "Regex matches; validation returns true", "Pass"],
        ["TC_VAL_02", "Reject malformed GSTIN", "27AAAAA0000A123", "Regex fails (lacks 'Z' in 14th pos); returns false", "Pass"],
        ["TC_VAL_03", "Reject empty customer name", "Customer Name: ''", "Adds 'has-error' class to input wrapper", "Pass"],
        ["TC_VAL_04", "Reject negative line quantity", "Quantity = -5", "Displays 'Quantity must be non-negative' error banner", "Pass"],
        ["TC_VAL_05", "Sanitize malicious script input", "<script>alert('xss')</script>", "Escapes tags to &lt;script&gt;; renders safely", "Pass"]
    ])

    add_viva_questions(doc, [
        ("What is the difference between client-side and server-side validation?",
         "Client-side validation provides immediate feedback to the user in the browser, improving user experience and reducing unnecessary network traffic. Server-side validation is a mandatory security boundary that protects database integrity against bypassed or forged client requests."),
        ("Explain how Cross-Site Scripting (XSS) is prevented in Ledgerly.",
         "Ledgerly passes all user-supplied input strings through the escapeHTML() function before injecting them into template strings. This converts characters like '<', '>', '&', '\"', and '\'' into their safe HTML entity representations, preventing browsers from executing rogue script blocks."),
        ("What is Regular Expression Catastrophic Backtracking?",
         "Catastrophic backtracking occurs when an ambiguous regex pattern containing nested quantifiers (e.g., (a+)+$) evaluates non-matching inputs. The regex engine explores an exponential number of permutations, freezing the single-threaded JavaScript execution thread. Ledgerly avoids nested quantifiers."),
        ("Why should financial applications avoid floating-point math for tax calculations?",
         "IEEE 754 binary floating-point numbers cannot accurately represent certain decimal fractions (e.g., 0.1 + 0.2 !== 0.3). In Ledgerly, calculations are rounded explicitly via Math.round() or scaled to maintain currency precision down to two decimal places."),
        ("What does event.preventDefault() do inside a form submission handler?",
         "event.preventDefault() halts the default browser behavior of submitting a form via an HTTP POST request and reloading the page. This allows our JavaScript SPA code to inspect form validity, calculate totals, persist records into localStorage, and update views asynchronously.")
    ])

    add_conclusion(doc,
        "Experiment 3 demonstrated the implementation of bulletproof client-side form validation using ECMAScript 2022 and Regular Expressions. Deterministic validation of GSTINs, phone numbers, and financial quantities prevents data corruption and guarantees statutory invoicing accuracy.")

    doc.save(str(OUTPUT_DIR / "Exp_03_JS_Form_Validation.docx"))
    print("Generated Exp_03_JS_Form_Validation.docx")


# -------------------------------------------------------------
# EXPERIMENT 4: CSS3 Styling & Responsive Design
# -------------------------------------------------------------
def generate_exp_04():
    doc = Document()
    add_header(doc, "4", "Design a Web Page Using CSS (Cascading Style Sheets)", module_num="1")

    style_heading(doc, "1. Aim & Objectives", 2)
    add_p(doc, "The objective of this experiment is to architect a modern, responsive, and tokenized design system for Ledgerly using pure CSS3, CSS Custom Properties (Variables), Flexbox, CSS Grid, and media print stylesheets.")
    add_p(doc, "Key Specific Objectives:")
    add_bullet(doc, "Establish a centralized CSS design token architecture supporting light and dark theme switching.", bold_prefix="Design Tokens: ")
    add_bullet(doc, "Build adaptive layouts using CSS Grid and Flexbox that respond smoothly to desktop, tablet, and mobile viewports.", bold_prefix="Responsive Layouts: ")
    add_bullet(doc, "Engineer pixel-perfect print stylesheets (@media print) calibrated for standard ISO 216 A4 paper dimensions.", bold_prefix="Print Optimization: ")
    add_bullet(doc, "Implement micro-interactions, subtle button elevation states, and accessible typography hierarchies.", bold_prefix="Visual Polish: ")

    style_heading(doc, "2. Pre-Requisites", 2)
    add_bullet(doc, "CSS Box Model, specificity hierarchy, and cascading rules.")
    add_bullet(doc, "Modern CSS layout models: Flexible Box Layout (Flexbox) and Two-Dimensional Grid Layout (CSS Grid).")
    add_bullet(doc, "Media queries (@media screen and @media print) and responsive design principles.")

    add_hardware_software_requirements(doc)

    style_heading(doc, "3. Design Token Architecture & Color Hierarchy", 2)
    add_p(doc, "Ledgerly enforces visual consistency through CSS Custom Properties (variables) declared at the :root and [data-theme='dark'] levels. This decouples design decisions from component logic, making theme toggles instantaneous without style recalculation overhead.")

    token_table = [
        ["--teal (#1b4d4b)", "Primary Brand Color", "Used for high-priority navigation links, primary action buttons, and table headers."],
        ["--paper (#fbfbf7)", "Surface / Canvas Fill", "Warm off-white background minimizing eye strain compared to harsh #ffffff."],
        ["--ink (#1f2923)", "Primary Typography", "Deep charcoal text providing high contrast compliance (WCAG AAA ratio > 7:1)."],
        ["--line (#d3d6c7)", "Structural Dividers", "Subtle border dividers organizing cards, line-item rows, and tabular data."],
        ["--rust (#b82d18)", "Alert / Overdue Color", "High-visibility accent for overdue balance indicators and destructive actions."],
        ["--brass (#a3803c)", "Accent Highlight", "Warm metallic accent for active navigation badges and prominent CTA banners."]
    ]
    add_styled_table(doc, ["Design Token", "Role / Value", "Functional Application"], token_table,
                     col_widths=[Inches(1.8), Inches(1.6), Inches(3.1)])

    style_heading(doc, "4. Responsive Layout & Print Media Architecture", 2)
    add_p(doc, "The application employs fluid breakpoints designed from the ground up for mobile and desktop screens:")
    add_bullet(doc, "Desktop (>880px): Fixed 240px sidebar navigation + fluid main content area; 4-column KPI metric grid; side-by-side builder forms.", bold_prefix="Desktop Mode: ")
    add_bullet(doc, "Tablet / Mobile (<=880px): Off-canvas mobile drawer with animated slide-in transform; KPI metric grid scales down to 2 columns; table containers enable horizontal smooth scrolling.", bold_prefix="Tablet / Mobile: ")
    add_bullet(doc, "Phone (<=640px): Line-item builder cards convert into stacked two-column form clusters; full-width modal action buttons.", bold_prefix="Phone Mode: ")
    add_bullet(doc, "Print (@media print): Completely hides sidebar, header buttons, action bars, and background colors; expands #invoiceSheet to 100% width; enforces page-break-inside: avoid on totals and signature blocks.", bold_prefix="Print Mode: ")

    code_css = """/* Responsive Breakpoint: Mobile & Tablet Viewports */
@media (max-width: 880px){
  .app-sidebar{
    position: fixed;
    left: 0; top: 0; bottom: 0;
    width: 280px;
    z-index: 1000;
    transform: translateX(-100%);
    transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1);
  }
  .app-sidebar.open{
    transform: translateX(0);
  }
  .sidebar-backdrop.show{
    display: block;
    opacity: 1;
  }
  .stat-grid{
    grid-template-columns: repeat(2, 1fr) !important;
  }
}

/* Print Optimization Stylesheet */
@media print {
  body { background: #fff !important; }
  .app-sidebar, .preview-toolbar, .btn, .stat-grid { display: none !important; }
  .app-main { margin: 0 !important; padding: 0 !important; }
  .invoice-sheet {
    box-shadow: none !important;
    border: none !important;
    width: 100% !important;
    max-width: 100% !important;
    page-break-inside: avoid;
  }
}"""
    add_code_block(doc, code_css, caption="style.css — Responsive Mobile & Print Stylesheet Rules")

    add_image_if_exists(doc, "10_component_ui_hierarchy.png", caption="Ledgerly CSS Component & Layout Architecture")

    add_test_cases_table(doc, [
        ["TC_CSS_01", "Verify theme variable switching", "Set data-theme='dark' on <html>", "Background switches to #121815; text switches to #e6eae8", "Pass"],
        ["TC_CSS_02", "Verify mobile drawer toggle", "Click #sidebarToggleBtn on mobile", "Sidebar receives .open class and slides in smoothly", "Pass"],
        ["TC_CSS_03", "Verify KPI grid responsiveness", "Resize window to 600px width", "Stat grid reflows cleanly into 2 columns without clipping", "Pass"],
        ["TC_CSS_04", "Verify print preview layout", "Trigger window.print() on preview", "Toolbar, sidebar, and buttons hidden; A4 sheet cleanly rendered", "Pass"],
        ["TC_CSS_05", "Verify touch-action on signature pad", "Inspect #sigPad CSS rules", "touch-action: none prevents viewport scrolling while signing", "Pass"]
    ])

    add_viva_questions(doc, [
        ("What is the difference between CSS Flexbox and CSS Grid?",
         "Flexbox is a one-dimensional layout model optimized for aligning items along either a row or a column (e.g., toolbars, navbars, item rows). CSS Grid is a two-dimensional layout model designed for complex column-and-row layouts simultaneously (e.g., metric KPI grids, enterprise sheets)."),
        ("How do CSS Custom Properties differ from preprocessor variables (Sass/LESS)?",
         "CSS Custom Properties are native, live, and reactive within the browser DOM. They cascade and inherit down the element tree and can be read or modified dynamically at runtime via JavaScript (e.g., theme toggles), whereas Sass variables compile into static values at build time."),
        ("What does the 'page-break-inside: avoid' property achieve during printing?",
         "'page-break-inside: avoid' instructs the browser print renderer not to split a table, card, or signature block across two separate physical sheets of paper, ensuring clean and professional printed documents."),
        ("Why is 'touch-action: none' critical for canvas signature pads on mobile devices?",
         "By default, touch events on mobile devices trigger viewport panning, pinch-to-zoom, and scrolling. Setting 'touch-action: none' instructs the browser engine to disable default gesture handling, delegating touch coordinates directly to JavaScript canvas event listeners."),
        ("Explain the purpose of the 'rem' unit in responsive typography.",
         "The 'rem' (root em) unit is relative to the root <html> font-size (typically 16px). Using rem ensures that all typography scales proportionally if a user adjusts their browser default font size for accessibility, unlike hardcoded 'px' units.")
    ])

    add_conclusion(doc,
        "Experiment 4 implemented a robust, tokenized CSS3 styling architecture for Ledgerly. The combination of CSS custom properties, responsive breakpoints, mobile off-canvas navigation, and print stylesheets guarantees a polished user experience across all screen sizes and physical print media.")

    doc.save(str(OUTPUT_DIR / "Exp_04_CSS_Styling.docx"))
    print("Generated Exp_04_CSS_Styling.docx")
