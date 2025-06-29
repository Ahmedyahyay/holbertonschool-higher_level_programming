#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa
Usage: ./0-select_states.py <mysql_username> <mysql_password> <database_name>
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Get MySQL credentials from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to the MySQL server on localhost:3306
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    # Create a cursor to execute queries
    cur = db.cursor()

    # Execute the SELECT query to get all states ordered by id
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all rows and print each
    for row in cur.fetchall():
        print(row)

    # Close cursor and connection
    cur.close()
    db.close()

