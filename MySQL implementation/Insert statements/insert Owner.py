import mysql.connector
cnx = mysql.connector.connect(user='root', password='Glover98', host="127.0.0.1", database='CATTERY')

cursor = cnx.cursor()

query = "INSERT INTO OWNERINFO(First_Name, Last_Name, Phone, AddrL1, AddrL2, AddrL3, PostCode) VALUES( %s, %s, %s, %s, %s, %s, %s)"


values = [
    ('Thomas', 'Storey', '90576945651', '12', 'darbey st', 'Bolton', 'BL41AB'),
    ('Dave', 'Something', '39393259971', '14', 'haliwell rd', 'Bolton', 'BL11AB'),
    ('Andrew', 'Rulez', '34961631281', '77', 'cooper st', 'Bolton', 'BL67AT'),
    ('Trevor', 'Cant remember', '33369121515', '69', 'turton-hgt', 'Bolton', 'BL23DU'),
    ('sally ', 'dailey', '20768557305', '44', 'appletree', 'Bolton', 'BL11DP'),
    ('Matty', 'Burton', '13757295556', '33', 'darby rd', 'Bolton', 'BL11AB'),
    ('Ben', 'Mackle', '50129187996', '24', 'haliwell rd', 'Bolton', 'BL11AB'),
    ('Stacey', 'Mackle', '15175790407', '24', 'haliwell rd', 'Bolton', 'BL11AB'),
    ('Damien', 'Buck', '32929268356', '29', 'fairy-ln', 'Bolton', 'BL44AP'),
    ('Andy', 'Pandy', '73787759463', '34', 'daisy st', 'Bolton', 'BL42CB'),
    ('Jordan', 'Burton', '3336929636', '1', 'dong ln', 'Bolton', 'BL11QC'),
    ('Mathew', 'Price', '56524251303', '55', 'mary ave', 'Bolton', 'BL22VB'),
    ('Kendle', 'Burrows', '44793722125', '77', 'newbank rd', 'Bolton', 'BL23CB'),
    ('Molly', 'Hart', '49689643441', '42', 'ventry ln', 'Bolton', 'BL34GV'),
    ('Naomi', 'Hart', '99143886524', '77', 'ventry ln', 'Bolton', 'BL34GV'),
    ('Paris', 'Hilton', '99143886524', '99', 'Hilton hotel', 'Bolton', 'BL11DP'),
    ('Daniel', 'Turner', '25074819564', '77', 'turton ave', 'Bolton', 'BL23DU'),
    ('Willaim', 'Smedley', '43852409761', '24', 'edgt rd', 'Bolton', 'BL35BC'),
    ('Jordan', 'Peterson', '68822629367', '32', 'edgt rd', 'Bolton', 'BL35BC')
]


cursor.executemany(query, values)

cnx.commit()

print(cursor.rowcount, "was inserted.")

cursor.close()
cnx.close()
