.. _register-page:

Signup Page Documentation
===========================

Usage
-----
The **Register/signup** page allows new users to create an account on MatchPoint by entering their full name, email, and password.  

Typical workflow:

#. Navigate to **Register** via the site header or “Login here” link.  
#. Enter **Full Name**, **Email**, and **Password** into the form fields.  
#. Click **Register**.  
#. A popup confirms success or displays error messages (e.g. “Email already in use”).  

Example request (via JavaScript `fetch`):

.. code-block:: http

   POST /api/register HTTP/1.1
   Host: example.com
   Content-Type: application/json

   {
     "full_name": "Lemich M",
     "email": "lemich@example.com",
     "password": "••••••••"
   }

Maintenance
-----------
This page is built with static HTML for structure, CSS for styling, and JavaScript for form handling.

- **HTML** (`Register.html`):  
  - Defines `<header>` with logo and navigation, `<main>` containing the registration form, and a `<footer>`.  
  - Uses standard `<form>` markup with `required` attributes for client-side validation. :contentReference[oaicite:0]{index=0}:contentReference[oaicite:1]{index=1}  
- **CSS** (`register.css`):  
  - Implements a responsive, centered container on a gradient background.  
  - Styles header, form controls, buttons, popup modal, and navigation. :contentReference[oaicite:2]{index=2}:contentReference[oaicite:3]{index=3}  
- **JavaScript** (`register.js`):  
  - Listens for `submit` on `#registerForm`.  
  - Sends form data as JSON to `/api/register`.  
  - Displays the `#popup` with success or error classes based on server response.  

**Dependencies**:

- Modern browser support for Fetch API, flexbox, and CSS gradients.  
- Logo and icons loaded from `assets/images/`.  

**Build & Deployment**:

No build pipeline required. Deploy by serving `Register.html`, `register.css`, and `register.js` as static assets.

Comments
--------
Code Comments
~~~~~~~~~~~~~
- Uses semantic HTML tags (`<header>`, `<main>`, `<footer>`) for accessibility.  
- Consistent BEM-inspired class names (e.g., `.form-group`, `.popup`, `.login-link`).  
- Hidden popup controlled via `.hidden` class toggled in JS.  

Implementation Comments
~~~~~~~~~~~~~~~~~~~~~~~
- **Accessibility**  
  - The popup lacks ARIA roles (e.g., `role="alertdialog"`).  
  - Recommend adding `aria-live="assertive"` to the message container.  
- **Security**  
  - Password input uses `type="password"`, but no strength meter—consider adding client-side strength feedback.  
- **Error Handling**  
  - Current JS maps any non-200 response to a generic error.  
  - Suggest parsing field-specific errors (e.g. invalid email format) and displaying inline.  
- **Performance**  
  - Popup markup always in DOM; consider injecting it on demand.  

Interface Comments
~~~~~~~~~~~~~~~~~~~
Form POST endpoint:
