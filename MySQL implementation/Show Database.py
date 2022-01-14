import mysql.connector
cnx = mysql.connector.connect(user='root', password='Glover98'
                              , host="127.0.0.1", database='CATTERY')

cursor = cnx.cursor()
cursor.execute("SHOW DATABASES")

for x in cursor:
  print(x)

print("-----------\n", cnx)
