import mysql.connector

cnx = mysql.connector.connect(user='root', password='Glover98', host="127.0.0.1", database='RADIO')

print(mysql)
cursor = cnx.cursor()

query = ("SELECT StationName, OwnerName from STATION INNER JOIN `OWNER` ON STATION.OwnerID = `OWNER`.OwnerID")

cursor.execute(query)

for (StationName, OwnerName) in cursor:
    print("{} Is owned by {}".format(StationName, OwnerName))

cursor.close()
cnx.close()