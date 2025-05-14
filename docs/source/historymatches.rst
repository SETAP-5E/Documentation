.. _match-history:

Match History Page Documentation
================================

Usage
-----
The **Match History** page enables users to review past matches, apply filters (date, player, winner, court), and navigate through paginated results.

Typical workflow:

#. Navigate to **History Matches** via the main menu.  
#. (Optional) Set any of the following filters:  
   - **Date**  
   - **Player** (participant name)  
   - **Winner**  
   - **Court**  
#. Click 🔍 **Search** to apply filters.  
#. Click ♻️ **Reset** to clear filters and reload all records.  
#. Review the results in the table.  
#. Use **Show Rows** dropdown to change the number of rows per page.  
#. Click ← **Previous** / **Next** → to navigate pages.  
#. Click **Close** on the modal to dismiss any messages.

Maintenance
-----------
This page is built with static HTML, CSS, and JavaScript.

- **HTML** (`History_matches.html`):  
  - Defines semantic page structure: `<header>`, `<nav>`, `<main>`, `<table>`, modal overlay, and `<footer>`.  
  - Filter inputs use `<input type="date">` and `<input type="text">` with clear `id` attributes for JS hooks. :contentReference[oaicite:0]{index=0}:contentReference[oaicite:1]{index=1}  
- **CSS** (`history_matches.css`):  
  - Page uses a full-viewport gradient background and flex-column layout.  
  - Styled header with logo and navigation; `.navbar-underline` as decorative accent.  
  - `.container` card holds filters, table, and pagination controls.  
  - Table styling includes zebra striping and responsive width.  
  - Modal overlay (`.modal-overlay`) and box styled for centered dialogs. :contentReference[oaicite:2]{index=2}:contentReference[oaicite:3]{index=3}  
- **JavaScript** (`history_matches.js`):  
  - On page load, issues  
    ``GET /api/history?page=1&per_page=5``  
    and populates `<tbody id="matchesTableBody">`.  
  - **Search**: reads filter values and re-fetches with query parameters  
    `date`, `player`, `winner`, `court`.  
  - **Reset**: clears filter inputs and reloads first page.  
  - **Pagination**: updates page number and row count on control events.  
  - **Modal**: toggles `.modal-overlay` to display status or error messages.

Comments
--------
Implementation Comments
~~~~~~~~~~~~~~~~~~~~~~~
- **Accessibility**  
  - Table should include `role="table"` and use `<caption>` or `aria-label`.  
  - Pagination buttons lack `aria-disabled`; add for disabled states.  
  - Modal requires `role="dialog"` and `aria-modal="true"`.  
- **Error Handling**  
  - Network or server errors should display descriptive messages instead of silent failures.  
  - Consider inline alerts above the table for transient errors.  
- **Performance**  
  - Debounce filter inputs to avoid excessive API calls on rapid clicks.  
  - Lazy-load table rows if “All” is selected to prevent browser slowdown.  
- **Time Zones**  
  - Date inputs use local timezone; server must normalize to UTC for consistency.

Interface Comments
~~~~~~~~~~~~~~~~~~~
**List Match History**  
