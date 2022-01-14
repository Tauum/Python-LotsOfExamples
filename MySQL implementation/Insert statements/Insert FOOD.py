import mysql.connector
cnx = mysql.connector.connect(user='root', password='Glover98', host="127.0.0.1", database='CATTERY')

cursor = cnx.cursor()

query = "INSERT INTO FOODOPT( ID, `Type`) VALUES( %s, %s )"

values = [
    (0, "Own"),
    (1, "Standard"),
    (2, "Luxuary")
]

cursor.executemany(query, values)

cnx.commit()

print(cursor.rowcount, "was inserted.")

cursor.close()
cnx.close()
