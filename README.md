# Hotel Grande Inn — Room Management System

A console-based hotel room management application built in Python. It manages room bookings, availability, and billing for a hotel using persistent file storage (`pickle`), with no external dependencies or database required.

**Project by:** Parikshith N, Class XII A1 CS

## Features

- **Insert** — Add one or more new room records in a single session, with duplicate room number prevention
- **Display** — View all rooms (sorted), plus a live summary of total / available / not available room counts
- **Search** — Look up rooms by:
  - Room provider's name
  - Room number
  - Availability status
  - Room type
  - Rooms with no assigned provider (`NULL`)
- **Update** — Modify an existing room's provider name, stay duration, availability, floor, or room type
- **Delete** — Remove a room record permanently
- **Billing** — Calculate the total bill for a single room or generate bills for every currently booked room, based on room type and number of nights stayed

## Room Types & Pricing

| Room Type    | Price per night |
|--------------|------------------|
| Normal       | $100             |
| Pro          | $200             |
| Deluxe       | $250             |
| Ultra        | $500             |

## Record Structure

Each room is stored as a list:

```python
[room_provider_name, room_number, availability, nights_stayed, floor, room_type]
```

## How to Run

1. Make sure you have Python 3 installed.
2. Run the script:
   ```
   python ROOM_MANAGEMENT_PROJECT__PARIKSHITH.py
   ```
3. Use the on-screen numbered menu to navigate between Insert, Display, Search, Update, Delete, and Bill options.
4. Data is automatically saved to `data.dat` in the same folder, so records persist between runs.

## Notes

- Room availability should be entered as `available` or `not available`.
- When entering a room's provider name, type `NULL` if the room currently has no guest assigned.
- This is a school project built to practice file handling (`pickle`), functions, and menu-driven program design in Python.
