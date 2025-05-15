.. _home-page:

Home / Main Page
=======================

Usage
-----
The **Main Page** (Home) of MatchPoint provides an entry point to all major features: registration, login, court booking, profile, friends, and match history.

Typical workflow:

#. User arrives at the Home Page (`index.html`).  
#. The header displays the site logo and primary navigation links.  
#. The main content shows a grid of action links:  
   - 📝 Register  
   - 🔐 Login  
   - 📅 Book a Court  
   - 👤 Profile  
   - 🤝 Friends  
   - 🕒 Booking History  
#. User clicks any tile to navigate to the corresponding page.  

Maintenance
-----------
This page is built with static HTML for structure, CSS for styling, and JavaScript for minor client-side behavior.

- **HTML** (`index.html`):  
  - Defines semantic structure: `<header>` with `.main-header`, `<nav>`, `<main>` with `.main-links-grid`, and `<footer>`.  
  - Includes `<link>` tags for `main_page.css` and a shared `style.css`. :contentReference[oaicite:0]{index=0}:contentReference[oaicite:1]{index=1}  
- **CSS** (`main_page.css`):  
  - Full-viewport gradient background and flexbox layout.  
  - Responsive grid for the action tiles (`.main-links-grid`).  
  - Styled header with logo (`.site-logo`) and navigation bar, plus a decorative underline bar (`.navbar-underline`). :contentReference[oaicite:2]{index=2}:contentReference[oaicite:3]{index=3}  
- **JavaScript** (`main_page.js`):  
  - (Assuming) Handles dynamic behaviors such as highlighting the active nav link, mobile menu toggling, and any welcome/message display on load.  

**Dependencies**:

- Modern browser support for CSS Grid, Flexbox, and ES6 JavaScript.  
- Shared styles from `style.css` for consistency across pages.  
- Assets: `assets/images/logo.png` for branding.  

**Build & Deployment**:

No preprocessing or build step required. Simply host the static files (`index.html`, CSS, JS, assets) on any web server or CDN.

Comments
--------
Implementation Comments
~~~~~~~~~~~~~~~~~~~~~~~
- **Accessibility**  
  - Navigation links could use `aria-current="page"` on the active link.  
  - Consider adding a “Skip to main content” link for screen readers.  
- **Responsive Design**  
  - The grid of links uses fixed `minmax(200px, 1fr)`; test on very small viewports to ensure no overflow.  
- **Performance**  
  - Inlining the small `main_page.js` in `<script>` could save one HTTP request.  
- **SEO**  
  - `<h1 class="page-title">MatchPoint</h1>` is appropriate, but consider adding `<meta name="description" content="Reserve sports courts, find friends, and view match history on MatchPoint.">`.  

Interface Comments
~~~~~~~~~~~~~~~~~~~
This page does not submit data but links to other pages:

- **Action Tiles** link to:  
  - `/Register.html`  
  - `/Login.html`  
  - `/Book_a_court.html`  
  - `/Profile.html`  
  - `/Friends.html`  
  - `/History_matches.html`  

Ensure these endpoints exist and follow the documented interfaces on their respective pages.

Version Control
---------------
- **Branching**  
  Use feature branches prefixed `feature/ui-home-page`.  
- **Issue Tracking**  
  Reference GitHub Issue IDs in commits and PR titles (e.g., `#101`).  
- **Pull Requests**  
  Title convention:  
