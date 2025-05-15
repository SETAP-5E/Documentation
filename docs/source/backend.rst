.. _backend:

Backend
==========================

This document describes the server-side architecture, the database module, route definitions, middleware, and implementation notes for the MatchPoint backend.

Architecture
------------
The backend is built with **Node.js** and **Express**, using a **MySQL** database. Key components:

- **server.js**: Entry point; configures middleware, static file serving, and mounts routes.  
- **config/db.js**: Establishes the MySQL connection.  
- **routes/**: Each file defines a set of RESTful endpoints and handler logic.  
- **middleware/**: Contains `requireAuth` to protect authenticated endpoints.  

Database Module
---------------
.. literalinclude:: ../config/db.js
   :language: javascript
   :caption: MySQL connection setup (db.js)

Express Server Setup
--------------------
.. literalinclude:: ../server.js
   :language: javascript
   :caption: Express app configuration (server.js)

Middleware
----------
- **helmet()**: Secures HTTP headers.  
- **cors()**: Allows cross-origin requests from front-end origins.  
- **express.json()**: Parses incoming JSON bodies.  
- **express.static()**: Serves `frontend/` and `uploads/`.  
- **express-session**: Manages user sessions (`SESSION_SECRET`).  
- **Fallback 404**: Catches unrecognized routes.  

API Endpoints
-------------

Authentication
^^^^^^^^^^^^^^
Base URL: `/api/auth`

+----------------------+----------------------------+--------------------------------------+
| Method & Path        | Description                | Body / Query                         |
+======================+============================+======================================+
| POST `/register`     | Register a new user        | `full_name`, `email`, `password`     |
+----------------------+----------------------------+--------------------------------------+
| POST `/login`        | Authenticate & start session | `email`, `password`                |
+----------------------+----------------------------+--------------------------------------+
| POST `/logout`       | Destroy session            | N/A                                  |
+----------------------+----------------------------+--------------------------------------+
| GET `/verify`        | Verify email token         | Query `token`                        |
+----------------------+----------------------------+--------------------------------------+

Court Booking
^^^^^^^^^^^^^^
Base URL: `/api/book`

+----------------------+--------------------------------------+---------------------------------------------+
| Method & Path        | Description                          | Body / Query                                |
+======================+======================================+=============================================+
| GET `/blocked`       | Get booked times for a court         | `court_id`, `booking_date`                  |
+----------------------+--------------------------------------+---------------------------------------------+
| GET `/`              | List authenticated user’s bookings   | Filters: `court_name`, `location`, etc.     |
+----------------------+--------------------------------------+---------------------------------------------+
| GET `/:id`           | Get a single booking by ID           | Path `id`                                   |
+----------------------+--------------------------------------+---------------------------------------------+
| POST `/`             | Create a new booking (with match request logic) | `court_id`, `booking_date`, etc.  |
+----------------------+--------------------------------------+---------------------------------------------+
| PUT `/:id`           | Update an existing booking           | Path `id`, updated fields                   |
+----------------------+--------------------------------------+---------------------------------------------+
| PUT `/:id/cancel`    | Cancel a booking                     | Path `id`                                   |
+----------------------+--------------------------------------+---------------------------------------------+
| DELETE `/:id`        | Delete a booking                     | Path `id`                                   |
+----------------------+--------------------------------------+---------------------------------------------+

Courts
^^^^^^
Base URL: `/api/courts`

+----------------------+--------------------------------------+------------------+
| GET `/`              | List available courts               | N/A              |
+----------------------+--------------------------------------+------------------+

Friends
^^^^^^^
Base URL: `/api/friends`

+----------------------+--------------------------------------+----------------------------------+
| GET `/`              | List user’s friends (filters & pagination) | Query `id`,`name`,`location`,etc. |
+----------------------+--------------------------------------+----------------------------------+

Match History
^^^^^^^^^^^^^
Base URL: `/api/history`

+----------------------+--------------------------------------+-------------------------------------+
| GET `/`              | List past matches (filters & pagination) | Query `date`,`player`,`winner`,etc. |
+----------------------+--------------------------------------+-------------------------------------+

Matchmaking
^^^^^^^^^^^^
Base URL: `/api/matchmaking`

+----------------------+--------------------------------------+-------------------------------------+
| GET `/`              | List players for matchmaking       | Query `id`,`name`,`gender`,`strength`|
+----------------------+--------------------------------------+-------------------------------------+

Match Requests
^^^^^^^^^^^^^^
Base URL: `/api/match-requests` (mount manually if needed)

+------------------------------+-------------------------------------------+----------------------+
| Method & Path                | Description                               | Body / Query         |
+==============================+===========================================+======================+
| GET `/`                      | List incoming match requests              | N/A                  |
+------------------------------+-------------------------------------------+----------------------+
| GET `/sent`                  | List outgoing match requests              | N/A                  |
+------------------------------+-------------------------------------------+----------------------+
| PUT `/:id/respond`           | Accept or reject a request                | Path `id`, body `response` |
+------------------------------+-------------------------------------------+----------------------+

Profile
^^^^^^^
Base URL: `/api/profile`

+----------------------+-------------------------------------------+---------------------------------------------+
| Method & Path        | Description                               | Body / Query                                |
+======================+===========================================+=============================================+
| GET `/`              | Get authenticated user’s profile          | N/A                                         |
+----------------------+-------------------------------------------+---------------------------------------------+
| GET `/stats`         | Get user stats (wins, losses, strength)   | N/A                                         |
+----------------------+-------------------------------------------+---------------------------------------------+
| PUT `/`              | Update profile details                    | `full_name`, `email`, `location`, etc.      |
+----------------------+-------------------------------------------+---------------------------------------------+
| POST `/upload`       | Upload profile picture                    | Form field `profile_picture`                |
+----------------------+-------------------------------------------+---------------------------------------------+

Implementation Notes
--------------------
- **Authentication middleware**: `requireAuth` protects routes requiring login.  
- **Error handling**: All handlers return JSON with appropriate HTTP status codes.  
- **Input validation**: Basic checks are performed in each route—consider using a validation library for robustness.  
- **Database access**: Uses `mysql2` callback API; for larger projects, consider a Promise‐based wrapper or ORM.  
- **Email**: Verification emails are sent via Nodemailer configured in `authRoutes.js`.  
- **File uploads**: Profile pictures handled with Multer and served from `/uploads`.  

References
----------
- DB connection: :file:`config/db.js`  
- Server setup: :file:`server.js`  
- Route definitions: :file:`routes/*.js`  
