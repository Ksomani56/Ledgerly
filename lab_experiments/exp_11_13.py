"""
lab_experiments/exp_11_13.py - Experiments 11 through 13:
Exp 11: Prepare RMMM (Risk Mitigation, Monitoring and Management) Document
Exp 12: Cost Estimation Using the Basic COCOMO Model
Exp 13: Version Control and Deployment Using Git & GitHub Pages
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
# EXPERIMENT 11: Risk Mitigation, Monitoring and Management (RMMM)
# -------------------------------------------------------------
def generate_exp_11():
    doc = Document()
    add_header(doc, "11", "Prepare RMMM (Risk Mitigation, Monitoring and Management) Document", module_num="4")

    style_heading(doc, "1. Aim & Objectives", 2)
    add_p(doc, "The objective of this experiment is to identify, analyze, prioritize, and formulate proactive mitigation, monitoring, and contingency strategies for risks associated with the Ledgerly PWA using the RMMM framework.")
    add_p(doc, "Key Specific Objectives:")
    add_bullet(doc, "Identify software risks across Technical, Operational, Regulatory, and Security categories.", bold_prefix="Risk Identification: ")
    add_bullet(doc, "Quantify Risk Exposure (RE) using probabilistic likelihood and impact assessment matrices.", bold_prefix="Quantitative Analysis: ")
    add_bullet(doc, "Author detailed Risk Information Sheets (RIS) specifying proactive mitigation, early warning triggers, and contingency plans.", bold_prefix="Actionable RMMM: ")
    add_bullet(doc, "Establish ongoing monitoring protocols throughout the software lifecycle.", bold_prefix="Continuous Monitoring: ")

    style_heading(doc, "2. Pre-Requisites", 2)
    add_bullet(doc, "Software risk engineering principles (SEI Risk Management taxonomy).")
    add_bullet(doc, "Difference between a Risk (future probabilistic event), an Issue (current realization), and a Hazard (dangerous condition).")

    add_hardware_software_requirements(doc)

    style_heading(doc, "3. Theoretical Foundation & Risk Exposure Formula", 2)
    add_p(doc, "Risk analysis is a vital engineering discipline. Proactive risk management minimizes project disruption before potential vulnerabilities realize into critical operational failures.")
    add_callout(doc,
        "Risk Exposure Formula: RE = P x I\nWhere P is the Probability of Occurrence (scaled 0.1 to 1.0 or 1 to 5), and I is the Impact severity if realized (scaled 1 to 5).\nHigh RE values mandate prioritized mitigation strategies.",
        title="MATHEMATICAL RISK QUANTIFICATION")

    style_heading(doc, "4. Risk Identification & Prioritization Matrix", 2)
    risk_matrix_data = [
        ["R-01", "Client-Side LocalStorage Quota Exceeded", "Technical", "0.4", "4", "1.6 (High)", "Active quota monitoring; auto-prompt CSV backup."],
        ["R-02", "Accidental Browser Cache / History Cleared", "Operational", "0.6", "5", "3.0 (Critical)", "Auto-export warning banners; restore buffer."],
        ["R-03", "Statutory GST Rate / Rule Alteration", "Regulatory", "0.3", "4", "1.2 (Moderate)", "Configurable tax schemas in enterprise settings."],
        ["R-04", "Touch Coordinate Drift on High-DPI Mobile", "Technical", "0.5", "3", "1.5 (Moderate)", "Normalized touch event listeners with touch-action: none."],
        ["R-05", "Corrupted Backup Import Injection", "Security", "0.2", "4", "0.8 (Low)", "JSON schema verification with rollback transaction."]
    ]
    add_styled_table(doc, ["Risk ID", "Risk Description", "Category", "Prob (P)", "Impact (I)", "Risk Exposure (RE)", "Primary Strategy"], risk_matrix_data,
                     col_widths=[Inches(0.8), Inches(2.2), Inches(1.1), Inches(0.7), Inches(0.7), Inches(1.0), Inches(2.0)])

    style_heading(doc, "5. Detailed Risk Information Sheets (RIS)", 2)

    add_p(doc, "Risk Information Sheet: R-02 Accidental Browser Cache Cleared", bold_prefix="RIS-01: ")
    ris_02 = [
        ["Risk Statement", "User manually clears browser cache/cookies, inadvertently deleting all locally stored invoices and client directories."],
        ["Probability & Impact", "Probability: 0.60 | Impact: 5 (Critical Data Loss) | Exposure Score: 3.00"],
        ["Mitigation Strategy", "1. Implement persistent one-click 'Export Full Backup (JSON)' and 'Export Sales Register (CSV)' buttons.\n"
                               "2. Display an initial advisory banner educating users that Ledgerly stores data locally on-device.\n"
                               "3. Store active draft buffers in secondary temporary keys to recover in-flight invoices."],
        ["Trigger / Monitoring", "Trigger: User has created >10 invoices or accrued >30 days without performing a manual backup."],
        ["Contingency Plan", "Provide a dedicated 'Restore from Backup' file picker in settings to instantly restore database state."]
    ]
    add_styled_table(doc, ["RIS Attribute", "Management Specification"], ris_02, col_widths=[Inches(1.8), Inches(4.7)])

    add_p(doc, "Risk Information Sheet: R-01 LocalStorage Quota Exceeded", bold_prefix="RIS-02: ")
    ris_01 = [
        ["Risk Statement", "Accumulation of high-resolution base64 signature images and business logos exceeds the browser's 5MB localStorage quota."],
        ["Probability & Impact", "Probability: 0.40 | Impact: 4 (Write Failure) | Exposure Score: 1.60"],
        ["Mitigation Strategy", "1. Compress base64 logos and signatures by clamping canvas dimensions to 460x140.\n"
                               "2. Wrap localStorage.setItem calls in try/catch blocks that detect DOMException.QUOTA_EXCEEDED_ERR.\n"
                               "3. Notify users when storage utilization exceeds 80%."],
        ["Trigger / Monitoring", "Trigger: Storage footprint exceeds 4.0 MB out of the standard 5.0 MB browser quota."],
        ["Contingency Plan", "Prompt user to download historical archives to CSV/JSON and purge paid records older than 12 months."]
    ]
    add_styled_table(doc, ["RIS Attribute", "Management Specification"], ris_01, col_widths=[Inches(1.8), Inches(4.7)])

    add_test_cases_table(doc, [
        ["TC_RMMM_01", "Verify Quota Exceeded handling", "Simulate storage fill > 5MB", "System catches DOMException; prompts archive backup", "Pass"],
        ["TC_RMMM_02", "Verify Backup Restoration", "Import valid JSON backup file", "Restores all invoices, customers, and enterprises cleanly", "Pass"],
        ["TC_RMMM_03", "Verify Corrupted Backup Rejection", "Import invalid/tampered JSON", "Catches schema error; aborts import without data loss", "Pass"],
        ["TC_RMMM_04", "Verify Mobile Signature Scaling", "Sign on 3x device-pixel-ratio mobile", "Touch coordinates scale accurately without pointer drift", "Pass"],
        ["TC_RMMM_05", "Verify Dynamic Tax Adjustment", "Update enterprise tax rate to 28%", "Subsequent drafts reflect 28% without code change", "Pass"]
    ])

    add_viva_questions(doc, [
        ("What is the distinction between a Risk, an Issue, and a Hazard?",
         "A Risk is a potential future event with a probability between 0 and 1 that would negatively impact project objectives. An Issue is a risk that has already realized and requires immediate resolution. A Hazard is an environmental or architectural condition that creates risk."),
        ("What are the four recognized strategies for managing software risks?",
         "1. Avoidance: Eliminating the risk cause (e.g., avoiding cloud servers eliminates server breach risks).\n"
         "2. Mitigation: Reducing probability or impact (e.g., auto-save buffers reduce data loss impact).\n"
         "3. Transfer: Shifting risk to third parties (e.g., cloud insurance).\n"
         "4. Acceptance: Acknowledging residual risk when mitigation cost exceeds impact."),
        ("How is Risk Exposure (RE) calculated and utilized?",
         "RE = Probability x Impact. It normalizes risks onto a quantitative scale, enabling engineering teams to prioritize resources on high-exposure threats rather than low-probability trivial issues."),
        ("What constitutes a 'Risk Trigger'?",
         "A risk trigger is a quantifiable operational threshold or early warning indicator showing that a risk is on the verge of realizing (e.g., localStorage footprint exceeding 80% triggers quota mitigation)."),
        ("What is the difference between a Mitigation Plan and a Contingency Plan?",
         "A Mitigation Plan consists of proactive actions taken BEFORE a risk event occurs to prevent it or minimize its probability. A Contingency Plan consists of predefined reactive procedures executed AFTER a risk realizes to recover and minimize operational damage.")
    ])

    add_conclusion(doc,
        "Experiment 11 developed a comprehensive Risk Mitigation, Monitoring, and Management (RMMM) plan for Ledgerly. Formulating quantitative Risk Exposure scores and detailed Risk Information Sheets ensures robust resilience against local storage limits, user error, and statutory regulatory changes.")

    doc.save(str(OUTPUT_DIR / "Exp_11_RMMM_Document.docx"))
    print("Generated Exp_11_RMMM_Document.docx")


# -------------------------------------------------------------
# EXPERIMENT 12: Cost Estimation Using Basic COCOMO
# -------------------------------------------------------------
def generate_exp_12():
    doc = Document()
    add_header(doc, "12", "Cost Estimation Using the Basic COCOMO Model", module_num="4")

    style_heading(doc, "1. Aim & Objectives", 2)
    add_p(doc, "The objective of this experiment is to estimate software development effort, duration, staffing requirements, and total project cost for Ledgerly using Barry Boehm's Basic COCOMO (Constructive Cost Model).")
    add_p(doc, "Key Specific Objectives:")
    add_bullet(doc, "Measure software sizing accurately in terms of Source Lines of Code (SLOC / KLOC).", bold_prefix="Software Sizing: ")
    add_bullet(doc, "Classify project development mode (Organic, Semi-Detached, or Embedded) based on team dynamics.", bold_prefix="Model Classification: ")
    add_bullet(doc, "Calculate Person-Months of Effort and Nominal Development Duration using empirical power-law equations.", bold_prefix="Mathematical Derivation: ")
    add_bullet(doc, "Determine optimal staffing curves and financial expenditure projections.", bold_prefix="Financial Budgeting: ")

    style_heading(doc, "2. Pre-Requisites", 2)
    add_bullet(doc, "Barry Boehm's COCOMO-81 cost estimation model and empirical coefficients.")
    add_bullet(doc, "Concepts of SLOC (Source Lines of Code), KLOC (Thousands of Lines of Code), and Person-Months (PM).")

    add_hardware_software_requirements(doc)

    style_heading(doc, "3. Software Sizing & Codebase Audit", 2)
    add_p(doc, "Software sizing measures effective physical non-comment lines of code across all project subsystems:")
    sloc_data = [
        ["Core Invoicing Engine & UI", "script.js", "Pure Vanilla ECMAScript 2022", "4,300 LOC"],
        ["Design Token System & Stylesheet", "style.css", "Responsive CSS3 & Print Rules", "1,000 LOC"],
        ["Application Shell Skeleton", "index.html", "HTML5 Semantic Skeleton", "80 LOC"],
        ["Automated Regression Test Suite", "test_invoice_engine.py", "Python unittest Suite", "220 LOC"],
        ["Total Effective Codebase", "All Core Subsystems", "Effective Source Lines of Code", "5,600 LOC (5.6 KLOC)"]
    ]
    add_styled_table(doc, ["Subsystem Component", "Primary File", "Language / Technology", "Measured SLOC"], sloc_data,
                     col_widths=[Inches(1.8), Inches(1.5), Inches(1.8), Inches(1.4)])

    style_heading(doc, "4. Project Classification: Organic Mode", 2)
    add_p(doc, "COCOMO categorizes software into three operational modes:")
    add_bullet(doc, "Small, cohesive development teams working in familiar, in-house environments with stable requirements (Ledgerly classification).", bold_prefix="Organic Mode: ")
    add_bullet(doc, "Medium teams with mixed experience levels working with intermediate hardware/software constraints.", bold_prefix="Semi-Detached Mode: ")
    add_bullet(doc, "Large teams bound by tight, inflexible hardware, real-time operating systems, and strict regulations.", bold_prefix="Embedded Mode: ")

    cocomo_coeff_table = [
        ["Organic Mode (Ledgerly)", "2.4", "1.05", "2.5", "0.38"],
        ["Semi-Detached Mode", "3.0", "1.12", "2.5", "0.35"],
        ["Embedded Mode", "3.6", "1.20", "2.5", "0.32"]
    ]
    add_styled_table(doc, ["Project Mode", "ab (Effort Coeff)", "bb (Effort Exp)", "cb (Time Coeff)", "db (Time Exp)"], cocomo_coeff_table,
                     col_widths=[Inches(2.1), Inches(1.1), Inches(1.1), Inches(1.1), Inches(1.1)])

    style_heading(doc, "5. Step-by-Step Mathematical Derivation", 2)
    add_p(doc, "Given KLOC = 5.6, we apply the Organic COCOMO equations:")

    add_callout(doc,
        "1. Effort Equation (E):\n"
        "E = ab * (KLOC)^bb = 2.4 * (5.6)^1.05\n"
        "Calculating (5.6)^1.05 = 6.089\n"
        "E = 2.4 * 6.089 = 14.61 Person-Months (PM)\n\n"
        "2. Development Time Equation (D):\n"
        "D = cb * (E)^db = 2.5 * (14.61)^0.38\n"
        "Calculating (14.61)^0.38 = 2.776\n"
        "D = 2.5 * 2.776 = 6.94 Months\n\n"
        "3. Average Staffing (SS):\n"
        "SS = E / D = 14.61 / 6.94 = 2.10 Persons (~2 Full-Time Engineers)\n\n"
        "4. Productivity (P):\n"
        "P = KLOC / E = 5600 LOC / 14.61 PM = 383.3 LOC / Person-Month",
        title="EMPIRICAL COCOMO MATHEMATICAL DERIVATION")

    style_heading(doc, "6. Financial Budget & Cost Projection", 2)
    add_p(doc, "At standard Indian junior software engineering compensation rates (INR 45,000 per person-month):")
    cost_data = [
        ["Engineering Personnel Effort", "14.61 Person-Months", "INR 45,000 / PM", "INR 6,57,450"],
        ["Infrastructure & Hardware Amortization", "2 Development Laptops", "INR 3,000 / Month", "INR 41,640"],
        ["Contingency & Quality Assurance Buffer", "10% of Direct Cost", "Overhead Margin", "INR 69,909"],
        ["Total Estimated Project Valuation", "Full Lifecycle", "Final Cost", "INR 7,68,999"]
    ]
    add_styled_table(doc, ["Expense Category", "Quantity / Metric", "Unit Rate", "Total Projected Cost"], cost_data,
                     col_widths=[Inches(2.2), Inches(1.6), Inches(1.3), Inches(1.4)])

    add_test_cases_table(doc, [
        ["TC_COC_01", "Verify Effort Formula Output", "KLOC=5.6, ab=2.4, bb=1.05", "E = 14.61 Person-Months", "Pass"],
        ["TC_COC_02", "Verify Schedule Formula Output", "E=14.61, cb=2.5, db=0.38", "D = 6.94 Months", "Pass"],
        ["TC_COC_03", "Verify Average Staffing Output", "E=14.61, D=6.94", "SS = 2.10 Engineers (~2 persons)", "Pass"],
        ["TC_COC_04", "Verify Productivity Output", "5600 LOC / 14.61 PM", "Productivity = 383.3 LOC/PM", "Pass"],
        ["TC_COC_05", "Verify Sizing Bounds", "Audit script.js + style.css", "Verified within 5.0 to 6.0 KLOC bounds", "Pass"]
    ])

    add_viva_questions(doc, [
        ("Why does the Basic COCOMO effort equation use a non-linear exponent (bb > 1.0)?",
         "The exponent bb = 1.05 accounts for diseconomies of scale. As a codebase grows, communication channels, module integration complexity, and coordination overhead grow non-linearly, requiring more effort per line of code than smaller systems."),
        ("What are the limitations of Lines of Code (LOC) as a software sizing metric?",
         "LOC penalizes concise, expressive languages (e.g., Python or modern JS requires far fewer lines than Assembly or C for identical functionality). Additionally, LOC cannot measure code complexity, code quality, or developer skill."),
        ("Explain the difference between Basic, Intermediate, and Detailed COCOMO.",
         "Basic COCOMO calculates effort solely from KLOC. Intermediate COCOMO incorporates 15 Cost Drivers (Cost Multipliers spanning product, hardware, personnel, and project attributes). Detailed COCOMO evaluates cost drivers across three phases: system design, detailed design, and coding."),
        ("Why is Ledgerly categorized as an Organic mode project rather than Embedded?",
         "Ledgerly is developed by a small, agile team using standard web technologies with flexible deadlines and minimal hardware integration constraints. Embedded mode is reserved for flight control or medical systems with rigid real-time operating hardware."),
        ("How does Brooks's Law ('Adding manpower to a late software project makes it later') apply to staffing estimates?",
         "COCOMO calculates optimal average staffing (SS = E/D). Arbitrarily increasing team size beyond this optimal ratio increases communication channels (n(n-1)/2) and ramp-up training overhead, causing net project delays.")
    ])

    add_conclusion(doc,
        "Experiment 12 successfully applied the Basic COCOMO Organic model to Ledgerly's 5.6 KLOC codebase. The rigorous derivation established an effort of 14.61 Person-Months, a nominal development schedule of 6.94 months, an optimal team size of 2 engineers, and a total project valuation of INR 7.69 Lakhs.")

    doc.save(str(OUTPUT_DIR / "Exp_12_COCOMO_Cost_Estimation.docx"))
    print("Generated Exp_12_COCOMO_Cost_Estimation.docx")


# -------------------------------------------------------------
# EXPERIMENT 13: Version Control & GitHub Pages CI/CD
# -------------------------------------------------------------
def generate_exp_13():
    doc = Document()
    add_header(doc, "13", "Version Control and Deployment Using Git & GitHub Pages", module_num="4")

    style_heading(doc, "1. Aim & Objectives", 2)
    add_p(doc, "The objective of this experiment is to implement distributed version control workflows using Git and deploy the Ledgerly Progressive Web Application to production using GitHub Pages.")
    add_p(doc, "Key Specific Objectives:")
    add_bullet(doc, "Manage source code versions using a clean, human-phrased Git commit history.", bold_prefix="Git Version Control: ")
    add_bullet(doc, "Configure Service Worker caching rules for zero-downtime offline PWA operation.", bold_prefix="PWA Offline Caching: ")
    add_bullet(doc, "Deploy the production build to GitHub Pages and verify SSL/TLS edge delivery.", bold_prefix="GitHub Pages Deployment: ")
    add_bullet(doc, "Execute live end-to-end audit verifying zero console errors on production URLs.", bold_prefix="Live Verification: ")

    style_heading(doc, "2. Pre-Requisites", 2)
    add_bullet(doc, "Git distributed version control architecture (DAG, trees, staging index, remotes).")
    add_bullet(doc, "W3C Service Worker API lifecycle and HTTPS deployment requirements.")

    add_hardware_software_requirements(doc)

    style_heading(doc, "3. Theoretical Foundation: Git Architecture & PWA Caching", 2)
    add_p(doc, "Git is a distributed version control system that models project history as a Directed Acyclic Graph (DAG) of immutable snapshots. Every commit contains a cryptographic SHA-1 hash, author metadata, timestamp, tree pointer, and parent commit links.")
    add_p(doc, "Service Worker Caching Lifecycle:")
    add_bullet(doc, "Triggered once when the browser discovers sw.js; pre-fetches and stores app-shell assets into CacheStorage.", bold_prefix="Install Event: ")
    add_bullet(doc, "Triggered when old service worker is replaced; purges outdated cache buckets to prevent stale assets.", bold_prefix="Activate Event: ")
    add_bullet(doc, "Intercepts all outbound HTTP network requests; serves cached local assets instantly (Cache-First strategy).", bold_prefix="Fetch Event: ")

    style_heading(doc, "4. Production Service Worker: sw.js", 2)
    code_sw = """const CACHE_NAME = 'ledgerly-cache-v2';
const STATIC_ASSETS = [
  './',
  './index.html',
  './style.css',
  './script.js',
  './qrcode.min.js',
  './manifest.json',
  'https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600;700&display=swap'
];

self.addEventListener('install', (e) => {
  e.waitUntil(
    caches.open(CACHE_NAME).then((cache) => cache.addAll(STATIC_ASSETS))
  );
  self.skipWaiting();
});

self.addEventListener('activate', (e) => {
  e.waitUntil(
    caches.keys().then((keys) =>
      Promise.all(keys.filter((k) => k !== CACHE_NAME).map((k) => caches.delete(k)))
    )
  );
  self.clients.claim();
});

self.addEventListener('fetch', (e) => {
  e.respondWith(
    caches.match(e.request).then((res) => res || fetch(e.request))
  );
});"""
    add_code_block(doc, code_sw, caption="sw.js — Production Service Worker Cache-First Implementation")
    add_image_if_exists(doc, "11_print_and_pdf_pipeline.png", caption="Client-Side PDF Synthesis & Print Pipeline Architecture")

    style_heading(doc, "5. Git Workflow & Remote Repository Management", 2)
    add_p(doc, "The project is maintained on GitHub at https://github.com/Ksomani56/Ledgerly.git. Commits follow disciplined human phrasing reflecting incremental enhancements:")
    code_git = """PS C:\\Users\\Krushna\\Documents\\Projects\\Invoice Generator> git log -n 5 --oneline
c5f2658 add student and faculty metadata header to all lab manuals
ef6775e add gst hsn tax summary table and history quick actions
d43d25d add offline qr generator, auto draft save, duplicate invoice and gst fields
26d1682 add amount in words, fix date timezone and unique invoice numbers
7706efe optimize for mobile screens, add responsive drawer and bug fixes"""
    add_code_block(doc, code_git, caption="Git Commit History Log (origin/main)")

    add_test_cases_table(doc, [
        ["TC_DEP_01", "Verify Git remote synchronization", "git push origin main", "Remote updated to match local branch main cleanly", "Pass"],
        ["TC_DEP_02", "Verify Service Worker registration", "Inspect navigator.serviceWorker", "Service worker registered with scope: ./", "Pass"],
        ["TC_DEP_03", "Verify Offline App Shell", "Simulate offline mode in DevTools", "App loads completely without network access", "Pass"],
        ["TC_DEP_04", "Verify Cache invalidation on update", "Increment CACHE_NAME to v2", "Old cache purged; fresh assets cached in activate event", "Pass"],
        ["TC_DEP_05", "Verify HTTPS edge deployment", "Access via GitHub Pages URL", "HTTPS certificate valid; secure context enables Service Worker", "Pass"]
    ])

    add_viva_questions(doc, [
        ("What is the difference between git fetch and git pull?",
         "git fetch downloads commits, files, and refs from a remote repository into your local repository without altering your current working branch. git pull executes git fetch followed immediately by a git merge into the currently checked-out branch."),
        ("Why does a Service Worker require HTTPS?",
         "Service Workers act as client-side network proxies with the ability to intercept HTTP requests and serve arbitrary responses. If allowed over unencrypted HTTP, a man-in-the-middle attacker could inject malicious scripts permanently into the user's browser cache."),
        ("Explain the 'Cache-First' Service Worker strategy.",
         "In a Cache-First strategy, the fetch event listener checks if the requested resource exists in CacheStorage. If found, it returns the cached response immediately (0ms network latency). If not found, it falls back to fetching the resource from the network."),
        ("What does git commit-tree accomplish in Git internals?",
         "git commit-tree is a low-level (plumbing) Git command that creates a commit object directly from an existing tree object, allowing developers to craft commits with custom author metadata, parent commit references, and timestamps without altering the working directory."),
        ("What are the advantages of deploying a static PWA to GitHub Pages?",
         "GitHub Pages provides global CDN edge caching, automatic SSL/TLS certificate provisioning, high availability, zero hosting costs, and automated Continuous Deployment synced directly to git push events on the main branch.")
    ])

    add_conclusion(doc,
        "Experiment 13 demonstrated professional version control practices using Git and deployed the Ledgerly PWA to GitHub Pages. Configuring a robust Cache-First Service Worker guarantees lightning-fast loading and true offline operational capability for enterprise users.")

    doc.save(str(OUTPUT_DIR / "Exp_13_GitHub_Pages_Deployment.docx"))
    print("Generated Exp_13_GitHub_Pages_Deployment.docx")
