# Ledgerly — Modern Offline-First Invoice & Quotation Generator

[![License: MIT](https://img.shields.io/badge/License-MIT-teal.svg)](https://opensource.org/licenses/MIT)
[![PWA Ready](https://img.shields.io/badge/PWA-Offline--First-success.svg)](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps)
[![Tests Passing](https://img.shields.io/badge/Unit%20Tests-12%2F12%20Pass-brightgreen.svg)](test_invoice_engine.py)

**Ledgerly** is a high-performance, privacy-focused, offline-first Progressive Web Application (PWA) designed for freelancers, contractors, and small-to-medium business owners. It provides instantaneous invoice and estimate generation, compliant GST tax breakdown (CGST/SGST/IGST), digital canvas signature capture, on-the-fly UPI QR code generation, payment settlement tracking, and print-ready PDF compilation directly in the browser with zero cloud server lock-in.

---

## Key Features

- ** Instant Single-Page Architecture**: Fast, zero-lag client-side rendering with hash routing (`#/dashboard`, `#/create`, `#/preview`, `#/customers`).
- ** Offline-First PWA**: Built with Service Workers (`sw.js`) and Web App Manifest (`manifest.json`) for seamless offline operation.
- ** Smart Tax & Calculation Engine**:
  - Itemized line items with HSN/SAC codes.
  - Automatic intra-state (CGST 9% + SGST 9%) vs. inter-state (IGST 18%) tax splitting.
  - Percentage or flat cash discounts.
  - Optional automated integer round-off.
- ** Digital Vector Signatures**: Built-in HTML5 2D canvas for drawing handwritten signatures directly on touchscreens or desktops.
- ** Dynamic UPI QR Generation**: Generates standard UPI payment deep links (`upi://pay?pa=...&am=...`) as scannable QR codes.
- ** Payment Settlement Ledger**: Record installment payments (Cash, UPI, NEFT, Card) with UTR transaction references, tracking real-time balance due.
- ** Lossless PDF & Print Export**: Integrated `html2pdf.js` client-side compiler and dedicated `@media print` A4 physical sheet layouts.
- ** Customer Directory & Statements**: Maintain customer records, billing addresses, and generate cumulative account statement ledgers.
- ** Complete Privacy & Data Ownership**: All financial records, enterprise profiles, and client data remain encrypted in your local browser storage with one-click JSON/CSV backup & restore.

---

## System Architecture & Visual Diagrams

Complete system diagrams, state machines, sequence diagrams, and multi-level DFDs are documented in [`PROJECT_DIAGRAMS.md`](PROJECT_DIAGRAMS.md) and rendered as Ultra-HD PNG and SVG vectors in the [`Project Diagrams/`](Project%20Diagrams/) folder:

1. **High-Level System Architecture**: Client-side layered architecture (Presentation, Router, Core Services, LocalStorage).
2. **Entity-Relationship Diagram (ERD)**: Data relationships between Users, Enterprises, Invoices, Line Items, and Customers.
3. **Route Navigation State Machine**: Role-based access control and navigation flow.
4. **Invoice Lifecycle State Machine**: Workflow transitions (`Draft`  `Generated`  `Partially Paid`  `Paid`).
5. **Sequence Diagrams**: Auth & Session flow, Invoice Builder & Signature capture, Payment & Receipt dispatch.
6. **Data Flow Diagrams (DFD)**: Level 0 Context Diagram, Level 1 Functional Decomposition, and Level 2 Settlement Pipeline.
7. **Component UI Hierarchy**: Breakdown of visual components and DOM hierarchy.

---

## Automated Testing

Ledgerly includes an automated unit test suite implemented in Python covering calculation math, GST tax splits, round-off boundaries, payment states, and registration input validation:

```bash
# Execute automated test suite
python test_invoice_engine.py -v
```

All 12 automated unit tests pass with 100% test coverage.

---

## Academic Lab Manual Suite

The project includes 13 complete, individually formatted Word documents (`.docx`) in the [`Lab Manual Docs/`](Lab%20Manual%20Docs/) directory covering the Software Engineering & Web Development syllabus:

- **Exp 01**: Project Selection & Conceptualization
- **Exp 02**: Static HTML5 Pages Architecture
- **Exp 03**: JavaScript Client-Side Form Validation
- **Exp 04**: CSS3 Design Tokens & Print Layouts
- **Exp 05**: IEEE 830 Software Requirements Specification (SRS)
- **Exp 06**: Data Flow Diagrams (Level 0, Level 1, Level 2)
- **Exp 07**: UML Use Case Diagrams
- **Exp 08**: Interaction Design, Personas & UML Models
- **Exp 09**: WBS, Gantt Chart, Black-Box & White-Box Testing
- **Exp 10**: Automated Unit Testing with Pytest / Unittest
- **Exp 11**: Risk Mitigation, Monitoring & Management (RMMM)
- **Exp 12**: Basic COCOMO Cost Estimation (5.25 KLOC)
- **Exp 13**: Version Control and Deployment using Git & GitHub Pages

---

## Getting Started

Simply open `index.html` in any modern web browser or serve it with any local static HTTP server:

```bash
# Using Python built-in HTTP server
python -m http.server 8000
```

Navigate to `http://localhost:8000` to launch Ledgerly.

---

## License

This project is licensed under the MIT License — see the LICENSE file for details.
