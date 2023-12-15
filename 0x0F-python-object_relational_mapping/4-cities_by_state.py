#!/usr/bin/python3
"""script that list all states from hbtn_0e_0_usa"""

import MySQLdb
import sys


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = conn.cursor()
    cur.execute("SELECT city.id, city.name, state.name\
                FROM cities as city INNER JOIN states as state \
                ON city.state_id = s.id")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()
