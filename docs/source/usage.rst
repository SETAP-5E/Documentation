.. _usage:

Usage Guide
===========

This guide walks you through the primary workflows in the MatchPoint web app—how to navigate, where to find key features, and the steps for each common task.

Getting Started
---------------

1. **Home Page**  
   - URL: `index.html`  
   - Displays links to all major features:  
     - Register  
     - Login  
     - Book a Court  
     - Friends  
     - Match History  
     - My Bookings  
     - Profile  
     - Matchmaking  

2. **Register / Login**  
   - If you’re new, click **Register** to create an account (enter name, email, password).  
   - If you already have an account, click **Login** (enter email, password).  
   - After successful login, you will be redirected to the Home Page with your user session active.

Primary Workflows
-----------------

Book a Court
^^^^^^^^^^^^
#. From the main menu, click **Book a Court**.  
#. Fill in your **Name**, **Email**, and select a **Country Code** + enter your **Phone Number**.  
#. Choose a **Match Date** and then a **Match Time** (slots already booked will be filtered out).  
#. Select a **Location** (court) from the dropdown.  
#. Click **Book Court**.  
#. A confirmation modal will appear; click **Close** to dismiss.

View / Edit Your Bookings
^^^^^^^^^^^^^^^^^^^^^^^^^
#. Click **My Bookings** in the header.  
#. By default, all your upcoming bookings are displayed in a paginated table.  
#. **Filter** by Date or Court Name, then click 🔍 **Search**.  
#. Click ♻️ **Reset** to clear filters and reload.  
#. Use **Previous** / **Next** buttons or change **Show Rows** to navigate pages.  
#. To **Edit** a booking, click the ✏️ button on its row, update fields in the modal, then **Save**.  
#. To **Cancel**, click ❌ on the row and confirm in the modal.

Browse Match History
^^^^^^^^^^^^^^^^^^^^
#. Select **History Matches** from the navigation.  
#. Optionally filter by **Date**, **Player**, **Winner**, or **Court**, then 🔍 **Search**.  
#. Click ♻️ **Reset** to clear.  
#. Navigate through results with **Previous** / **Next**, or change **Show Rows**.  
#. Dismiss any modal messages with **Close**.

Manage Your Friends
^^^^^^^^^^^^^^^^^^^
#. Go to **Friends** via the main menu.  
#. Filter your friends list by **Player ID**, **Name**, or **Location**, then click 🔍 **Search**; or ♻️ **Reset**.  
#. Change **Show Rows** and use **Previous** / **Next** to page through.  
#. (Future) Click on a friend record to view details or send new requests.

Profile & Settings
^^^^^^^^^^^^^^^^^^
#. Click **Profile** in the header.  
#. Your current stats (strength, wins/losses) and personal details are displayed.  
#. To update, edit the form fields (Name, Birthday, Gender, Email, Location, Phone, Password).  
#. To change your photo, click **Choose File**, pick an image, then **Update Profile**.  
#. Use **Logout** to end your session and return to the login page.

Matchmaking
^^^^^^^^^^^
#. Navigate to **Matchmaking** from the header.  
#. Filter available players by **Player ID**, **Name**, **Gender**, or **Strength**.  
#. Click 🔍 **Search** or ♻️ **Reset**.  
#. To get a random selection, click 🎲 **Random**.  
#. Check the **Select** boxes next to one or more players, then click ✅ **Choose Selected**.  
#. A modal will confirm your new match.

Tips & Shortcuts
---------------
- Use the **navigation bar** at the top of every page to jump between sections.  
- Look for 🔍 icons to **search/​filter**, ❌ to **cancel**, ✏️ to **edit**, and 🎲 for **random** operations.  
- Most pages support pagination (`Show Rows`, **Previous**, **Next**).  
- Forms use HTML5 validation (required fields, correct formats); errors will be shown in a modal.  

Need Help?
----------
If you encounter issues or have questions, please refer to the **API Documentation** (`api.rst`) or open an issue in the project's GitHub repository under the **Issues** tab.
