import mysql.connector
cnx = mysql.connector.connect(user='root', password='Glover98', host="127.0.0.1", database='CATTERY')
cursor = cnx.cursor()
query = "INSERT INTO PAYMENTS( Ref, ID, Status, Method, `Date`) VALUES( %s, %s, %s, %s, %s)"

values = [
    (1, 1, "Finalized", "Electronic Transaction", "2019-11-25"),
    (2, 1, "Finalized", "Cash", "2019-11-28"),
    (3, 1, "Pending", "Cheque", "2019-12-02"),
    (4, 2, "Unpaid", None, None),
    (5, 3, "Unpaid", None, None),
    (6, 4, "Unpaid", None, None),
    (7, 5, "Unpaid", None, None),
    (8, 6, "Unpaid", None, None),
    (9, 7, "Unpaid", None, None),
    (10, 8, "Unpaid", None, None),
    (11, 9, "Unpaid", None, None),
    (12, 10, "Unpaid", None, None),
    (13, 11, "Unpaid", None, None),
    (14, 12, "Unpaid", None, None),
    (15, 13, "Unpaid", None, None),
    (16, 14, "Unpaid", None, None),
    (17, 15, "Unpaid", None, None),
    (18, 16, "Unpaid", None, None),
    (19, 17, "Unpaid", None, None),
    (20, 18, "Unpaid", None, None),
    (21, 19, "Unpaid", None, None)
]
cursor.executemany(query, values)
cnx.commit()
print(cursor.rowcount, "was inserted.")
cursor.close()
cnx.close()