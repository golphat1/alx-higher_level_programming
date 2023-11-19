#!/usr/bin/python3
"""
script that lists all states with a name
starting with N from the database hbtn_0e_0usa.
script takes 3 arguments: mysql username,
mysql password and database name
Use the module MySQLdb
script connect to MYSQL server runninng on localhost at port 3306
Result sorted in ascending order by states.id
"""
import MySQLdb
from sys import argv


"""
Below is a function of the above requirements
"""


def main():
    """takes the three arguments"""
    user = argv[1]
    password = argv[2]
    database = argv[3]

    """connect to the database"""
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=user, passwd=password,
                         db=database)

    """Create a cursor to interact with the database"""
    cursor = db.cursor()

    """SQL query to retrieve states sorted by id in ascending order"""
    query = "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC"

    """Execute the query"""
    cursor.execute(query)

    """Fetch all the results"""
    results = cursor.fetchall()

    """Display the results"""
    for row in results:
        print(row)


if __name__ == "__main__":
    main()
