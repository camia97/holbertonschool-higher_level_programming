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
cur.execute("SELECT cities.id, states.name, cities.name \
FROM states \
JOIN cities \
ON cities.state_id = states.id \
ORDER BY states.id")
rows = cur.fetchall()
for i in rows:
    print(i)
