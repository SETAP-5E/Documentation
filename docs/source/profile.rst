.. _profile-page:

Profile Page Documentation
==========================

Usage
-----
The **Profile** page enables users to view and edit their personal information and statistics, upload a profile photo, and log out.

Typical workflow:

#. Navigate to **Profile** via the main menu.  
#. The page automatically loads and displays user stats (Player ID, strength, wins/losses/total).  
#. Preview your current profile photo; click **Choose File** to select and preview a new one.  
#. Edit **Full Name**, **Birthday**, **Gender**, **Email**, **Location**, **Phone Number**, and optionally **New Password**/**Confirm Password**.  
#. Click **Update Profile** to submit changes. A modal displays success or error.  
#. Click **Logout** to sign out and return to the login page.

Maintenance
-----------
This page is built with static HTML, CSS, and JavaScript.

- **HTML** (`Profile.html`):  
  - Defines semantic structure: `<header>` with active nav link, `.navbar-underline`, `<main>` containing the `#profileForm`, and `<footer>`.  
  - Uses `id` attributes for JS hooks (`userIdStat`, `strengthStars`, `profilePreview`, etc.). :contentReference[oaicite:0]{index=0}:contentReference[oaicite:1]{index=1}  
- **CSS** (`Profile.css`):  
  - Applies a full-viewport gradient background, styled header, centered `.container` card, form controls, custom phone-dropdown, and modal overlay.  
  - Responsive design with flexbox and consistent branding colors. :contentReference[oaicite:2]{index=2}:contentReference[oaicite:3]{index=3}  
- **JavaScript** (`profile.js`):  
  - On `DOMContentLoaded`, fetches user data via `GET /api/profile` and populates stats and form fields.  
  - Handles profile-photo selection and live preview.  
  - Manages country-code dropdown and synchronises the hidden `country_code` input.  
  - Submits updated data via `PUT /api/profile` (multipart/form-data when a photo is included).  
  - Displays a modal with server response and handles “Close” and logout actions (`POST /api/logout`).

**Dependencies**:

- Font Awesome icons via CDN.  
- Assets: `assets/images/logo.png`, `assets/flags/*.png`.  
- Modern browsers supporting Fetch API, ES6, and flexbox.

**Build & Deployment**:

No build step required; deploy by hosting these static files on any web server (e.g., NGINX, GitHub Pages).

Comments
--------
Implementation Comments
~~~~~~~~~~~~~~~~~~~~~~~
- **Accessibility**  
  - The modal overlay lacks `role="dialog"` and focus trapping; add ARIA attributes and keyboard management.  
  - Custom file-input label should include `aria-label` and support keyboard activation.  
  - Consider adding `aria-live="polite"` to status text for screen-reader updates.  
- **Validation**  
  - Confirm Password matching should be validated client-side before submission.  
  - HTML5 validation covers required fields, but the server must re-validate all inputs.  
- **Error Handling**  
  - Current modal shows generic messages; consider inline error messages next to invalid fields.  
- **Performance**  
  - Modal markup is always present; lazy-insert via JS to reduce initial DOM size if needed.

Interface Comments
~~~~~~~~~~~~~~~~~~~
**Fetch Profile**  
