# Ledgerly — Comprehensive Test Case Suite

This document contains structured, tabular test cases for **Ledgerly (Invoice & Estimate Generator)**, covering all authentication flows, calculations, tax engines, templates, payment ledgers, communications, data portability, and offline capabilities.

---

## 1. Authentication & Session Management

| Test ID | Module | Scenario / Description | Preconditions & Test Data | Test Steps | Expected Result | Priority |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **TC-AUTH-01** | Login | Valid user authentication | User registered with `admin@admin.com` / `admin123` | 1. Navigate to `#/login`<br>2. Enter email and password<br>3. Click "Sign in" | Session created in `ig_session`, redirected to `#/dashboard` with welcome banner. | **P1** |
| **TC-AUTH-02** | Login | Invalid credentials rejection | Existing user account | 1. Enter valid email and incorrect password<br>2. Click "Sign in" | Error banner displayed: "Invalid email or password". Session not created. | **P1** |
| **TC-AUTH-03** | Login | Empty field validation | User on `#/login` | 1. Leave fields blank<br>2. Submit form | Validation error indicators shown under email and password inputs. | **P2** |
| **TC-AUTH-04** | Register | New account creation | No existing user with `test@user.com` | 1. Navigate to `#/register`<br>2. Fill Name, Email, Business Name, Password (>=6 chars)<br>3. Submit form | New user record added to `ig_users`, default enterprise created in `ig_enterprises`, auto-logged in to `#/dashboard`. | **P1** |
| **TC-AUTH-05** | Guard | Protected route unauthorized access | No active session in `localStorage` | 1. Directly open browser URL to `#/dashboard` or `#/create` | Route guard intercepts navigation and redirects user to `#/login`. | **P1** |
| **TC-AUTH-06** | Session | Logout and session clearance | User is logged in | 1. Click "Log out" button in the sidebar | Active session removed from `ig_session`, redirected immediately to `#/login`. | **P2** |

---

## 2. Dashboard & Analytics Engine

| Test ID | Module | Scenario / Description | Preconditions & Test Data | Test Steps | Expected Result | Priority |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **TC-DASH-01** | Dashboard | KPI accuracy validation | User has multiple invoices (Paid, Partial, Pending) | 1. Open `#/dashboard`<br>2. Compare KPI cards with database totals | Total Billed equals sum of `grandTotal`. Collected equals sum of payments. Balance equals sum of remaining dues. | **P1** |
| **TC-DASH-02** | Dashboard | Overdue bills count and value | At least 1 invoice past `dueDate` with balance > 0 | 1. View "Overdue Bills" card on dashboard | Count matches total overdue invoices; overdue past-due currency total matches accurately. | **P1** |
| **TC-DASH-03** | Dashboard | Monthly revenue SVG trend chart | Invoices spread across last 6 months | 1. Inspect "Monthly Revenue Trend" chart on dashboard | SVG displays two colored bars per month: Billed (Teal) and Collected (Green) proportional to invoice data. | **P2** |
| **TC-DASH-04** | Dashboard | Receivables aging breakdown | Invoices with various overdue ages (current, 15d, 45d, 70d) | 1. Inspect "Receivables Aging" card | Invoices accurately bucketed into Current, 1-30d, 31-60d, and 60+ days overdue. | **P2** |
| **TC-DASH-05** | Dashboard | Top clients leaderboard | Invoices created for distinct customer names | 1. Inspect "Top Clients by Revenue" widget | Customers ranked descending by total lifetime billed volume with invoice counts. | **P2** |

---

## 3. Invoice & Estimate Builder

| Test ID | Module | Scenario / Description | Preconditions & Test Data | Test Steps | Expected Result | Priority |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **TC-BLD-01** | Builder | Document type switcher | Navigated to `#/create` | 1. Change document type dropdown from "Tax Invoice" to "Quotation / Estimate" | Title updates to "New Quotation", document number updates to `EST-YYYY-XXX`, action button says "Generate Quotation". | **P1** |
| **TC-BLD-02** | Builder | Enterprise profile autofill | At least 1 enterprise profile saved | 1. Select enterprise profile from dropdown | Seller Name, Address, Email, Phone, GSTIN, UPI ID, Bank details, Currency, and Logo autofill into builder inputs. | **P1** |
| **TC-BLD-03** | Builder | Customer profile autofill | At least 1 customer profile saved | 1. Select customer from dropdown | Customer Name, Address, Email, Phone, GSTIN, and default Terms autofill. | **P1** |
| **TC-BLD-04** | Builder | Dynamic line-item CRUD | On `#/create` with 1 default item | 1. Click "+ Add Line Item"<br>2. Fill HSN, Qty, Unit, Price, Tax %<br>3. Click remove (`&times;`) on a row | Row is added with responsive inputs; line totals update dynamically; removing line recalculates totals; prevents removing last item. | **P1** |
| **TC-BLD-05** | Builder | Form validation before saving | Customer name or line item empty | 1. Clear customer name or item name<br>2. Click "Generate Invoice" | Form highlights missing fields with red error messages and blocks submission. | **P1** |
| **TC-BLD-06** | Builder | Company logo upload & preview | Image file (PNG/JPG) | 1. Upload an image under "Company Logo"<br>2. Check preview thumbnail | File is converted to Base64 data URL, thumbnail renders preview, and data persists into invoice seller snapshot. | **P2** |
| **TC-BLD-07** | Builder | Canvas digital signature capture | Signature pad rendered | 1. Draw signature on builder canvas<br>2. Click "Save Draft & Preview" | Canvas captures vector stroke and saves Base64 image in invoice record. | **P2** |

---

## 4. Financial Calculations, Taxes & Round-Off

| Test ID | Module | Scenario / Description | Preconditions & Test Data | Test Steps | Expected Result | Priority |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **TC-CALC-01** | Engine | Subtotal math verification | Item 1: 3 pcs @ \$100; Item 2: 2 hrs @ \$50 | 1. Enter items in builder | Subtotal calculates exactly to \$400.00 (`3*100 + 2*50`). | **P1** |
| **TC-CALC-02** | Engine | Percentage discount vs Flat discount | Subtotal = ₹1000 | 1. Set discount to 10% (toggle `%`)<br>2. Verify discount = ₹100<br>3. Toggle to "Flat" and enter 150 | In `%` mode, discount = ₹100.00. In `Flat` mode, discount = ₹150.00. | **P1** |
| **TC-CALC-03** | Engine | Per-item tax rate computation | Item 1: ₹1000 (18% tax); Item 2: ₹500 (5% tax) | 1. Enter line items with individual tax rates | Tax calculates dynamically: `₹180 + ₹25 = ₹205.00`. | **P1** |
| **TC-CALC-04** | Engine | Intra-state (CGST+SGST) vs Inter-state (IGST) | Taxable = ₹1000, Tax Rate = 18% | 1. Uncheck Inter-state supply<br>2. Check Inter-state supply | Unchecked: CGST = 9% (₹90), SGST = 9% (₹90). Checked: IGST = 18% (₹180). | **P1** |
| **TC-CALC-05** | Engine | Additional charges addition | Subtotal = ₹500, Shipping = ₹50 | 1. Enter ₹50 in extra charges input with label "Express Shipping" | Grand total increases by ₹50.00 and label displays on summary. | **P2** |
| **TC-CALC-06** | Engine | Auto Round-Off calculation | Pre-round total = ₹1045.35 | 1. Enable "Auto Round Off" checkbox<br>2. Disable checkbox | Enabled: Grand Total = ₹1045.00, Round Off = -₹0.35. Disabled: Grand Total = ₹1045.35. | **P2** |

---

## 5. Preview, Templates & Document Rendering

| Test ID | Module | Scenario / Description | Preconditions & Test Data | Test Steps | Expected Result | Priority |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **TC-PRV-01** | Preview | Template switching & styling | Saved invoice | 1. Inspect template dropdown / classes on `#invoiceSheet` | Applies matching class (`theme-classic`, `theme-navy`, `theme-minimal`, `theme-compact`) with appropriate layout, typography, and borders. | **P2** |
| **TC-PRV-02** | Preview | Logo rendering in invoice header | Invoice seller has logo data URL | 1. Open invoice preview | Logo renders inside `.sheet-logo-container` at proper proportions without distortion. | **P2** |
| **TC-PRV-03** | Preview | Dynamic QR code generation | Invoice with UPI ID and grand total | 1. Open preview of unpaid invoice | QR code image loads from `api.qrserver.com` with encoded UPI string (`upi://pay?pa=...&am=...`). | **P1** |
| **TC-PRV-04** | Preview | Direct PDF download (`html2pdf.js`) | User on `#/preview?id=...` | 1. Click "📄 Download PDF" button | `html2pdf.js` compiles `#invoiceSheet` into a downloaded PDF file (`INV-YYYY-XXX.pdf`) with proper margins. | **P1** |
| **TC-PRV-05** | Preview | Browser print layout | User on `#/preview?id=...` | 1. Click "Print" button / press `Ctrl+P` | Opens print dialog; toolbar and app shell hidden (`no-print`), clean invoice sheet on white paper. | **P1** |

---

## 6. Payment Recording & Settlement Tracking

| Test ID | Module | Scenario / Description | Preconditions & Test Data | Test Steps | Expected Result | Priority |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **TC-PAY-01** | Payments | Record milestone / partial payment | Unpaid invoice with Grand Total = ₹10,000 | 1. Open Payment Modal<br>2. Record ₹4,000 via UPI with UTR ref<br>3. Submit form | Status updates to `Partially Paid`. Amber banner renders with Total Settled = ₹4,000 and Balance Due = ₹6,000. | **P1** |
| **TC-PAY-02** | Payments | Settlement ledger display on preview | Invoice has 2 recorded installment payments | 1. Open invoice preview | Payment Settlement Ledger table displays both installments with dates, methods, UTR refs, and amounts. | **P1** |
| **TC-PAY-03** | Payments | Full settlement completion | Invoice with remaining balance = ₹6,000 | 1. Open Payment Modal<br>2. Record remaining ₹6,000 | Balance Due reaches ₹0.00; status changes to `Paid`; green "Official Settled Receipt" banner and "PAID" watermark appear. | **P1** |
| **TC-PAY-04** | Payments | Delete / reverse payment record | Invoice has recorded payment | 1. Open Payment Modal<br>2. Click "&times; Remove" on an installment | Payment is removed from ledger; Balance Due and invoice status recalculate immediately. | **P2** |

---

## 7. Estimate Workflow & Overdue Tracking

| Test ID | Module | Scenario / Description | Preconditions & Test Data | Test Steps | Expected Result | Priority |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **TC-FLOW-01** | Workflow | 1-Click Quotation to Invoice conversion | Document is an Estimate (`EST-...`) | 1. Open Estimate preview<br>2. Click "🔄 Convert to Invoice"<br>3. Confirm prompt | Document type changes to `invoice`, receives fresh invoice number (`INV-...`), status changes to `Generated`. | **P1** |
| **TC-FLOW-02** | Workflow | Overdue detection and badge display | Invoice with `dueDate` in the past and balance > 0 | 1. View invoice in Dashboard, Preview, or History | Red overdue badge displayed indicating elapsed overdue days (e.g. `+12d Overdue`). | **P1** |
| **TC-FLOW-03** | Sharing | 1-Click WhatsApp Share link | Invoice with customer phone number | 1. Click "💬 WhatsApp Share" on preview | Generates formatted `https://wa.me/{phone}?text=...` URL with invoice number, amount, balance, due date, and UPI ID. | **P1** |
| **TC-FLOW-04** | Sharing | Precomposed Email dispatch | Invoice preview | 1. Click "✉ Email" button | Opens modal with prefilled recipient, subject, and professional message body, with `mailto:` link. | **P2** |

---

## 8. Customer Accounts & Ledger Statements

| Test ID | Module | Scenario / Description | Preconditions & Test Data | Test Steps | Expected Result | Priority |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **TC-CUST-01** | Customers | Customer profile CRUD | On `#/customers` | 1. Click "+ Add Customer"<br>2. Fill details and save<br>3. Edit details<br>4. Delete profile | Customer creates, appears in directory grid with contact details, updates correctly, and deletes with confirmation. | **P1** |
| **TC-CUST-02** | Customers | Account Statement modal opening | Customer with multiple past invoices | 1. Click "📜 Statement" button on customer card | Modal opens showing Lifetime Billed, Total Payments Received, Current Balance Due, and transaction list. | **P1** |
| **TC-CUST-03** | Customers | Statement printing | Customer statement modal opened | 1. Click "Print Statement" | Triggers clean browser print dialog with full customer transaction ledger. | **P2** |

---

## 9. Data Portability, Backup & PWA Offline

| Test ID | Module | Scenario / Description | Preconditions & Test Data | Test Steps | Expected Result | Priority |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **TC-DATA-01** | Export | Export Invoices to CSV | Invoices exist in database | 1. Click "📊 Export CSV" from Dashboard or History | Browser downloads `.csv` file containing all invoice columns, amounts, balances, and customer details. | **P1** |
| **TC-DATA-02** | Backup | Full JSON system backup download | Database populated with users, enterprises, customers, invoices | 1. Go to `#/profile`<br>2. Click "📥 Export Full Backup (JSON)" | Browser downloads `ledgerly-backup-YYYY-MM-DD.json` containing entire state. | **P1** |
| **TC-DATA-03** | Restore | JSON database restore | Valid backup JSON file | 1. Go to `#/profile`<br>2. Select backup file via "📂 Restore Backup (JSON)" | Database in `localStorage` is restored, validation succeeds, and app reloads with restored state. | **P1** |
| **TC-DATA-04** | PWA | Service worker and offline capability | Browser with service worker support | 1. Disconnect network / toggle Offline in DevTools<br>2. Reload page | Service worker serves cached assets; app functions completely offline without connection errors. | **P2** |
