import csv, sqlite3

con = sqlite3.connect("test3") # if db doesnt exist it will create one
cur = con.cursor()
cur.execute("CREATE TABLE data (col1, col2);") # use your column names here

with open('2005-19_Local_Authority_CO2_emissions.csv','r') as fin: # `with` statement available in 2.5+
    # csv.DictReader uses first line in file for column headings by default
    dr = csv.DictReader(fin) # comma is default delimiter
    to_db = [(i['col1'], i['col2']) for i in dr]

cur.executemany("INSERT INTO data (col1, col2) VALUES (?, ?);", to_db)
con.commit()
con.close()