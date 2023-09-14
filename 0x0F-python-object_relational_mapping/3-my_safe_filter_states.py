#!/usr/bin/python3
"""
3-my_safe_filter_states module

"""
import MySQLdb
import sys


argv = sys.argv[1:]
username = argv[0]
password = argv[1]
db_name = argv[2]
state_name = argv[3]

if __name__ == "__main__":
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=db_name
            )
    cur = db.cursor()
    query = "SELECT * FROM states WHERE name = %s"
    cur.execute(query, (state_name, ))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
