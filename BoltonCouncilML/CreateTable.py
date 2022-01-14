import csv, sqlite3

con = sqlite3.connect("test3") # if db doesnt exist it will create one
cur = con.cursor()
cur.execute("""CREATE TABLE Data
    (
    Country text,
    `Country Code` text,
    Region text,
    `Region Code` text,
    `Second Tier Authority` text,
    `Local Authority` text,
    `Local Authority Code` text,
    `Calendar Year` integer,
    `LA CO2 Sector` text,
    `LA CO2 Sub - sector` text,
    `Territorial emissions(kt CO2)` real,
    `Emissions within the scope of influence of LAs(kt CO2)` real,
    `Mid - year Population(thousands)` real,
    `Area(km2)` real
    ) """)

# Opening the person-records.csv file
file = open('2005-19_Local_Authority_CO2_emissions.csv')

# Reading the contents of the file
contents = csv.reader(file)

# SQL query to insert data
insert_records = "INSERT INTO Data (Country, 'Country Code', Region, 'Region Code', 'Second Tier Authority', 'Local Authority', " \
                 "'Local Authority Code', 'Calendar Year', 'LA CO2 Sector', 'LA CO2 Sub - sector', " \
                 "'Territorial emissions(kt CO2)', 'Emissions within the scope of influence of LAs(kt CO2)', " \
                 "'Mid - year Population(thousands)', 'Area(km2)') VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,? )"

# Importing the contents of the file
cur.executemany(insert_records, contents)

# SQL query to retrieve all data from table To verify csv file has been successfully inserted
select_all = "SELECT * FROM Data"
rows = cur.execute(select_all).fetchall()

# Output to the console screen
for r in rows:
    print(r)

# Committing the changes
con.commit()
# closing the database connection
con.close()

