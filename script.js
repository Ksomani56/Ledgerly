/* ================================================================
   LEDGERLY — INVOICE & ESTIMATE GENERATOR (COMPREHENSIVE SUITE)
   ================================================================ */

/* ================================================================
   THEME HELPER (DARK / LIGHT MODE)
   ================================================================ */
function getTheme(){
  return localStorage.getItem('ig_theme') || 'light';
}
function setTheme(t){
  localStorage.setItem('ig_theme', t);
  document.documentElement.setAttribute('data-theme', t);
}
// Apply saved theme immediately on script load
document.documentElement.setAttribute('data-theme', getTheme());

/* ================================================================
   STORAGE HELPERS & DATA MODELS
   ================================================================ */
const DB = {
  users: 'ig_users',
  session: 'ig_session',
  invoices: 'ig_invoices',
  customers: 'ig_customers',
  enterprises: 'ig_enterprises',
  items: 'ig_items',
  expenses: 'ig_expenses'
};

const DEFAULT_ADMIN = {
  id: 'u_admin',
  name: 'Admin User',
  email: 'admin@admin.com',
  password: 'admin123',
  businessName: 'Ledgerly Enterprise Solutions',
  phone: '+91 98765 43210',
  address: '100 Executive Way, Suite 500, Mumbai, MH',
  upiId: 'admin@upi',
  taxId: '27AAAAA0000A1Z5',
  logo: ''
};

const SAMPLE_ENTERPRISES = [
  {
    id: 'ent_default',
    userId: 'u_admin',
    isDefault: true,
    name: 'Ledgerly Global Tech',
    tagline: 'Enterprise Software & Financial Solutions',
    email: 'billing@ledgerly.com',
    phone: '+91 98765 43210',
    address: '100 Executive Tower, BKC, Mumbai, MH 400051',
    taxId: '27AAAAA0000A1Z5',
    currency: 'INR (₹)',
    currencySymbol: '₹',
    upiId: 'ledgerly@icici',
    bankName: 'HDFC Bank',
    accountNumber: '50200012345678',
    ifscCode: 'HDFC0000123',
    paymentUrl: 'https://pay.ledgerly.com/checkout',
    notes: 'Thank you for choosing Ledgerly Global Tech.',
    defaultTemplate: 'classic',
    logo: ''
  }
];

const SAMPLE_CUSTOMERS = [
  {
    id: 'cust_sample_1',
    userId: 'u_admin',
    name: 'Acme Corporation',
    contactPerson: 'Sarah Jenkins',
    email: 'accounts@acme.com',
    phone: '+91 91234 56789',
    address: '45 Corporate Blvd, Cyber City, Gurugram, HR',
    taxId: '06AAACA1234B1Z2',
    terms: 'Net 15 Days'
  },
  {
    id: 'cust_sample_2',
    userId: 'u_admin',
    name: 'Starlight Media Pvt Ltd',
    contactPerson: 'Rajesh Sharma',
    email: 'finance@starlightmedia.in',
    phone: '+91 98111 22233',
    address: '12 Film City Road, Goregaon East, Mumbai, MH',
    taxId: '27AABCS9876C1Z9',
    terms: 'Due on Receipt'
  }
];

const SAMPLE_ITEMS = [
  { id: 'item_1', userId: 'u_admin', name: 'Web Application Development', desc: 'Custom frontend & backend full-stack development', hsn: '998314', unit: 'hrs', price: 1500, taxRate: 18 },
  { id: 'item_2', userId: 'u_admin', name: 'UI/UX Design & Prototyping', desc: 'Figma wireframes, responsive mobile UI and brand assets', hsn: '998311', unit: 'screens', price: 2500, taxRate: 18 },
  { id: 'item_3', userId: 'u_admin', name: 'Cloud Infrastructure & DevOps', desc: 'AWS/GCP setup, Docker containers and CI/CD pipelines', hsn: '998313', unit: 'hrs', price: 2000, taxRate: 18 },
  { id: 'item_4', userId: 'u_admin', name: 'Annual Software Maintenance (SLA)', desc: 'Bug fixes, security updates, and database backup monitoring', hsn: '998319', unit: 'mo', price: 8000, taxRate: 18 },
  { id: 'item_5', userId: 'u_admin', name: 'Technical Consultation & Code Audit', desc: 'Architecture review, security vulnerability assessment', hsn: '998312', unit: 'sessions', price: 5000, taxRate: 18 }
];

const SAMPLE_EXPENSES = [
  { id: 'exp_1', userId: 'u_admin', title: 'AWS Cloud Hosting & Databases', category: 'Hosting', amount: 3200, date: '2026-09-15', vendor: 'Amazon Web Services', method: 'Credit Card', ref: 'AWS-INV-99231' },
  { id: 'exp_2', userId: 'u_admin', title: 'Figma Professional Team Plan', category: 'Software', amount: 1500, date: '2026-09-22', vendor: 'Figma Inc.', method: 'UPI', ref: 'UPI-FIGMA-4421' },
  { id: 'exp_3', userId: 'u_admin', title: 'High-Speed Fiber Internet & Backup', category: 'Office', amount: 1200, date: '2026-10-02', vendor: 'Airtel Broadband', method: 'Net Banking', ref: 'AIR-OCT-091' },
  { id: 'exp_4', userId: 'u_admin', title: 'Google Workspace Email Business Starter', category: 'Software', amount: 800, date: '2026-10-05', vendor: 'Google India', method: 'Credit Card', ref: 'GSUITE-10829' }
];

function getAll(key){
  try{
    const data = JSON.parse(localStorage.getItem(key));
    if(key === DB.users){
      let users = Array.isArray(data) ? data : [];
      if(!users.some(u => u.email && u.email.toLowerCase() === DEFAULT_ADMIN.email)){
        users.unshift(DEFAULT_ADMIN);
        localStorage.setItem(DB.users, JSON.stringify(users));
      }
      return users;
    }
    if(key === DB.enterprises){
      let items = Array.isArray(data) ? data : [];
      if(items.length === 0){
        items = [...SAMPLE_ENTERPRISES];
        localStorage.setItem(DB.enterprises, JSON.stringify(items));
      }
      return items;
    }
    if(key === DB.customers){
      let items = Array.isArray(data) ? data : [];
      if(items.length === 0){
        items = [...SAMPLE_CUSTOMERS];
        localStorage.setItem(DB.customers, JSON.stringify(items));
      }
      return items;
    }
    if(key === DB.items){
      let items = Array.isArray(data) ? data : [];
      if(items.length === 0){
        items = [...SAMPLE_ITEMS];
        localStorage.setItem(DB.items, JSON.stringify(items));
      }
      return items;
    }
    if(key === DB.expenses){
      let items = Array.isArray(data) ? data : [];
      if(items.length === 0){
        items = [...SAMPLE_EXPENSES];
        localStorage.setItem(DB.expenses, JSON.stringify(items));
      }
      return items;
    }
    return Array.isArray(data) ? data : [];
  }catch(e){
    if(key === DB.users) return [DEFAULT_ADMIN];
    if(key === DB.enterprises) return [...SAMPLE_ENTERPRISES];
    if(key === DB.customers) return [...SAMPLE_CUSTOMERS];
    if(key === DB.items) return [...SAMPLE_ITEMS];
    if(key === DB.expenses) return [...SAMPLE_EXPENSES];
    return [];
  }
}

function setAll(key, val){
  localStorage.setItem(key, JSON.stringify(val));
}

function uid(prefix){
  return prefix + '_' + Date.now().toString(36) + Math.random().toString(36).slice(2,7);
}

function getSession(){
  try{ return JSON.parse(localStorage.getItem(DB.session)); }catch(e){ return null; }
}

function setSession(userId, remember){
  const s = { userId, remember: !!remember };
  localStorage.setItem(DB.session, JSON.stringify(s));
}

function clearSession(){
  localStorage.removeItem(DB.session);
}

function currentUser(){
  const s = getSession();
  if(!s) return null;
  return getAll(DB.users).find(u => u.id === s.userId) || null;
}

/* ================================================================
   FORMATTING & UTILITY HELPERS
   ================================================================ */
function isValidEmail(v){
  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v);
}

function fmtMoney(n, symbol = '₹'){
  n = Number(n) || 0;
  return symbol + ' ' + n.toLocaleString('en-IN', { minimumFractionDigits: 2, maximumFractionDigits: 2 });
}

function fmtDate(d){
  if(!d) return '—';
  const dt = new Date(d + 'T00:00:00');
  if(isNaN(dt)) return d;
  return dt.toLocaleDateString('en-US', { year: 'numeric', month: 'short', day: 'numeric' });
}

function todayISO(){
  return new Date().toISOString().slice(0, 10);
}

function escapeHTML(str){
  return String(str ?? '').replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
}

function showToast(msg){
  const t = document.getElementById('toast');
  if(!t) return;
  t.textContent = msg;
  t.classList.add('show');
  clearTimeout(showToast._tm);
  showToast._tm = setTimeout(()=> t.classList.remove('show'), 2600);
}

/* ================================================================
   OVERDUE & PAYMENT TRACKING ENGINE
   ================================================================ */
function getOverdueDays(dueDateStr){
  if(!dueDateStr) return 0;
  const due = new Date(dueDateStr + 'T23:59:59');
  if(isNaN(due)) return 0;
  const now = new Date();
  if(now > due){
    return Math.max(1, Math.ceil((now - due) / (1000 * 60 * 60 * 24)));
  }
  return 0;
}

function getInvoicePayments(inv){
  if(Array.isArray(inv.payments) && inv.payments.length > 0){
    return inv.payments;
  }
  if(inv.status === 'Paid'){
    return [{
      id: 'pay_legacy_' + inv.id,
      amount: Number(inv.grandTotal) || 0,
      date: inv.paidAt || inv.invoiceDate || todayISO(),
      method: inv.paymentMethod || 'Direct Payment',
      transactionRef: inv.transactionRef || '',
      notes: inv.paidMessage || 'Settled in full'
    }];
  }
  return [];
}

function getInvoicePaidTotal(inv){
  const payments = getInvoicePayments(inv);
  return payments.reduce((sum, p) => sum + (Number(p.amount) || 0), 0);
}

function getInvoiceBalance(inv){
  const grandTotal = Number(inv.grandTotal) || 0;
  const paid = getInvoicePaidTotal(inv);
  const bal = grandTotal - paid;
  return bal > 0.009 ? bal : 0;
}

function getInvoiceEffectiveStatus(inv){
  if(inv.docType === 'estimate') {
    return inv.status || 'Draft';
  }
  const bal = getInvoiceBalance(inv);
  const paid = getInvoicePaidTotal(inv);
  if(paid > 0 && bal <= 0.009){
    return 'Paid';
  }
  if(paid > 0 && bal > 0.009){
    return 'Partially Paid';
  }
  if(inv.status === 'Paid' && paid === 0){
    return 'Paid';
  }
  return inv.status || 'Draft';
}

/* ================================================================
   ADVANCED CALCULATION ENGINE (PER-ITEM TAX, HSN, UNITS, ROUND-OFF)
   ================================================================ */
function computeTotals(items, discountVal = 0, taxPct = 0, discountType = 'pct', extraCharges = 0, isInterState = false, isRoundOff = true){
  let subtotal = 0;
  let itemsTaxTotal = 0;
  let hasPerItemTax = false;

  items.forEach(i => {
    const qty = Number(i.qty) || 0;
    const price = Number(i.price) || 0;
    const lineSub = qty * price;
    subtotal += lineSub;
    if(Number(i.taxPct) > 0){
      hasPerItemTax = true;
      itemsTaxTotal += lineSub * (Number(i.taxPct) / 100);
    }
  });

  let discount = 0;
  if(discountType === 'flat'){
    discount = Math.min(subtotal, Math.max(0, Number(discountVal) || 0));
  } else {
    discount = subtotal * (Math.max(0, Number(discountVal) || 0) / 100);
  }

  const taxableAmount = Math.max(0, subtotal - discount);
  let tax = 0;
  if(hasPerItemTax){
    const ratio = subtotal > 0 ? (taxableAmount / subtotal) : 1;
    tax = itemsTaxTotal * ratio;
  } else {
    tax = taxableAmount * (Math.max(0, Number(taxPct) || 0) / 100);
  }

  const extra = Math.max(0, Number(extraCharges) || 0);
  const preTotal = taxableAmount + tax + extra;

  let roundOff = 0;
  let grandTotal = preTotal;
  if(isRoundOff){
    grandTotal = Math.round(preTotal);
    roundOff = grandTotal - preTotal;
  }

  return {
    subtotal,
    discount,
    taxableAmount,
    tax,
    cgst: isInterState ? 0 : (tax / 2),
    sgst: isInterState ? 0 : (tax / 2),
    igst: isInterState ? tax : 0,
    extraCharges: extra,
    roundOff,
    grandTotal
  };
}

/* ================================================================
   DATA PORTABILITY: CSV & JSON BACKUP / RESTORE
   ================================================================ */
function exportInvoicesToCSV(invoices){
  if(!invoices || !invoices.length){
    showToast('No invoices available to export.');
    return;
  }
  const headers = [
    'Document Number', 'Type', 'Date', 'Due Date', 'Customer', 'Customer Email',
    'Currency', 'Subtotal', 'Discount', 'Tax', 'Extra Charges', 'Grand Total',
    'Amount Paid', 'Balance Due', 'Status'
  ];

  const rows = invoices.map(inv => {
    const status = getInvoiceEffectiveStatus(inv);
    const paid = getInvoicePaidTotal(inv);
    const bal = getInvoiceBalance(inv);
    return [
      inv.invoiceNumber || '',
      inv.docType || 'invoice',
      inv.invoiceDate || '',
      inv.dueDate || '',
      inv.customer ? inv.customer.name : '',
      inv.customer ? (inv.customer.email || '') : '',
      inv.currencySymbol || '₹',
      inv.subtotal || 0,
      inv.discount || 0,
      inv.tax || 0,
      inv.extraCharges || 0,
      inv.grandTotal || 0,
      paid.toFixed(2),
      bal.toFixed(2),
      status
    ].map(val => `"${String(val).replace(/"/g, '""')}"`).join(',');
  });

  const csvContent = 'data:text/csv;charset=utf-8,' + [headers.join(','), ...rows].join('\n');
  const encodedUri = encodeURI(csvContent);
  const link = document.createElement('a');
  link.setAttribute('href', encodedUri);
  link.setAttribute('download', `ledgerly-invoices-${todayISO()}.csv`);
  document.body.appendChild(link);
  link.click();
  document.body.removeChild(link);
  showToast('Invoices exported to CSV.');
}

function exportFullBackupJSON(){
  const backup = {
    version: '2.0',
    exportDate: new Date().toISOString(),
    users: getAll(DB.users),
    enterprises: getAll(DB.enterprises),
    customers: getAll(DB.customers),
    invoices: getAll(DB.invoices),
    items: getAll(DB.items),
    expenses: getAll(DB.expenses)
  };
  const jsonStr = JSON.stringify(backup, null, 2);
  const blob = new Blob([jsonStr], { type: 'application/json' });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = `ledgerly-backup-${todayISO()}.json`;
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
  URL.revokeObjectURL(url);
  showToast('Full system backup downloaded.');
}

function restoreBackupJSON(fileContent){
  try{
    const data = JSON.parse(fileContent);
    if(!data.users && !data.invoices && !data.customers){
      showToast('Invalid backup file format.');
      return false;
    }
    if(Array.isArray(data.users)) setAll(DB.users, data.users);
    if(Array.isArray(data.enterprises)) setAll(DB.enterprises, data.enterprises);
    if(Array.isArray(data.customers)) setAll(DB.customers, data.customers);
    if(Array.isArray(data.invoices)) setAll(DB.invoices, data.invoices);
    if(Array.isArray(data.items)) setAll(DB.items, data.items);
    if(Array.isArray(data.expenses)) setAll(DB.expenses, data.expenses);
    showToast('Database restored successfully!');
    setTimeout(()=> location.reload(), 800);
    return true;
  }catch(e){
    showToast('Error parsing backup file: ' + e.message);
    return false;
  }
}

/* ================================================================
   SIGNATURE PAD
   ================================================================ */
function initSignaturePad(canvas, existingDataUrl){
  const ctx = canvas.getContext('2d');
  ctx.lineWidth = 2.4;
  ctx.lineCap = 'round';
  ctx.lineJoin = 'round';
  ctx.strokeStyle = '#16241f';
  canvas.style.touchAction = 'none';
  let drawing = false;
  let hasDrawing = false;

  function pos(e){
    const rect = canvas.getBoundingClientRect();
    let cx = 0, cy = 0;
    if(e.touches && e.touches.length > 0){
      cx = e.touches[0].clientX;
      cy = e.touches[0].clientY;
    } else if(e.changedTouches && e.changedTouches.length > 0){
      cx = e.changedTouches[0].clientX;
      cy = e.changedTouches[0].clientY;
    } else {
      cx = e.clientX;
      cy = e.clientY;
    }
    return {
      x: (cx - rect.left) * (canvas.width / rect.width),
      y: (cy - rect.top) * (canvas.height / rect.height)
    };
  }

  function start(e){
    if(e.cancelable) e.preventDefault();
    drawing = true; hasDrawing = true;
    const p = pos(e);
    ctx.beginPath();
    ctx.moveTo(p.x, p.y);
    if(e.pointerId && canvas.setPointerCapture){
      try{ canvas.setPointerCapture(e.pointerId); }catch(err){}
    }
  }

  function move(e){
    if(!drawing) return;
    if(e.cancelable) e.preventDefault();
    const p = pos(e);
    ctx.lineTo(p.x, p.y);
    ctx.stroke();
  }

  function end(e){
    if(e && e.cancelable) e.preventDefault();
    drawing = false;
  }

  // Pointer listeners (standard modern desktop & mobile browsers)
  canvas.addEventListener('pointerdown', start);
  canvas.addEventListener('pointermove', move);
  canvas.addEventListener('pointerup', end);
  canvas.addEventListener('pointercancel', end);

  // Native touch listeners (fallback for iOS Safari and mobile WebViews)
  canvas.addEventListener('touchstart', start, { passive: false });
  canvas.addEventListener('touchmove', move, { passive: false });
  canvas.addEventListener('touchend', end, { passive: false });
  canvas.addEventListener('touchcancel', end, { passive: false });

  if(existingDataUrl){
    const img = new Image();
    img.onload = ()=> {
      ctx.drawImage(img, 0, 0, canvas.width, canvas.height);
      hasDrawing = true;
    };
    img.src = existingDataUrl;
  }

  return {
    clear(){ ctx.clearRect(0,0,canvas.width,canvas.height); hasDrawing = false; },
    isEmpty(){ return !hasDrawing; },
    toDataURL(){ return canvas.toDataURL('image/png'); }
  };
}

/* ================================================================
   PAYMENT QR & UPI HELPERS
   ================================================================ */
function buildUpiLink(invoice){
  const upiId = invoice.seller && invoice.seller.upiId;
  if(!upiId) return null;
  const balance = getInvoiceBalance(invoice);
  const payable = balance > 0 ? balance : invoice.grandTotal;
  const params = new URLSearchParams({
    pa: upiId,
    pn: invoice.seller.name || 'Merchant',
    am: Number(payable || 0).toFixed(2),
    cu: 'INR',
    tn: (invoice.docType === 'estimate' ? 'Estimate ' : 'Invoice ') + invoice.invoiceNumber
  });
  return 'upi://pay?' + params.toString();
}

function getPaymentQrTarget(invoice){
  if(invoice.seller && invoice.seller.paymentUrl){
    return invoice.seller.paymentUrl;
  }
  return buildUpiLink(invoice);
}

function qrImageUrl(data, size = 200){
  if(!data) return '';
  return `https://api.qrserver.com/v1/create-qr-code/?size=${size}x${size}&data=${encodeURIComponent(data)}`;
}

/* ================================================================
   ROUTER & ROUTE GUARD
   ================================================================ */
const routes = {
  '/login': renderLogin,
  '/register': renderRegister,
  '/dashboard': guarded(renderDashboard),
  '/create': guarded(renderCreateInvoice),
  '/edit': guarded(renderCreateInvoice),
  '/preview': guarded(renderPreview),
  '/history': guarded(renderHistory),
  '/customers': guarded(renderCustomers),
  '/items': guarded(renderCatalog),
  '/expenses': guarded(renderExpenses),
  '/enterprise': guarded(renderEnterprise),
  '/profile': guarded(renderProfile),
};

function guarded(fn){
  return function(params){
    if(!currentUser()){ location.hash = '#/login'; return; }
    fn(params);
  };
}

function parseHash(){
  const raw = location.hash.replace(/^#/, '') || '/login';
  const [path, qs] = raw.split('?');
  const params = new URLSearchParams(qs || '');
  return { path: path || '/login', params };
}

function route(){
  const { path, params } = parseHash();
  const handler = routes[path];
  const app = document.getElementById('app');
  if(!handler){ location.hash = '#/login'; return; }
  app.innerHTML = '';
  handler(params);
}

window.addEventListener('hashchange', route);
window.addEventListener('DOMContentLoaded', ()=>{
  if(!location.hash) location.hash = currentUser() ? '#/dashboard' : '#/login';
  route();
});

/* ================================================================
   SHARED SHELL (SIDEBAR & HEADER)
   ================================================================ */
function appShell(activePath, title, eyebrow, contentHTML){
  const user = currentUser();
  const currentTheme = getTheme();
  const themeLabel = currentTheme === 'dark' ? 'Light Mode' : 'Dark Mode';

  const nav = [
    {path:'/dashboard', label:'Dashboard', ico:'D'},
    {path:'/create', label:'New Invoice', ico:'+'},
    {path:'/history', label:'Invoices &amp; Quotes', ico:'I'},
    {path:'/customers', label:'Customers', ico:'C'},
    {path:'/items', label:'Item Catalog', ico:'T'},
    {path:'/expenses', label:'Expenses', ico:'X'},
    {path:'/enterprise', label:'Enterprise', ico:'E'},
    {path:'/profile', label:'Profile', ico:'P'},
  ];
  const navHTML = nav.map(n => `
    <a class="nav-link ${activePath===n.path?'active':''}" href="#${n.path}">
      <span class="ico">${n.ico}</span>${n.label}
    </a>`).join('');

  return `
  <div class="shell">
    <div class="sidebar-backdrop no-print" id="sidebarBackdrop"></div>
    <div class="mobile-topbar no-print">
      <div class="brandmark"><div class="seal">L</div><div class="word">Ledger<span>ly</span></div></div>
      <button id="menuToggle" aria-label="Open menu">&#9776;</button>
    </div>
    <aside class="sidebar no-print" id="sidebar">
      <div style="display:flex;justify-content:space-between;align-items:center;">
        <div class="brandmark"><div class="seal">L</div><div class="word">Ledger<span>ly</span></div></div>
        <button class="sidebar-close-btn no-print" id="sidebarCloseBtn" aria-label="Close menu">&times;</button>
      </div>
      <nav class="sidebar-nav">${navHTML}</nav>
      <div class="sidebar-user">
        <div class="name">${escapeHTML(user?.name || '')}</div>
        <div class="biz">${escapeHTML(user?.businessName || 'Ledgerly Account')}</div>
        <button class="btn btn-ghost btn-sm btn-block" id="logoutBtn" style="border-color:rgba(255,255,255,0.25);color:#eef1ea;">Log out</button>
      </div>
    </aside>
    <main class="main">
      <div class="topbar">
        <div>
          ${eyebrow ? `<p class="eyebrow">${eyebrow}</p>` : ''}
          <h1>${title}</h1>
        </div>
        <button class="theme-toggle no-print" id="themeToggleBtn">${themeLabel}</button>
      </div>
      <div id="viewContent">${contentHTML}</div>
    </main>
  </div>`;
}

function mountShellEvents(){
  const toggle = document.getElementById('menuToggle');
  const closeBtn = document.getElementById('sidebarCloseBtn');
  const backdrop = document.getElementById('sidebarBackdrop');
  const sidebar = document.getElementById('sidebar');

  function openSidebar(){
    if(sidebar) sidebar.classList.add('open');
    if(backdrop) backdrop.classList.add('show');
    document.body.style.overflow = 'hidden';
  }
  function closeSidebar(){
    if(sidebar) sidebar.classList.remove('open');
    if(backdrop) backdrop.classList.remove('show');
    document.body.style.overflow = '';
  }

  if(toggle) toggle.addEventListener('click', openSidebar);
  if(closeBtn) closeBtn.addEventListener('click', closeSidebar);
  if(backdrop) backdrop.addEventListener('click', closeSidebar);

  // Close sidebar on navigation click on mobile screens
  if(sidebar){
    sidebar.querySelectorAll('.nav-link, #logoutBtn').forEach(el => {
      el.addEventListener('click', closeSidebar);
    });
  }
  
  const logout = document.getElementById('logoutBtn');
  if(logout){ logout.addEventListener('click', ()=>{ clearSession(); location.hash = '#/login'; }); }

  const themeBtn = document.getElementById('themeToggleBtn');
  if(themeBtn){
    themeBtn.addEventListener('click', ()=>{
      const nextTheme = getTheme() === 'dark' ? 'light' : 'dark';
      setTheme(nextTheme);
      themeBtn.textContent = nextTheme === 'dark' ? 'Light Mode' : 'Dark Mode';
      showToast(`Switched to ${nextTheme} mode.`);
    });
  }
}

/* ================================================================
   VIEW: LOGIN
   ================================================================ */
function renderLogin(){
  const app = document.getElementById('app');
  app.innerHTML = `
    <div class="auth-shell">
      <div class="auth-card">
        <div class="brandmark"><div class="seal">L</div><div class="word">Ledger<span>ly</span></div></div>
        <h2 style="font-size:22px;margin:0 0 4px;">Sign in to your account</h2>
        <p class="auth-sub">Enter your credentials to manage invoices and payments.</p>
        <div id="authMsg" class="form-msg"></div>
        <form id="loginForm">
          <div class="field" id="f-email">
            <label>Email address</label>
            <input type="email" id="email" autocomplete="email" placeholder="admin@admin.com">
            <div class="field-error">Enter a valid email address.</div>
          </div>
          <div class="field" id="f-password">
            <label>Password</label>
            <input type="password" id="password" autocomplete="current-password" placeholder="••••••••">
            <div class="field-error">Password is required.</div>
          </div>
          <div class="remember-row">
            <input type="checkbox" id="remember" checked>
            <label for="remember">Keep me signed in</label>
          </div>
          <button type="submit" class="btn btn-primary btn-block">Sign in</button>
        </form>
        <div class="auth-links">
          Don't have an account? <a href="#/register">Create one</a>
        </div>
      </div>
    </div>`;

  document.getElementById('loginForm').addEventListener('submit', (e)=>{
    e.preventDefault();
    const emailField = document.getElementById('f-email');
    const passField = document.getElementById('f-password');
    const msg = document.getElementById('authMsg');
    emailField.classList.remove('has-error');
    passField.classList.remove('has-error');
    msg.className = 'form-msg';

    const email = document.getElementById('email').value.trim();
    const password = document.getElementById('password').value;
    const remember = document.getElementById('remember').checked;

    let valid = true;
    if(!isValidEmail(email)){ emailField.classList.add('has-error'); valid = false; }
    if(!password){ passField.classList.add('has-error'); valid = false; }
    if(!valid) return;

    const user = getAll(DB.users).find(u => u.email.toLowerCase() === email.toLowerCase());
    if(!user || user.password !== password){
      msg.textContent = 'Invalid email or password.';
      msg.className = 'form-msg error show';
      return;
    }

    setSession(user.id, remember);
    location.hash = '#/dashboard';
  });
}

/* ================================================================
   VIEW: REGISTER
   ================================================================ */
function renderRegister(){
  const app = document.getElementById('app');
  app.innerHTML = `
    <div class="auth-shell">
      <div class="auth-card">
        <div class="brandmark"><div class="seal">L</div><div class="word">Ledger<span>ly</span></div></div>
        <h2 style="font-size:22px;margin:0 0 4px;">Create your account</h2>
        <p class="auth-sub">Set up your business billing workspace in seconds.</p>
        <div id="authMsg" class="form-msg"></div>
        <form id="regForm">
          <div class="field" id="f-rname">
            <label>Your full name</label>
            <input id="rname" autocomplete="name" placeholder="John Doe">
            <div class="field-error">Name is required.</div>
          </div>
          <div class="field" id="f-remail">
            <label>Email address</label>
            <input type="email" id="remail" autocomplete="email" placeholder="john@example.com">
            <div class="field-error">Enter a valid email address.</div>
          </div>
          <div class="field" id="f-rbiz">
            <label>Business / Company name</label>
            <input id="rbiz" placeholder="Acme Studio">
            <div class="field-error">Business name is required.</div>
          </div>
          <div class="field" id="f-rpass">
            <label>Password</label>
            <input type="password" id="rpass" autocomplete="new-password" placeholder="At least 6 characters">
            <div class="field-error">Password must be at least 6 characters.</div>
          </div>
          <button type="submit" class="btn btn-primary btn-block">Create account</button>
        </form>
        <div class="auth-links">
          Already have an account? <a href="#/login">Sign in</a>
        </div>
      </div>
    </div>`;

  document.getElementById('regForm').addEventListener('submit', (e)=>{
    e.preventDefault();
    const nameField = document.getElementById('f-rname');
    const emailField = document.getElementById('f-remail');
    const bizField = document.getElementById('f-rbiz');
    const passField = document.getElementById('f-rpass');
    const msg = document.getElementById('authMsg');
    [nameField, emailField, bizField, passField].forEach(f => f.classList.remove('has-error'));
    msg.className = 'form-msg';

    const name = document.getElementById('rname').value.trim();
    const email = document.getElementById('remail').value.trim();
    const businessName = document.getElementById('rbiz').value.trim();
    const password = document.getElementById('rpass').value;

    let valid = true;
    if(!name){ nameField.classList.add('has-error'); valid = false; }
    if(!isValidEmail(email)){ emailField.classList.add('has-error'); valid = false; }
    if(!businessName){ bizField.classList.add('has-error'); valid = false; }
    if(!password || password.length < 6){ passField.classList.add('has-error'); valid = false; }
    if(!valid) return;

    const users = getAll(DB.users);
    if(users.some(u => u.email.toLowerCase() === email.toLowerCase())){
      msg.textContent = 'An account with that email already exists.';
      msg.className = 'form-msg error show';
      return;
    }

    const newUser = {
      id: uid('u'),
      name, email, businessName, password,
      phone: '', address: '', upiId: '', taxId: '', logo: '', signature: ''
    };
    users.push(newUser);
    setAll(DB.users, users);

    const newEnt = {
      id: uid('ent'),
      userId: newUser.id,
      isDefault: true,
      name: businessName,
      tagline: 'Professional Billing & Invoicing',
      email: email,
      phone: '', address: '', taxId: '',
      currency: 'INR (₹)', currencySymbol: '₹',
      upiId: '', bankName: '', accountNumber: '', ifscCode: '',
      paymentUrl: '', notes: 'Thank you for your business.',
      defaultTemplate: 'classic', logo: ''
    };
    const ents = getAll(DB.enterprises);
    ents.push(newEnt);
    setAll(DB.enterprises, ents);

    setSession(newUser.id, true);
    location.hash = '#/dashboard';
  });
}

/* ================================================================
   VIEW: DASHBOARD (KPIS, ANALYTICS CHART, AGING BREAKDOWN)
   ================================================================ */
function renderDashboard(){
  const user = currentUser();
  const allInvoices = getAll(DB.invoices).filter(i => i.userId === user.id)
    .sort((a,b)=> b.createdAt - a.createdAt);

  const totalInvoiced = allInvoices.reduce((s,i)=> s + (Number(i.grandTotal)||0), 0);
  const totalCollected = allInvoices.reduce((s,i)=> s + getInvoicePaidTotal(i), 0);
  const totalBalanceDue = allInvoices.reduce((s,i)=> s + getInvoiceBalance(i), 0);

  // Business Expenses & Net Profit Calculations
  const allExpenses = getAll(DB.expenses).filter(e => e.userId === user.id);
  const totalExpenses = allExpenses.reduce((s,e) => s + (Number(e.amount)||0), 0);
  const netProfit = totalCollected - totalExpenses;

  // Recurring Retainers
  const recurringInvoices = allInvoices.filter(i => i.isRecurring);

  // Overdue count and value
  const overdueInvoices = allInvoices.filter(i => {
    return getInvoiceBalance(i) > 0 && getOverdueDays(i.dueDate) > 0;
  });
  const overdueValue = overdueInvoices.reduce((s,i)=> s + getInvoiceBalance(i), 0);

  // Aging Analysis
  let agingCurrent = 0;
  let aging1to30 = 0;
  let aging31to60 = 0;
  let aging60plus = 0;

  allInvoices.forEach(i => {
    const bal = getInvoiceBalance(i);
    if(bal <= 0) return;
    const days = getOverdueDays(i.dueDate);
    if(days === 0) agingCurrent += bal;
    else if(days <= 30) aging1to30 += bal;
    else if(days <= 60) aging31to60 += bal;
    else aging60plus += bal;
  });

  // Monthly Revenue Data (Last 6 Months)
  const monthNames = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];
  const now = new Date();
  const monthsData = [];
  for(let m = 5; m >= 0; m--){
    const d = new Date(now.getFullYear(), now.getMonth() - m, 1);
    const yr = d.getFullYear();
    const mo = d.getMonth();
    const key = `${yr}-${String(mo+1).padStart(2,'0')}`;
    const label = `${monthNames[mo]} ${String(yr).slice(-2)}`;
    monthsData.push({ key, label, billed: 0, collected: 0 });
  }

  allInvoices.forEach(i => {
    const dStr = i.invoiceDate || '';
    if(!dStr) return;
    const mKey = dStr.slice(0,7);
    const mObj = monthsData.find(m => m.key === mKey);
    if(mObj){
      mObj.billed += Number(i.grandTotal) || 0;
      mObj.collected += getInvoicePaidTotal(i);
    }
  });

  // Calculate SVG Bar Chart
  const maxVal = Math.max(...monthsData.map(m => Math.max(m.billed, m.collected)), 1000);
  const chartHeight = 120;
  const svgWidth = 460;
  const colWidth = svgWidth / monthsData.length;

  const barsSVG = monthsData.map((m, idx) => {
    const xBase = idx * colWidth + 15;
    const billedH = Math.max(4, (m.billed / maxVal) * chartHeight);
    const collectedH = Math.max(4, (m.collected / maxVal) * chartHeight);
    const billedY = chartHeight - billedH + 20;
    const collectedY = chartHeight - collectedH + 20;

    return `
      <g>
        <title>${m.label}: Billed ${fmtMoney(m.billed)}, Collected ${fmtMoney(m.collected)}</title>
        <rect x="${xBase}" y="${billedY}" width="20" height="${billedH}" class="chart-bar-billed" />
        <rect x="${xBase + 24}" y="${collectedY}" width="20" height="${collectedH}" class="chart-bar-paid" />
        <text x="${xBase + 22}" y="152" class="chart-axis-label">${m.label}</text>
      </g>
    `;
  }).join('');

  // Top 5 Clients by Revenue
  const custRevenueMap = {};
  allInvoices.forEach(i => {
    if(!i.customer || !i.customer.name) return;
    const cName = i.customer.name;
    if(!custRevenueMap[cName]) custRevenueMap[cName] = { name: cName, billed: 0, count: 0, custId: i.customer.id };
    custRevenueMap[cName].billed += Number(i.grandTotal) || 0;
    custRevenueMap[cName].count++;
  });
  const topClients = Object.values(custRevenueMap).sort((a,b)=> b.billed - a.billed).slice(0, 5);

  const topClientsHTML = topClients.length ? topClients.map(c => `
    <div style="display:flex;justify-content:space-between;align-items:center;padding:10px 0;border-bottom:1px solid var(--line);">
      <div>
        <div style="font-weight:600;font-size:13.5px;">${escapeHTML(c.name)}</div>
        <div style="font-size:11.5px;color:var(--ink-faint);">${c.count} ${c.count===1?'Invoice':'Invoices'}</div>
      </div>
      <div class="mono" style="font-weight:600;font-size:13.5px;color:var(--teal);">${fmtMoney(c.billed)}</div>
    </div>
  `).join('') : '<div style="color:var(--ink-faint);font-size:13px;padding:12px 0;">No client data recorded yet.</div>';

  const recent = allInvoices.slice(0, 6);
  const rows = recent.length ? recent.map(rowHTML).join('') :
    `<tr class="empty-row"><td colspan="6">No invoices or estimates yet. Create your first document below!</td></tr>`;

  const content = `
    <div class="cta-banner">
      <div>
        <h2>Fast Invoicing &amp; Estimates</h2>
        <p>Create tax-compliant invoices, track partial payments, or draft client estimates with instant QR code.</p>
      </div>
      <div style="display:flex;gap:10px;flex-wrap:wrap;">
        <a href="#/create" class="btn btn-brass">+ New Invoice</a>
        <a href="#/create?type=estimate" class="btn btn-ghost" style="border-color:rgba(255,255,255,0.4);color:#fff;">+ New Estimate</a>
        <button id="quickCsvBtn" class="btn btn-ghost" style="border-color:rgba(255,255,255,0.4);color:#fff;">Export CSV</button>
      </div>
    </div>

    <!-- Primary KPIs -->
    <div class="stat-grid">
      <div class="card stat-card accent">
        <div class="label">Total Billed</div>
        <div class="value mono">${fmtMoney(totalInvoiced)}</div>
        <div class="helper-text" style="margin-top:2px;">${allInvoices.length} Documents</div>
      </div>
      <div class="card stat-card">
        <div class="label">Payments Collected</div>
        <div class="value mono" style="color:#2c6b3f;">${fmtMoney(totalCollected)}</div>
        <div class="helper-text" style="margin-top:2px;">Settled Funds</div>
      </div>
      <div class="card stat-card">
        <div class="label">Balance Due</div>
        <div class="value mono" style="color:var(--rust);">${fmtMoney(totalBalanceDue)}</div>
        <div class="helper-text" style="margin-top:2px;">Outstanding Receivables</div>
      </div>
      <div class="card stat-card">
        <div class="label">Overdue Bills</div>
        <div class="value mono" style="color:#b82d18;">${overdueInvoices.length}</div>
        <div class="helper-text" style="margin-top:2px;">${fmtMoney(overdueValue)} past due</div>
      </div>
      <div class="card stat-card">
        <div class="label">Business Expenses</div>
        <div class="value mono" style="color:#b82d18;">${fmtMoney(totalExpenses)}</div>
        <div class="helper-text" style="margin-top:2px;">${allExpenses.length} Logged Receipts</div>
      </div>
      <div class="card stat-card">
        <div class="label">Net Operating Profit</div>
        <div class="value mono ${netProfit >= 0 ? 'profit-positive' : 'profit-negative'}">${fmtMoney(netProfit)}</div>
        <div class="helper-text" style="margin-top:2px;">Collected − Expenses</div>
      </div>
    </div>

    <!-- Visual Analytics: Revenue Trend & Aging Analysis -->
    <div class="analytics-grid">
      <div class="card chart-card">
        <h3>
          <span>Monthly Revenue Trend</span>
          <span class="chart-sub">Last 6 Months (Billed vs Collected)</span>
        </h3>
        <svg viewBox="0 0 460 160" class="svg-chart">
          ${barsSVG}
        </svg>
        <div class="chart-legend">
          <span><span class="legend-dot" style="background:var(--teal);"></span> Billed</span>
          <span><span class="legend-dot" style="background:#2c6b3f;"></span> Collected</span>
        </div>
      </div>

      <div class="card chart-card">
        <h3>
          <span>Receivables Aging</span>
          <span class="chart-sub">Overdue Risk</span>
        </h3>
        <div class="aging-list">
          <div class="aging-item">
            <span class="tag" style="color:#2c6b3f;">Current (Not Due)</span>
            <span class="val">${fmtMoney(agingCurrent)}</span>
          </div>
          <div class="aging-item">
            <span class="tag" style="color:#c47d10;">1 – 30 Days Overdue</span>
            <span class="val">${fmtMoney(aging1to30)}</span>
          </div>
          <div class="aging-item">
            <span class="tag" style="color:#d45b24;">31 – 60 Days Overdue</span>
            <span class="val">${fmtMoney(aging31to60)}</span>
          </div>
          <div class="aging-item">
            <span class="tag" style="color:#b82d18;">60+ Days Overdue</span>
            <span class="val">${fmtMoney(aging60plus)}</span>
          </div>
        </div>
      </div>
    </div>

    <!-- Top Clients & Recent Invoices Grid -->
    <div style="display:grid;grid-template-columns:1fr 2fr;gap:20px;">
      <div class="card" style="padding:22px 24px;">
        <h3 style="font-size:16px;margin:0 0 14px;">Top Clients by Revenue</h3>
        <div>${topClientsHTML}</div>
      </div>

      <div class="card" style="padding:22px 24px;">
        <div class="section-head">
          <h2>Recent Documents</h2>
          <a class="see-all" href="#/history">View all </a>
        </div>
        <table class="ledger-table">
          <thead>
            <tr>
              <th>Doc #</th>
              <th>Customer</th>
              <th>Date</th>
              <th class="num">Amount</th>
              <th class="num">Balance</th>
              <th>Status</th>
            </tr>
          </thead>
          <tbody id="recentBody">${rows}</tbody>
        </table>
      </div>
    </div>
  `;

  document.getElementById('app').innerHTML = appShell('/dashboard', `Welcome, ${escapeHTML(user.name.split(' ')[0])}`, 'Dashboard & Analytics', content);
  mountShellEvents();

  document.querySelectorAll('#recentBody tr[data-id]').forEach(tr=>{
    tr.addEventListener('click', ()=> location.hash = '#/preview?id=' + tr.dataset.id);
  });

  document.getElementById('quickCsvBtn').addEventListener('click', ()=>{
    exportInvoicesToCSV(allInvoices);
  });
}

function rowHTML(inv){
  const symbol = inv.currencySymbol || '₹';
  const effectiveStatus = getInvoiceEffectiveStatus(inv);
  const bal = getInvoiceBalance(inv);
  const overdueDays = getOverdueDays(inv.dueDate);
  const isOverdue = bal > 0 && overdueDays > 0;
  const isEstimate = inv.docType === 'estimate';

  const statusClass = effectiveStatus.toLowerCase().replace(/\s+/g, '-');

  return `<tr data-id="${inv.id}">
    <td class="mono">
      ${escapeHTML(inv.invoiceNumber)}
      ${isEstimate ? '<span class="stamp estimate" style="font-size:10px;padding:2px 5px;margin-left:4px;">EST</span>' : ''}
    </td>
    <td>${escapeHTML(inv.customer ? inv.customer.name : 'Unknown')}</td>
    <td>${fmtDate(inv.invoiceDate)}</td>
    <td class="num">${fmtMoney(inv.grandTotal, symbol)}</td>
    <td class="num ${bal>0?'balance-due-text':''}">${fmtMoney(bal, symbol)}</td>
    <td>
      <span class="stamp ${statusClass}">${effectiveStatus}</span>
      ${isOverdue ? `<span class="stamp overdue" style="font-size:10px;padding:2px 5px;margin-left:3px;">+${overdueDays}d</span>` : ''}
    </td>
  </tr>`;
}

/* ================================================================
   VIEW: CREATE / EDIT INVOICE & ESTIMATE (ADVANCED BUILDER)
   ================================================================ */
let builderItems = [];
let builderEditId = null;
let builderDiscountType = 'pct'; // 'pct' or 'flat'

function blankItem(){
  return {
    id: uid('it'),
    name: '',
    description: '',
    hsn: '',
    qty: 1,
    unit: 'pcs',
    price: 0,
    taxPct: 0
  };
}

function renderCreateInvoice(params){
  const user = currentUser();
  const editId = params.get('id');
  const preCustId = params.get('cust_id');
  const preEntId = params.get('ent_id');
  const requestedType = params.get('type') || 'invoice';

  let invoice = null;
  if(editId){
    invoice = getAll(DB.invoices).find(i => i.id === editId && i.userId === user.id);
  }
  builderEditId = invoice ? invoice.id : null;
  builderItems = (invoice && invoice.items && invoice.items.length)
    ? invoice.items.map(i => ({
        id: i.id || uid('it'),
        name: i.name || '',
        description: i.description || '',
        hsn: i.hsn || '',
        qty: Number(i.qty) || 1,
        unit: i.unit || 'pcs',
        price: Number(i.price) || 0,
        taxPct: Number(i.taxPct) || 0
      }))
    : [blankItem()];

  builderDiscountType = (invoice && invoice.discountType) ? invoice.discountType : 'pct';

  let savedCustomers = getAll(DB.customers).filter(c => c.userId === user.id);
  let savedEnterprises = getAll(DB.enterprises).filter(e => e.userId === user.id);

  const defaultEnt = preEntId
    ? (savedEnterprises.find(e => e.id === preEntId) || savedEnterprises[0])
    : (savedEnterprises.find(e => e.isDefault) || savedEnterprises[0]);

  const preloadedCust = preCustId ? savedCustomers.find(c => c.id === preCustId) : null;

  const seller = invoice ? invoice.seller : {
    name: defaultEnt ? defaultEnt.name : (user.businessName || ''),
    address: defaultEnt ? defaultEnt.address : (user.address || ''),
    email: defaultEnt ? defaultEnt.email : (user.email || ''),
    phone: defaultEnt ? defaultEnt.phone : (user.phone || ''),
    upiId: defaultEnt ? defaultEnt.upiId : (user.upiId || ''),
    taxId: defaultEnt ? defaultEnt.taxId : (user.taxId || ''),
    bankName: defaultEnt ? defaultEnt.bankName : '',
    accountNumber: defaultEnt ? defaultEnt.accountNumber : '',
    ifscCode: defaultEnt ? defaultEnt.ifscCode : '',
    paymentUrl: defaultEnt ? defaultEnt.paymentUrl : '',
    logo: defaultEnt ? (defaultEnt.logo || '') : (user.logo || '')
  };

  const customer = invoice ? invoice.customer : {
    name: preloadedCust ? preloadedCust.name : '',
    address: preloadedCust ? preloadedCust.address : '',
    email: preloadedCust ? preloadedCust.email : '',
    phone: preloadedCust ? preloadedCust.phone : '',
    taxId: preloadedCust ? preloadedCust.taxId : ''
  };

  const docType = invoice ? (invoice.docType || 'invoice') : requestedType;
  const docTemplate = invoice ? (invoice.template || 'classic') : (defaultEnt?.defaultTemplate || 'classic');
  const invoiceNumber = invoice ? invoice.invoiceNumber : nextDocNumber(user.id, docType);
  const invoiceDate = invoice ? invoice.invoiceDate : todayISO();
  const dueDate = invoice ? invoice.dueDate : '';
  const discountVal = invoice ? (invoice.discountVal ?? invoice.discountPct ?? 0) : 0;
  const taxPct = invoice ? (invoice.taxPct || 0) : 0;
  const extraCharges = invoice ? (invoice.extraCharges || 0) : 0;
  const extraChargesLabel = invoice ? (invoice.extraChargesLabel || 'Shipping & Handling') : 'Shipping & Handling';
  const isInterState = invoice ? !!invoice.isInterState : false;
  const isRoundOff = invoice ? (invoice.isRoundOff !== false) : true;
  const notes = invoice ? (invoice.notes || '') : (defaultEnt ? defaultEnt.notes : '');
  const paymentTerms = invoice ? invoice.paymentTerms : (preloadedCust?.terms || 'Due within 15 days of invoice date.');
  const currencySymbol = invoice ? (invoice.currencySymbol || '₹') : (defaultEnt ? (defaultEnt.currencySymbol || '₹') : '₹');
  const signatureData = invoice ? (invoice.signature || user.signature || '') : (user.signature || '');

  function getCustOptionsHtml(selectedId){
    return savedCustomers.map(c =>
      `<option value="${c.id}" ${c.id === selectedId ? 'selected' : ''}>${escapeHTML(c.name)} ${c.contactPerson ? `(${c.contactPerson})` : ''}</option>`
    ).join('');
  }

  function getEntOptionsHtml(selectedId){
    return savedEnterprises.map(e =>
      `<option value="${e.id}" ${(selectedId ? e.id === selectedId : defaultEnt && defaultEnt.id === e.id) ? 'selected' : ''}>${escapeHTML(e.name)} ${e.isDefault ? '[Default]' : ''}</option>`
    ).join('');
  }

  const content = `
    <div id="createMsg" class="form-msg"></div>

    <!-- Document Setup & Template Bar -->
    <div class="card builder-card" style="margin-bottom:20px;padding:18px 24px;">
      <div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:14px;">
        <div style="display:flex;align-items:center;gap:12px;flex-wrap:wrap;">
          <label style="font-weight:700;font-size:13px;text-transform:uppercase;color:var(--ink-soft);">Document Type:</label>
          <select id="doc_type" class="btn btn-ghost" style="padding:6px 12px;font-weight:600;">
            <option value="invoice" ${docType==='invoice'?'selected':''}>Tax Invoice</option>
            <option value="estimate" ${docType==='estimate'?'selected':''}>Quotation / Estimate</option>
            <option value="proforma" ${docType==='proforma'?'selected':''}>Proforma Invoice</option>
          </select>

          <!-- Recurring Retainer Toggle -->
          <label style="display:flex;align-items:center;gap:6px;cursor:pointer;font-size:13px;font-weight:600;margin-left:8px;">
            <input type="checkbox" id="doc_is_recurring" ${invoice?.isRecurring ? 'checked' : ''}>
            Recurring Retainer
          </label>
          <select id="doc_recur_freq" class="btn btn-ghost btn-sm" style="padding:4px 8px;font-size:12px;${invoice?.isRecurring?'':'display:none;'}">
            <option value="Monthly" ${invoice?.recurFreq==='Monthly'?'selected':''}>Monthly</option>
            <option value="Quarterly" ${invoice?.recurFreq==='Quarterly'?'selected':''}>Quarterly</option>
            <option value="Annually" ${invoice?.recurFreq==='Annually'?'selected':''}>Annually</option>
            <option value="Weekly" ${invoice?.recurFreq==='Weekly'?'selected':''}>Weekly</option>
          </select>
        </div>

        <div style="display:flex;align-items:center;gap:12px;flex-wrap:wrap;">
          <!-- Currency Selector -->
          <div style="display:flex;align-items:center;gap:6px;">
            <label style="font-weight:700;font-size:13px;text-transform:uppercase;color:var(--ink-soft);">Currency:</label>
            <select id="doc_currency" class="btn btn-ghost" style="padding:6px 10px;font-weight:600;">
              <option value="INR (₹)" data-sym="₹" ${currencySymbol==='₹'?'selected':''}>INR (₹)</option>
              <option value="USD ($)" data-sym="$" ${currencySymbol==='$'?'selected':''}>USD ($)</option>
              <option value="EUR (€)" data-sym="€" ${currencySymbol==='€'?'selected':''}>EUR (€)</option>
              <option value="GBP (£)" data-sym="£" ${currencySymbol==='£'?'selected':''}>GBP (£)</option>
              <option value="AED (د.إ)" data-sym="د.إ" ${currencySymbol==='د.إ'?'selected':''}>AED (د.إ)</option>
              <option value="CAD ($)" data-sym="CA$" ${currencySymbol==='CA$'?'selected':''}>CAD (CA$)</option>
              <option value="AUD ($)" data-sym="AU$" ${currencySymbol==='AU$'?'selected':''}>AUD (AU$)</option>
            </select>
          </div>

          <label style="font-weight:700;font-size:13px;text-transform:uppercase;color:var(--ink-soft);">Sheet Template:</label>
          <select id="doc_template" class="btn btn-ghost" style="padding:6px 12px;font-weight:600;">
            <option value="classic" ${docTemplate==='classic'?'selected':''}>Classic Brass</option>
            <option value="navy" ${docTemplate==='navy'?'selected':''}>Corporate Navy</option>
            <option value="minimal" ${docTemplate==='minimal'?'selected':''}>Modern Minimalist</option>
            <option value="compact" ${docTemplate==='compact'?'selected':''}>Compact Slip</option>
          </select>
        </div>
      </div>
    </div>

    <div class="builder-grid">
      <!-- Seller / Enterprise Section -->
      <div class="card builder-card">
        <h3>
          <span>Seller / Enterprise Details</span>
          <div class="builder-header-actions">
            <select id="enterpriseSelect" class="autofill-select">
              <option value="">-- Load Profile --</option>
              ${getEntOptionsHtml(defaultEnt?.id)}
            </select>
            <button type="button" class="btn-xs" id="quickAddEntBtn" title="Create new enterprise profile">+ New</button>
            <button type="button" class="btn-xs" id="saveAsEntBtn" title="Save filled details as a reusable Enterprise Profile"> Save Profile</button>
          </div>
        </h3>
        <div class="field"><label>Business / Company Name</label><input id="s_name" value="${escapeHTML(seller.name)}" placeholder="Your Enterprise Name"></div>
        <div class="field"><label>Address</label><input id="s_address" value="${escapeHTML(seller.address)}" placeholder="Street, City, State, ZIP"></div>
        <div class="field-row">
          <div class="field"><label>Email</label><input id="s_email" type="email" value="${escapeHTML(seller.email)}" placeholder="billing@enterprise.com"></div>
          <div class="field"><label>Phone</label><input id="s_phone" value="${escapeHTML(seller.phone)}" placeholder="+91 00000 00000"></div>
        </div>
        <div class="field-row">
          <div class="field"><label>GSTIN / Tax ID</label><input id="s_tax" value="${escapeHTML(seller.taxId || '')}" placeholder="27AAAAA0000A1Z5"></div>
          <div class="field">
            <label>Currency Symbol</label>
            <select id="i_currency">
              <option value="₹" ${currencySymbol==='₹'?'selected':''}>INR (₹)</option>
              <option value="$" ${currencySymbol==='$'?'selected':''}>USD ($)</option>
              <option value="€" ${currencySymbol==='€'?'selected':''}>EUR (€)</option>
              <option value="£" ${currencySymbol==='£'?'selected':''}>GBP (£)</option>
            </select>
          </div>
        </div>
        <div class="field" style="margin-bottom:0;">
          <label>Company Logo</label>
          <div class="logo-upload-wrap">
            <img id="sellerLogoPreview" src="${seller.logo || 'data:image/svg+xml,<svg xmlns=\'http://www.w3.org/2000/svg\' viewBox=\'0 0 100 100\'><rect fill=\'%23eef1ea\' width=\'100\' height=\'100\'/><text x=\'50\' y=\'55\' text-anchor=\'middle\' fill=\'%237c8c85\' font-size=\'12\'>No Logo</text></svg>'}" class="logo-thumb" alt="Logo preview">
            <input type="file" id="sellerLogoInput" accept="image/*" style="font-size:12px;">
            <input type="hidden" id="s_logo" value="${escapeHTML(seller.logo || '')}">
          </div>
        </div>
      </div>

      <!-- Customer Section -->
      <div class="card builder-card">
        <h3>
          <span>Customer Information</span>
          <div class="builder-header-actions">
            <select id="customerSelect" class="autofill-select">
              <option value="">-- Load Saved Customer --</option>
              ${getCustOptionsHtml(preloadedCust?.id)}
            </select>
            <button type="button" class="btn-xs" id="quickAddCustBtn" title="Create new customer profile">+ New</button>
            <button type="button" class="btn-xs" id="saveAsCustBtn" title="Save filled details as a reusable Customer Profile"> Save Profile</button>
          </div>
        </h3>
        <div class="field" id="f-c_name"><label>Customer / Client Name *</label><input id="c_name" value="${escapeHTML(customer.name)}" placeholder="Client or Company Name"><div class="field-error">Customer name is required.</div></div>
        <div class="field"><label>Customer Address</label><input id="c_address" value="${escapeHTML(customer.address)}" placeholder="Street, City, State, ZIP"></div>
        <div class="field-row">
          <div class="field"><label>Customer Email</label><input id="c_email" type="email" value="${escapeHTML(customer.email)}" placeholder="client@company.com"></div>
          <div class="field"><label>Customer Phone (For WhatsApp Share)</label><input id="c_phone" value="${escapeHTML(customer.phone)}" placeholder="+91 00000 00000"></div>
        </div>
        <div class="field" style="margin-bottom:0;"><label>Customer GSTIN / Tax ID</label><input id="c_tax" value="${escapeHTML(customer.taxId || '')}" placeholder="Optional Tax ID"></div>
      </div>
    </div>

    <!-- Document Meta Information -->
    <div class="card builder-card">
      <h3 id="metaTitle">Document Details</h3>
      <div class="field-row">
        <div class="field"><label>Number</label><input id="i_number" class="mono" value="${escapeHTML(invoiceNumber)}"></div>
        <div class="field"><label>Date Issued</label><input id="i_date" type="date" value="${invoiceDate}"></div>
        <div class="field"><label id="dueDateLabel">Due Date / Valid Until</label><input id="i_due" type="date" value="${dueDate}"></div>
      </div>
    </div>

    <!-- Payment QR & Bank Transfer Details -->
    <div class="card builder-card">
      <h3>Payment &amp; Bank Settlement (For QR Code &amp; Bank Details)</h3>
      <div class="field-row">
        <div class="field"><label>UPI ID (Generates Dynamic Payment QR)</label><input id="s_upi" value="${escapeHTML(seller.upiId || '')}" placeholder="yourname@bank"></div>
        <div class="field"><label>Custom Payment Link / URL (Stripe, Razorpay, etc.)</label><input id="s_payurl" value="${escapeHTML(seller.paymentUrl || '')}" placeholder="https://pay.example.com/checkout"></div>
      </div>
      <div class="field-row" style="margin-bottom:0;">
        <div class="field"><label>Bank Name</label><input id="s_bank" value="${escapeHTML(seller.bankName || '')}" placeholder="HDFC Bank"></div>
        <div class="field"><label>Account Number</label><input id="s_acc" class="mono" value="${escapeHTML(seller.accountNumber || '')}" placeholder="502000xxxxxx"></div>
        <div class="field"><label>IFSC / SWIFT Code</label><input id="s_ifsc" class="mono" value="${escapeHTML(seller.ifscCode || '')}" placeholder="HDFC0000123"></div>
      </div>
    </div>

    <!-- Products / Services Line Items -->
    <div class="card builder-card">
      <div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:10px;margin-bottom:8px;">
        <h3 style="margin:0;">Products &amp; Services</h3>
        <div class="quick-catalog-bar" style="margin:0;">
          <span style="font-size:12.5px;font-weight:700;color:var(--teal-dark);">Add from Catalog:</span>
          <select id="catalogPicker" class="btn btn-ghost btn-sm" style="padding:5px 8px;font-size:12.5px;">
            <option value="">-- Choose Item from Inventory / Catalog --</option>
            ${getAll(DB.items).filter(it => it.userId === user.id).map(it => `
              <option value="${it.id}">${escapeHTML(it.name)} (${fmtMoney(it.price, currencySymbol)}) - HSN: ${it.hsn||'N/A'}</option>
            `).join('')}
          </select>
          <a href="#/items" target="_blank" class="btn btn-ghost btn-sm" style="font-size:11.5px;padding:4px 8px;">Manage Catalog</a>
        </div>
      </div>
      <div style="overflow-x:auto;">
        <table class="items-table inv-builder-table" id="itemsTable">
          <thead>
            <tr>
              <th style="min-width:160px;">Item / Title</th>
              <th style="min-width:140px;">Description</th>
              <th class="col-hsn">HSN/SAC</th>
              <th class="col-qty">Qty</th>
              <th class="col-unit">Unit</th>
              <th class="col-price">Unit Price</th>
              <th class="col-tax">Tax %</th>
              <th style="min-width:90px;" class="num">Total</th>
              <th class="col-remove"></th>
            </tr>
          </thead>
          <tbody id="itemsBody"></tbody>
        </table>
      </div>
      <button type="button" class="btn btn-ghost btn-sm" id="addItemBtn" style="margin-top:12px;">+ Add Line Item</button>
    </div>

    <!-- Discount, Tax & Totals Breakdown -->
    <div class="card builder-card">
      <h3>Calculations, Discounts &amp; Taxes</h3>
      <div class="totals-box" style="max-width:520px;">
        <div class="row">
          <span>Subtotal</span>
          <span class="amt" id="t_subtotal">₹0.00</span>
        </div>

        <div class="row" style="align-items:center;">
          <div style="display:flex;align-items:center;gap:6px;">
            <span>Discount</span>
            <div class="toggle-group" id="discountTypeToggle">
              <button type="button" class="toggle-btn ${builderDiscountType==='pct'?'active':''}" data-type="pct">%</button>
              <button type="button" class="toggle-btn ${builderDiscountType==='flat'?'active':''}" data-type="flat">Flat</button>
            </div>
            <input type="number" class="pct-input" id="i_discount" value="${discountVal}" min="0" step="0.1" style="width:75px;">
          </div>
          <span class="amt" id="t_discount">−₹0.00</span>
        </div>

        <div class="row">
          <div style="display:flex;align-items:center;gap:8px;">
            <span>General Tax Rate</span>
            <input type="number" class="pct-input" id="i_tax" value="${taxPct}" min="0" max="100" step="0.1" style="width:65px;">%
          </div>
          <span class="amt" id="t_tax">+₹0.00</span>
        </div>

        <div class="row" style="font-size:12px;color:var(--ink-soft);padding:4px 0;">
          <label style="display:flex;align-items:center;gap:6px;cursor:pointer;">
            <input type="checkbox" id="i_interstate" ${isInterState?'checked':''}>
            Inter-State Supply (IGST instead of CGST + SGST)
          </label>
          <span id="taxSplitLabel" class="mono" style="font-size:11.5px;">Split: CGST 50% / SGST 50%</span>
        </div>

        <div class="row" style="align-items:center;">
          <div style="display:flex;align-items:center;gap:6px;">
            <input id="i_extra_label" value="${escapeHTML(extraChargesLabel)}" placeholder="Charges label" style="padding:4px 8px;font-size:12px;width:160px;border:1px solid var(--line);">
            <input type="number" id="i_extra" value="${extraCharges}" min="0" step="0.01" style="width:75px;padding:4px 8px;font-size:12px;border:1px solid var(--line);">
          </div>
          <span class="amt" id="t_extra">+₹0.00</span>
        </div>

        <div class="row" style="font-size:12px;color:var(--ink-soft);padding:4px 0;">
          <label style="display:flex;align-items:center;gap:6px;cursor:pointer;">
            <input type="checkbox" id="i_roundoff" ${isRoundOff?'checked':''}>
            Auto Round Off Grand Total
          </label>
          <span class="amt" id="t_roundoff">±₹0.00</span>
        </div>

        <div class="row grand">
          <span>Net Payable Amount</span>
          <span class="amt" id="t_grand">₹0.00</span>
        </div>
      </div>
    </div>

    <!-- Digital Signature Box in Builder -->
    <div class="card builder-card">
      <h3>Authorised Signature</h3>
      <p class="helper-text">Draw a signature below, or leave blank to use your default profile signature.</p>
      <div class="builder-sig-box">
        <canvas id="builderSigPad" class="builder-sig-canvas" width="360" height="120"></canvas>
        <div>
          <button type="button" class="btn btn-ghost btn-sm" id="clearBuilderSigBtn">Clear Canvas</button>
          ${user.signature ? `<button type="button" class="btn btn-ghost btn-sm" id="loadUserSigBtn" style="margin-left:6px;">Load Profile Signature</button>` : ''}
        </div>
      </div>
    </div>

    <!-- Terms & Notes -->
    <div class="card builder-card">
      <h3>Payment Terms &amp; Notes</h3>
      <div class="field"><label>Payment Terms / Validity</label><textarea id="i_terms" rows="2">${escapeHTML(paymentTerms)}</textarea></div>
      <div class="field" style="margin-bottom:0;"><label>Notes / Client Remarks</label><textarea id="i_notes" rows="2" placeholder="Thank you for your business.">${escapeHTML(notes)}</textarea></div>
    </div>

    <div class="form-actions">
      <a href="#/dashboard" class="btn btn-ghost">Cancel</a>
      <button type="button" class="btn btn-ghost" id="previewBtn">Save Draft &amp; Preview</button>
      <button type="button" class="btn btn-primary" id="generateBtn">${docType==='estimate'?'Generate Quotation':'Generate Invoice'}</button>
    </div>

    <!-- Quick Add Customer Modal -->
    <div class="modal-overlay" id="quickCustModal">
      <div class="modal-card">
        <div class="modal-head">
          <h2>Quick Add Customer</h2>
          <button class="modal-close" id="closeQuickCustModal">&times;</button>
        </div>
        <form id="quickCustForm">
          <div class="field"><label>Customer / Company Name *</label><input id="qc_name" required placeholder="Acme Inc."></div>
          <div class="field"><label>Contact Person</label><input id="qc_contact" placeholder="Jane Doe"></div>
          <div class="field-row">
            <div class="field"><label>Email</label><input id="qc_email" type="email" placeholder="billing@acme.com"></div>
            <div class="field"><label>Phone</label><input id="qc_phone" placeholder="+91 98765 43210"></div>
          </div>
          <div class="field"><label>Address</label><input id="qc_address" placeholder="123 Business Way, City, State"></div>
          <div class="field-row">
            <div class="field"><label>GSTIN / Tax ID</label><input id="qc_tax" placeholder="27AAAAA0000A1Z5"></div>
            <div class="field"><label>Default Terms</label><input id="qc_terms" placeholder="Net 15 Days"></div>
          </div>
          <div class="form-actions" style="margin-top:20px;">
            <button type="button" class="btn btn-ghost" id="cancelQuickCustModal">Cancel</button>
            <button type="submit" class="btn btn-primary">Save &amp; Use Customer</button>
          </div>
        </form>
      </div>
    </div>

    <!-- Quick Add Enterprise Modal -->
    <div class="modal-overlay" id="quickEntModal">
      <div class="modal-card">
        <div class="modal-head">
          <h2>Quick Add Enterprise Profile</h2>
          <button class="modal-close" id="closeQuickEntModal">&times;</button>
        </div>
        <form id="quickEntForm">
          <div class="field"><label>Enterprise / Business Name *</label><input id="qe_name" required placeholder="Ledgerly Tech Ltd"></div>
          <div class="field"><label>Tagline / Description</label><input id="qe_tagline" placeholder="Enterprise Financial Solutions"></div>
          <div class="field-row">
            <div class="field"><label>Business Email</label><input id="qe_email" type="email" placeholder="billing@ledgerly.com"></div>
            <div class="field"><label>Business Phone</label><input id="qe_phone" placeholder="+91 98765 43210"></div>
          </div>
          <div class="field"><label>Business Address</label><input id="qe_address" placeholder="100 Executive Tower, Mumbai"></div>
          <div class="field-row">
            <div class="field"><label>GSTIN / Tax ID</label><input id="qe_tax" placeholder="27AAAAA0000A1Z5"></div>
            <div class="field">
              <label>Currency</label>
              <select id="qe_currency">
                <option value="INR (₹)">INR (₹)</option>
                <option value="USD ($)">USD ($)</option>
                <option value="EUR (€)">EUR (€)</option>
                <option value="GBP (£)">GBP (£)</option>
              </select>
            </div>
          </div>
          <div class="field-row">
            <div class="field"><label>UPI ID (For QR)</label><input id="qe_upi" placeholder="ledgerly@icici"></div>
            <div class="field"><label>Custom Payment URL</label><input id="qe_payurl" placeholder="https://pay.ledgerly.com"></div>
          </div>
          <div class="field-row">
            <div class="field"><label>Bank Name</label><input id="qe_bank" placeholder="HDFC Bank"></div>
            <div class="field"><label>Account Number</label><input id="qe_acc" class="mono" placeholder="502000xxxxxx"></div>
            <div class="field"><label>IFSC Code</label><input id="qe_ifsc" class="mono" placeholder="HDFC0000123"></div>
          </div>
          <div class="form-actions" style="margin-top:20px;">
            <button type="button" class="btn btn-ghost" id="cancelQuickEntModal">Cancel</button>
            <button type="submit" class="btn btn-primary">Save &amp; Use Profile</button>
          </div>
        </form>
      </div>
    </div>
  `;

  document.getElementById('app').innerHTML = appShell(
    invoice ? '/history' : '/create',
    invoice ? (docType==='estimate'?'Edit Quotation':'Edit Invoice') : (docType==='estimate'?'New Quotation':'New Invoice'),
    'Builder',
    content
  );
  mountShellEvents();

  // Signature Pad in Builder
  const bCanvas = document.getElementById('builderSigPad');
  const bPad = initSignaturePad(bCanvas, signatureData);

  document.getElementById('clearBuilderSigBtn').addEventListener('click', ()=> bPad.clear());
  const loadUserBtn = document.getElementById('loadUserSigBtn');
  if(loadUserBtn){
    loadUserBtn.addEventListener('click', ()=>{
      if(user.signature){
        bPad.clear();
        const img = new Image();
        img.onload = ()=> bCanvas.getContext('2d').drawImage(img, 0, 0, bCanvas.width, bCanvas.height);
        img.src = user.signature;
        showToast('Default profile signature loaded.');
      }
    });
  }

  // Logo file upload handler
  const logoInput = document.getElementById('sellerLogoInput');
  const logoPreview = document.getElementById('sellerLogoPreview');
  const logoHidden = document.getElementById('s_logo');
  if(logoInput){
    logoInput.addEventListener('change', (e)=>{
      const file = e.target.files[0];
      if(file){
        const reader = new FileReader();
        reader.onload = (evt)=>{
          logoPreview.src = evt.target.result;
          logoHidden.value = evt.target.result;
          showToast('Company logo loaded.');
        };
        reader.readAsDataURL(file);
      }
    });
  }

  // Autofill from Enterprise Select
  document.getElementById('enterpriseSelect').addEventListener('change', (e)=>{
    const ent = savedEnterprises.find(item => item.id === e.target.value);
    if(ent){
      document.getElementById('s_name').value = ent.name || '';
      document.getElementById('s_address').value = ent.address || '';
      document.getElementById('s_email').value = ent.email || '';
      document.getElementById('s_phone').value = ent.phone || '';
      document.getElementById('s_tax').value = ent.taxId || '';
      document.getElementById('s_upi').value = ent.upiId || '';
      document.getElementById('s_payurl').value = ent.paymentUrl || '';
      document.getElementById('s_bank').value = ent.bankName || '';
      document.getElementById('s_acc').value = ent.accountNumber || '';
      document.getElementById('s_ifsc').value = ent.ifscCode || '';
      if(ent.currencySymbol) document.getElementById('i_currency').value = ent.currencySymbol;
      if(ent.notes && !document.getElementById('i_notes').value) document.getElementById('i_notes').value = ent.notes;
      if(ent.logo){
        logoPreview.src = ent.logo;
        logoHidden.value = ent.logo;
      }
      if(ent.defaultTemplate){
        document.getElementById('doc_template').value = ent.defaultTemplate;
      }
      showToast('Loaded enterprise profile: ' + ent.name);
      recalcTotals();
    }
  });

  // Autofill from Customer Select
  document.getElementById('customerSelect').addEventListener('change', (e)=>{
    const cust = savedCustomers.find(item => item.id === e.target.value);
    if(cust){
      document.getElementById('c_name').value = cust.name || '';
      document.getElementById('c_address').value = cust.address || '';
      document.getElementById('c_email').value = cust.email || '';
      document.getElementById('c_phone').value = cust.phone || '';
      document.getElementById('c_tax').value = cust.taxId || '';
      if(cust.terms) document.getElementById('i_terms').value = cust.terms;
      showToast('Loaded customer: ' + cust.name);
    }
  });

  // Discount Type Switcher Toggle
  document.querySelectorAll('#discountTypeToggle .toggle-btn').forEach(btn => {
    btn.addEventListener('click', ()=>{
      document.querySelectorAll('#discountTypeToggle .toggle-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      builderDiscountType = btn.dataset.type;
      recalcTotals();
    });
  });

  // Inter-state tax checkbox event
  document.getElementById('i_interstate').addEventListener('change', (e)=>{
    const label = document.getElementById('taxSplitLabel');
    label.textContent = e.target.checked ? 'Applied: IGST (100%)' : 'Split: CGST 50% / SGST 50%';
    recalcTotals();
  });

  // Document Type Change
  document.getElementById('doc_type').addEventListener('change', (e)=>{
    const t = e.target.value;
    const genBtn = document.getElementById('generateBtn');
    genBtn.textContent = (t === 'estimate') ? 'Generate Quotation' : 'Generate Invoice';
    document.getElementById('i_number').value = nextDocNumber(user.id, t);
    recalcTotals();
  });

  // Save as Customer quick action
  document.getElementById('saveAsCustBtn').addEventListener('click', ()=>{
    const name = document.getElementById('c_name').value.trim();
    if(!name){ showToast('Enter a customer name first.'); return; }
    let allCusts = getAll(DB.customers);
    const newCust = {
      id: uid('cust'),
      userId: user.id,
      name,
      contactPerson: '',
      email: document.getElementById('c_email').value.trim(),
      phone: document.getElementById('c_phone').value.trim(),
      address: document.getElementById('c_address').value.trim(),
      taxId: document.getElementById('c_tax').value.trim(),
      terms: document.getElementById('i_terms').value.trim()
    };
    allCusts.push(newCust);
    setAll(DB.customers, allCusts);
    savedCustomers = allCusts.filter(c => c.userId === user.id);
    document.getElementById('customerSelect').innerHTML = '<option value="">-- Load Saved Customer --</option>' + getCustOptionsHtml(newCust.id);
    showToast('Customer profile saved to directory.');
  });

  // Save as Enterprise quick action
  document.getElementById('saveAsEntBtn').addEventListener('click', ()=>{
    const name = document.getElementById('s_name').value.trim();
    if(!name){ showToast('Enter an enterprise name first.'); return; }
    let allEnts = getAll(DB.enterprises);
    const currSym = document.getElementById('i_currency').value;
    const newEnt = {
      id: uid('ent'),
      userId: user.id,
      isDefault: false,
      name,
      tagline: '',
      email: document.getElementById('s_email').value.trim(),
      phone: document.getElementById('s_phone').value.trim(),
      address: document.getElementById('s_address').value.trim(),
      taxId: document.getElementById('s_tax').value.trim(),
      currency: currSym === '₹' ? 'INR (₹)' : currSym === '$' ? 'USD ($)' : 'EUR (€)',
      currencySymbol: currSym,
      upiId: document.getElementById('s_upi').value.trim(),
      paymentUrl: document.getElementById('s_payurl').value.trim(),
      bankName: document.getElementById('s_bank').value.trim(),
      accountNumber: document.getElementById('s_acc').value.trim(),
      ifscCode: document.getElementById('s_ifsc').value.trim(),
      notes: document.getElementById('i_notes').value.trim(),
      defaultTemplate: document.getElementById('doc_template').value,
      logo: logoHidden.value
    };
    allEnts.push(newEnt);
    setAll(DB.enterprises, allEnts);
    savedEnterprises = allEnts.filter(e => e.userId === user.id);
    document.getElementById('enterpriseSelect').innerHTML = '<option value="">-- Load Profile --</option>' + getEntOptionsHtml(newEnt.id);
    showToast('Enterprise profile saved to directory.');
  });

  // Quick Customer Modal
  const quickCustModal = document.getElementById('quickCustModal');
  document.getElementById('quickAddCustBtn').addEventListener('click', ()=> quickCustModal.classList.add('show'));
  document.getElementById('closeQuickCustModal').addEventListener('click', ()=> quickCustModal.classList.remove('show'));
  document.getElementById('cancelQuickCustModal').addEventListener('click', ()=> quickCustModal.classList.remove('show'));

  document.getElementById('quickCustForm').addEventListener('submit', (e)=>{
    e.preventDefault();
    const newCust = {
      id: uid('cust'),
      userId: user.id,
      name: document.getElementById('qc_name').value.trim(),
      contactPerson: document.getElementById('qc_contact').value.trim(),
      email: document.getElementById('qc_email').value.trim(),
      phone: document.getElementById('qc_phone').value.trim(),
      address: document.getElementById('qc_address').value.trim(),
      taxId: document.getElementById('qc_tax').value.trim(),
      terms: document.getElementById('qc_terms').value.trim()
    };
    let allCusts = getAll(DB.customers);
    allCusts.push(newCust);
    setAll(DB.customers, allCusts);
    savedCustomers = allCusts.filter(c => c.userId === user.id);
    document.getElementById('customerSelect').innerHTML = '<option value="">-- Load Saved Customer --</option>' + getCustOptionsHtml(newCust.id);

    document.getElementById('c_name').value = newCust.name;
    document.getElementById('c_address').value = newCust.address;
    document.getElementById('c_email').value = newCust.email;
    document.getElementById('c_phone').value = newCust.phone;
    document.getElementById('c_tax').value = newCust.taxId;
    if(newCust.terms) document.getElementById('i_terms').value = newCust.terms;

    quickCustModal.classList.remove('show');
    showToast('Customer created & applied.');
  });

  // Quick Enterprise Modal
  const quickEntModal = document.getElementById('quickEntModal');
  document.getElementById('quickAddEntBtn').addEventListener('click', ()=> quickEntModal.classList.add('show'));
  document.getElementById('closeQuickEntModal').addEventListener('click', ()=> quickEntModal.classList.remove('show'));
  document.getElementById('cancelQuickEntModal').addEventListener('click', ()=> quickEntModal.classList.remove('show'));

  document.getElementById('quickEntForm').addEventListener('submit', (e)=>{
    e.preventDefault();
    const currVal = document.getElementById('qe_currency').value;
    const symMatch = currVal.match(/\((.*?)\)/);
    const newEnt = {
      id: uid('ent'),
      userId: user.id,
      name: document.getElementById('qe_name').value.trim(),
      tagline: document.getElementById('qe_tagline').value.trim(),
      email: document.getElementById('qe_email').value.trim(),
      phone: document.getElementById('qe_phone').value.trim(),
      address: document.getElementById('qe_address').value.trim(),
      taxId: document.getElementById('qe_tax').value.trim(),
      currency: currVal,
      currencySymbol: symMatch ? symMatch[1] : '₹',
      upiId: document.getElementById('qe_upi').value.trim(),
      paymentUrl: document.getElementById('qe_payurl').value.trim(),
      bankName: document.getElementById('qe_bank').value.trim(),
      accountNumber: document.getElementById('qe_acc').value.trim(),
      ifscCode: document.getElementById('qe_ifsc').value.trim(),
      isDefault: false,
      logo: ''
    };
    let allEnts = getAll(DB.enterprises);
    allEnts.push(newEnt);
    setAll(DB.enterprises, allEnts);
    savedEnterprises = allEnts.filter(e => e.userId === user.id);
    document.getElementById('enterpriseSelect').innerHTML = '<option value="">-- Load Profile --</option>' + getEntOptionsHtml(newEnt.id);

    document.getElementById('s_name').value = newEnt.name;
    document.getElementById('s_address').value = newEnt.address;
    document.getElementById('s_email').value = newEnt.email;
    document.getElementById('s_phone').value = newEnt.phone;
    document.getElementById('s_tax').value = newEnt.taxId;
    document.getElementById('s_upi').value = newEnt.upiId;
    document.getElementById('s_payurl').value = newEnt.paymentUrl;
    document.getElementById('s_bank').value = newEnt.bankName;
    document.getElementById('s_acc').value = newEnt.accountNumber;
    document.getElementById('s_ifsc').value = newEnt.ifscCode;
    document.getElementById('i_currency').value = newEnt.currencySymbol;

    quickEntModal.classList.remove('show');
    showToast('Enterprise profile created & applied.');
    recalcTotals();
  });

  // Line Items & Totals Listeners
  document.getElementById('addItemBtn').addEventListener('click', ()=>{
    builderItems.push(blankItem());
    renderItemsBody();
    recalcTotals();
  });

  // Quick Catalog Picker: Autofill into line items
  const catalogPicker = document.getElementById('catalogPicker');
  if(catalogPicker){
    catalogPicker.addEventListener('change', (e)=>{
      const itemId = e.target.value;
      if(!itemId) return;
      const catItems = getAll(DB.items).filter(it => it.userId === user.id);
      const chosen = catItems.find(it => it.id === itemId);
      if(chosen){
        builderItems.push({
          id: uid('item'),
          name: chosen.name,
          description: chosen.desc || '',
          hsn: chosen.hsn || '',
          qty: 1,
          unit: chosen.unit || 'pcs',
          price: Number(chosen.price) || 0,
          taxPct: chosen.taxRate !== undefined ? Number(chosen.taxRate) : (Number(defaultEnt?.defaultTaxRate) || 18)
        });
        renderItemsBody();
        recalcTotals();
        showToast(`Added '${chosen.name}' from catalog.`);
        e.target.value = '';
      }
    });
  }

  // Currency select change updates symbol throughout builder
  const currencySelect = document.getElementById('doc_currency');
  if(currencySelect){
    currencySelect.addEventListener('change', (e)=>{
      const selOpt = e.target.options[e.target.selectedIndex];
      const newSym = selOpt.getAttribute('data-sym') || '₹';
      const curInp = document.getElementById('i_currency');
      if(curInp) curInp.value = newSym;
      renderItemsBody();
      recalcTotals();
      showToast('Currency set to ' + e.target.value);
    });
  }

  // Recurring Retainer toggle
  const recurCheck = document.getElementById('doc_is_recurring');
  const recurFreqSelect = document.getElementById('doc_recur_freq');
  if(recurCheck && recurFreqSelect){
    recurCheck.addEventListener('change', (e)=>{
      recurFreqSelect.style.display = e.target.checked ? 'inline-block' : 'none';
    });
  }

  document.getElementById('i_discount').addEventListener('input', recalcTotals);
  document.getElementById('i_tax').addEventListener('input', recalcTotals);
  document.getElementById('i_extra').addEventListener('input', recalcTotals);
  document.getElementById('i_roundoff').addEventListener('change', recalcTotals);
  document.getElementById('i_currency').addEventListener('change', ()=>{
    renderItemsBody();
    recalcTotals();
  });

  document.getElementById('previewBtn').addEventListener('click', ()=> handleSave('Draft', true, bPad));
  document.getElementById('generateBtn').addEventListener('click', ()=> handleSave('Generated', true, bPad));

  renderItemsBody();
  recalcTotals();
}

function renderItemsBody(){
  const sym = document.getElementById('i_currency') ? document.getElementById('i_currency').value : '₹';
  const body = document.getElementById('itemsBody');
  if(!body) return;

  const units = ['pcs','hrs','days','kg','sq ft','units','service','m','sets'];

  body.innerHTML = builderItems.map((item, idx) => `
    <tr data-idx="${idx}">
      <td><input class="it-name" value="${escapeHTML(item.name)}" placeholder="Title / Service name"></td>
      <td><input class="it-desc" value="${escapeHTML(item.description)}" placeholder="Details (optional)"></td>
      <td><input class="it-hsn mono" value="${escapeHTML(item.hsn || '')}" placeholder="HSN/SAC" style="width:75px;"></td>
      <td><input class="it-qty mono" type="number" min="0" step="1" value="${item.qty}" style="width:60px;"></td>
      <td>
        <select class="it-unit" style="padding:4px;font-size:12px;width:75px;">
          ${units.map(u => `<option value="${u}" ${item.unit===u?'selected':''}>${u}</option>`).join('')}
        </select>
      </td>
      <td><input class="it-price mono" type="number" min="0" step="0.01" value="${item.price}" style="width:85px;"></td>
      <td><input class="it-tax mono" type="number" min="0" max="100" step="0.1" value="${item.taxPct || 0}" placeholder="0%" style="width:55px;"></td>
      <td class="item-total mono num" id="itemTotal-${item.id}">${fmtMoney(item.qty * item.price, sym)}</td>
      <td class="col-remove"><button type="button" class="remove-item" title="Remove row" data-idx="${idx}">&times;</button></td>
    </tr>
  `).join('');

  body.querySelectorAll('tr').forEach(tr=>{
    const idx = Number(tr.dataset.idx);
    tr.querySelector('.it-name').addEventListener('input', e => { builderItems[idx].name = e.target.value; });
    tr.querySelector('.it-desc').addEventListener('input', e => { builderItems[idx].description = e.target.value; });
    tr.querySelector('.it-hsn').addEventListener('input', e => { builderItems[idx].hsn = e.target.value; });
    tr.querySelector('.it-unit').addEventListener('change', e => { builderItems[idx].unit = e.target.value; });
    tr.querySelector('.it-tax').addEventListener('input', e => { builderItems[idx].taxPct = Number(e.target.value) || 0; recalcTotals(); });
    tr.querySelector('.it-qty').addEventListener('input', e => {
      builderItems[idx].qty = Number(e.target.value) || 0;
      updateItemRow(idx);
    });
    tr.querySelector('.it-price').addEventListener('input', e => {
      builderItems[idx].price = Number(e.target.value) || 0;
      updateItemRow(idx);
    });
  });

  body.querySelectorAll('.remove-item').forEach(btn=>{
    btn.addEventListener('click', ()=>{
      if(builderItems.length === 1){ showToast('An invoice needs at least one line item.'); return; }
      const idx = Number(btn.dataset.idx);
      builderItems.splice(idx, 1);
      renderItemsBody();
      recalcTotals();
    });
  });
}

function updateItemRow(idx){
  const sym = document.getElementById('i_currency') ? document.getElementById('i_currency').value : '₹';
  const item = builderItems[idx];
  const cell = document.getElementById('itemTotal-' + item.id);
  if(cell) cell.textContent = fmtMoney(item.qty * item.price, sym);
  recalcTotals();
}

function recalcTotals(){
  const sym = document.getElementById('i_currency') ? document.getElementById('i_currency').value : '₹';
  const discountVal = Number(document.getElementById('i_discount')?.value) || 0;
  const taxPct = Number(document.getElementById('i_tax')?.value) || 0;
  const extraCharges = Number(document.getElementById('i_extra')?.value) || 0;
  const isInterState = !!document.getElementById('i_interstate')?.checked;
  const isRoundOff = !!document.getElementById('i_roundoff')?.checked;

  const res = computeTotals(builderItems, discountVal, taxPct, builderDiscountType, extraCharges, isInterState, isRoundOff);

  const tSub = document.getElementById('t_subtotal');
  const tDisc = document.getElementById('t_discount');
  const tTax = document.getElementById('t_tax');
  const tExtra = document.getElementById('t_extra');
  const tRound = document.getElementById('t_roundoff');
  const tGrand = document.getElementById('t_grand');

  if(tSub) tSub.textContent = fmtMoney(res.subtotal, sym);
  if(tDisc) tDisc.textContent = '−' + fmtMoney(res.discount, sym);
  if(tTax) tTax.textContent = '+' + fmtMoney(res.tax, sym);
  if(tExtra) tExtra.textContent = '+' + fmtMoney(res.extraCharges, sym);
  if(tRound) tRound.textContent = (res.roundOff >= 0 ? '+' : '−') + fmtMoney(Math.abs(res.roundOff), sym);
  if(tGrand) tGrand.textContent = fmtMoney(res.grandTotal, sym);
}

function nextDocNumber(userId, docType = 'invoice'){
  const count = getAll(DB.invoices).filter(i => i.userId === userId).length;
  const year = new Date().getFullYear();
  const prefix = (docType === 'estimate') ? 'EST' : (docType === 'proforma') ? 'PRO' : 'INV';
  return `${prefix}-${year}-${String(count+1).padStart(3,'0')}`;
}

function handleSave(status, goToPreview, bPad){
  const msg = document.getElementById('createMsg');
  msg.className = 'form-msg';

  const cNameField = document.getElementById('f-c_name');
  cNameField.classList.remove('has-error');
  const customerName = document.getElementById('c_name').value.trim();

  const cleanItems = builderItems
    .map(i => ({
      ...i,
      name: i.name.trim(),
      description: i.description ? i.description.trim() : '',
      hsn: i.hsn ? i.hsn.trim() : ''
    }))
    .filter(i => i.name || i.qty || i.price);

  let valid = true;
  if(!customerName){ cNameField.classList.add('has-error'); valid = false; }
  if(cleanItems.length === 0){
    msg.textContent = 'Add at least one product or service with a name.';
    msg.className = 'form-msg error show';
    valid = false;
  }
  const hasInvalidQtyPrice = cleanItems.some(i => Number(i.qty) < 0 || Number(i.price) < 0 || isNaN(i.qty) || isNaN(i.price));
  if(hasInvalidQtyPrice){
    msg.textContent = 'Quantity and price must be valid, non-negative numbers.';
    msg.className = 'form-msg error show';
    valid = false;
  }
  if(!valid){
    if(!msg.textContent){ msg.textContent = 'Please fix the highlighted fields before continuing.'; msg.className = 'form-msg error show'; }
    return;
  }

  const user = currentUser();
  const docType = document.getElementById('doc_type').value;
  const template = document.getElementById('doc_template').value;
  const discountVal = Number(document.getElementById('i_discount').value) || 0;
  const taxPct = Number(document.getElementById('i_tax').value) || 0;
  const extraCharges = Number(document.getElementById('i_extra').value) || 0;
  const extraChargesLabel = document.getElementById('i_extra_label').value.trim() || 'Shipping & Handling';
  const isInterState = document.getElementById('i_interstate').checked;
  const isRoundOff = document.getElementById('i_roundoff').checked;
  const currencySymbol = document.getElementById('i_currency').value;

  const totals = computeTotals(cleanItems, discountVal, taxPct, builderDiscountType, extraCharges, isInterState, isRoundOff);

  const invoices = getAll(DB.invoices);
  const existingIdx = builderEditId ? invoices.findIndex(i => i.id === builderEditId) : -1;
  const existingInv = existingIdx >= 0 ? invoices[existingIdx] : null;

  const invoiceSignature = (bPad && !bPad.isEmpty())
    ? bPad.toDataURL()
    : (user.signature || (existingInv ? existingInv.signature : '') || '');

  const invoiceData = {
    id: builderEditId || uid('inv'),
    userId: user.id,
    docType,
    template,
    currencySymbol,
    isRecurring: document.getElementById('doc_is_recurring')?.checked || false,
    recurFreq: document.getElementById('doc_recur_freq')?.value || 'Monthly',
    invoiceNumber: document.getElementById('i_number').value.trim() || nextDocNumber(user.id, docType),
    invoiceDate: document.getElementById('i_date').value || todayISO(),
    dueDate: document.getElementById('i_due').value || '',
    seller: {
      name: document.getElementById('s_name').value.trim(),
      address: document.getElementById('s_address').value.trim(),
      email: document.getElementById('s_email').value.trim(),
      phone: document.getElementById('s_phone').value.trim(),
      taxId: document.getElementById('s_tax').value.trim(),
      upiId: document.getElementById('s_upi').value.trim(),
      paymentUrl: document.getElementById('s_payurl').value.trim(),
      bankName: document.getElementById('s_bank').value.trim(),
      accountNumber: document.getElementById('s_acc').value.trim(),
      ifscCode: document.getElementById('s_ifsc').value.trim(),
      logo: document.getElementById('s_logo').value || (existingInv?.seller?.logo || '')
    },
    customer: {
      name: customerName,
      address: document.getElementById('c_address').value.trim(),
      email: document.getElementById('c_email').value.trim(),
      phone: document.getElementById('c_phone').value.trim(),
      taxId: document.getElementById('c_tax').value.trim(),
    },
    items: cleanItems,
    discountType: builderDiscountType,
    discountVal,
    discountPct: builderDiscountType === 'pct' ? discountVal : 0,
    taxPct,
    extraCharges,
    extraChargesLabel,
    isInterState,
    isRoundOff,
    subtotal: totals.subtotal,
    discount: totals.discount,
    tax: totals.tax,
    cgst: totals.cgst,
    sgst: totals.sgst,
    igst: totals.igst,
    roundOff: totals.roundOff,
    grandTotal: totals.grandTotal,
    paymentTerms: document.getElementById('i_terms').value.trim(),
    notes: document.getElementById('i_notes').value.trim(),
    status: existingInv ? existingInv.status : status,
    payments: existingInv ? (existingInv.payments || []) : [],
    paidAt: existingInv ? existingInv.paidAt : null,
    paymentMethod: existingInv ? existingInv.paymentMethod : '',
    transactionRef: existingInv ? existingInv.transactionRef : '',
    paidMessage: existingInv ? existingInv.paidMessage : '',
    createdAt: existingInv ? existingInv.createdAt : Date.now(),
    signature: invoiceSignature
  };

  if(existingIdx >= 0){ invoices[existingIdx] = invoiceData; } else { invoices.push(invoiceData); }
  setAll(DB.invoices, invoices);
  showToast((docType==='estimate' ? 'Quotation ' : 'Invoice ') + (status === 'Generated' ? 'generated.' : 'saved.'));
  if(goToPreview){ location.hash = '#/preview?id=' + invoiceData.id; }
}

/* ================================================================
   VIEW: PREVIEW & EXPORT (TEMPLATES, PARTIAL PAYMENTS, PDF, WHATSAPP)
   ================================================================ */
function renderPreview(params){
  const user = currentUser();
  const id = params.get('id');
  let invoices = getAll(DB.invoices);
  let invoice = invoices.find(i => i.id === id && i.userId === user.id);

  if(!invoice){
    document.getElementById('app').innerHTML = appShell('/history', 'Document Not Found', 'Preview',
      `<p>We couldn't find that document. It may have been deleted.</p><a class="btn btn-primary" href="#/history">Back to invoices</a>`);
    mountShellEvents();
    return;
  }

  const sym = invoice.currencySymbol || '₹';
  const docType = invoice.docType || 'invoice';
  const template = invoice.template || 'classic';
  const effectiveStatus = getInvoiceEffectiveStatus(invoice);
  const isPaid = (effectiveStatus === 'Paid');
  const isPartiallyPaid = (effectiveStatus === 'Partially Paid');
  const isEstimate = (docType === 'estimate');

  const paidTotal = getInvoicePaidTotal(invoice);
  const balanceDue = getInvoiceBalance(invoice);
  const overdueDays = getOverdueDays(invoice.dueDate);
  const isOverdue = balanceDue > 0 && overdueDays > 0;
  const paymentsList = getInvoicePayments(invoice);

  // Line items rows
  const itemsRows = invoice.items.map(it => `
    <tr>
      <td class="desc-cell">
        <strong>${escapeHTML(it.name)}</strong>
        ${it.description ? `<div class="item-desc">${escapeHTML(it.description)}</div>` : ''}
      </td>
      <td class="mono col-hsn">${escapeHTML(it.hsn || '—')}</td>
      <td class="num mono">${it.qty} <span style="font-size:11px;color:var(--ink-faint);">${escapeHTML(it.unit || '')}</span></td>
      <td class="num mono">${fmtMoney(it.price, sym)}</td>
      <td class="num mono col-tax">${it.taxPct ? it.taxPct + '%' : '—'}</td>
      <td class="num mono">${fmtMoney(it.qty * it.price, sym)}</td>
    </tr>`).join('');

  // Status dropdown options
  const statusList = isEstimate
    ? ['Draft', 'Sent', 'Accepted', 'Declined']
    : ['Draft', 'Generated', 'Pending', 'Partially Paid', 'Paid'];

  const statusOptions = statusList.map(s =>
    `<option value="${s}" ${effectiveStatus === s ? 'selected' : ''}>${s}</option>`).join('');

  const qrTarget = getPaymentQrTarget(invoice);
  const isCustomUrl = !!(invoice.seller && invoice.seller.paymentUrl);

  // Banner: Paid Settled Receipt
  const paidBannerHTML = isPaid ? `
    <div class="paid-receipt-banner">
      <div class="banner-head">
        <div class="banner-title">
          <span style="font-size:18px;"></span> Payment Received &amp; Settled
        </div>
        <div class="banner-badge">OFFICIAL RECEIPT</div>
      </div>
      <div class="banner-msg">
        "${escapeHTML(invoice.paidMessage || 'Payment received with thanks. This invoice is officially settled in full.')}"
      </div>
      <div class="banner-meta">
        <div class="meta-col">
          <div class="lbl">Amount Settled</div>
          <div class="val">${fmtMoney(invoice.grandTotal, sym)}</div>
        </div>
        <div class="meta-col">
          <div class="lbl">Settlement Date</div>
          <div class="val">${fmtDate(invoice.paidAt || invoice.invoiceDate)}</div>
        </div>
        <div class="meta-col">
          <div class="lbl">Payment Method</div>
          <div class="val">${escapeHTML(invoice.paymentMethod || 'Direct Payment')}</div>
        </div>
        ${invoice.transactionRef ? `
        <div class="meta-col">
          <div class="lbl">Transaction / UTR Ref</div>
          <div class="val">${escapeHTML(invoice.transactionRef)}</div>
        </div>` : ''}
      </div>
    </div>` : '';

  // Banner: Partial Payment Received
  const partialBannerHTML = isPartiallyPaid ? `
    <div class="partial-payment-banner">
      <div class="banner-head">
        <div class="banner-title">
          <span></span> Partial Payment Received
        </div>
        <div class="banner-badge">PARTIALLY PAID</div>
      </div>
      <div class="banner-meta">
        <div class="meta-col">
          <div class="lbl">Total Invoice</div>
          <div class="val">${fmtMoney(invoice.grandTotal, sym)}</div>
        </div>
        <div class="meta-col">
          <div class="lbl">Amount Settled</div>
          <div class="val" style="color:#2c6b3f;">${fmtMoney(paidTotal, sym)}</div>
        </div>
        <div class="meta-col">
          <div class="lbl">Remaining Balance Due</div>
          <div class="val balance-due-text">${fmtMoney(balanceDue, sym)}</div>
        </div>
        <div class="meta-col">
          <div class="lbl">Due Date</div>
          <div class="val">${fmtDate(invoice.dueDate)}</div>
        </div>
      </div>
    </div>` : '';

  // Payment Installment Ledger Table on preview
  const paymentLedgerHTML = paymentsList.length > 0 ? `
    <div class="sheet-ledger">
      <div class="sheet-ledger-head">Payment Settlement Ledger</div>
      <table>
        <thead>
          <tr>
            <th>Date</th>
            <th>Method</th>
            <th>Ref / UTR</th>
            <th>Notes</th>
            <th class="num">Amount Settled</th>
          </tr>
        </thead>
        <tbody>
          ${paymentsList.map(p => `
            <tr>
              <td>${fmtDate(p.date)}</td>
              <td>${escapeHTML(p.method || 'Direct')}</td>
              <td class="mono">${escapeHTML(p.transactionRef || '—')}</td>
              <td>${escapeHTML(p.notes || '—')}</td>
              <td class="num mono">${fmtMoney(p.amount, sym)}</td>
            </tr>
          `).join('')}
        </tbody>
      </table>
    </div>` : '';

  // Document Title
  const documentDisplayTitle = isEstimate
    ? 'QUOTATION / ESTIMATE'
    : (docType === 'proforma')
      ? 'PROFORMA INVOICE'
      : 'TAX INVOICE';

  const sheet = `
    <div class="invoice-sheet theme-${template}" id="invoiceSheet">
      ${isPaid ? `<div class="paid-watermark">PAID</div>` : ''}

      <div class="inv-head">
        <div>
          ${invoice.seller.logo ? `
          <div class="sheet-logo-container">
            <img src="${invoice.seller.logo}" class="sheet-logo" alt="Company Logo">
          </div>` : ''}
          <p class="biz-name">${escapeHTML(invoice.seller.name || 'Your Business')}</p>
          <div class="biz-meta">
            ${escapeHTML(invoice.seller.address || '')}<br>
            ${escapeHTML(invoice.seller.email || '')}${invoice.seller.email && invoice.seller.phone ? ' · ' : ''}${escapeHTML(invoice.seller.phone || '')}
            ${invoice.seller.taxId ? `<br><strong>Tax ID / GSTIN:</strong> ${escapeHTML(invoice.seller.taxId)}` : ''}
          </div>
        </div>
        <div class="inv-head-right">
          <p class="inv-title">${documentDisplayTitle}</p>
          <div class="inv-num">${escapeHTML(invoice.invoiceNumber)}</div>
        </div>
      </div>

      <div class="inv-meta-grid">
        <div><div class="label">Issued Date</div><div class="val mono">${fmtDate(invoice.invoiceDate)}</div></div>
        <div><div class="label">${isEstimate ? 'Valid Until' : 'Due Date'}</div><div class="val mono">${fmtDate(invoice.dueDate)}</div></div>
        <div>
          <div class="label">Status</div>
          <div class="val">
            <span class="stamp ${effectiveStatus.toLowerCase().replace(/\s+/g,'-')}">${effectiveStatus}</span>
            ${isOverdue ? `<span class="stamp overdue" style="margin-left:4px;">${overdueDays}d Overdue</span>` : ''}
          </div>
        </div>
      </div>

      ${paidBannerHTML}
      ${partialBannerHTML}

      <div class="bill-to">
        <div class="label">${isEstimate ? 'Quotation For' : 'Bill To'}</div>
        <div class="cust-name">${escapeHTML(invoice.customer.name)}</div>
        <div class="cust-meta">
          ${escapeHTML(invoice.customer.address || '')}<br>
          ${escapeHTML(invoice.customer.email || '')}${invoice.customer.email && invoice.customer.phone ? ' · ' : ''}${escapeHTML(invoice.customer.phone || '')}
          ${invoice.customer.taxId ? `<br><strong>Tax ID / GSTIN:</strong> ${escapeHTML(invoice.customer.taxId)}` : ''}
        </div>
      </div>

      <table class="inv-items">
        <thead>
          <tr>
            <th>Item / Service</th>
            <th class="col-hsn">HSN/SAC</th>
            <th class="num">Qty</th>
            <th class="num">Unit Price</th>
            <th class="num col-tax">Tax</th>
            <th class="num">Total</th>
          </tr>
        </thead>
        <tbody>${itemsRows}</tbody>
      </table>

      <div class="inv-totals">
        <div class="row"><span>Subtotal</span><span class="amt">${fmtMoney(invoice.subtotal, sym)}</span></div>
        ${invoice.discount > 0 ? `
        <div class="row">
          <span>Discount ${invoice.discountType==='pct' ? `(${invoice.discountVal}%)` : ''}</span>
          <span class="amt">−${fmtMoney(invoice.discount, sym)}</span>
        </div>` : ''}

        ${invoice.tax > 0 ? (
          invoice.isInterState ? `
          <div class="row"><span>IGST (${invoice.taxPct}%)</span><span class="amt">+${fmtMoney(invoice.tax, sym)}</span></div>` : `
          <div class="row"><span>CGST (${(invoice.taxPct/2).toFixed(1)}%)</span><span class="amt">+${fmtMoney(invoice.cgst || invoice.tax/2, sym)}</span></div>
          <div class="row"><span>SGST (${(invoice.taxPct/2).toFixed(1)}%)</span><span class="amt">+${fmtMoney(invoice.sgst || invoice.tax/2, sym)}</span></div>`
        ) : ''}

        ${invoice.extraCharges > 0 ? `
        <div class="row"><span>${escapeHTML(invoice.extraChargesLabel || 'Shipping & Extra')}</span><span class="amt">+${fmtMoney(invoice.extraCharges, sym)}</span></div>` : ''}

        ${invoice.roundOff ? `
        <div class="row"><span>Round Off</span><span class="amt">${invoice.roundOff >= 0 ? '+' : '−'}${fmtMoney(Math.abs(invoice.roundOff), sym)}</span></div>` : ''}

        <div class="row grand"><span>Grand Total</span><span class="amt">${fmtMoney(invoice.grandTotal, sym)}</span></div>

        ${paidTotal > 0 ? `
        <div class="row" style="color:#2c6b3f;font-weight:600;"><span>Total Paid</span><span class="amt">${fmtMoney(paidTotal, sym)}</span></div>
        <div class="row" style="color:var(--rust);font-weight:700;"><span>Balance Due</span><span class="amt">${fmtMoney(balanceDue, sym)}</span></div>` : ''}
      </div>

      ${paymentLedgerHTML}

      <div class="inv-foot">
        <div class="block"><div class="label">Payment Terms &amp; Conditions</div>${escapeHTML(invoice.paymentTerms || '—')}</div>
        <div class="block"><div class="label">Notes</div>${escapeHTML(invoice.notes || '—')}</div>
      </div>

      <div class="inv-pay-sign">
        <div class="pay-block-container">
          ${qrTarget && !isPaid ? `
          <div class="pay-block">
            <div class="label">${isCustomUrl ? 'Scan to Pay Link' : 'Scan to Pay (UPI)'}</div>
            <img src="${qrImageUrl(qrTarget, 200)}" alt="Payment QR code" width="110" height="110">
            <div class="upi-id">${escapeHTML(invoice.seller.upiId || 'Scan with any UPI App')}</div>
          </div>` : ''}

          ${(invoice.seller.bankName || invoice.seller.accountNumber) ? `
          <div class="pay-details-box">
            <div class="label" style="margin-bottom:4px;font-size:10px;text-transform:uppercase;font-weight:700;color:#7c8c85;">
              ${isPaid ? 'Settlement Account' : 'Direct Bank Settlement'}
            </div>
            ${invoice.seller.bankName ? `<div><strong>Bank:</strong> ${escapeHTML(invoice.seller.bankName)}</div>` : ''}
            ${invoice.seller.accountNumber ? `<div><strong>A/C No:</strong> <span class="mono">${escapeHTML(invoice.seller.accountNumber)}</span></div>` : ''}
            ${invoice.seller.ifscCode ? `<div><strong>IFSC/SWIFT:</strong> <span class="mono">${escapeHTML(invoice.seller.ifscCode)}</span></div>` : ''}
          </div>` : ''}
        </div>

        <div class="sign-block">
          <div class="sig-slot">${invoice.signature ? `<img src="${invoice.signature}" class="sig-img" alt="Authorised signature">` : ''}</div>
          <div class="sig-line"></div>
          <div class="sig-label">Authorised Signature</div>
          <div class="sig-name">${escapeHTML(invoice.seller.name || '')}</div>
        </div>
      </div>
    </div>`;

  // Precomposed WhatsApp Message
  const waText = encodeURIComponent(
    `Hello *${invoice.customer.name}*,\n` +
    `Please find your ${isEstimate ? 'Estimate' : 'Invoice'} *${invoice.invoiceNumber}* from *${invoice.seller.name || 'Ledgerly'}*.\n\n` +
    `• Amount: *${fmtMoney(invoice.grandTotal, sym)}*\n` +
    (balanceDue > 0 ? `• Balance Due: *${fmtMoney(balanceDue, sym)}*\n` : '') +
    `• Due Date: *${fmtDate(invoice.dueDate)}*\n` +
    (invoice.seller.upiId ? `• Pay via UPI: *${invoice.seller.upiId}*\n` : '') +
    (invoice.seller.paymentUrl ? `• Online Payment: ${invoice.seller.paymentUrl}\n` : '') +
    `\nThank you for your business!`
  );

  const cleanPhone = (invoice.customer.phone || '').replace(/[^0-9]/g, '');
  let formattedPhone = cleanPhone;
  if(formattedPhone.length === 10 && /^[6-9]/.test(formattedPhone)){
    formattedPhone = '91' + formattedPhone;
  }
  const waUrl = formattedPhone ? `https://wa.me/${formattedPhone}?text=${waText}` : `https://wa.me/?text=${waText}`;

  // Precomposed Email Content
  const emailSubject = isPaid
    ? `Payment Receipt for Invoice ${invoice.invoiceNumber} from ${invoice.seller.name || 'Merchant'}`
    : `${isEstimate ? 'Quotation' : 'Invoice'} ${invoice.invoiceNumber} from ${invoice.seller.name || 'Merchant'}`;

  const emailBody = isPaid
    ? `Dear ${invoice.customer.name},\n\nThank you for your payment! Here is your official receipt for Invoice ${invoice.invoiceNumber}.\n\n` +
      `Amount Paid: ${fmtMoney(paidTotal || invoice.grandTotal, sym)}\n` +
      `Payment Date: ${fmtDate(invoice.paidAt || invoice.invoiceDate)}\n` +
      `Payment Method: ${invoice.paymentMethod || 'Direct Payment'}\n` +
      (invoice.transactionRef ? `Transaction Ref: ${invoice.transactionRef}\n` : '') +
      `\nMessage: ${invoice.paidMessage || 'Thank you for your business!'}\n\nBest regards,\n${invoice.seller.name || ''}`
    : `Dear ${invoice.customer.name},\n\nPlease find the details for ${isEstimate ? 'Quotation' : 'Invoice'} ${invoice.invoiceNumber}.\n\n` +
      `Amount Due: ${fmtMoney(balanceDue || invoice.grandTotal, sym)}\nDue Date: ${fmtDate(invoice.dueDate)}\n\n` +
      (invoice.seller.upiId ? `Pay via UPI: ${invoice.seller.upiId}\n` : '') +
      (invoice.seller.paymentUrl ? `Pay Online: ${invoice.seller.paymentUrl}\n` : '') +
      `\nThank you for your business!\n\nBest regards,\n${invoice.seller.name || ''}`;

  const content = `
    <div class="preview-toolbar no-print">
      <div class="left">
        <a href="#/edit?id=${invoice.id}" class="btn btn-ghost btn-sm">Edit</a>
        <select id="statusSelect" class="btn btn-ghost btn-sm" style="padding:7px 10px;">${statusOptions}</select>
        ${!isEstimate ? `
        <button class="btn ${isPaid ? 'btn-ghost' : 'btn-success'} btn-sm" id="recordPaymentBtn">
          ${isPaid ? 'Payment Records' : 'Record / Manage Payments'}
        </button>` : `
        <button class="btn btn-primary btn-sm" id="convertEstimateBtn">Convert to Invoice</button>`}
        ${invoice.isRecurring ? `
        <button class="btn btn-brass btn-sm" id="renewRecurringBtn" title="Clone and advance invoice date for next billing cycle">
          Renew for Next Period
        </button>` : ''}
      </div>
      <div class="left">
        ${(typeof navigator !== 'undefined' && navigator.share) ? `
        <button class="btn btn-whatsapp btn-sm" id="nativeShareBtn" title="Share via Mobile Share Sheet">Share</button>
        ` : ''}
        <a href="${waUrl}" target="_blank" class="btn btn-whatsapp btn-sm" id="waShareBtn">WhatsApp Share</a>
        <button class="btn btn-ghost btn-sm" id="emailBtn">Email ${isPaid ? 'Receipt' : 'Doc'}</button>
        <button class="btn btn-ghost btn-sm" id="downloadPdfBtn">Download PDF</button>
        <button class="btn btn-primary btn-sm" id="printBtn">Print</button>
      </div>
    </div>
    ${sheet}

    <!-- Record / Manage Payments Modal -->
    <div class="modal-overlay" id="paymentModal">
      <div class="modal-card">
        <div class="modal-head">
          <h2>Payment Records &amp; Installments</h2>
          <button class="modal-close" id="closePaymentModal">&times;</button>
        </div>

        <div style="background:var(--paper);padding:14px;border-radius:4px;margin-bottom:18px;">
          <div style="display:flex;justify-content:space-between;font-size:13px;margin-bottom:4px;">
            <span>Grand Total:</span><strong class="mono">${fmtMoney(invoice.grandTotal, sym)}</strong>
          </div>
          <div style="display:flex;justify-content:space-between;font-size:13px;margin-bottom:4px;color:#2c6b3f;">
            <span>Total Collected:</span><strong class="mono">${fmtMoney(paidTotal, sym)}</strong>
          </div>
          <div style="display:flex;justify-content:space-between;font-size:14px;font-weight:700;color:var(--rust);">
            <span>Balance Remaining:</span><strong class="mono">${fmtMoney(balanceDue, sym)}</strong>
          </div>
        </div>

        <!-- Recorded Installments List -->
        <h3 style="font-size:13px;text-transform:uppercase;margin:0 0 8px;color:var(--ink-soft);">Recorded Installments</h3>
        <div id="installmentsList" style="margin-bottom:16px;">
          ${paymentsList.length ? paymentsList.map((p, pIdx) => `
            <div style="display:flex;justify-content:space-between;align-items:center;padding:8px 10px;border-bottom:1px solid var(--line);font-size:12.5px;">
              <div>
                <strong>${fmtMoney(p.amount, sym)}</strong> via ${escapeHTML(p.method)}
                <span style="color:var(--ink-faint);">(${fmtDate(p.date)})</span>
                ${p.transactionRef ? `<div style="font-size:11px;color:var(--ink-soft);">Ref: ${escapeHTML(p.transactionRef)}</div>` : ''}
              </div>
              <button type="button" class="btn-xs delete-pay-btn" data-pidx="${pIdx}" style="color:var(--rust);">&times; Remove</button>
            </div>
          `).join('') : '<div style="font-size:12.5px;color:var(--ink-faint);padding:6px 0;">No payments recorded yet.</div>'}
        </div>

        <!-- Add Payment Form -->
        <h3 style="font-size:13px;text-transform:uppercase;margin:16px 0 10px;color:var(--ink-soft);">+ Record New Payment</h3>
        <form id="paymentForm">
          <div class="field-row">
            <div class="field">
              <label>Amount to Record (${sym})</label>
              <input type="number" id="pay_amt" step="0.01" min="0.01" max="${invoice.grandTotal}" value="${balanceDue > 0 ? balanceDue : invoice.grandTotal}" required>
            </div>
            <div class="field">
              <label>Payment Date</label>
              <input type="date" id="pay_date" value="${todayISO()}" required>
            </div>
          </div>
          <div class="field-row">
            <div class="field">
              <label>Payment Method</label>
              <select id="pay_method">
                <option value="UPI / QR Code" selected>UPI / QR Code</option>
                <option value="Bank Transfer (NEFT/IMPS)">Bank Transfer (NEFT/IMPS)</option>
                <option value="Credit / Debit Card">Credit / Debit Card</option>
                <option value="Cash">Cash</option>
                <option value="Cheque">Cheque</option>
                <option value="Online Payment Gateway">Online Payment Gateway</option>
                <option value="Other">Other</option>
              </select>
            </div>
            <div class="field">
              <label>Transaction / UTR / Cheque Ref</label>
              <input id="pay_ref" placeholder="e.g. UTR-49102849102">
            </div>
          </div>
          <div class="field">
            <label>Settlement / Receipt Message</label>
            <textarea id="pay_msg" rows="2" placeholder="Note to acknowledge receipt of this payment">${escapeHTML(invoice.paidMessage || 'Payment received with thanks.')}</textarea>
          </div>
          <div class="form-actions" style="margin-top:16px;">
            <button type="button" class="btn btn-ghost" id="cancelPaymentModal">Close</button>
            <button type="submit" class="btn btn-primary">Save Payment Record</button>
          </div>
        </form>
      </div>
    </div>

    <!-- Email Modal -->
    <div class="modal-overlay" id="emailModal">
      <div class="modal-card">
        <div class="modal-head">
          <h2>Email ${isPaid ? 'Payment Receipt' : (isEstimate ? 'Quotation' : 'Invoice')}</h2>
          <button class="modal-close" id="closeEmailModal">&times;</button>
        </div>
        <div class="field">
          <label>Recipient Email</label>
          <input id="em_to" type="email" value="${escapeHTML(invoice.customer.email || '')}" placeholder="client@email.com">
        </div>
        <div class="field">
          <label>Subject</label>
          <input id="em_subj" value="${escapeHTML(emailSubject)}">
        </div>
        <div class="field">
          <label>Message Body</label>
          <textarea id="em_body" rows="7">${escapeHTML(emailBody)}</textarea>
        </div>
        <div class="form-actions" style="margin-top:20px;">
          <button type="button" class="btn btn-ghost" id="copyEmailBtn">Copy Text</button>
          <a class="btn btn-primary" id="openMailClientBtn" target="_blank">Open Mail App (mailto:)</a>
        </div>
      </div>
    </div>
  `;

  document.getElementById('app').innerHTML = appShell('/history', 'Document Preview', 'Preview & Dispatch', content);
  mountShellEvents();

  // Print button
  document.getElementById('printBtn').addEventListener('click', ()=> window.print());

  // Native Web Share API (Mobile phones & tablets)
  const nativeShareBtn = document.getElementById('nativeShareBtn');
  if(nativeShareBtn){
    nativeShareBtn.addEventListener('click', async ()=>{
      if(navigator.share){
        try{
          await navigator.share({
            title: `${isEstimate ? 'Quotation' : 'Invoice'} ${invoice.invoiceNumber}`,
            text: decodeURIComponent(waText.replace(/\+/g, ' '))
          });
        }catch(err){
          // User cancelled or share dismissed
        }
      }
    });
  }

  // Direct PDF Download with html2pdf.js (Optimized for both mobile and desktop)
  document.getElementById('downloadPdfBtn').addEventListener('click', ()=>{
    const sheetEl = document.getElementById('invoiceSheet');
    if(!sheetEl){ window.print(); return; }

    showToast('Generating PDF...');
    if(window.html2pdf){
      const opt = {
        margin: [8, 8, 8, 8],
        filename: `${invoice.invoiceNumber}.pdf`,
        image: { type: 'jpeg', quality: 0.98 },
        html2canvas: { scale: 2, useCORS: true, scrollY: 0, windowWidth: 850 },
        jsPDF: { unit: 'mm', format: 'a4', orientation: 'portrait' }
      };
      window.html2pdf().set(opt).from(sheetEl).save().then(()=>{
        showToast('PDF downloaded successfully!');
      }).catch(err => {
        console.error(err);
        showToast('Direct PDF download failed. Opening print view...');
        window.print();
      });
    } else {
      window.print();
    }
  });

  // Convert Estimate to Invoice
  const convertBtn = document.getElementById('convertEstimateBtn');
  if(convertBtn){
    convertBtn.addEventListener('click', ()=>{
      if(!confirm('Convert this Quotation into a formal billable Tax Invoice?')) return;
      invoice.docType = 'invoice';
      invoice.invoiceNumber = nextDocNumber(user.id, 'invoice');
      invoice.status = 'Generated';
      setAll(DB.invoices, invoices);
      showToast('Converted to formal invoice: ' + invoice.invoiceNumber);
      location.hash = '#/preview?id=' + invoice.id;
    });
  }

  // 1-Click Renew Recurring Retainer Invoice
  const renewBtn = document.getElementById('renewRecurringBtn');
  if(renewBtn){
    renewBtn.addEventListener('click', ()=>{
      const freq = invoice.recurFreq || 'Monthly';
      if(!confirm(`Generate renewed ${freq} invoice for the next billing cycle?`)) return;

      const newId = uid('inv');
      const newNum = nextDocNumber(user.id, 'invoice');
      const today = todayISO();

      // Advance due date by 1 month
      const dueDt = new Date();
      dueDt.setDate(dueDt.getDate() + 15);
      const newDue = dueDt.toISOString().slice(0, 10);

      const renewed = {
        ...JSON.parse(JSON.stringify(invoice)),
        id: newId,
        invoiceNumber: newNum,
        invoiceDate: today,
        dueDate: newDue,
        status: 'Generated',
        payments: [],
        paidAt: null,
        transactionRef: '',
        createdAt: Date.now()
      };

      const allInvs = getAll(DB.invoices);
      allInvs.unshift(renewed);
      setAll(DB.invoices, allInvs);

      showToast(`Renewed retainer: New invoice ${newNum} generated!`);
      location.hash = '#/preview?id=' + newId;
    });
  }

  // Status select quick change
  document.getElementById('statusSelect').addEventListener('change', (e)=>{
    const nextStatus = e.target.value;
    invoice.status = nextStatus;
    if(nextStatus === 'Paid' && !invoice.paidAt){
      invoice.paidAt = todayISO();
    }
    setAll(DB.invoices, invoices);
    showToast('Status updated to ' + nextStatus);
    location.reload();
  });

  // Payment Modal Events
  const paymentModal = document.getElementById('paymentModal');
  const recordPayBtn = document.getElementById('recordPaymentBtn');
  if(recordPayBtn){
    recordPayBtn.addEventListener('click', ()=> paymentModal.classList.add('show'));
  }
  document.getElementById('closePaymentModal').addEventListener('click', ()=> paymentModal.classList.remove('show'));
  document.getElementById('cancelPaymentModal').addEventListener('click', ()=> paymentModal.classList.remove('show'));

  // Delete an installment
  document.querySelectorAll('.delete-pay-btn').forEach(btn => {
    btn.addEventListener('click', ()=>{
      const pIdx = Number(btn.dataset.pidx);
      invoice.payments = invoice.payments || [];
      invoice.payments.splice(pIdx, 1);
      invoice.status = getInvoiceEffectiveStatus(invoice);
      setAll(DB.invoices, invoices);
      showToast('Payment record removed.');
      location.reload();
    });
  });

  // Add Payment Form submit
  document.getElementById('paymentForm').addEventListener('submit', (e)=>{
    e.preventDefault();
    const amount = Number(document.getElementById('pay_amt').value) || 0;
    const date = document.getElementById('pay_date').value || todayISO();
    const method = document.getElementById('pay_method').value;
    const ref = document.getElementById('pay_ref').value.trim();
    const msg = document.getElementById('pay_msg').value.trim();

    invoice.payments = invoice.payments || [];
    invoice.payments.push({
      id: uid('pay'),
      amount,
      date,
      method,
      transactionRef: ref,
      notes: msg,
      recordedAt: Date.now()
    });

    invoice.paidAt = date;
    invoice.paymentMethod = method;
    invoice.transactionRef = ref;
    invoice.paidMessage = msg;
    invoice.status = getInvoiceEffectiveStatus(invoice);

    setAll(DB.invoices, invoices);
    paymentModal.classList.remove('show');
    showToast('Payment recorded successfully!');
    location.reload();
  });

  // Email Modal Events
  const emailModal = document.getElementById('emailModal');
  document.getElementById('emailBtn').addEventListener('click', ()=> emailModal.classList.add('show'));
  document.getElementById('closeEmailModal').addEventListener('click', ()=> emailModal.classList.remove('show'));

  document.getElementById('copyEmailBtn').addEventListener('click', ()=>{
    const body = document.getElementById('em_body').value;
    navigator.clipboard.writeText(body).then(()=>{
      showToast('Email content copied to clipboard.');
    });
  });

  document.getElementById('openMailClientBtn').addEventListener('click', ()=>{
    const to = document.getElementById('em_to').value.trim();
    const subj = document.getElementById('em_subj').value.trim();
    const body = document.getElementById('em_body').value;
    window.location.href = `mailto:${encodeURIComponent(to)}?subject=${encodeURIComponent(subj)}&body=${encodeURIComponent(body)}`;
  });
}

/* ================================================================
   VIEW: HISTORY / ALL INVOICES & ESTIMATES (SEARCH, FILTER & CSV)
   ================================================================ */
function renderHistory(){
  const user = currentUser();
  const content = `
    <div class="filter-bar">
      <input type="text" id="searchInput" placeholder="Search by number, customer, or items...">
      <select id="typeFilter">
        <option value="">All Document Types</option>
        <option value="invoice">Invoices Only</option>
        <option value="estimate">Estimates / Quotes Only</option>
      </select>
      <select id="statusFilter">
        <option value="">All statuses</option>
        <option value="Draft">Draft</option>
        <option value="Generated">Generated</option>
        <option value="Pending">Pending</option>
        <option value="Partially Paid">Partially Paid</option>
        <option value="Paid">Paid</option>
        <option value="Overdue">Overdue Bills</option>
      </select>
      <input type="date" id="dateFilter" title="Filter by date">
      <button class="btn btn-ghost" id="historyCsvBtn" style="white-space:nowrap;">Export CSV</button>
    </div>
    <div class="card" style="padding:22px 24px;">
      <table class="ledger-table">
        <thead>
          <tr>
            <th>Document #</th>
            <th>Customer</th>
            <th>Date</th>
            <th class="num">Amount</th>
            <th class="num">Balance Due</th>
            <th>Status</th>
          </tr>
        </thead>
        <tbody id="historyBody"></tbody>
      </table>
    </div>`;

  document.getElementById('app').innerHTML = appShell('/history', 'Documents & History', 'Archive', content);
  mountShellEvents();

  function draw(){
    const q = document.getElementById('searchInput').value.trim().toLowerCase();
    const docType = document.getElementById('typeFilter').value;
    const status = document.getElementById('statusFilter').value;
    const date = document.getElementById('dateFilter').value;
    let invoices = getAll(DB.invoices).filter(i => i.userId === user.id);

    if(q){
      invoices = invoices.filter(i =>
        (i.invoiceNumber && i.invoiceNumber.toLowerCase().includes(q)) ||
        (i.customer && i.customer.name && i.customer.name.toLowerCase().includes(q))
      );
    }
    if(docType){
      invoices = invoices.filter(i => (i.docType || 'invoice') === docType);
    }
    if(status){
      if(status === 'Overdue'){
        invoices = invoices.filter(i => getInvoiceBalance(i) > 0 && getOverdueDays(i.dueDate) > 0);
      } else {
        invoices = invoices.filter(i => getInvoiceEffectiveStatus(i) === status);
      }
    }
    if(date){
      invoices = invoices.filter(i => i.invoiceDate === date);
    }
    invoices.sort((a,b)=> b.createdAt - a.createdAt);

    const body = document.getElementById('historyBody');
    body.innerHTML = invoices.length
      ? invoices.map(rowHTML).join('')
      : `<tr class="empty-row"><td colspan="6">No documents match your search criteria.</td></tr>`;

    body.querySelectorAll('tr[data-id]').forEach(tr=>{
      tr.addEventListener('click', ()=> location.hash = '#/preview?id=' + tr.dataset.id);
    });

    // Wire up CSV export for currently filtered subset
    document.getElementById('historyCsvBtn').onclick = () => exportInvoicesToCSV(invoices);
  }

  document.getElementById('searchInput').addEventListener('input', draw);
  document.getElementById('typeFilter').addEventListener('change', draw);
  document.getElementById('statusFilter').addEventListener('change', draw);
  document.getElementById('dateFilter').addEventListener('change', draw);
  draw();
}

/* ================================================================
   VIEW: CUSTOMER DIRECTORY & ACCOUNT STATEMENTS (`/customers`)
   ================================================================ */
function renderCustomers(){
  const user = currentUser();
  const content = `
    <div class="filter-bar">
      <input type="text" id="custSearch" placeholder="Search customers by name, contact, or email...">
      <button class="btn btn-primary" id="addCustBtn">+ Add Customer</button>
    </div>
    <div class="directory-grid" id="custGrid"></div>

    <!-- Add/Edit Customer Modal -->
    <div class="modal-overlay" id="custModal">
      <div class="modal-card">
        <div class="modal-head">
          <h2 id="custModalTitle">Add Customer Profile</h2>
          <button class="modal-close" id="closeCustModal">&times;</button>
        </div>
        <form id="custForm">
          <input type="hidden" id="c_id">
          <div class="field"><label>Company / Customer Name *</label><input id="mc_name" required placeholder="Acme Inc."></div>
          <div class="field"><label>Contact Person</label><input id="mc_contact" placeholder="Jane Doe"></div>
          <div class="field-row">
            <div class="field"><label>Email</label><input id="mc_email" type="email" placeholder="billing@acme.com"></div>
            <div class="field"><label>Phone</label><input id="mc_phone" placeholder="+91 98765 43210"></div>
          </div>
          <div class="field"><label>Address</label><input id="mc_address" placeholder="123 Business Way, City, State"></div>
          <div class="field-row">
            <div class="field"><label>GSTIN / Tax ID</label><input id="mc_tax" placeholder="27AAAAA0000A1Z5"></div>
            <div class="field"><label>Default Payment Terms</label><input id="mc_terms" placeholder="Net 15 Days"></div>
          </div>
          <div class="form-actions" style="margin-top:20px;">
            <button type="button" class="btn btn-ghost" id="cancelCustModal">Cancel</button>
            <button type="submit" class="btn btn-primary">Save Customer</button>
          </div>
        </form>
      </div>
    </div>

    <!-- Customer Account Statement Modal -->
    <div class="modal-overlay" id="statementModal">
      <div class="modal-card" style="max-width:760px;">
        <div class="modal-head">
          <h2 id="statementTitle">Customer Statement of Account</h2>
          <button class="modal-close" id="closeStatementModal">&times;</button>
        </div>
        <div id="statementBody"></div>
        <div class="form-actions" style="margin-top:20px;">
          <button type="button" class="btn btn-ghost" id="closeStatementBtn">Close</button>
          <button type="button" class="btn btn-primary" id="printStatementBtn">Print Statement</button>
        </div>
      </div>
    </div>
  `;

  document.getElementById('app').innerHTML = appShell('/customers', 'Customer Directory &amp; Ledger', 'Accounts', content);
  mountShellEvents();

  function draw(){
    const q = document.getElementById('custSearch').value.trim().toLowerCase();
    let customers = getAll(DB.customers).filter(c => c.userId === user.id);
    if(q){
      customers = customers.filter(c =>
        c.name.toLowerCase().includes(q) ||
        (c.contactPerson && c.contactPerson.toLowerCase().includes(q)) ||
        (c.email && c.email.toLowerCase().includes(q))
      );
    }

    const grid = document.getElementById('custGrid');
    if(!customers.length){
      grid.innerHTML = `<div class="card" style="grid-column:1/-1;padding:40px;text-align:center;color:var(--ink-soft);">No customers found. Click "+ Add Customer" to create one.</div>`;
      return;
    }

    const allInvoices = getAll(DB.invoices).filter(i => i.userId === user.id);

    grid.innerHTML = customers.map(c => {
      const cInvoices = allInvoices.filter(i => i.customer && i.customer.name && i.customer.name.toLowerCase() === c.name.toLowerCase());
      const cBilled = cInvoices.reduce((s,i)=> s + (Number(i.grandTotal)||0), 0);
      const cBalance = cInvoices.reduce((s,i)=> s + getInvoiceBalance(i), 0);

      return `
        <div class="card dir-card">
          <div>
            <div class="title">${escapeHTML(c.name)}</div>
            ${c.contactPerson ? `<div class="subtitle">Contact: ${escapeHTML(c.contactPerson)}</div>` : ''}
            ${c.email ? `<div class="meta-item">Email: ${escapeHTML(c.email)}</div>` : ''}
            ${c.phone ? `<div class="meta-item">Phone: ${escapeHTML(c.phone)}</div>` : ''}
            ${c.address ? `<div class="meta-item">Address: ${escapeHTML(c.address)}</div>` : ''}
            ${c.taxId ? `<div class="meta-item">GST/Tax: <span class="mono">${escapeHTML(c.taxId)}</span></div>` : ''}

            <div style="margin-top:12px;padding-top:10px;border-top:1px dashed var(--line);font-size:12px;display:flex;justify-content:space-between;">
              <span>Total Billed: <strong class="mono">${fmtMoney(cBilled)}</strong></span>
              <span>Balance: <strong class="mono ${cBalance>0?'balance-due-text':''}">${fmtMoney(cBalance)}</strong></span>
            </div>
          </div>
          <div class="card-actions">
            <a href="#/create?cust_id=${c.id}" class="btn btn-primary btn-sm" style="text-decoration:none;">+ Invoice</a>
            <button class="btn btn-ghost btn-sm stat-c-btn" data-id="${c.id}">Statement</button>
            <button class="btn btn-ghost btn-sm edit-c-btn" data-id="${c.id}">Edit</button>
            <button class="btn btn-danger btn-sm del-c-btn" data-id="${c.id}">Delete</button>
          </div>
        </div>
      `;
    }).join('');

    grid.querySelectorAll('.edit-c-btn').forEach(b => b.addEventListener('click', () => openCustModal(b.dataset.id)));
    grid.querySelectorAll('.del-c-btn').forEach(b => b.addEventListener('click', () => deleteCustomer(b.dataset.id)));
    grid.querySelectorAll('.stat-c-btn').forEach(b => b.addEventListener('click', () => openCustomerStatement(b.dataset.id)));
  }

  const modal = document.getElementById('custModal');
  document.getElementById('addCustBtn').addEventListener('click', () => openCustModal());
  document.getElementById('closeCustModal').addEventListener('click', () => modal.classList.remove('show'));
  document.getElementById('cancelCustModal').addEventListener('click', () => modal.classList.remove('show'));

  function openCustModal(id){
    const title = document.getElementById('custModalTitle');
    title.textContent = id ? 'Edit Customer Profile' : 'Add Customer Profile';
    document.getElementById('c_id').value = id || '';

    if(id){
      const c = getAll(DB.customers).find(item => item.id === id);
      if(c){
        document.getElementById('mc_name').value = c.name || '';
        document.getElementById('mc_contact').value = c.contactPerson || '';
        document.getElementById('mc_email').value = c.email || '';
        document.getElementById('mc_phone').value = c.phone || '';
        document.getElementById('mc_address').value = c.address || '';
        document.getElementById('mc_tax').value = c.taxId || '';
        document.getElementById('mc_terms').value = c.terms || '';
      }
    } else {
      document.getElementById('custForm').reset();
      document.getElementById('c_id').value = '';
    }
    modal.classList.add('show');
  }

  function deleteCustomer(id){
    if(!confirm('Are you sure you want to delete this customer profile?')) return;
    let customers = getAll(DB.customers).filter(c => c.id !== id);
    setAll(DB.customers, customers);
    showToast('Customer deleted.');
    draw();
  }

  document.getElementById('custForm').addEventListener('submit', (e) => {
    e.preventDefault();
    const id = document.getElementById('c_id').value;
    const name = document.getElementById('mc_name').value.trim();
    if(!name) return;

    let customers = getAll(DB.customers);
    const data = {
      id: id || uid('cust'),
      userId: user.id,
      name,
      contactPerson: document.getElementById('mc_contact').value.trim(),
      email: document.getElementById('mc_email').value.trim(),
      phone: document.getElementById('mc_phone').value.trim(),
      address: document.getElementById('mc_address').value.trim(),
      taxId: document.getElementById('mc_tax').value.trim(),
      terms: document.getElementById('mc_terms').value.trim()
    };

    if(id){
      const idx = customers.findIndex(c => c.id === id);
      if(idx >= 0) customers[idx] = data;
    } else {
      customers.push(data);
    }

    setAll(DB.customers, customers);
    modal.classList.remove('show');
    showToast(id ? 'Customer updated.' : 'Customer added.');
    draw();
  });

  // Statement of Account Modal logic
  const statModal = document.getElementById('statementModal');
  document.getElementById('closeStatementModal').addEventListener('click', ()=> statModal.classList.remove('show'));
  document.getElementById('closeStatementBtn').addEventListener('click', ()=> statModal.classList.remove('show'));
  document.getElementById('printStatementBtn').addEventListener('click', ()=> window.print());

  function openCustomerStatement(custId){
    const cust = getAll(DB.customers).find(c => c.id === custId);
    if(!cust) return;

    const allInvoices = getAll(DB.invoices).filter(i =>
      i.userId === user.id &&
      i.customer && i.customer.name &&
      i.customer.name.toLowerCase() === cust.name.toLowerCase()
    ).sort((a,b)=> a.createdAt - b.createdAt);

    const lifetimeBilled = allInvoices.reduce((s,i)=> s + (Number(i.grandTotal)||0), 0);
    const lifetimePaid = allInvoices.reduce((s,i)=> s + getInvoicePaidTotal(i), 0);
    const outstandingBalance = allInvoices.reduce((s,i)=> s + getInvoiceBalance(i), 0);

    const statementRows = allInvoices.length ? allInvoices.map(inv => {
      const paid = getInvoicePaidTotal(inv);
      const bal = getInvoiceBalance(inv);
      const status = getInvoiceEffectiveStatus(inv);
      return `
        <tr>
          <td class="mono"><a href="#/preview?id=${inv.id}" style="color:var(--teal);">${escapeHTML(inv.invoiceNumber)}</a></td>
          <td>${fmtDate(inv.invoiceDate)}</td>
          <td>${fmtDate(inv.dueDate)}</td>
          <td class="num mono">${fmtMoney(inv.grandTotal, inv.currencySymbol)}</td>
          <td class="num mono" style="color:#2c6b3f;">${fmtMoney(paid, inv.currencySymbol)}</td>
          <td class="num mono ${bal>0?'balance-due-text':''}">${fmtMoney(bal, inv.currencySymbol)}</td>
          <td><span class="stamp ${status.toLowerCase().replace(/\s+/g,'-')}">${status}</span></td>
        </tr>
      `;
    }).join('') : `<tr><td colspan="7" style="text-align:center;padding:20px;">No transactions recorded for this customer.</td></tr>`;

    document.getElementById('statementTitle').textContent = `Account Statement: ${cust.name}`;
    document.getElementById('statementBody').innerHTML = `
      <div style="margin-bottom:18px;">
        <p style="margin:0 0 4px;font-size:13px;color:var(--ink-soft);">${escapeHTML(cust.address || '')}</p>
        <p style="margin:0;font-size:13px;color:var(--ink-soft);">${escapeHTML(cust.email || '')} ${cust.phone ? ' · ' + escapeHTML(cust.phone) : ''}</p>
      </div>

      <div class="statement-kpis">
        <div class="statement-kpi">
          <div class="kpi-lbl">Lifetime Billed</div>
          <div class="kpi-val">${fmtMoney(lifetimeBilled)}</div>
        </div>
        <div class="statement-kpi">
          <div class="kpi-lbl">Total Payments Received</div>
          <div class="kpi-val" style="color:#2c6b3f;">${fmtMoney(lifetimePaid)}</div>
        </div>
        <div class="statement-kpi">
          <div class="kpi-lbl">Current Balance Due</div>
          <div class="kpi-val balance-due-text">${fmtMoney(outstandingBalance)}</div>
        </div>
      </div>

      <table class="ledger-table" style="font-size:12.5px;">
        <thead>
          <tr>
            <th>Invoice #</th>
            <th>Date</th>
            <th>Due Date</th>
            <th class="num">Billed</th>
            <th class="num">Paid</th>
            <th class="num">Balance</th>
            <th>Status</th>
          </tr>
        </thead>
        <tbody>${statementRows}</tbody>
      </table>
    `;
    statModal.classList.add('show');
  }

  document.getElementById('custSearch').addEventListener('input', draw);
  draw();
}

/* ================================================================
   VIEW: ENTERPRISE PROFILES MANAGEMENT (`/enterprise`)
   ================================================================ */
function renderEnterprise(){
  const user = currentUser();
  const content = `
    <div class="filter-bar">
      <input type="text" id="entSearch" placeholder="Search enterprise profiles...">
      <button class="btn btn-primary" id="addEntBtn">+ Add Enterprise Profile</button>
    </div>
    <div class="directory-grid" id="entGrid"></div>

    <!-- Enterprise Modal -->
    <div class="modal-overlay" id="entModal">
      <div class="modal-card">
        <div class="modal-head">
          <h2 id="entModalTitle">Add Enterprise Profile</h2>
          <button class="modal-close" id="closeEntModal">&times;</button>
        </div>
        <form id="entForm">
          <input type="hidden" id="e_id">
          <div class="field"><label>Enterprise / Business Name *</label><input id="me_name" required placeholder="Acme Global Solutions"></div>
          <div class="field"><label>Tagline / Description</label><input id="me_tagline" placeholder="Premium Consulting Services"></div>
          <div class="field-row">
            <div class="field"><label>Business Email</label><input id="me_email" type="email" placeholder="billing@acme.com"></div>
            <div class="field"><label>Business Phone</label><input id="me_phone" placeholder="+91 98765 43210"></div>
          </div>
          <div class="field"><label>Business Address</label><input id="me_address" placeholder="100 Tech Park, Suite 400"></div>
          <div class="field-row">
            <div class="field"><label>GSTIN / Tax ID</label><input id="me_tax" placeholder="27AAAAA0000A1Z5"></div>
            <div class="field">
              <label>Default Currency</label>
              <select id="me_currency">
                <option value="INR (₹)">INR (₹)</option>
                <option value="USD ($)">USD ($)</option>
                <option value="EUR (€)">EUR (€)</option>
                <option value="GBP (£)">GBP (£)</option>
              </select>
            </div>
          </div>

          <div class="field-row">
            <div class="field">
              <label>Default Sheet Template</label>
              <select id="me_template">
                <option value="classic">Classic Brass</option>
                <option value="navy">Corporate Navy</option>
                <option value="minimal">Modern Minimalist</option>
                <option value="compact">Compact Slip</option>
              </select>
            </div>
            <div class="field">
              <label>Company Logo</label>
              <div class="logo-upload-wrap">
                <img id="entLogoPreview" src="data:image/svg+xml,<svg xmlns=\'http://www.w3.org/2000/svg\' viewBox=\'0 0 100 100\'><rect fill=\'%23eef1ea\' width=\'100\' height=\'100\'/><text x=\'50\' y=\'55\' text-anchor=\'middle\' fill=\'%237c8c85\' font-size=\'12\'>No Logo</text></svg>" class="logo-thumb" alt="Logo preview">
                <input type="file" id="entLogoInput" accept="image/*" style="font-size:12px;">
                <input type="hidden" id="me_logo">
              </div>
            </div>
          </div>

          <h3 style="font-size:14px;margin:20px 0 10px;text-transform:uppercase;color:var(--brass-dark);">Payment &amp; QR Settings</h3>
          <div class="field-row">
            <div class="field"><label>UPI ID (for Payment QR)</label><input id="me_upi" placeholder="yourname@upi"></div>
            <div class="field"><label>Custom Checkout URL</label><input id="me_payurl" placeholder="https://pay.example.com"></div>
          </div>
          <div class="field-row">
            <div class="field"><label>Bank Name</label><input id="me_bank" placeholder="HDFC Bank"></div>
            <div class="field"><label>Account Number</label><input id="me_acc" class="mono" placeholder="50200012345"></div>
            <div class="field"><label>IFSC/SWIFT</label><input id="me_ifsc" class="mono" placeholder="HDFC0000123"></div>
          </div>

          <div class="field" style="margin-top:10px;">
            <label><input type="checkbox" id="me_isdefault"> Set as Default Enterprise Profile</label>
          </div>

          <div class="form-actions" style="margin-top:20px;">
            <button type="button" class="btn btn-ghost" id="cancelEntModal">Cancel</button>
            <button type="submit" class="btn btn-primary">Save Profile</button>
          </div>
        </form>
      </div>
    </div>`;

  document.getElementById('app').innerHTML = appShell('/enterprise', 'Enterprise Profiles', 'Multi-Entity', content);
  mountShellEvents();

  // Logo upload listener
  const logoInput = document.getElementById('entLogoInput');
  const logoPreview = document.getElementById('entLogoPreview');
  const logoHidden = document.getElementById('me_logo');
  if(logoInput){
    logoInput.addEventListener('change', (e)=>{
      const file = e.target.files[0];
      if(file){
        const reader = new FileReader();
        reader.onload = (evt)=>{
          logoPreview.src = evt.target.result;
          logoHidden.value = evt.target.result;
        };
        reader.readAsDataURL(file);
      }
    });
  }

  function draw(){
    const q = document.getElementById('entSearch').value.trim().toLowerCase();
    let enterprises = getAll(DB.enterprises).filter(e => e.userId === user.id);
    if(q){
      enterprises = enterprises.filter(e => e.name.toLowerCase().includes(q) || (e.email && e.email.toLowerCase().includes(q)));
    }

    const grid = document.getElementById('entGrid');
    if(!enterprises.length){
      grid.innerHTML = `<div class="card" style="grid-column:1/-1;padding:40px;text-align:center;color:var(--ink-soft);">No enterprise profiles found. Click "+ Add Enterprise Profile" to create one.</div>`;
      return;
    }

    grid.innerHTML = enterprises.map(e => `
      <div class="card dir-card">
        <div>
          <div style="display:flex;justify-content:space-between;align-items:flex-start;gap:10px;">
            <div style="display:flex;align-items:center;gap:10px;">
              ${e.logo ? `<img src="${e.logo}" style="width:36px;height:36px;object-fit:contain;border-radius:3px;border:1px solid var(--line);">` : ''}
              <div class="title">${escapeHTML(e.name)}</div>
            </div>
            ${e.isDefault ? `<span class="badge">Default</span>` : ''}
          </div>
          ${e.tagline ? `<div class="subtitle">${escapeHTML(e.tagline)}</div>` : ''}
          ${e.email ? `<div class="meta-item">Email: ${escapeHTML(e.email)}</div>` : ''}
          ${e.phone ? `<div class="meta-item">Phone: ${escapeHTML(e.phone)}</div>` : ''}
          ${e.upiId ? `<div class="meta-item">UPI: <span class="mono">${escapeHTML(e.upiId)}</span></div>` : ''}
          ${e.bankName ? `<div class="meta-item">Bank: ${escapeHTML(e.bankName)} (${escapeHTML(e.accountNumber || '')})</div>` : ''}
        </div>
        <div class="card-actions">
          <a href="#/create?ent_id=${e.id}" class="btn btn-primary btn-sm" style="text-decoration:none;">+ Invoice</a>
          <button class="btn btn-ghost btn-sm edit-e-btn" data-id="${e.id}">Edit</button>
          ${!e.isDefault ? `<button class="btn btn-ghost btn-sm default-e-btn" data-id="${e.id}">Make Default</button>` : ''}
          <button class="btn btn-danger btn-sm del-e-btn" data-id="${e.id}">Delete</button>
        </div>
      </div>
    `).join('');

    grid.querySelectorAll('.edit-e-btn').forEach(b => b.addEventListener('click', () => openEntModal(b.dataset.id)));
    grid.querySelectorAll('.default-e-btn').forEach(b => b.addEventListener('click', () => setDefaultEnt(b.dataset.id)));
    grid.querySelectorAll('.del-e-btn').forEach(b => b.addEventListener('click', () => deleteEnt(b.dataset.id)));
  }

  const modal = document.getElementById('entModal');
  document.getElementById('addEntBtn').addEventListener('click', () => openEntModal());
  document.getElementById('closeEntModal').addEventListener('click', () => modal.classList.remove('show'));
  document.getElementById('cancelEntModal').addEventListener('click', () => modal.classList.remove('show'));

  function openEntModal(id){
    const title = document.getElementById('entModalTitle');
    title.textContent = id ? 'Edit Enterprise Profile' : 'Add Enterprise Profile';
    document.getElementById('e_id').value = id || '';

    if(id){
      const e = getAll(DB.enterprises).find(item => item.id === id);
      if(e){
        document.getElementById('me_name').value = e.name || '';
        document.getElementById('me_tagline').value = e.tagline || '';
        document.getElementById('me_email').value = e.email || '';
        document.getElementById('me_phone').value = e.phone || '';
        document.getElementById('me_address').value = e.address || '';
        document.getElementById('me_tax').value = e.taxId || '';
        document.getElementById('me_currency').value = e.currency || 'INR (₹)';
        document.getElementById('me_template').value = e.defaultTemplate || 'classic';
        document.getElementById('me_upi').value = e.upiId || '';
        document.getElementById('me_payurl').value = e.paymentUrl || '';
        document.getElementById('me_bank').value = e.bankName || '';
        document.getElementById('me_acc').value = e.accountNumber || '';
        document.getElementById('me_ifsc').value = e.ifscCode || '';
        document.getElementById('me_isdefault').checked = !!e.isDefault;
        logoHidden.value = e.logo || '';
        logoPreview.src = e.logo || "data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><rect fill='%23eef1ea' width='100' height='100'/><text x='50' y='55' text-anchor='middle' fill='%237c8c85' font-size='12'>No Logo</text></svg>";
      }
    } else {
      document.getElementById('entForm').reset();
      document.getElementById('e_id').value = '';
      logoHidden.value = '';
      logoPreview.src = "data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><rect fill='%23eef1ea' width='100' height='100'/><text x='50' y='55' text-anchor='middle' fill='%237c8c85' font-size='12'>No Logo</text></svg>";
    }
    modal.classList.add('show');
  }

  function setDefaultEnt(id){
    let enterprises = getAll(DB.enterprises);
    enterprises.forEach(e => e.isDefault = (e.id === id));
    setAll(DB.enterprises, enterprises);
    showToast('Default enterprise profile updated.');
    draw();
  }

  function deleteEnt(id){
    let enterprises = getAll(DB.enterprises);
    if(enterprises.length === 1){
      showToast('You must keep at least one enterprise profile.');
      return;
    }
    if(!confirm('Delete this enterprise profile?')) return;
    enterprises = enterprises.filter(e => e.id !== id);
    if(!enterprises.some(e => e.isDefault) && enterprises.length){
      enterprises[0].isDefault = true;
    }
    setAll(DB.enterprises, enterprises);
    showToast('Enterprise profile deleted.');
    draw();
  }

  document.getElementById('entForm').addEventListener('submit', (e) => {
    e.preventDefault();
    const id = document.getElementById('e_id').value;
    const name = document.getElementById('me_name').value.trim();
    if(!name) return;

    let enterprises = getAll(DB.enterprises);
    const isDefault = document.getElementById('me_isdefault').checked || enterprises.length === 0;

    if(isDefault){
      enterprises.forEach(item => item.isDefault = false);
    }

    const currVal = document.getElementById('me_currency').value;
    const symMatch = currVal.match(/\((.*?)\)/);
    const currencySymbol = symMatch ? symMatch[1] : '₹';

    const data = {
      id: id || uid('ent'),
      userId: user.id,
      name,
      tagline: document.getElementById('me_tagline').value.trim(),
      email: document.getElementById('me_email').value.trim(),
      phone: document.getElementById('me_phone').value.trim(),
      address: document.getElementById('me_address').value.trim(),
      taxId: document.getElementById('me_tax').value.trim(),
      currency: currVal,
      currencySymbol,
      defaultTemplate: document.getElementById('me_template').value,
      logo: logoHidden.value,
      upiId: document.getElementById('me_upi').value.trim(),
      paymentUrl: document.getElementById('me_payurl').value.trim(),
      bankName: document.getElementById('me_bank').value.trim(),
      accountNumber: document.getElementById('me_acc').value.trim(),
      ifscCode: document.getElementById('me_ifsc').value.trim(),
      isDefault
    };

    if(id){
      const idx = enterprises.findIndex(item => item.id === id);
      if(idx >= 0) enterprises[idx] = data;
    } else {
      enterprises.push(data);
    }

    setAll(DB.enterprises, enterprises);
    modal.classList.remove('show');
    showToast(id ? 'Enterprise profile updated.' : 'Enterprise profile created.');
    draw();
  });

  document.getElementById('entSearch').addEventListener('input', draw);
  draw();
}

/* ================================================================
   VIEW: PROFILE & SYSTEM BACKUP / RESTORE
   ================================================================ */
function renderProfile(){
  const user = currentUser();
  const content = `
    <div class="card profile-card">
      <div id="profileMsg" class="form-msg"></div>
      <form id="profileForm">
        <div class="field"><label>Your Full Name</label><input id="p_name" value="${escapeHTML(user.name)}"></div>
        <div class="field" id="f-p_email"><label>Login Email</label><input id="p_email" type="email" value="${escapeHTML(user.email)}"><div class="field-error">Enter a valid email address.</div></div>
        <div class="field"><label>Default Business Name</label><input id="p_business" value="${escapeHTML(user.businessName || '')}"></div>
        <div class="field"><label>Phone Number</label><input id="p_phone" value="${escapeHTML(user.phone || '')}"></div>
        <div class="field"><label>Business Address</label><input id="p_address" value="${escapeHTML(user.address || '')}"></div>
        <div class="field"><label>UPI ID (Default for Payment QR)</label><input id="p_upi" value="${escapeHTML(user.upiId || '')}" placeholder="yourname@bank"></div>
        <div class="form-actions" style="justify-content:flex-start;">
          <button type="submit" class="btn btn-primary">Save Profile Changes</button>
        </div>
      </form>
    </div>

    <!-- Authorised Signature Card -->
    <div class="card profile-card sig-pad-card" style="margin-top:20px;">
      <h3>Authorised Signature</h3>
      <p class="helper-text" style="margin-bottom:14px;">Draw your official signature below. It is automatically embedded into every invoice or estimate you issue.</p>
      <canvas id="sigPad" width="360" height="140"></canvas>
      <div style="display:flex;gap:10px;margin-top:12px;align-items:center;flex-wrap:wrap;">
        <button type="button" class="btn btn-ghost btn-sm" id="clearSigBtn">Clear</button>
        <button type="button" class="btn btn-primary btn-sm" id="saveSigBtn">Save Signature</button>
        <span class="helper-text" id="sigStatus" style="margin:0;"></span>
      </div>
    </div>

    <!-- Data Portability, Backup & Restore Card -->
    <div class="card profile-card" style="margin-top:20px;">
      <h3>Data Portability &amp; System Backup</h3>
      <p class="helper-text" style="margin-bottom:16px;">Download all your records as a secure JSON backup file, export your complete invoices ledger as CSV, or restore an earlier backup onto this machine.</p>

      <div style="display:flex;flex-wrap:wrap;gap:12px;align-items:center;">
        <button type="button" class="btn btn-ghost btn-sm" id="profBackupBtn">Export Full Backup (JSON)</button>
        <button type="button" class="btn btn-ghost btn-sm" id="profCsvBtn">Export All Invoices (CSV)</button>

        <label class="btn btn-ghost btn-sm" style="cursor:pointer;margin:0;">
          Restore Backup (JSON)
          <input type="file" id="restoreFileInput" accept=".json" style="display:none;">
        </label>
      </div>
    </div>
  `;

  document.getElementById('app').innerHTML = appShell('/profile', 'Account &amp; Data Settings', 'Preferences', content);
  mountShellEvents();

  // Profile Form submit
  document.getElementById('profileForm').addEventListener('submit', (e)=>{
    e.preventDefault();
    const emailField = document.getElementById('f-p_email');
    emailField.classList.remove('has-error');
    const email = document.getElementById('p_email').value.trim();
    if(!isValidEmail(email)){ emailField.classList.add('has-error'); return; }

    const users = getAll(DB.users);
    const dup = users.find(u => u.id !== user.id && u.email.toLowerCase() === email.toLowerCase());
    const msg = document.getElementById('profileMsg');
    if(dup){
      msg.textContent = 'That email is already used by another account.';
      msg.className = 'form-msg error show';
      return;
    }
    const idx = users.findIndex(u => u.id === user.id);
    users[idx] = {
      ...users[idx],
      name: document.getElementById('p_name').value.trim() || users[idx].name,
      email,
      businessName: document.getElementById('p_business').value.trim(),
      phone: document.getElementById('p_phone').value.trim(),
      address: document.getElementById('p_address').value.trim(),
      upiId: document.getElementById('p_upi').value.trim(),
    };
    setAll(DB.users, users);
    msg.textContent = 'Profile updated successfully.';
    msg.className = 'form-msg success show';
    showToast('Profile saved.');
  });

  // Signature Pad
  const sigCanvas = document.getElementById('sigPad');
  const pad = initSignaturePad(sigCanvas, user.signature || '');
  const sigStatus = document.getElementById('sigStatus');
  if(user.signature){ sigStatus.textContent = 'Saved signature loaded.'; }

  document.getElementById('clearSigBtn').addEventListener('click', ()=>{
    pad.clear();
    sigStatus.textContent = '';
  });
  document.getElementById('saveSigBtn').addEventListener('click', ()=>{
    const users = getAll(DB.users);
    const idx = users.findIndex(u => u.id === user.id);
    users[idx].signature = pad.isEmpty() ? '' : pad.toDataURL();
    setAll(DB.users, users);
    sigStatus.textContent = pad.isEmpty() ? 'Signature cleared.' : 'Signature saved.';
    showToast(pad.isEmpty() ? 'Signature cleared.' : 'Signature saved.');
  });

  // Data Management actions
  document.getElementById('profBackupBtn').addEventListener('click', exportFullBackupJSON);
  document.getElementById('profCsvBtn').addEventListener('click', ()=>{
    const userInvoices = getAll(DB.invoices).filter(i => i.userId === user.id);
    exportInvoicesToCSV(userInvoices);
  });

  document.getElementById('restoreFileInput').addEventListener('change', (e)=>{
    const file = e.target.files[0];
    if(!file) return;
    const reader = new FileReader();
    reader.onload = (evt)=>{
      restoreBackupJSON(evt.target.result);
    };
    reader.readAsText(file);
  });
}

/* ================================================================
   VIEW: ITEM CATALOG / INVENTORY (#/items)
   ================================================================ */
function renderCatalog(){
  const user = currentUser();
  const content = `
    <div class="filter-bar">
      <input type="text" id="catSearch" placeholder="Search catalog items by name, HSN, or description...">
      <button class="btn btn-primary" id="openAddItemModal" style="white-space:nowrap;">+ Add New Item</button>
      <button class="btn btn-ghost" id="exportCatalogCsvBtn" style="white-space:nowrap;">Export Catalog (CSV)</button>
    </div>

    <!-- Catalog Summary KPIs -->
    <div class="stat-grid" style="margin-bottom:24px;">
      <div class="card stat-card accent">
        <div class="label">Total Catalog Items</div>
        <div class="value mono" id="catTotalCount">0</div>
        <div class="helper-text">Ready for 1-click billing</div>
      </div>
      <div class="card stat-card">
        <div class="label">Average Unit Price</div>
        <div class="value mono" id="catAvgPrice">₹0.00</div>
        <div class="helper-text">Standard inventory rate</div>
      </div>
    </div>

    <div class="catalog-grid" id="catalogGrid"></div>

    <!-- Add / Edit Item Modal -->
    <div class="modal-overlay" id="itemModal">
      <div class="modal-card">
        <div class="modal-head">
          <h2 id="itemModalTitle">Add Catalog Item</h2>
          <button class="modal-close" id="closeItemModal">&times;</button>
        </div>
        <form id="itemForm">
          <input type="hidden" id="edit_item_id">
          <div class="field">
            <label>Item Name / Service Title *</label>
            <input id="item_name" required placeholder="e.g. Full-Stack Web Development">
          </div>
          <div class="field">
            <label>Item Description / Scope</label>
            <textarea id="item_desc" rows="2" placeholder="e.g. End-to-end custom responsive design and API implementation."></textarea>
          </div>
          <div class="field-row">
            <div class="field">
              <label>HSN / SAC Code</label>
              <input id="item_hsn" class="mono" placeholder="998314">
            </div>
            <div class="field">
              <label>Unit of Measure</label>
              <select id="item_unit">
                <option value="pcs">Pieces (pcs)</option>
                <option value="hrs">Hours (hrs)</option>
                <option value="days">Days (days)</option>
                <option value="mo">Months (mo)</option>
                <option value="screens">Screens</option>
                <option value="units">Units</option>
              </select>
            </div>
          </div>
          <div class="field-row">
            <div class="field">
              <label>Default Unit Price (₹) *</label>
              <input type="number" id="item_price" required min="0" step="0.01" placeholder="1500.00">
            </div>
            <div class="field">
              <label>Default GST / Tax Rate (%)</label>
              <input type="number" id="item_tax" min="0" max="100" step="0.1" value="18" placeholder="18">
            </div>
          </div>
          <div class="form-actions" style="margin-top:20px;">
            <button type="button" class="btn btn-ghost" id="cancelItemBtn">Cancel</button>
            <button type="submit" class="btn btn-primary" id="saveItemBtn">Save Item</button>
          </div>
        </form>
      </div>
    </div>
  `;

  document.getElementById('app').innerHTML = appShell('/items', 'Product &amp; Service Catalog', 'Inventory', content);
  mountShellEvents();

  function draw(){
    const q = (document.getElementById('catSearch')?.value || '').trim().toLowerCase();
    let items = getAll(DB.items).filter(it => it.userId === user.id);
    if(q){
      items = items.filter(it =>
        it.name.toLowerCase().includes(q) ||
        (it.desc && it.desc.toLowerCase().includes(q)) ||
        (it.hsn && it.hsn.toLowerCase().includes(q))
      );
    }

    const grid = document.getElementById('catalogGrid');
    const totalCountEl = document.getElementById('catTotalCount');
    const avgPriceEl = document.getElementById('catAvgPrice');

    if(totalCountEl) totalCountEl.textContent = items.length;
    if(avgPriceEl){
      const sum = items.reduce((s, it) => s + (Number(it.price) || 0), 0);
      avgPriceEl.textContent = fmtMoney(items.length ? (sum / items.length) : 0);
    }

    if(!items.length){
      grid.innerHTML = `<div class="card" style="grid-column:1/-1;padding:40px;text-align:center;color:var(--ink-soft);">No catalog items found. Click "+ Add New Item" to populate your inventory.</div>`;
      return;
    }

    grid.innerHTML = items.map(it => `
      <div class="catalog-card">
        <div>
          <div style="display:flex;justify-content:space-between;align-items:flex-start;gap:8px;">
            <h3>${escapeHTML(it.name)}</h3>
            ${it.hsn ? `<span class="badge-category cat-hardware mono" style="font-size:10.5px;">HSN: ${escapeHTML(it.hsn)}</span>` : ''}
          </div>
          <p>${escapeHTML(it.desc || 'No description provided.')}</p>
        </div>
        <div>
          <div class="catalog-meta">
            <div>
              <div class="catalog-price">${fmtMoney(it.price)}</div>
              <div style="font-size:11px;color:var(--ink-faint);">per ${escapeHTML(it.unit || 'unit')} (Tax: ${it.taxRate ?? 18}%)</div>
            </div>
            <div style="display:flex;gap:6px;">
              <button class="btn btn-ghost btn-sm edit-item-btn" data-id="${it.id}">Edit</button>
              <button class="btn btn-danger btn-sm delete-item-btn" data-id="${it.id}">&times;</button>
            </div>
          </div>
        </div>
      </div>
    `).join('');

    // Attach card actions
    document.querySelectorAll('.edit-item-btn').forEach(btn => {
      btn.addEventListener('click', ()=>{
        const it = items.find(x => x.id === btn.getAttribute('data-id'));
        if(!it) return;
        document.getElementById('edit_item_id').value = it.id;
        document.getElementById('item_name').value = it.name;
        document.getElementById('item_desc').value = it.desc || '';
        document.getElementById('item_hsn').value = it.hsn || '';
        document.getElementById('item_unit').value = it.unit || 'pcs';
        document.getElementById('item_price').value = it.price;
        document.getElementById('item_tax').value = it.taxRate !== undefined ? it.taxRate : 18;
        document.getElementById('itemModalTitle').textContent = 'Edit Catalog Item';
        document.getElementById('itemModal').classList.add('show');
      });
    });

    document.querySelectorAll('.delete-item-btn').forEach(btn => {
      btn.addEventListener('click', ()=>{
        const id = btn.getAttribute('data-id');
        if(!confirm('Delete this item from your catalog?')) return;
        let allItems = getAll(DB.items);
        allItems = allItems.filter(x => x.id !== id);
        setAll(DB.items, allItems);
        showToast('Catalog item removed.');
        draw();
      });
    });
  }

  draw();
  document.getElementById('catSearch')?.addEventListener('input', draw);

  const modal = document.getElementById('itemModal');
  document.getElementById('openAddItemModal').addEventListener('click', ()=>{
    document.getElementById('itemForm').reset();
    document.getElementById('edit_item_id').value = '';
    document.getElementById('itemModalTitle').textContent = 'Add Catalog Item';
    modal.classList.add('show');
  });

  const closeModal = ()=> modal.classList.remove('show');
  document.getElementById('closeItemModal').addEventListener('click', closeModal);
  document.getElementById('cancelItemBtn').addEventListener('click', closeModal);

  document.getElementById('itemForm').addEventListener('submit', (e)=>{
    e.preventDefault();
    const id = document.getElementById('edit_item_id').value;
    const name = document.getElementById('item_name').value.trim();
    const desc = document.getElementById('item_desc').value.trim();
    const hsn = document.getElementById('item_hsn').value.trim();
    const unit = document.getElementById('item_unit').value;
    const price = Number(document.getElementById('item_price').value) || 0;
    const taxRate = Number(document.getElementById('item_tax').value) || 0;

    let items = getAll(DB.items);
    if(id){
      const idx = items.findIndex(x => x.id === id);
      if(idx !== -1){
        items[idx] = { ...items[idx], name, desc, hsn, unit, price, taxRate };
      }
    } else {
      items.push({
        id: uid('item'),
        userId: user.id,
        name, desc, hsn, unit, price, taxRate,
        createdAt: Date.now()
      });
    }

    setAll(DB.items, items);
    closeModal();
    showToast(id ? 'Catalog item updated.' : 'Item added to catalog.');
    draw();
  });

  document.getElementById('exportCatalogCsvBtn').addEventListener('click', ()=>{
    const items = getAll(DB.items).filter(it => it.userId === user.id);
    const headers = ['Item Name', 'Description', 'HSN/SAC', 'Unit', 'Price', 'Tax Rate %'];
    const rows = items.map(it => [
      it.name, it.desc || '', it.hsn || '', it.unit || 'pcs', it.price, it.taxRate ?? 18
    ].map(v => `"${String(v).replace(/"/g, '""')}"`).join(','));

    const csvContent = 'data:text/csv;charset=utf-8,' + [headers.join(','), ...rows].join('\n');
    const link = document.createElement('a');
    link.href = encodeURI(csvContent);
    link.download = `ledgerly-catalog-${todayISO()}.csv`;
    link.click();
    showToast('Catalog exported to CSV.');
  });
}

/* ================================================================
   VIEW: BUSINESS EXPENSE TRACKER (#/expenses)
   ================================================================ */
function renderExpenses(){
  const user = currentUser();
  const content = `
    <div class="filter-bar">
      <input type="text" id="expSearch" placeholder="Search expenses by vendor, title, or reference...">
      <select id="expCategoryFilter">
        <option value="">All Categories</option>
        <option value="Software">Software &amp; Tools</option>
        <option value="Hosting">Hosting &amp; Cloud</option>
        <option value="Office">Office &amp; Coworking</option>
        <option value="Marketing">Marketing &amp; Ads</option>
        <option value="Hardware">Hardware &amp; Equipment</option>
        <option value="Misc">Miscellaneous</option>
      </select>
      <button class="btn btn-primary" id="openAddExpModal" style="white-space:nowrap;">+ Log Expense</button>
      <button class="btn btn-ghost" id="exportExpCsvBtn" style="white-space:nowrap;">Export CSV</button>
    </div>

    <!-- Expenses Summary KPIs -->
    <div class="stat-grid" style="margin-bottom:24px;">
      <div class="card stat-card">
        <div class="label">Total Logged Expenses</div>
        <div class="value mono" id="kpiTotalExpenses" style="color:#b82d18;">₹0.00</div>
        <div class="helper-text" id="kpiExpCount">0 Receipts Recorded</div>
      </div>
      <div class="card stat-card">
        <div class="label">This Month's Spending</div>
        <div class="value mono" id="kpiMonthExpenses" style="color:#b82d18;">₹0.00</div>
        <div class="helper-text" id="kpiMonthLabel">Current Month</div>
      </div>
      <div class="card stat-card accent">
        <div class="label">Top Spending Category</div>
        <div class="value" id="kpiTopCategory" style="font-size:18px;">—</div>
        <div class="helper-text">Highest operational outflow</div>
      </div>
    </div>

    <div class="card" style="padding:22px 24px;">
      <table class="ledger-table">
        <thead>
          <tr>
            <th>Date</th>
            <th>Expense / Title</th>
            <th>Category</th>
            <th>Vendor / Payee</th>
            <th>Payment Method</th>
            <th>Ref / Invoice #</th>
            <th class="num">Amount</th>
            <th style="width:70px;"></th>
          </tr>
        </thead>
        <tbody id="expensesBody"></tbody>
      </table>
    </div>

    <!-- Add Expense Modal -->
    <div class="modal-overlay" id="expModal">
      <div class="modal-card">
        <div class="modal-head">
          <h2 id="expModalTitle">Log Business Expense</h2>
          <button class="modal-close" id="closeExpModal">&times;</button>
        </div>
        <form id="expForm">
          <input type="hidden" id="edit_exp_id">
          <div class="field">
            <label>Expense Title / Purpose *</label>
            <input id="exp_title" required placeholder="e.g. AWS Cloud Hosting">
          </div>
          <div class="field-row">
            <div class="field">
              <label>Category *</label>
              <select id="exp_category">
                <option value="Software">Software &amp; Tools</option>
                <option value="Hosting">Hosting &amp; Cloud</option>
                <option value="Office">Office &amp; Coworking</option>
                <option value="Marketing">Marketing &amp; Ads</option>
                <option value="Hardware">Hardware &amp; Equipment</option>
                <option value="Misc">Miscellaneous</option>
              </select>
            </div>
            <div class="field">
              <label>Amount (₹) *</label>
              <input type="number" id="exp_amount" required min="0" step="0.01" placeholder="1500.00">
            </div>
          </div>
          <div class="field-row">
            <div class="field">
              <label>Expense Date *</label>
              <input type="date" id="exp_date" required value="${todayISO()}">
            </div>
            <div class="field">
              <label>Vendor / Payee</label>
              <input id="exp_vendor" placeholder="e.g. Amazon Web Services">
            </div>
          </div>
          <div class="field-row">
            <div class="field">
              <label>Payment Method</label>
              <select id="exp_method">
                <option value="Credit Card">Credit Card</option>
                <option value="UPI">UPI</option>
                <option value="Net Banking">Net Banking</option>
                <option value="Debit Card">Debit Card</option>
                <option value="Cash">Cash</option>
              </select>
            </div>
            <div class="field">
              <label>Receipt / Transaction Ref #</label>
              <input id="exp_ref" class="mono" placeholder="INV-2026-991">
            </div>
          </div>
          <div class="form-actions" style="margin-top:20px;">
            <button type="button" class="btn btn-ghost" id="cancelExpBtn">Cancel</button>
            <button type="submit" class="btn btn-primary" id="saveExpBtn">Save Expense</button>
          </div>
        </form>
      </div>
    </div>
  `;

  document.getElementById('app').innerHTML = appShell('/expenses', 'Business Expense Tracker', 'Finances', content);
  mountShellEvents();

  function draw(){
    const q = (document.getElementById('expSearch')?.value || '').trim().toLowerCase();
    const cat = document.getElementById('expCategoryFilter')?.value || '';
    let expenses = getAll(DB.expenses).filter(e => e.userId === user.id)
      .sort((a,b)=> new Date(b.date) - new Date(a.date));

    // Compute KPIs
    const totalExp = expenses.reduce((s, e) => s + (Number(e.amount) || 0), 0);
    const curMonthKey = todayISO().slice(0, 7);
    const monthExp = expenses.filter(e => (e.date || '').startsWith(curMonthKey))
      .reduce((s, e) => s + (Number(e.amount) || 0), 0);

    const catSums = {};
    expenses.forEach(e => {
      catSums[e.category] = (catSums[e.category] || 0) + (Number(e.amount) || 0);
    });
    const topCat = Object.entries(catSums).sort((a,b)=> b[1] - a[1])[0];

    document.getElementById('kpiTotalExpenses').textContent = fmtMoney(totalExp);
    document.getElementById('kpiExpCount').textContent = `${expenses.length} Receipts Logged`;
    document.getElementById('kpiMonthExpenses').textContent = fmtMoney(monthExp);
    document.getElementById('kpiTopCategory').textContent = topCat ? `${topCat[0]} (${fmtMoney(topCat[1])})` : 'None';

    if(cat) expenses = expenses.filter(e => e.category === cat);
    if(q){
      expenses = expenses.filter(e =>
        e.title.toLowerCase().includes(q) ||
        (e.vendor && e.vendor.toLowerCase().includes(q)) ||
        (e.ref && e.ref.toLowerCase().includes(q))
      );
    }

    const tbody = document.getElementById('expensesBody');
    if(!expenses.length){
      tbody.innerHTML = `<tr class="empty-row"><td colspan="8">No expenses found matching filter criteria.</td></tr>`;
      return;
    }

    const catClassMap = {
      'Software': 'cat-software',
      'Hosting': 'cat-hosting',
      'Office': 'cat-office',
      'Marketing': 'cat-marketing',
      'Hardware': 'cat-hardware',
      'Misc': 'cat-misc'
    };

    tbody.innerHTML = expenses.map(e => `
      <tr>
        <td class="mono">${fmtDate(e.date)}</td>
        <td><strong>${escapeHTML(e.title)}</strong></td>
        <td><span class="badge-category ${catClassMap[e.category] || 'cat-misc'}">${escapeHTML(e.category)}</span></td>
        <td>${escapeHTML(e.vendor || '—')}</td>
        <td>${escapeHTML(e.method || 'Direct')}</td>
        <td class="mono" style="font-size:12px;">${escapeHTML(e.ref || '—')}</td>
        <td class="num mono font-semibold" style="color:#b82d18;">−${fmtMoney(e.amount)}</td>
        <td style="text-align:right;">
          <button class="btn btn-danger btn-sm delete-exp-btn" data-id="${e.id}">&times;</button>
        </td>
      </tr>
    `).join('');

    document.querySelectorAll('.delete-exp-btn').forEach(btn => {
      btn.addEventListener('click', ()=>{
        const id = btn.getAttribute('data-id');
        if(!confirm('Delete this expense record?')) return;
        let allExp = getAll(DB.expenses);
        allExp = allExp.filter(x => x.id !== id);
        setAll(DB.expenses, allExp);
        showToast('Expense record deleted.');
        draw();
      });
    });
  }

  draw();
  document.getElementById('expSearch')?.addEventListener('input', draw);
  document.getElementById('expCategoryFilter')?.addEventListener('change', draw);

  const modal = document.getElementById('expModal');
  document.getElementById('openAddExpModal').addEventListener('click', ()=>{
    document.getElementById('expForm').reset();
    document.getElementById('exp_date').value = todayISO();
    document.getElementById('edit_exp_id').value = '';
    modal.classList.add('show');
  });

  const closeModal = ()=> modal.classList.remove('show');
  document.getElementById('closeExpModal').addEventListener('click', closeModal);
  document.getElementById('cancelExpBtn').addEventListener('click', closeModal);

  document.getElementById('expForm').addEventListener('submit', (e)=>{
    e.preventDefault();
    const title = document.getElementById('exp_title').value.trim();
    const category = document.getElementById('exp_category').value;
    const amount = Number(document.getElementById('exp_amount').value) || 0;
    const date = document.getElementById('exp_date').value || todayISO();
    const vendor = document.getElementById('exp_vendor').value.trim();
    const method = document.getElementById('exp_method').value;
    const ref = document.getElementById('exp_ref').value.trim();

    let exps = getAll(DB.expenses);
    exps.unshift({
      id: uid('exp'),
      userId: user.id,
      title, category, amount, date, vendor, method, ref,
      createdAt: Date.now()
    });

    setAll(DB.expenses, exps);
    closeModal();
    showToast('Business expense recorded.');
    draw();
  });

  document.getElementById('exportExpCsvBtn').addEventListener('click', ()=>{
    const expenses = getAll(DB.expenses).filter(e => e.userId === user.id);
    const headers = ['Date', 'Title', 'Category', 'Vendor', 'Method', 'Ref', 'Amount'];
    const rows = expenses.map(e => [
      e.date, e.title, e.category, e.vendor || '', e.method || '', e.ref || '', e.amount
    ].map(v => `"${String(v).replace(/"/g, '""')}"`).join(','));

    const csvContent = 'data:text/csv;charset=utf-8,' + [headers.join(','), ...rows].join('\n');
    const link = document.createElement('a');
    link.href = encodeURI(csvContent);
    link.download = `ledgerly-expenses-${todayISO()}.csv`;
    link.click();
    showToast('Expenses exported to CSV.');
  });
}
