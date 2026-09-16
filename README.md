<div align="center">

# 🏨 HOTEL GRANDE INN

### Python Hotel Room Management System

A menu-driven **Python + Pickle** project for managing hotel room records, searching rooms, updating availability, deleting records, and calculating customer bills.

<br>

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Storage](https://img.shields.io/badge/Storage-Pickle-FFB000?style=for-the-badge&logo=python&logoColor=white)](#-technology-stack)
[![Interface](https://img.shields.io/badge/Interface-CLI-111827?style=for-the-badge&logo=windowsterminal&logoColor=white)](#-application-menu)
[![Status](https://img.shields.io/badge/Status-Academic%20Project-22C55E?style=for-the-badge)](#-project-information)

**[📂 Repository](https://github.com/bookspdf705-coder/picklestay) · [💻 Source Code](https://github.com/bookspdf705-coder/picklestay/blob/main/ROOM_MANAGEMENT_PROJECT__PARIKSHITH%20(3).py) · [📄 Project Document](https://github.com/bookspdf705-coder/picklestay/blob/main/HOTEL-GRANDE_INN_PARIKSHITH-XII-A1.docx)**

</div>

---

## 📖 About the Project

**HOTEL GRANDE INN** is a Python-based hotel room management program created as a Class XII Computer Science project.

The application uses a simple command-line menu to let the user:

- ➕ Insert room records
- 📋 Display stored records
- 🔎 Search for rooms
- ✏️ Update existing records
- 🗑️ Delete records
- 💵 Calculate customer bills
- 🚪 Exit the application

The project demonstrates practical use of **functions, lists, loops, conditional statements, file handling, serialization, and Python modules**.

Room records are stored as lists containing:

```text
[Provider Name, Room Number, Availability, Nights, Floor, Room Type]
```

The program stores these records in the binary file `data.dat` using Python's `pickle` module.

---

## ✨ Key Features

| Feature | What it does |
|---|---|
| ➕ **Insert** | Creates room records and checks for duplicate room numbers during insertion. |
| 📋 **Display** | Shows room information and counts total, available, and unavailable rooms. |
| 🔎 **Search** | Searches by provider name, room number, availability, room type, or rooms without a provider. |
| ✏️ **Update** | Adds records or modifies provider, nights, availability, floor, or room type. |
| 🗑️ **Delete** | Removes a selected room record and rewrites the stored data. |
| 💵 **Billing** | Calculates bills for all customers or for one selected room. |

---

## 🧭 Application Menu

```text
=============================================================
                || WELCOME TO HOTEL GRANDE INN ||
=============================================================

ENTER WHAT FUNCTION YOU WANT TO DO:

|1| -----------------> || INSERT ||
|2| -----------------> || DISPLAY ||
|3| -----------------> || SEARCH ||
|4| -----------------> || UPDATE ||
|5| -----------------> || DELETE ||
|6| -----------------> || BILL ||
|7| -----------------> || EXIT ||

=============================================================
```

The menu is implemented around the project's six core functions:

`ins()` · `dis()` · `sea()` · `update()` · `delete()` · `billc()`

---

## 🔧 Core Functions

### `ins()` — Insert Records

Creates room records containing the provider's name, room number, availability, number of nights, floor, and room type. The function checks for duplicate room numbers before accepting a record and writes records to `data.dat` using binary file handling.

> **Important:** The original project opens `data.dat` in write-binary mode for this operation, so a new insertion session replaces the previously stored set of records.

### `dis()` — Display Records

Reads the stored records and displays each room's provider, room number, availability, nights, floor, and room type. It also calculates total, available, and unavailable room counts.

### `sea()` — Search Records

```text
1 → Room provider's name
2 → Room number
3 → Availability
4 → Room type
5 → Rooms with no provider (NULL)
```

### `update()` — Update Records

Provides two operations:

```text
1 → ADD A RECORD
2 → UPDATE
```

An existing room can be modified by room number. The program supports changing provider name, nights, availability, floor, or room type.

### `delete()` — Delete Records

The user supplies a room number and confirms the deletion. The remaining records are written temporarily to `script.dat`; the original `data.dat` is removed with `os.remove()`, and the temporary file is renamed to `data.dat` using `os.rename()`.

### `billc()` — Calculate Bills

The billing function can display all customer bills or the bill for one selected room.

| Room Type | Rate / Night |
|---|---:|
| 🛏️ Normal | $100 |
| ⭐ Pro | $200 |
| 💎 Deluxe | $250 |
| 👑 Ultra | $500 |

```text
Bill = Number of Nights × Room Rate
```

---

## 🧰 Technology Stack

| Technology | Purpose |
|---|---|
| 🐍 **Python** | Main programming language |
| 📦 **pickle** | Serializes and retrieves room records |
| 🗂️ **os** | Handles file removal and renaming during deletion |
| 💾 **data.dat** | Binary file used for room-record storage |
| 🖥️ **CLI** | User interface |

---

# 🖥️ Demonstration — Screenshot Transcription

The original project document contains sample-output screenshots for the application's main menu and the functions `ins()`, `dis()`, `sea()`, `update()`, `delete()`, and `billc()`.

The following section converts the visible screenshot content into **copyable text**, with decorative separator spacing normalized for readability.

### 1. Insert — Creating Room Records

```text
enter the room donater's name, if no enter 'null' Ramesh
enter room number101

enter if the room AVAILABLE or NOT AVAILABLE available
enter how many nights you are going to stay in the room3
enter which floor1

enter room type:

| NORMAL [100$] |
| PRO [200$] |
| DELUXE [250$] |
| ULTRA [500$] |

normal

do you want to add more records, enter | y | or | n | y

enter the room donater's name, if no enter 'null' Suresh
enter room number201

enter if the room AVAILABLE or NOT AVAILABLE not available
enter how many nights you are going to stay in the room2
enter which floor2

enter room type:

| NORMAL [100$] |
| PRO [200$] |
| DELUXE [250$] |
| ULTRA [500$] |

Pro

do you want to add more records, enter | y | or | n | n
```

Result:

```text
RECORDS ADDED SUCCESSFULLY
```

### 2. Display — Stored Records

```text
ROOM PROVIDER NAME ===> || Ramesh ||
ROOM NO.              ===> || 101 ||
ROOM AVAILABILITY     ===> || available ||
NO. OF NIGHTS         ===> || 3 ||
FLOOR                 ===> || 1 ||
ROOM TYPE             ===> || normal ||

ROOM PROVIDER NAME ===> || Suresh ||
ROOM NO.              ===> || 201 ||
ROOM AVAILABILITY     ===> || not available ||
NO. OF NIGHTS         ===> || 2 ||
FLOOR                 ===> || 2 ||
ROOM TYPE             ===> || Pro ||
```

### 3. Search — Provider Name

```text
enter what you want to search;

ROOM PROVIDER'S NAME
```

Example result:

```text
ROOM PROVIDER NAME ===> || Ramesh ||
ROOM NO.            ===> || 101 ||
ROOM AVAILABILITY   ===> || available ||
NO. OF NIGHTS       ===> || 3 ||
FLOOR               ===> || 1 ||
ROOM TYPE           ===> || normal ||
```

Another documented search result:

```text
ROOM PROVIDER NAME ===> || Suresh ||
ROOM NO.            ===> || 201 ||
ROOM AVAILABILITY   ===> || not available ||
NO. OF NIGHTS       ===> || 2 ||
FLOOR               ===> || 2 ||
ROOM TYPE           ===> || Pro ||
```

### 4. Search — Room Type

```text
enter what you want to search;

NORMAL ROOMS:

ROOM PROVIDER NAME ===> || Ramesh ||
ROOM NO.            ===> || 101 ||
ROOM AVAILABILITY   ===> || available ||
NO. OF NIGHTS       ===> || 3 ||
FLOOR               ===> || 1 ||
ROOM TYPE           ===> || normal ||
```

The search menu also supports `NORMAL`, `PRO`, `DELUXE`, and `ULTRA`.

### 5. Update — Adding / Modifying a Record

Example from the documented output:

```text
enter the room holder's name, if no enter 'NULL' mohan
enter room number102
enter if the room AVAILABLE or NOT AVAILABLE available
enter how nights you are going to stay in the room4
enter which floor1

enter room type:

| NORMAL [100$] |
| PRO [200$] |
| DELUXE [250$] |
| ULTRA [500$] |

ultra

do you want to add more records, enter | y | or | n | n

RECORD ADDED SUCCESSFULLY
```

Example availability update:

```text
enter the room no. to be changed102

TO CHANGE:
ROOM PROVIDER NAME..................1
STAY NIGHTS........................2
MAKE AVAILABLE.....................3
MAKE NOT AVAILABLE.................4
FLOOR..............................5
ROOM TYPE..........................6

RECORD MARKED NOT AVAILABLE
RECORD UPDATED SUCCESSFULLY
```

### 6. Delete — Removing a Record

```text
ENTER WHAT FUNCTION YOU WANT TO DO:

|1| -----------------> || INSERT ||
|2| -----------------> || DISPLAY ||
|3| -----------------> || SEARCH ||
|4| -----------------> || UPDATE ||
|5| -----------------> || DELETE ||
|6| -----------------> || BILL ||

ENTER ROOM NO. TO BE DELETED102

are you sure you want to delete the record...

THE RECORD HAS BEEN DELETED
```

### 7. Billing — Customer Bills

```text
SHOW:
ALL CUSTOMER'S BILLS.........1
ONE CUSTOMER'S BILL..........2
```

Example documented output:

```text
300 $ is the bill amount for 3 nights for room number 101 [ normal ]

400 $ is the bill amount for 2 nights for room number 201 [ Pro ]
```

---

## 🔄 Program Flow

```mermaid
flowchart TD
    A([Start]) --> B[Display Main Menu]
    B --> C{Select Operation}

    C -->|1| D[ins() - Insert]
    C -->|2| E[dis() - Display]
    C -->|3| F[sea() - Search]
    C -->|4| G[update() - Update]
    C -->|5| H[delete() - Delete]
    C -->|6| I[billc() - Billing]
    C -->|7| J([Exit])

    D --> K[(data.dat)]
    E --> K
    F --> K
    G --> K
    H --> K
    I --> K

    D --> B
    E --> B
    F --> B
    G --> B
    H --> B
    I --> B
```

---

## 📂 Repository Structure

```text
PickleStay/
│
├── ROOM_MANAGEMENT_PROJECT__PARIKSHITH (3).py
├── HOTEL-GRANDE_INN_PARIKSHITH-XII-A1.docx
├── LICENSE
├── README.md
│
└── docs/
    └── project documentation
```

---

## ▶️ Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/bookspdf705-coder/picklestay.git
cd picklestay
```

### 2. Run the Python program

```bash
python "ROOM_MANAGEMENT_PROJECT__PARIKSHITH (3).py"
```

### 3. Choose an operation

Use the menu to insert, display, search, update, delete, or calculate bills.

> **Note:** The project is based on the Python source file currently stored in the repository. The generated `data.dat` file is used by the program for local record storage.

---

## ⚠️ Current Limitations

The project document identifies several limitations in the current version:

- The application uses a text-based command-line interface.
- Room data is stored locally using `pickle`, rather than a database system.
- `ins()` uses write-binary mode and therefore replaces the previous stored set of records.
- There is no login or password protection.
- The program does not provide multi-user simultaneous access.
- Input validation is limited.

---

## 🚀 Future Enhancements

The project documentation proposes:

- 🎨 Build a graphical interface using **Tkinter**.
- 🗄️ Upgrade storage to a database such as **MySQL**.
- ➕ Change insertion to append records rather than replace the previous set.
- 🔐 Add authentication/login protection.
- ✅ Improve input validation and error handling.
- 🧾 Enhance billing with taxes, discounts, and printable invoices/receipts.

---

## 📚 Project Information

| Field | Details |
|---|---|
| **Project** | HOTEL GRANDE INN |
| **Student** | Parikshith |
| **Class & Section** | XII A1 |
| **School** | Sri Vageesha Vidhyashram |
| **Subject** | Computer Science |
| **Academic Session** | 2026–2027 |

---

## 🙏 Acknowledgement

I would like to express my sincere gratitude to my Computer Science teacher **Mrs. Ramya** for providing valuable guidance, encouragement, and support throughout the development of the Python project **HOTEL GRANDE INN**.

I am also thankful to **Sri Vageesha Vidhyashram** for providing the academic environment and facilities required to complete the project.

---

## 📚 References

1. Sumita Arora — *Computer Science with Python, Class XI*, Dhanpat Rai & Co.
2. Sumita Arora — *Computer Science with Python, Class XII*, Dhanpat Rai & Co.
3. Mosh Hamedani — Python Programming Videos, YouTube
4. GeeksforGeeks — Python programming reference material

---

<div align="center">

### 🏨 HOTEL GRANDE INN

**A Class XII Python Hotel Management Project**

Built with 🐍 Python · 📦 Pickle · 💾 File Handling

**[View Source Code →](https://github.com/bookspdf705-coder/picklestay/blob/main/ROOM_MANAGEMENT_PROJECT__PARIKSHITH%20(3).py)**

</div>
