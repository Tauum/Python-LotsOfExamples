import mysql.connector

cnx = mysql.connector.connect(user='root', password='Glover98', host="127.0.0.1", database='CATTERY')

cursor = cnx.cursor()

query = "INSERT INTO OBSCAT( ID, Chip_ID ) VALUES( %s, %s )"

values = [
    (1, 21),
    (2, 21),
    (3, 21),
    (4, 22),
    (5, 23),
    (6, 22),
    (7, 23),
    (8, 23),
    (9, 22),
    (10, 23),
    (11, 22),
    (12, 23),
    (13, 22),
    (14, 23),
    (15, 1),
    (16, 2),
    (17, 1),
    (18, 2),
    (19, 3),
    (20, 4),
    (21, 2),
    (22, 3),
    (23, 4),
    (24, 5),
    (25, 6),
    (26, 7),
    (27, 8)
]

cursor.executemany(query, values)

cnx.commit()

print(cursor.rowcount, "was inserted.")

cursor.close()
cnx.close()


