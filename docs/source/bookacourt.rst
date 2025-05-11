.. _book-a-court:

Book a Court Page Documentation
================================

Usage
-----
The **Book a Court** page enables users to reserve a sports court by entering their personal details, selecting a date & time, and choosing a location.  

Typical workflow:

#. User navigates to **Book a Court** via the main menu.  
#. User fills in **Name**, **Email**, and selects a **Country Code** + enters **Phone Number**.  
#. User picks a **Match Date**; the **Match Time** dropdown is then populated with available slots.  
#. User selects a **Location** from the courts list.  
#. User clicks **Book Court**; a modal confirms success or shows errors.  

Maintenance
-----------
This page is composed of static HTML, CSS for styling, and JavaScript for dynamic behaviour.

- **HTML** (`Book_a_court.html`):  
  - Semantic structure: `<header>`, `<nav>`, `<main>`, `<form>`, modal overlay, `<footer>`.  
  - Relies on HTML5 form validation via `required` attributes.  
- **CSS** (`Book_a_court.css`):  
  - Responsive layout using flexbox and percentage widths.  
  - Themed styling: gradient backgrounds, centered container, styled form controls, custom dropdown, modal.  
- **JavaScript** (`book_a_court.js`):  
  - Wrapped in an IIFE on `DOMContentLoaded` to avoid global scope pollution.  
  - **Dynamic court list**: fetches available courts on load and populates the **Location** `<select>`.  
  - **Time slot loading**: on date or location change, queries  
    ``GET /api/book/blocked?court_id={id}&booking_date={YYYY-MM-DD}``  
    to filter out blocked times and repopulates the **Match Time** dropdown.  
  - **Form submission**: intercepts submit, sends data via `fetch`, and shows modal with server response.  
  - **Zoom fallback**: applies `document.body.style.zoom = "140%"`, with CSS transform fallback for browsers without `zoom` support.

**Dependencies**:

- Browser must support HTML5, Fetch API, and Flexbox.  
- Flag images and logo loaded from `assets/flags/*.png` and `assets/images/logo.png`.  

**Build & Deployment**:

No build tool required. Deploy by hosting these static files (HTML, CSS, JS, assets) on any web server (e.g., NGINX, GitHub Pages).

Comments
--------
Implementation Comments
~~~~~~~~~~~~~~~~~~~~~~~
- **Accessibility**:  
  - The custom country dropdown is CSS-only on `:hover`; it lacks keyboard navigation and ARIA attributes.  
  - Recommend adding `role="listbox"`/`role="option"` and managing `aria-expanded`/`aria-activedescendant`.  
- **Error handling**:  
  - Current code logs fetch errors to console; consider displaying a user-friendly message in the modal.  
- **Performance**:  
  - Modal markup is always loaded; could be injected on demand to reduce initial DOM size.  
- **Time zone**:  
  - Date & time inputs assume user locale; server should validate and normalize to UTC.

Interface Comments
~~~~~~~~~~~~~~~~~~~
Form POST endpoint:  
