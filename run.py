import os
import pymysql


# Get username from Cloud9 workspace
# (modify this variable if running on another environment)
username = os.getenv('c9_user')

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user=username,
                             password='',
                             db='Chinook')

try:
    # Run a query
    with connection.cursor() as cursor:
        sql = "SELECT * FROM Artist LIMIT 1;"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    # Close the connection, regardless of whether or not the above was successful
    connection.close()