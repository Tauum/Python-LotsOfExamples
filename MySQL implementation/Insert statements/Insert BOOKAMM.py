import mysql.connector
cnx = mysql.connector.connect(user='root', password='Glover98', host="127.0.0.1", database='CATTERY')
cursor = cnx.cursor()

query = "INSERT INTO BOOKAMM( Ref, Num_Cat ) VALUES( %s, %s)"

values = [
    (1, "1"),
    (2, "2"),
    (3, "1"),
    (4, "1"),
    (5, "2"),
    (6, "1"),
    (7, "3"),
    (8, "3"),
    (9, "3"),
    (10, "1"),
    (11, "3"),
    (12, "2"),
    (13, "3"),
    (14, "2"),
    (15, "1"),
    (16, "2"),
    (17, "1"),
    (18, "1"),
    (19, "2"),
    (20, "2"),
    (21, "1")
]

cursor.executemany(query, values)
cnx.commit()
print(cursor.rowcount, "was inserted.")
cursor.close()
cnx.close()