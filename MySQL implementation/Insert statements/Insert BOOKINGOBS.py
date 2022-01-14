import mysql.connector
cnx = mysql.connector.connect(user='root', password='Glover98', host="127.0.0.1", database='CATTERY')
cursor = cnx.cursor()

query = "INSERT INTO BOOKOBS( Ref, ID ) VALUES( %s, %s)"

values = [
    (1, 1),
    (1, 2),
    (1, 3),
    (1, 4),
    (2, 5),
    (2, 6),
    (2, 7),
    (2, 8),
    (2, 9),
    (2, 10),
    (2, 11),
    (2, 12),
    (2, 13),
    (2, 14),
    (2, 15),
    (3, 16),
    (4, 17),
    (3, 18),
    (4, 19),
    (5, 20),
    (5, 21),
    (4, 22),
    (5, 23),
    (5, 24),
    (6, 25),
    (7, 26),
    (7, 27)
]

cursor.executemany(query, values)
cnx.commit()
print(cursor.rowcount, "was inserted.")
cursor.close()
cnx.close()