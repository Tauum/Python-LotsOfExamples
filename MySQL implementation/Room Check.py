import mysql.connector
cnx = mysql.connector.connect(user='root', password='Glover98', host="127.0.0.1", database='CATTERY')
cursor = cnx.cursor()

cursor.execute("USE CATTERY; "
               "SELECT * FROM BOOK "
               "WHERE Start_Date BETWEEN '2019-11-22' AND '2019-12-05' "
               "ORDER BY Start_Date ASC;")


