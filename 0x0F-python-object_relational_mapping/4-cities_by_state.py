#!/usr/bin/python3
"""
    a script that lists all states with a name starting with N (upper N)
    from the database hbtn_0e_0_usa
"""
import MySQLdb
from sys import argv


if __name__ == '__main__':
    av = argv
    if len(av) == 4:
        user = argv[1]
        passwd = argv[2]
        db_name = argv[3]

        try:
            db = MySQLdb.connect(
                    host='localhost', port=3306,
                    user=user, passwd=passwd, db=db_name
                )
            cur = db.cursor()
            cur.execute(
                    "SELECT cities.id, cities.name, states.name FROM cities \
                    INNER JOIN states \
                    ON cities.state_id = states.id")
            for each in cur.fetchall():
                print(each)
            cur.close()
            db.close()
        except MySQLdb.Error as e:
            print(f"Error: {e}")
    else:
        print("Usage: <py script> <user> <password> <db>")
