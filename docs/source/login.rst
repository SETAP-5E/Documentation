.. _login-page:

Login Page Documentation
========================

Usage
-----
The **Login** page lets existing users authenticate to MatchPoint by entering their email and password.

Typical workflow:

#. Navigate to **Login** via the main menu or “Register here” link on the Register page.  
#. Enter **Email** and **Password** into the form fields.  
#. Click **Login**.  
#. A popup modal appears indicating success (redirect to dashboard) or error (e.g. “Invalid credentials”).

Maintenance
-----------
This page consists of static HTML for structure, CSS for styling, and JavaScript for client-side logic.

- **HTML** (`Login.html`):  
  - Defines `<header>` with logo and navigation, a `<main>` block containing the login form, and a `<footer>`.  
  - Uses semantic tags and `required` attributes for basic validation. :contentReference[oaicite:0]{index=0}:contentReference[oaicite:1]{index=1}  
- **CSS** (`login.css`):  
  - Implements a full-screen gradient background, centered form container, styled inputs and buttons, navigation bar, and popup modal.  
  - Utilises flexbox and responsive percentages for layout. :contentReference[oaicite:2]{index=2}:contentReference[oaicite:3]{index=3}  
- **JavaScript** (`login.js`):  
  - Attaches a `submit` listener to `#loginForm`.  
  - Sends credentials via `fetch` to `/api/login`.  
  - Based on JSON response, toggles the popup’s `.success` or `.error` class and message text.  
  - Hides the popup on clicking “OK” and, on success, redirects the user.

**Dependencies**:

- Modern browser support for Fetch API, CSS Flexbox, and CSS gradients.  
- Logo and icons served from `assets/images/`.

**Build & Deployment**:

No build pipeline required; deploy by hosting `Login.html`, `login.css`, `login.js`, and assets on any static-file server.

Comments
--------
Implementation Comments
~~~~~~~~~~~~~~~~~~~~~~~
- **Accessibility**  
  - The popup lacks ARIA roles (`role="alertdialog"`) and `aria-live` regions; add these for screen-reader announcements.  
  - Navigation links could benefit from `aria-current="page"` on the active item.  
- **Security**  
  - Credentials are sent over Fetch; ensure HTTPS is enforced.  
  - Consider adding a CSRF token if the API requires it.  
- **Error Handling**  
  - All non-200 responses currently display a generic error—consider parsing field-specific errors for inline feedback.  
- **Performance**  
  - The popup markup is always present in the DOM; injecting it on demand could reduce initial payload.

Interface Comments
~~~~~~~~~~~~~~~~~~~
Form POST endpoint:
