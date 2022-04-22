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
    cur.execute("SELECT cities.name\
            FROM `cities`\
            JOIN `states`\
            ON cities.state_id = states.id\
            WHERE states.name = BINARY (%s)\
            ORDER BY cities.id", (sys.argv[4], ))
    rows = cur.fetchall()
    if len(rows) > 0:
        for i in range(len(rows)):
            if i < len(rows) - 1:
                print(rows[i][0], end=", ")
            else:
                print(rows[i][0])
    else:
        print()
