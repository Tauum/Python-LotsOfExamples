import mysql.connector
cnx = mysql.connector.connect(user='root', password='Glover98', host="127.0.0.1", database='CATTERY')

cursor = cnx.cursor()

query = "INSERT INTO INTERACTOPT( ID, `Type`) VALUES( %s, %s )"

values = [
    (0, "No service"),
    (1, "Full service")
]

cursor.executemany(query, values)

cnx.commit()

print(cursor.rowcount, "was inserted.")

cursor.close()
cnx.close()
