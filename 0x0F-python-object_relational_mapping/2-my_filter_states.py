#!/usr/bin/python3
'''Get all States'''
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name= BINARY '{}'\
            ORDER BY states.id".format(sys.argv[4]))
    rows = cur.fetchall()
    for i in rows:
        print(i)
