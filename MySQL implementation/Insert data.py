import mysql.connector
cnx = mysql.connector.connect(user='root', password='Glover98', host="127.0.0.1", database='RADIO')

cursor = cnx.cursor()

DataInsert = input("New Data:")
query = ("INSERT INTO Genre (GenreName) VALUES (%(GenreName)s)")
query_data = { 'GenreName': DataInsert }

cursor.execute(query, query_data)


cnx.commit()
cursor.close()
cnx.close()