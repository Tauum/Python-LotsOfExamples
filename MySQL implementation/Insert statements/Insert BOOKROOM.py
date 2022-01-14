import mysql.connector
cnx = mysql.connector.connect(user='root', password='Glover98', host="127.0.0.1", database='CATTERY')
cursor = cnx.cursor()

query = "INSERT INTO BOOKROOM( Ref, ID ) VALUES( %s, %s)"

values = [
    (1, 4),
    (2, 3),
    (3, 4),
    (4, 5),
    (5, 6),
    (6, 7),
    (7, 3),
    (8, 2),
    (9, 1),
    (10, 8),
    (11, 3),
    (12, 9),
    (13, 2),
    (14, 10),
    (15, 4),
    (16, 5),
    (17, 6),
    (18, 7),
    (19, 2),
    (20, 1),
    (21, 10)
]

cursor.executemany(query, values)
cnx.commit()
print(cursor.rowcount, "was inserted.")
cursor.close()
cnx.close()