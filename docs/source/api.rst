.. _api-documentation:

API Documentation
=================

This section describes the REST API endpoints available in the MatchPoint application.

Authentication
--------------

### Register

**Endpoint**  
``POST /api/register``

**Description**  
Create a new user account.

**Request Body**  

+--------------+--------+----------------------------------------+
| Parameter    | Type   | Description                            |
+==============+========+========================================+
| full_name    | string | User’s full name (required)            |
+--------------+--------+----------------------------------------+
| email        | string | User’s email address (required, unique)|
+--------------+--------+----------------------------------------+
| password     | string | User’s password (required)             |
+--------------+--------+----------------------------------------+

**Responses**  

- **201 Created**  
  .. code-block:: json

     {
       "status": "success",
       "message": "Account created successfully."
     }

- **400 Bad Request**  
  .. code-block:: json

     {
       "status": "error",
       "message": "Email already in use."
     }


### Login

**Endpoint**  
``POST /api/login``

**Description**  
Authenticate an existing user and obtain a session token.

**Request Body**  

+-----------+--------+----------------------------------+
| Parameter | Type   | Description                      |
+===========+========+==================================+
| email     | string | User’s email address (required)  |
+-----------+--------+----------------------------------+
| password  | string | User’s password (required)       |
+-----------+--------+----------------------------------+

**Responses**  

- **200 OK**  
  .. code-block:: json

     {
       "status": "success",
       "message": "Logged in successfully.",
       "token": "JWT_OR_SESSION_TOKEN"
     }

- **401 Unauthorized**  
  .. code-block:: json

     {
       "status": "error",
       "message": "Invalid email or password."
     }


User Profile
------------

### Get Profile

**Endpoint**  
``GET /api/profile``

**Description**  
Retrieve the currently authenticated user’s profile information.

**Headers**  
:Authorization: Bearer `<token>`

**Responses**  

- **200 OK**  
  .. code-block:: json

     {
       "status": "success",
       "data": {
         "playerId": 5,
         "fullName": "Jane Doe",
         "email": "jane@example.com",
         "birthdate": "1990-05-15",
         "gender": "Female",
         "location": "London",
         "countryCode": "+44",
         "phoneNumber": "7123456789",
         "strength": 7,
         "wins": 10,
         "losses": 5,
         "profilePhotoUrl": "/uploads/jane.jpg"
       }
     }

- **401 Unauthorized**  
  .. code-block:: json

     {
       "status": "error",
       "message": "Authentication required."
     }


### Update Profile

**Endpoint**  
``PUT /api/profile``

**Description**  
Update the authenticated user’s profile. Supports multipart form data for photo uploads.

**Headers**  
:Authorization: Bearer `<token>`  
:Content-Type: multipart/form-data

**Form Data Parameters**  

+----------------+----------------------+---------------------------------------+
| Parameter      | Type                 | Description                           |
+================+======================+=======================================+
| fullName       | string               | User’s full name                      |
+----------------+----------------------+---------------------------------------+
| birthdate      | YYYY-MM-DD           | Date of birth                         |
+----------------+----------------------+---------------------------------------+
| gender         | string               | “Male”/“Female”/“Other”               |
+----------------+----------------------+---------------------------------------+
| location       | string               | User’s location                       |
+----------------+----------------------+---------------------------------------+
| countryCode    | string               | Dialing code, e.g. “+44”              |
+----------------+----------------------+---------------------------------------+
| phoneNumber    | string               | Local phone number                    |
+----------------+----------------------+---------------------------------------+
| newPassword    | string               | Optional new password                 |
+----------------+----------------------+---------------------------------------+
| confirmPassword| string               | Must match `newPassword`              |
+----------------+----------------------+---------------------------------------+
| profilePhoto   | file                 | Optional image upload                 |
+----------------+----------------------+---------------------------------------+

**Responses**  

- **200 OK**  
  .. code-block:: json

     {
       "status": "success",
       "message": "Profile updated successfully."
     }

- **400 Bad Request**  
  .. code-block:: json

     {
       "status": "error",
       "message": "Passwords do not match."
     }


### Logout

**Endpoint**  
``POST /api/logout``

**Description**  
Invalidate the current session.

**Headers**  
:Authorization: Bearer `<token>`

**Responses**  

- **200 OK**  
  .. code-block:: json

     {
       "status": "success",
       "redirect": "/Login.html"
     }


Courts & Bookings
-----------------

### List Blocked Times

**Endpoint**  
``GET /api/book/blocked?court_id={id}&booking_date={YYYY-MM-DD}``

**Description**  
Retrieve time slots already booked for a specific court on a given date.

**Responses**  

- **200 OK**  
  .. code-block:: json

     {
       "status": "success",
       "blocked_times": ["10:00:00","12:00:00","15:00:00"]
     }


### Book Court

**Endpoint**  
``POST /api/book``

**Description**  
Create a new court booking.

**Headers**  
:Content-Type: application/json  
:Authorization: Bearer `<token>`

**Request Body**  

+-------------+----------------------+----------------------------------+
| Parameter   | Type                 | Description                      |
+=============+======================+==================================+
| userId      | integer              | Authenticated user’s ID          |
+-------------+----------------------+----------------------------------+
| courtId     | integer              | Selected court ID                |
+-------------+----------------------+----------------------------------+
| booking_date| YYYY-MM-DD           | Desired date                     |
+-------------+----------------------+----------------------------------+
| booking_time| HH:MM:SS             | Desired time                     |
+-------------+----------------------+----------------------------------+

**Responses**  

- **201 Created**  
  .. code-block:: json

     {
       "status": "success",
       "message": "Court booked for 2025-05-15 at 18:00"
     }

- **409 Conflict**  
  .. code-block:: json

     {
       "status": "error",
       "message": "Time slot unavailable."
     }


### List Bookings

**Endpoint**  
``GET /api/bookings?date={YYYY-MM-DD}&court={courtName}&page={n}&per_page={n}``

**Description**  
Fetch the authenticated user’s bookings, with optional filtering and pagination.

**Responses**  

- **200 OK**  
  .. code-block:: json

     {
       "status": "success",
       "data": [ … ],
       "pagination": { "page":1, "per_page":5, "total":12 }
     }


### Edit Booking

**Endpoint**  
``PUT /api/bookings/{bookingId}``

**Description**  
Modify date, time, or location of an existing booking.

**Headers**  
:Content-Type: application/json  
:Authorization: Bearer `<token>`

**Request Body**  

+--------------+----------------------+----------------------------------+
| Parameter    | Type                 | Description                      |
+==============+======================+==================================+
| booking_date | YYYY-MM-DD           | New date                         |
+--------------+----------------------+----------------------------------+
| booking_time | HH:MM:SS             | New time                         |
+--------------+----------------------+----------------------------------+
| location     | string               | New court identifier             |
+--------------+----------------------+----------------------------------+

**Responses**  

- **200 OK**  
  .. code-block:: json

     {
       "status": "success",
       "message": "Booking updated."
     }

- **404 Not Found**  
  .. code-block:: json

     {
       "status": "error",
       "message": "Booking not found."
     }


### Cancel Booking

**Endpoint**  
``DELETE /api/bookings/{bookingId}``

**Description**  
Cancel an existing booking.

**Headers**  
:Authorization: Bearer `<token>`

**Responses**  

- **200 OK**  
  .. code-block:: json

     {
       "status": "success",
       "message": "Booking cancelled."
     }


Social
------

### Get Friends

**Endpoint**  
``GET /api/friends?playerId={id}&playerName={name}&location={loc}&page={n}&per_page={n}``

**Description**  
Retrieve a paginated list of friends, with optional filtering.

**Responses**  

- **200 OK**  
  .. code-block:: json

     {
       "status": "success",
       "data": [ … ],
       "pagination": { "page":1, "per_page":5, "total":8 }
     }


Match History
-------------

### Get Match History

**Endpoint**  
``GET /api/history?date={YYYY-MM-DD}&player={name}&winner={name}&court={name}&page={n}&per_page={n}``

**Description**  
Retrieve past match records with optional filters and pagination.

**Responses**  

- **200 OK**  
  .. code-block:: json

     {
       "status": "success",
       "data": [ … ],
       "pagination": { "page":1, "per_page":5, "total":27 }
     }


Matchmaking
-----------

### List Players

**Endpoint**  
``GET /api/players?playerId={id}&playerName={name}&gender={Male|Female}&strength={1–10}&page={n}&per_page={n}``

**Description**  
Retrieve a list of players available for matchmaking.

**Responses**  

- **200 OK**  
  .. code-block:: json

     {
       "status": "success",
       "data": [ … ],
       "pagination": { "page":1, "per_page":5, "total":42 }
     }


### Random Matchmaking

**Endpoint**  
``GET /api/matchmaking/random?count={n}``

**Description**  
Get a random selection of `n` players.

**Responses**  

- **200 OK**  
  .. code-block:: json

     {
       "status": "success",
       "selected": [ … ]
     }


### Create Match

**Endpoint**  
``POST /api/matchmaking``

**Description**  
Create a match from selected players.

**Headers**  
:Content-Type: application/json  
:Authorization: Bearer `<token>`

**Request Body**  

+-----------+------------+--------------------------------------+
| Parameter | Type       | Description                          |
+===========+============+======================================+
| playerIds | list[int]  | Array of user IDs to include in match|
+-----------+------------+--------------------------------------+

**Responses**  

- **201 Created**  
  .. code-block:: json

     {
       "status": "success",
       "message": "Match created successfully."
     }
