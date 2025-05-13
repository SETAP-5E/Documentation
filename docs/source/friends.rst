.. _friends-page:

Friends Page Documentation
==========================

Usage
-----
The **Friends** page lets users view, search, and paginate through their list of connected players.

Typical workflow:

#. Navigate to **Friends** via the main menu.  
#. (Optional) Enter filter criteria:  
   - **Player ID**  
   - **Player Name**  
   - **Location**  
#. Click **🔍 Search** to apply filters.  
#. Click **♻️ Reset** to clear filters and reload full list.  
#. Browse results in the table; use **Show Rows** to change page size.  
#. Use **Previous**/ **Next** buttons to navigate pages.  
#. Click on a row or button (if implemented) to view friend details or send requests.

Maintenance
-----------
This page is implemented with static HTML, CSS for styling, and JavaScript for dynamic behavior.

- **HTML** (`Friends.html`):  
  - Semantic structure: `<header>` (logo, nav, logout), decorative underline, `<main>` with filters, table, pagination, modal overlay, and `<footer>`.  
  :contentReference[oaicite:0]{index=0}:contentReference[oaicite:1]{index=1}  
- **CSS** (`Friends.css`):  
  - Full-viewport gradient background, flexbox header, centered `.container` with white card, styled form controls, table styling (striped rows, bold cells), buttons, and modal.  
  :contentReference[oaicite:2]{index=2}:contentReference[oaicite:3]{index=3}  
- **JavaScript** (`friends.js`):  
  - On load, fetches friend list from backend and populates the table.  
  - Implements **Search** (reads filter inputs, requests filtered data), **Reset** (clears inputs/reloads), and **Pagination** (requests specific pages).  
  - Handles display and hiding of the modal for error or status messages.  

**Dependencies**:

- Modern browsers with Fetch API, flexbox, CSS gradients, and ES6 support.  
- Assets: `assets/images/logo.png` for branding.  

**Build & Deployment**:

No build step required. Serve `Friends.html`, `Friends.css`, `friends.js`, and assets from any static-file host (e.g. GitHub Pages, NGINX).

Comments
--------
Implementation Comments
~~~~~~~~~~~~~~~~~~~~~~~
- **Accessibility**  
  - Table lacks `role="table"`/`aria-labelledby`; consider adding ARIA roles and keyboard focus styles for pagination controls.  
  - Filter inputs should be grouped in a `<fieldset>` with a `<legend>` for screen-reader context.  
- **Performance**  
  - Debounce rapid clicks on **Search** to avoid redundant API calls.  
  - Consider virtual scrolling for large datasets instead of fixed pagination.  
- **Error Handling**  
  - Fetch errors are shown via modal; ensure timeouts and 500-level errors produce clear messages.  
- **Responsive Design**  
  - Test on narrow viewports; the table may overflow—consider horizontal scroll or card layout fallback.

Interface Comments
~~~~~~~~~~~~~~~~~~~
**Endpoint:**  
