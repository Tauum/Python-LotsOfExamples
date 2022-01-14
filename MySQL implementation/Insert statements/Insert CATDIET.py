import mysql.connector
cnx = mysql.connector.connect(user='root', password='Glover98', host="127.0.0.1", database='CATTERY')

cursor = cnx.cursor()

query = "INSERT INTO CATDIET( Chip_ID, Diet_Req ) VALUES( %s, %s)"


values = [
    (1, None),
    (2, "Low carb diet"),
    (3, "nut allergy"),
    (4, None),
    (5, None),
    (6, "Low fat diet"),
    (7, None),
    (8, "Low carb diet"),
    (8, "nut allergy"),
    (9, None),
    (10, None),
    (11, "low fat diet"),
    (12, "low carb diet"),
    (13, None),
    (14, "nut allergy"),
    (15, None),
    (16, "seed alergy"),
    (17, None),
    (18, "seed & nut allergy"),
    (19, None),
    (20, "Low fat diet"),
    (20, "seed alergy"),
    (21, None),
    (22, None),
    (23, None),
    (24, None),
    (25, "low carb diet"),
    (26, None),
    (27, None),
    (28, None),
    (29, "High fat diet"),
    (29, "seed alergy"),
    (30, None),
    (31, None),
    (32, None),
    (33, "high carb diet"),
    (34, None),
    (35, None)
]

cursor.executemany(query, values)

cnx.commit()

print(cursor.rowcount, "was inserted.")

cursor.close()
cnx.close()
