.. _view-bookings:

View / My Bookings Page
================================

Usage
-----
The **View Bookings** page lets users review, filter, edit, or cancel their existing court reservations.

Typical workflow:

#. Navigate to **My Bookings** via the main menu.  
#. (Optional) Filter by **Date** or **Court Name**; click 🔍 **Search**.  
#. Click ♻️ **Reset** to clear filters and reload all bookings.  
#. Browse bookings in the table; change **Show Rows** to adjust page size.  
#. Use ← **Previous** / **Next** → to navigate pages.  
#. Click ✏️ **Edit** on a row to modify date/time/location.  
#. Click ❌ **Cancel** on a row to delete the booking (confirmation in modal).

Maintenance
-----------
This page comprises static HTML, CSS, and JavaScript:

- **HTML** (`My_bookings.html`):  
  - `<header>` with logo, navigation, and **Logout** button.  
  - Filter section with `<input type="date">` and `<input type="text">`.  
  - `<table>` for bookings, with `<thead>` and dynamic `<tbody id="bookingsTable">`.  
  - Pagination controls: `<select id="rowCount">` and buttons.  
  - Modal overlay (`.modal-overlay`) containing:  
    - `<form id="editBookingForm">` for editing.  
    - `<div id="modalActions">` for cancel confirmation.  
  - `<footer>` with copyright. :contentReference[oaicite:0]{index=0}:contentReference[oaicite:1]{index=1}

- **CSS** (`My_bookings.css`):  
  - Full-viewport gradient background & flex layout.  
  - Styled header, nav links, and **Logout** button.  
  - `.container` card with white background for contrast.  
  - Filter controls and buttons with consistent theming.  
  - Table styling (striped rows, responsive).  
  - Pagination buttons and row-count selector.  
  - Modal overlay & box with centered layout. :contentReference[oaicite:2]{index=2}:contentReference[oaicite:3]{index=3}

- **JavaScript** (`My_bookings.js`):  
  - On load: fetches all bookings via  
    ``GET /api/bookings?page=1&per_page=5``  
    and populates `#bookingsTable`.  
  - **Filtering**: on 🔍 **Search**, re-fetch with `filterDate` & `filterCourt` as query parameters.  
  - **Pagination**: listens to page/nav buttons and `#rowCount` changes.  
  - **Edit**: opens `#editBookingForm`, fetches available time slots for selected date & court, submits changes via  
    ``PUT /api/bookings/{bookingId}``.  
  - **Cancel**: shows confirm buttons in `#modalActions`, sends  
    ``DELETE /api/bookings/{bookingId}``.  
  - Handles modal show/hide and error/success messages.

**Dependencies**:

- Modern browsers with Fetch API, ES6, Flexbox, and CSS gradients.  
- Logo asset at `assets/images/logo.png`.

**Build & Deployment**:

Serve `My_bookings.html`, `My_bookings.css`, `My_bookings.js`, and assets on any static host (e.g., NGINX, GitHub Pages).

Comments
--------
Implementation Comments
~~~~~~~~~~~~~~~~~~~~~~~
- **Accessibility**  
  - Add `role="table"` to the table and `aria-label` to pagination controls.  
  - Use `<fieldset>`/`<legend>` for filter inputs.  
  - Ensure modal uses `role="dialog"` and `aria-modal="true"`.  
- **Error Handling**  
  - Currently displays errors only in modal text; consider inline alerts for network failures.  
- **Performance**  
  - Debounce filter input changes to avoid excessive API calls.  
  - Inject modal markup on demand instead of always in DOM.  
- **Time Zone**  
  - Date/time inputs rely on user locale; server must normalize to UTC.

Interface Comments
~~~~~~~~~~~~~~~~~~~
**List Bookings**  
