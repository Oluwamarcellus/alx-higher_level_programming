#!/usr/bin/python3
"""
5-filter_cities module

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

    query = """
    SELECT cities.name
    FROM cities, states
    WHERE cities.state_id = states.id AND states.name = %s
    ORDER BY cities.id ASC
    """
    cur.execute(query, (state_name, ))
    rows = cur.fetchall()
    for index, row in enumerate(rows):
        if index > 0:
            print(", ", end="")
        print(row[0], end="")
    print()

    cur.close()
    db.close()
