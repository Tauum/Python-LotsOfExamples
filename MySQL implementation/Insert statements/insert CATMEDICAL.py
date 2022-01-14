import mysql.connector
cnx = mysql.connector.connect(user='root', password='Glover98', host="127.0.0.1", database='CATTERY')

cursor = cnx.cursor()

query = "INSERT INTO CATMEDICAL( Chip_ID, Med_His ) VALUES( %s, %s)"

values = [
    (1, None),
    (2, "digestive issues"),
    (3, "allergy emergency"),
    (3, "hip surgery"),
    (4, None),
    (5, None),
    (6, "divestive issues"),
    (7, None),
    (8, "digestive issues"),
    (8, "stomach surgery"),
    (9, None),
    (10, None),
    (11, "leg surgery"),
    (11, "paw surgery"),
    (12, "ear surgery"),
    (12, "digestive issues"),
    (13, None),
    (14, None),
    (15, None),
    (16, None),
    (17, None),
    (18, "Tendon damage"),
    (18, "leg surgery"),
    (18, "paw surgery"),
    (19, None),
    (20, None),
    (21, "infection"),
    (22, None),
    (23, "paw surgery"),
    (23, "broken hip"),
    (24, None),
    (25, None),
    (26, None),
    (27, None),
    (28, None),
    (29, "digestive issues"),
    (30, None),
    (31, None),
    (32, None),
    (33, "tendon damage"),
    (34, None),
    (35, None)
]

cursor.executemany(query, values)

cnx.commit()

print(cursor.rowcount, "was inserted.")

cursor.close()
cnx.close()




