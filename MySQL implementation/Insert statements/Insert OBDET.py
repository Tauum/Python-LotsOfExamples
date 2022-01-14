import mysql.connector

cnx = mysql.connector.connect(user='root', password='Glover98', host="127.0.0.1", database='CATTERY')

cursor = cnx.cursor()

query = "INSERT INTO OBSDET(First_Name, Last_Name, `Date`, `Desc` ) VALUES( %s, %s, %s, %s )"

values = [
    ("james", "bond", "2019-11-22", None),
    ("wesley", "sands", "2019-11-23", None),
    ("georgial", "heart", "2019-11-24", "infection getting worse vet called"),
    ("grant", "flow", "2019-11-24", None),
    ("james", "bond", "2019-11-24", None),
    ("wesley", "sands", "2019-11-25", None),
    ("wesley", "sands", "2019-11-25", None),
    ("wesley", "sands", "2019-11-25", None),
    ("georgial", "heart", "2019-11-26", None),
    ("georgial", "heart", "2019-11-26", None),
    ("grant", "flow", "2019-11-27", None),
    ("grant", "flow", "2019-11-27", "cat fallen off tower broken hip vet called"),
    ("james", "bond", "2019-11-28", None),
    ("james", "bond", "2019-11-28", "cast pulled off vet called"),
    ("wesley", "sands", "2019-12-01", None),
    ("wesley", "sands", "2019-12-01", None),
    ("georgial", "heart", "2019-12-02", None),
    ("georgial", "heart", "2019-12-02", None),
    ("georgial", "heart", "2019-12-02", None),
    ("georgial", "heart", "2019-12-02", None),
    ("grant", "flow", "2019-12-03", None),
    ("grant", "flow", "2019-12-03", None),
    ("grant", "flow", "2019-12-03", None),
    ("james", "bond", "2019-12-04", None),
    ("james", "bond", "2019-12-04", None),
    ("james", "bond", "2019-12-04", None),
    ("james", "bond", "2019-12-04", None)
]

cursor.executemany(query, values)

cnx.commit()

print(cursor.rowcount, "was inserted.")

cursor.close()
cnx.close()
