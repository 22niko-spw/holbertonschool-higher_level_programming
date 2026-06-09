import MySQLdb
import sys

conn = MySQLdb.connect(
	host="localhost",
	port=3306,
	user=sys.argv[1],
	passwd=sys.argv[2],
	db=sys.argv[3])

cursor = conn.cursor()
cursor.execute("SELECT * FROM states ORDER BY states.id")

rows = cursor.fetchall()
for row in rows:
    print(row)
