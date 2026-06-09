#!/usr/bin/python3
"""
Module to list state from a database
"""
import MySQLdb
import sys

if __name__ == "__main__":

	user = sys.argv[1]
	password = sys.Argv[2]
	data_base = sys.argv[3]

	db = MySQLdb.connect(
		host="localhost",
		port=3306,
		user=user,
		passwd=password,
		db=data_base
	)

	cursor = db.cursor()
	
	cursor.execute("SELECT * FROM states ORDER BY id")
	rows = cursor.fetchall()

	for row in rows:
		print(row)

	cursor.close()
	db.close()