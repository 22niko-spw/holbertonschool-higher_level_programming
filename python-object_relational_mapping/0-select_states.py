#!/usr/bin/python3
"""
Module to list state from a database
"""

import MySQLdb
import sys

if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.Argv[2]
    data_base = sys.argv[3]

    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username
        passwd=password,
        db=data_base
    )

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM states ORDER BY id")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    conn.close()
