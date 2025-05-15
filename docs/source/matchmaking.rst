.. _matchmaking-page:

Matchmaking Page
================================

Usage
-----
The **Matchmaking** page enables users to find and pair up with other players based on filter criteria or randomly. Users can search by **Player ID**, **Name**, **Gender**, and **Strength**, then select one or more players to create a match. Alternatively, the **Random** button auto-selects players.

Typical workflow:

#. Navigate to **Matchmaking** via the header nav.  
#. Use filter inputs to narrow down the player list.  
#. Click 🔍 **Search** to refresh the table with matching players.  
#. Click ♻️ **Reset** to clear filters.  
#. Click 🎲 **Random** to automatically select a set of players.  
#. Tick the **Select** checkbox next to desired players.  
#. Click ✅ **Choose Selected** to confirm match creation.  
#. A modal displays success or error messages.

Maintenance
-----------
This page is implemented with static HTML, CSS, and JavaScript.

- **HTML** (`Match_making.html`): Defines header, navigation, filter form, player table, pagination controls, modal overlay, and footer. :contentReference[oaicite:0]{index=0}:contentReference[oaicite:1]{index=1}  
- **CSS** (`Match_making.css`): Styles the gradient background, header, nav links, buttons, table, and modal overlay with responsive design. :contentReference[oaicite:2]{index=2}:contentReference[oaicite:3]{index=3}  
- **JavaScript** (`match_making.js`):  
  - Fetches and displays player data based on filters and pagination.  
  - Handles **Search**, **Reset**, **Random**, and **Choose Selected** actions.  
  - Manages pagination controls and **Show Rows** selector.  
  - Displays modal messages for success or errors.

**Dependencies**:

- Browser support for ES6, Fetch API, CSS Flexbox, and CSS Grid.  
- Assets (logos/icons) in `assets/images/`.  

**Build & Deployment**:

Static files can be served by any web server (NGINX, GitHub Pages) without build steps.

Comments
--------
Implementation Comments
~~~~~~~~~~~~~~~~~~~~~~~
- **Accessibility**  
  - Add `role="table"` on `<table>` and `role="dialog"` plus `aria-modal="true"` on the modal.  
  - Wrap filter inputs in a `<fieldset>` with `<legend>` for screen-reader context.  
  - Ensure keyboard focus is trapped within the modal when open.

- **Error Handling**  
  - Currently displays generic messages; consider granular feedback for network vs. server errors.  
  - Validate that at least one player is selected before sending the match creation request.

- **Performance**  
  - Debounce the **Search** button to prevent rapid consecutive API calls.  
  - Lazy-load table rows or implement infinite scroll for large data sets.

- **Code Maintainability**  
  - Refactor repeated DOM queries into utility functions.  
  - Modularize API calls into a separate service layer.

Interface Comments
~~~~~~~~~~~~~~~~~~~
**List Players**  
```http
GET /api/players
Query Parameters:
  playerId=<integer>    (optional)
  playerName=<string>   (optional)
  gender=<Male|Female>  (optional)
  strength=<1–10>       (optional)
  page=<integer>        (default=1)
  per_page=<integer>    (default=5)
