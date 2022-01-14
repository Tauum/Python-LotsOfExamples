import mysql.connector
cnx = mysql.connector.connect(user='root', password='Glover98', host="127.0.0.1", database='CATTERY')
cursor = cnx.cursor()


sql = "SELECT \
  OWNERINFO.ID AS Owner, \
  OWNERCAT.Chip_ID AS Cat \
  FROM OWNERINFO \
  INNER JOIN OWNERCAT ON OWNERINFO.ID = OWNERCAT.ID"

cursor.execute(sql)

result = cursor.fetchall()

for x in result:
  print(x)


