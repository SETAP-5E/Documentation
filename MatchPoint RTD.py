"""
MatchPoint Client Library
=========================

A lightweight Python client for the MatchPoint sports-court booking and matchmaking platform.
Provides idiomatic access to:
  - User registration, login and profile management  
  - Court availability queries and reservations  
  - Friend lists and match history retrieval  
  - Automated matchmaking and random opponent suggestions  

Install
-------
::

    pip install matchpoint-client

Quickstart
----------

.. code-block:: python

    from matchpoint import MatchPoint

    client = MatchPoint(api_key="YOUR_API_KEY")
    courts = client.get_available_courts(date="2025-05-20", location="ABC")
    booking = client.book_court(court_id=courts[0].id, date="2025-05-20", time="18:00")
    print(f"Booked court {booking.court_id} at {booking.time}")

Version
-------
"""
__version__ = "0.1.0"

