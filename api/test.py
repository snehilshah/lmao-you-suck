import mysql.connector
cnx = mysql.connector.connect(user='avnadmin', password='tiger',
                              host='127.0.0.1',
                              database='employees')

try:
    cursor = cnx.cursor()
    cursor.execute("""
      select 3 from your_table
   """)
    result = cursor.fetchall()

    print(result)
finally:
    cnx.close()
