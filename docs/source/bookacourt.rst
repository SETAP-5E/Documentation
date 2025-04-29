.. _book-a-court:

Book a Court Page Documentation
================================

Usage
-----
The **Book a Court** page allows users to reserve a sports court by providing personal details and scheduling information.

Typical workflow:

#. Navigate via the main menu to **Book a Court**.
#. Fill in personal information (name, email).
#. Select country code and enter a phone number.
#. Choose match date and time using date/time pickers.
#. Select a court location from the dropdown.
#. Click **Book Court** to submit the form.

Example form submission:

.. code-block:: http

   POST /reserve-court HTTP/1.1
   Host: example.com
   Content-Type: application/x-www-form-urlencoded

   name=Jane+Doe&email=jane%40example.com \
   &country_code=%2B44&phone_number=7123456789 \
   &match_date=2025-05-10&match_time=18%3A30&location=stadium_2

Maintenance
-----------
This page is implemented with static HTML, CSS for styling, and JavaScript for interactivity.

- **HTML** (`Book_a_court.html`):
  - Defines semantic structure (`<header>`, `<nav>`, `<form>`, modal overlay, `<footer>`).
  - Uses HTML5 form validation via `required` attributes.
- **CSS** (`Book_a_court.css`):
  - Styles layout, form elements, navigation bar, custom phone-code dropdown, and modal.
  - Responsive design via `%` widths and flexbox.
- **JavaScript** (`app.js`):
  - Drives country-code dropdown logic.
  - Synchronises hidden input `country_code`.
  - Toggles modal overlay to show booking confirmation.

**Dependencies**:

- Flag icons loaded via CDN in image tags.
- Modern browser support for HTML5 and flexbox.

**Build & Deployment**:

No build step required. Deploy by serving static files from any web server (NGINX, GitHub Pages, etc.).

Component Breakdown
~~~~~~~~~~~~~~~~~~~
- **header & nav**  
  Navigation links to all app pages.
- **form.group**  
  Grouped inputs for capturing user and match details.
- **.phone-group & .custom-dropdown**  
  Flex layout for phone input and country-code selector.
- **.modal-overlay & .modal-box**  
  Hidden overlay and centered box for booking confirmation.

Comments
--------
Code Comments
~~~~~~~~~~~~~
- Semantic HTML tags improve accessibility (e.g., `<nav>`, `<main>`).
- CSS class names follow a clear, BEM-inspired convention (e.g., `.form-group`, `.phone-group`).
- `data-code` and `data-flag` attributes in dropdown items drive JS logic.

Implementation Comments
~~~~~~~~~~~~~~~~~~~~~~~
- **Accessibility**:  
  Current CSS-only dropdown `:hover` show/hide lacks keyboard support.  
  → Recommend adding `aria-expanded` on the button and JS key event handling.
- **Performance**:  
  Modal markup is always present; consider injecting via JS to reduce initial DOM size.
- **Validation**:  
  Client-side HTML5 checks are useful but server must validate all fields and return JSON errors.

Interface Comments
~~~~~~~~~~~~~~~~~~~
:URL: `/reserve-court`  (method: POST)  
:Content-Type: `application/x-www-form-urlencoded`

+----------------+-----------------------------------------------+
| Parameter      | Description                                   |
+================+===============================================+
| `name`         | User’s full name (string, required)           |
+----------------+-----------------------------------------------+
| `email`        | User’s email address (string, required)       |
+----------------+-----------------------------------------------+
| `country_code` | International dialing code (string, hidden)    |
+----------------+-----------------------------------------------+
| `phone_number` | Local phone number (string, required)         |
+----------------+-----------------------------------------------+
| `match_date`   | Desired date (YYYY-MM-DD, required)           |
+----------------+-----------------------------------------------+
| `match_time`   | Desired time (HH:MM, required)                |
+----------------+-----------------------------------------------+
| `location`     | Court identifier (e.g., `stadium_1`, required)|
+----------------+-----------------------------------------------+

Version Control
---------------
- **Branching**:  
  Feature branches named `feature/book-court`.
- **Issue Tracking**:  
  Linked to GitHub issues (e.g., Issue #45).
- **Pull Requests**:  
  Titles follow convention `feat(booking): add court reservation page (#45)`.
- **Release Tagging**:  
  UI updates tagged as `v1.0.0-booking`.

