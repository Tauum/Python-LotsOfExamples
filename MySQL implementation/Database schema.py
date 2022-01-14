import mysql.connector
cnx = mysql.connector.connect(user='root', password='Glover98'
                              , host="127.0.0.1", database='RADIO')

cursor = cnx.cursor()

query = ("CREATE DATABASE CATTERY")

cursor.execute(query)

cnx.commit()
cursor.close()
cnx.close()


