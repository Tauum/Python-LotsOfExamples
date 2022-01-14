import mysql.connector
cnx = mysql.connector.connect(user='root', password='Glover98', host="127.0.0.1", database='CATTERY')

cursor = cnx.cursor()

query = "INSERT INTO VETERINARY( Phone, AddrL2, AddrL3, PostCode ) VALUES( %s, %s, %s, %s)"


values = [
        ("45217083478", "42", "Mobeldy rd", "bl12AB"),
        ("30923864765", "21", "Haliwell rd", "bl11AB"),
        ("23137604434", "22", "Fairly ln", "BL44AP"),
        ("98716472783", "1", "Bentley st", "BL23AB"),
        ("42831962439", "21", "Edgt rd", "BL36BC"),
        ("35841677749", "45", "Dong st", "BL11CQ")
        ]

cursor.executemany(query, values)

cnx.commit()

print(cursor.rowcount, "was inserted.")

cursor.close()
cnx.close()




