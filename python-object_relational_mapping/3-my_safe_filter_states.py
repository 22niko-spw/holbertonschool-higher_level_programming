#!/usr/bin/python3
"""
Module to list state from a database
"""

import sys
import MySQLdb

if __name__ == "__main__":

    user = sys.argv[1]
    password = sys.argv[2]
    data_base = sys.argv[3]
    state_name_searched = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=password,
        db=data_base
    )

    cursor = db.cursor()

    cursor.execute(
        "SELECT * FROM states "
        "WHERE BINARY name = %s "
        "ORDER BY id ASC", (state_name_searched,))

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
