import mysql.connector
cnx = mysql.connector.connect(user='root', password='Glover98', host="127.0.0.1", database='CATTERY')
cursor = cnx.cursor()

query = "INSERT INTO BOOKCAT( Ref, Chip_ID ) VALUES( %s, %s)"

values = [
    (1, 1),
    (2, 2),
    (2, 3),
    (3, 1),
    (4, 2),
    (5, 3),
    (5, 4),
    (6, 5),
    (7, 6),
    (7, 7),
    (7, 8),
    (8, 9),
    (8, 10),
    (8, 11),
    (9, 12),
    (9, 13),
    (9, 14),
    (10, 15),
    (11, 16),
    (11, 17),
    (11, 18),
    (12, 19),
    (12, 20),
    (13, 21),
    (13, 22),
    (13, 23),
    (14, 24),
    (14, 25),
    (15, 26),
    (16, 27),
    (16, 28),
    (17, 29),
    (18, 30),
    (19, 31),
    (19, 32),
    (20, 33),
    (20, 34),
    (21, 35),
]

cursor.executemany(query, values)
cnx.commit()
print(cursor.rowcount, "was inserted.")
cursor.close()
cnx.close()