#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa in ascending order by states.id
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Connect to MySQL server
    conn = MySQLdb.connect(
        host="localhost", port=3306,
        user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3]
    )

    # Create a cursor
    cur = conn.cursor()

    # Execute the query
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch and print all rows
    for row in cur.fetchall():
        print(row)

    # Clean up
    cur.close()
    conn.close()
