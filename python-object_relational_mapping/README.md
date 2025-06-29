
# Python - Object-relational mapping

This project is part of the **Holberton School Higher Level Programming curriculum**, focused on learning **how to map Python classes to database tables using SQL and ORM (Object Relational Mapping)**.

---

## 📚 Learning Objectives

By completing this project, I gained knowledge in:

- Connecting to a MySQL database using MySQLdb and SQLAlchemy.
- Executing SQL queries using both raw SQL and ORM.
- Preventing SQL injection in Python scripts.
- Interacting with relational databases using Python objects.
- Building models that map to database tables.

---

## 🛠️ Technologies Used

- Python 3.x
- MySQLdb (for SQL queries)
- SQLAlchemy (for ORM)
- MySQL Server (localhost, port 3306)
- Ubuntu 20.04 (for testing)

---

## 📁 Project Files Overview

Each file addresses a specific task related to SQL, MySQLdb, or SQLAlchemy usage.

| File | Description |
|------|-------------|
| `0-select_states.py` | Lists all states from a database using MySQLdb |
| `1-filter_states.py` | Lists all states that start with `N` |
| `2-my_filter_states.py` | Filters states using a given argument (vulnerable to SQL injection) |
| `3-my_safe_filter_states.py` | Filters states safely using placeholders to avoid SQL injection |
| `4-cities_by_state.py` | Lists all cities with their states |
| `5-filter_cities.py` | Lists all cities of a specific state (safe from SQL injection) |
| `model_state.py` | SQLAlchemy model for `State` class |
| `6-model_state.py` | Creates the `states` table via SQLAlchemy |
| `7-model_state_fetch_all.py` | Lists all `State` objects using SQLAlchemy |
| `8-model_state_fetch_first.py` | Prints the first `State` object |
| `9-model_state_filter_a.py` | Lists states with names containing the letter `a` |
| `10-model_state_my_get.py` | Prints the state with a given name |
| `11-model_state_insert.py` | Adds the state “Louisiana” to the database |
| `12-model_state_update_id_2.py` | Updates the name of the state with `id = 2` |
| `13-model_state_delete_a.py` | Deletes all states with names containing `a` |
| `model_city.py` | Defines the `City` model |
| `14-model_city_fetch_by_state.py` | Lists all cities by state using a relationship between models 
