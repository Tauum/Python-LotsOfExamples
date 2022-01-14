import mysql.connector
cnx = mysql.connector.connect(user='root', password='Glover98', host="127.0.0.1", database='CATTERY')

cursor = cnx.cursor()

query = "INSERT INTO ROOMINFO( `Type`, Max) VALUES( %s, %s )"

values = [
        ("Family", "4"),
        ("Family", "4"),
        ("Family", "4"),
        ("Dual", "2"),
        ("Dual", "2"),
        ("Dual", "2"),
        ("Dual", "2"),
        ("Dual", "2"),
        ("Dual", "2"),
        ("Dual", "2")
        ]

cursor.executemany(query, values)

cnx.commit()

print(cursor.rowcount, "was inserted.")

cursor.close()
cnx.close()
