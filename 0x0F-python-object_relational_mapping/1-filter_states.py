#!/usr/bin/python3
"""
1-filter_states module

"""
import MySQLdb
import sys


argv = sys.argv[1:]
username = argv[0]
password = argv[1]
db_name = argv[2]

if __name__ == "__main__":
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=db_name
            )
    cur = db.cursor()
    cur.execute(
            """SELECT id, name FROM states
            WHERE name LIKE 'N%'
            ORDER BY states.id ASC"""
            )
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
