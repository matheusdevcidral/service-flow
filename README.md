# ServiceFlow

A CLI-based customer and revenue management system built with Python, using SQLite for persistent storage and a modular architecture.

---

##  Overview

ServiceFlow is a command-line application designed to manage customers and track revenue in a simple and organized way.
All data is stored in a SQLite database, and the system is structured into separate modules to improve readability and maintainability.

---

##  Features

* Register new customers
* List all registered customers
* Update customer information
* Delete customers
* Search customers by name
* Automatic total revenue calculation based on stored data

---

##  Project Structure

```
serviceflow/
│
├── app.py          # Application entry point (main loop and menu control)
├── database.py     # Database connection and table creation (SQLite)
├── services.py     # Business logic and CRUD operations
├── validators.py   # Input validation (name, text, numeric values)
├── ui.py           # Interface using Rich (tables, panels, messages)
│
└── data/
    └── shop.db     # SQLite database file (not included in version control)
```

---

##  Technologies Used

* Python
* SQLite
* Rich (for terminal interface)

---

##  How to Run

1. Clone the repository:

```bash
git clone https://github.com/matheusdevcidral/service-flow.git
cd service-flow
```

2. Run the application:

```bash
python app.py
```

---

##  Key Concepts Applied

* Modular project structure
* Separation of responsibilities (UI, validation, business logic, database)
* CRUD operations with SQLite
* Input validation and error handling
* Terminal UI with formatted tables using Rich

---

##  Author

Matheus Cidral
https://github.com/matheusdevcidral

---
