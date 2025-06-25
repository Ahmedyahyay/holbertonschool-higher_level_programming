# SQL Introduction Project

This repository contains SQL scripts for the **SQL Introduction** project as part of the Holberton School curriculum.

## Description

You will write SQL scripts to:

- List databases on a MySQL server.
- Create and delete databases.
- List tables in a database.
- Create tables.
- Insert, update, delete, and query records.
- Use MySQL functions and subqueries.
- Work with database schema and metadata without using `SHOW` or `DESCRIBE` commands where specified.

## Environment

- All SQL scripts are tested on **Ubuntu 20.04 LTS** with **MySQL 8.0** (e.g., version 8.0.25).
- Allowed editors: `vi`, `vim`, `emacs`.
- SQL keywords are written in uppercase.
- Each SQL file starts with a comment describing the task.
- Each query is preceded by a comment explaining the syntax.
- All files end with a newline.
- Use the sandbox environment or your own MySQL server to run the scripts.

## Repository Structure

| File Name                     | Description                                      |
|-------------------------------|------------------------------------------------|
| `0-list_databases.sql`         | Lists all databases on the MySQL server.       |
| `1-create_database_if_missing.sql` | Creates database `hbtn_0c_0` if it doesn't exist.|
| `2-remove_database.sql`        | Deletes the database `hbtn_0c_0` if it exists. |
| `3-list_tables.sql`            | Lists all tables in a given database.           |
| `4-first_table.sql`            | Creates a table `first_table` in the specified database.|
| `5-full_table.sql`             | Prints full description (CREATE statement) of `first_table`.|
| `6-list_values.sql`            | Lists all rows from the `first_table`.          |
| `7-insert_value.sql`           | Inserts a new row into `first_table`.           |
| `8-count_89.sql`               | Counts rows where id = 89 in `first_table`.     |
| `9-full_creation.sql`          | Creates `second_table` and inserts multiple rows.|
| `10-top_score.sql`             | Lists all rows from `second_table` ordered by score descending.|
| `11-best_score.sql`            | Lists records from `second_table` with score >= 10.|
| `12-no_cheating.sql`           | Updates Bob's score to 10 without using id.     |
| `13-change_class.sql`          | Deletes rows with score <= 5 from `second_table`.|
| `14-average.sql`               | Computes average score of all records in `second_table`.|
| `15-groups.sql`                | Counts number of records per score in `second_table`.|
| `16-no_link.sql`               | Lists records from `second_table` where name is not NULL, ordered by descending score.|

## How to Run Scripts

Use the following command pattern to run SQL scripts (replace password and database as needed):

```bash
cat <script.sql> | mysql -hlocalhost -uroot -p[password] [database_name]
Example:

bash
Copy code
cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
Notes
Avoid using SELECT or SHOW commands in scripts where disallowed.

Scripts must be idempotent: creating or deleting databases/tables should not fail if the object already exists or not.

Comments are required before each SQL query for clarity.

Use proper indentation and uppercase SQL keywords.

Author
Ahmed Dawwari - Holberton School Student
