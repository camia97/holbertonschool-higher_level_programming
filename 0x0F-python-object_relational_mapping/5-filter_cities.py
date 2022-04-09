#!/usr/bin/python3
'''Get all States'''
import MySQLdb
import sys


db = MySQLdb.connect(
    host="localhost",
    port=3306,
    user=sys.argv[1],
    passwd=sys.argv[2],
    db=sys.argv[3]
)
cur = db.cursor()
cur.execute("SELECT cities.name\
            FROM cities\
            JOIN states\
            ON cities.state_id = states.id\
            WHERE states.name = (%s)\
            ORDER BY states.id", [sys.argv[4], ])
rows = cur.fetchall()
for i in rows:
    print(i[0], end=", ")
print()