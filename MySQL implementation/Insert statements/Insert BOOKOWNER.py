import mysql.connector
cnx = mysql.connector.connect(user='root', password='Glover98', host="127.0.0.1", database='CATTERY')
cursor = cnx.cursor()

query = "INSERT INTO BOOKOWNER( Ref, ID) VALUES( %s, %s)"

values = [
    (1, 1),
    (2, 1),
    (3, 1),
    (4, 2),
    (5, 3),
    (6, 4),
    (7, 5),
    (8, 6),
    (9, 7),
    (10, 8),
    (11, 9),
    (12, 10),
    (13, 11),
    (14, 12),
    (15, 13),
    (16, 14),
    (17, 15),
    (18, 16),
    (19, 17),
    (20, 18),
    (21, 19)
]

cursor.executemany(query, values)
cnx.commit()
print(cursor.rowcount, "was inserted.")
cursor.close()
cnx.close()

