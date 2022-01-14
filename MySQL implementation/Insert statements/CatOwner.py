import mysql.connector
cnx = mysql.connector.connect(user='root', password='Glover98', host="127.0.0.1", database='CATTERY')

cursor = cnx.cursor()

query = "INSERT INTO OWNERCAT( ID, Chip_ID ) VALUES( %s, %s)"


values = [
    (1, 1),
    (2, 2),
    (3, 3),
    (3, 4),
    (4, 5),
    (5, 6),
    (5, 7),
    (5, 8),
    (6, 9),
    (6, 10),
    (6, 11),
    (7, 12),
    (7, 13),
    (7, 14),
    (8, 15),
    (8, 16),
    (9, 17),
    (9, 18),
    (9, 19),
    (10, 20),
    (11, 21),
    (11, 22),
    (11, 23),
    (12, 24),
    (12, 25),
    (13, 26),
    (14, 27),
    (14, 28),
    (15, 29),
    (16, 30),
    (17, 31),
    (17, 32),
    (18, 33),
    (18, 34),
    (19, 35)
]

cursor.executemany(query, values)

cnx.commit()

print(cursor.rowcount, "was inserted.")

cursor.close()
cnx.close()
