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
cur = sys.argv[3].cursor()
cur.execute("SELECT states FROM argv[3] ORDER BY states.id ASC")
rows = cur.fetchall()
for i in rows:
    print(i)