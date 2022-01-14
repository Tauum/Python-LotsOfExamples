import mysql.connector
cnx = mysql.connector.connect(user='root', password='Glover98', host="127.0.0.1", database='CATTERY')
cursor = cnx.cursor()

sql2 = "SELECT \
  CATINFO.Chip_ID AS Cat, \
  CATDIET.Diet_Req AS Diet, \
  CATMEDICAL.Med_his AS Med, \
  CATREQ.Add_Req AS Req \
  FROM CATINFO \
  LEFT JOIN CATDIET ON CATINFO.Chip_ID = CATDIET.Chip_ID \
  LEFT JOIN CATMEDICAL ON CATINFO.Chip_ID = CATMEDICAL.Chip_ID \
  LEFT JOIN CATREQ ON CATINFO.Chip_ID = CATREQ.chip_ID "


sql = "SELECT \
  CATINFO.Chip_ID AS Cat, \
  CATDIET.Diet_Req AS Diet, \
  GROUP_CONCAT(DISTINCT CATMEDICAL.Med_his) AS Med, \
  GROUP_CONCAT(DISTINCT CATREQ.Add_Req) AS Req  \
  FROM CATINFO \
  INNER JOIN CATDIET ON CATINFO.Chip_ID = CATDIET.Chip_ID\
  INNER JOIN CATMEDICAL ON CATINFO.Chip_ID = CATMEDICAL.Chip_ID  \
  LEFT JOIN CATREQ ON CATINFO.Chip_ID = CATREQ.chip_ID \
  INNER JOIN CATREQ ON CATINFO.Chip_ID = CATREQ.chip_ID \
  GROUP BY CATINFO.Chip_ID, CATDIET.Diet_Req"

cursor.execute(sql2)
result = cursor.fetchall()

for x in result:
  print(x)
