import mysql.connector
cnx = mysql.connector.connect(user='root', password='Glover98', host="127.0.0.1", database='CATTERY')

cursor = cnx.cursor()

query = "INSERT INTO CATREQ( Chip_ID, Add_Req ) VALUES( %s, %s)"

values = [
    (1, "likes belly rubs"),
    (2, "likes dark room"),
    (3, "left alone"),
    (3, "tv on"),
    (4, "likes playtime"),
    (5, "likes tv on"),
    (6, "likes belly rubs"),
    (7, "fragile"),
    (7, "likes treats"),
    (8, None),
    (9, None),
    (10, None),
    (11, "likes dark room"),
    (12, "likes belly rubs"),
    (12, "dark room"),
    (13, "fragile"),
    (14, None),
    (15, "likes treats"),
    (15, "left alone"),
    (16, None),
    (17, None),
    (18, "likes playtime"),
    (19, None),
    (20, "likes dark room"),
    (21, None),
    (22, "likes tv on"),
    (22, "belly rubs"),
    (23, "likes tv on"),
    (24, None),
    (25, "likes belly rubs"),
    (26, None),
    (27, "likes playtime"),
    (28, None),
    (29, "likes playtime"),
    (30, "likes playtime"),
    (30, "treats"),
    (31, None),
    (32, "left alone"),
    (33, None),
    (34, "likes dark room"),
    (34, "left alone"),
    (35, "likes dark room")
]

cursor.executemany(query, values)

cnx.commit()

print(cursor.rowcount, "was inserted.")

cursor.close()
cnx.close()
