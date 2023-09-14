#!/usr/bin/python3
"""
4-cities_by_state module

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
    query = """
    SELECT cities.id, cities.name, states.name
    FROM cities, states
    WHERE cities.state_id = states.id
    ORDER BY cities.id ASC
    """
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
