# SQL - More Queries

This project is part of the **Higher Level Programming** curriculum at Holberton School. It focuses on more advanced MySQL topics, including user and privilege management, database/table constraints, foreign keys, and subqueries.

## 📁 Project Directory
`holbertonschool-higher_level_programming/SQL_more_queries`

---

## 📚 Learning Objectives

- How to create and manage MySQL users and privileges.
- How to define and enforce constraints (e.g., `NOT NULL`, `UNIQUE`, `DEFAULT`).
- How to use `FOREIGN KEY` constraints to link tables.
- How to perform subqueries.
- How to use `JOIN` and understand its effects.
- How to use aggregate functions like `COUNT()` and `AVG()`.

---

## 📝 Task List

### 0. My privileges!
- **File:** `0-privileges.sql`
- Lists all privileges of `user_0d_1` and `user_0d_2`.

---

### 1. Root user
- **File:** `1-create_user.sql`
- Creates MySQL user `user_0d_1` with all privileges.

---

### 2. Read user
- **File:** `2-create_read_user.sql`
- Creates database `hbtn_0d_2` and user `user_0d_2` with only `SELECT` privileges.

---

### 3. Always a name
- **File:** `3-force_name.sql`
- Creates table `force_name` with a `NOT NULL` constraint on the `name` column.

---

### 4. ID can't be null
- **File:** `4-never_empty.sql`
- Creates table `id_not_null` with a default value of `1` for the `id` column.

---

### 5. Unique ID
- **File:** `5-unique_id.sql`
- Creates table `unique_id` where `id` must be `UNIQUE` with a default value of `1`.

---

### 6. States table
- **File:** `6-states.sql`
- Creates database `hbtn_0d_usa` and table `states` with an `id` as `PRIMARY KEY` and `AUTO_INCREMENT`.

---

### 7. Cities table
- **File:** `7-cities.sql`
- Adds table `cities` linked to `states` via `FOREIGN KEY (state_id)`.

---

### 8. Cities of California
- **File:** `8-cities_of_california_subquery.sql`
- Lists cities in California without using `JOIN`.

---

### 9. Cities by States
- **File:** `9-cities_by_state_join.sql`
- Lists all cities and their corresponding states using `JOIN`.

---

### 10. Genre ID by show
- **File:** `10-genre_id_by_show.sql`
- Lists all shows with at least one linked genre.

---

### 11. Genre ID for all shows
- **File:** `11-genre_id_all_shows.sql`
- Lists all shows with their genre IDs (or `NULL` if none linked).

---

### 12. No genre
- **File:** `12-no_genre.sql`
- Lists shows without any genre linked.

---

### 13. Number of shows by genre
- **File:** `13-count_shows_by_genre.sql`
- Lists genres and the count of shows linked to each.

---

### 14. My genres
- **File:** `14-my_genres.sql`
- Lists all genres linked to the show **Dexter**.

---

### 15. Only Comedy
- **File:** `15-comedy_only.sql`
- Lists all shows belonging to the **Comedy** genre.

---

### 16. List shows and genres
- **File:** `16-shows_by_genre.sql`
- Lists all shows with their genres (including `NULL` where no genre exists).

---
