import mysql.connector
cnx = mysql.connector.connect(user='root', password='Glover98',
                              host="127.0.0.1", database='CATTERY')
cursor = cnx.cursor()
#OWNER BULK INFORMATION
query1 = ("CREATE TABLE OWNERINFO("
          "ID INT NOT NULL AUTO_INCREMENT, "                   #PRIMARY KEY
          "First_Name varchar(20) NOT NULL,"
          "Last_Name varchar(20) NOT NULL,"
          "Phone VARCHAR(11) NOT NULL,"
          "AddrL1 varchar(30) NULL,"
          "AddrL2 varchar(30) NULL,"
          "AddrL3 varchar(30) NOT NULL,"
          "PostCode varchar(6) NOT NULL,"
          "PRIMARY KEY (ID))")
# #CAT BULK INFORMATION
query2 = ("CREATE TABLE CATINFO("
          "Chip_ID INT NOT NULL AUTO_INCREMENT,"                    #PRIMARY KEY
          "`Name` VARCHAR(30) NOT NULL,"
          "Sex CHAR (1) NOT NULL,"
          "DOB DATE NOT NULL,"
          "Charac VARCHAR(30) NOT NULL,"
          "Vac DATE NOT NULL,"
          "Pref_Vet VARCHAR(60) NOT NULL,"
          "Checked_In TINYINT NOT NULL,"
          "PRIMARY KEY(Chip_ID))")
#LINK OWNER CAT
query3 = ("CREATE TABLE OWNERCAT(" 
          "ID INT NOT NULL,"                                        #FOREIGN KEY   
          "Chip_ID INT NOT NULL,"                                   #FOREIGN KEY
          "FOREIGN KEY (ID) REFERENCES OWNERINFO(ID),"              
          "FOREIGN KEY (Chip_ID)  REFERENCES CATINFO(Chip_ID))")
#CAT DIET
query4 = ("CREATE TABLE CATDIET("
          "Chip_ID INT NOT NULL,"                                   #FOREIGN KEY
          "Diet_Req VARCHAR(255) NULL,"
          "FOREIGN KEY (Chip_ID) REFERENCES CATINFO(Chip_ID))")
#CAT MEDICAL HISTORY
query5 = ("CREATE TABLE CATMEDICAL("
          "Chip_ID INT NOT NULL,"                                   #FOREIGN KEY
          "Med_His VARCHAR(255) NULL,"
          "FOREIGN KEY (Chip_ID) REFERENCES CATINFO(Chip_ID))")
#CAT ADDITIONAL REQUIREMENTS
query6 = ("CREATE TABLE CATREQ("
          "Chip_ID INT NOT NULL,"                                   #FOREIGN KEY
          "Add_Req VARCHAR(255) NULL,"
          "FOREIGN KEY (Chip_ID) REFERENCES CATINFO(Chip_ID))")
#BULK VETERINARY INFORMATION
query7 = ("CREATE TABLE VETERINARY("
          "ID INT NOT NULL AUTO_INCREMENT,"                         #PRIMARY KEY
          "Phone VARCHAR(11) NOT NULL,"
          "AddrL1 VARCHAR(30) NULL,"
          "AddrL2 VARCHAR(30) NULL,"
          "AddrL3 VARCHAR(30) NOT NULL,"
          "PostCode VARCHAR(6) NOT NULL,"
          "PRIMARY KEY(ID))")
#BULK ROOM INFORMATION
query8 = ("CREATE TABLE ROOMINFO("
          "ID INT NOT NULL AUTO_INCREMENT,"                         #PRIMARY KEY
          "`Type` VARCHAR(10) NOT NULL,"
          "Max TINYINT NOT NULL,"
          "PRIMARY KEY(ID))")
#BULK OBSERVATION
query9 = ("CREATE TABLE OBSDET("
           "ID INT NOT NULL AUTO_INCREMENT,"                         #PRIMARY KEY
           "First_Name VARCHAR(30) NOT NULL,"
           "Last_Name VARCHAR(30) NOT NULL,"
           "`Date` DATE NOT NULL,"
           "`Desc` VARCHAR(255) NULL,"
           "PRIMARY KEY (ID))")
#OBSERVATION CAT LINK
query10 = ("CREATE TABLE OBSCAT("
           "ID INT NOT NULL,"                                       #FOREIGN KEY
           "Chip_ID INT NOT NULL,"                                   #FOREIGN KEY
           "FOREIGN KEY (ID) REFERENCES OBSDET(ID),"
           "FOREIGN KEY (Chip_ID) REFERENCES CATINFO(Chip_ID))")
#FOOD
query11 = ("CREATE TABLE FOODOPT("
           "ID TINYINT NOT NULL,"
           "`Type` VARCHAR(15) NOT NULL,"
           "PRIMARY KEY (ID))")
#LITTER
query12 = ("CREATE TABLE LITTEROPT("
           "ID TINYINT NOT NULL,"
           "`Type` VARCHAR(15) NOT NULL,"
           "PRIMARY KEY (ID))")
#INTERACT
query13 = ("CREATE TABLE INTERACTOPT("
           "ID TINYINT NOT NULL,"
           "`Type` VARCHAR(15) NOT NULL,"
           "PRIMARY KEY (ID))")
#BOOKING TYPE
query14 = ("CREATE TABLE BOOK(" 
           "Ref INT NOT NULL AUTO_INCREMENT,"                       #PRIMARY KEY
           "Food TINYINT NOT NULL,"
           "Interact TINYINT NOT NULL,"
           "Litter TINYINT NOT NULL,"
           "Start_Date DATE NOT NULL,"
           "End_Date DATE NOT NULL,"
           "Deposit DECIMAL(6,2) NOT NULL,"          #make trigger for this
           "Cost DECIMAL(8,2) NOT NULL,"             # make trigger for this
           "PRIMARY KEY(Ref),"
           "FOREIGN KEY (Food) REFERENCES FOODOPT(ID),"
           "FOREIGN KEY (Interact) REFERENCES INTERACTOPT(ID),"
           "FOREIGN KEY (Litter) REFERENCES LITTEROPT(ID))"
           )
#BOOKING OWNER LINK
query15 = ("CREATE TABLE BOOKOWNER("
           "Ref INT NOT NULL,"                                      #FOREIGN KEY
           "ID INT NOT NULL,"                                       #FOREIGN KEY
           "FOREIGN KEY (Ref) REFERENCES BOOK(Ref),"
           "FOREIGN KEY (ID) REFERENCES OWNERINFO(ID))")
#BOOKING CAT LINK
query16 = ("CREATE TABLE BOOKCAT("
           "Ref INT NOT NULL,"                                      #FOREIGN KEY
           "Chip_ID INT NOT NULL,"                                  #FOREIGN KEY                                 
           "FOREIGN KEY (Ref) REFERENCES BOOK(Ref),"      
           "FOREIGN KEY (Chip_ID) REFERENCES CATINFO(Chip_ID))")
#BOOKING OBSERVATION LINK
query17 = ("CREATE TABLE BOOKOBS("
           "Ref INT NOT NULL,"                                      #FOREIGN KEY
           "ID INT NOT NULL,"                                       #FOREIGN KEY
           "FOREIGN KEY (Ref) REFERENCES BOOK(Ref),"
           "FOREIGN KEY (ID) REFERENCES OBSDET(ID))")
#BOOKING ROOM LINK
query18 = ("CREATE TABLE BOOKROOM("
           "Ref INT NOT NULL,"
           "ID INT NOT NULL,"
           "FOREIGN KEY (Ref) REFERENCES BOOK(Ref),"
           "FOREIGN KEY (ID) REFERENCES ROOMINFO(ID))")
#payments
query19= ("CREATE TABLE PAYMENTS("
          "Ref INT NOT NULL,"
          "ID INT NOT NULL,"
          "Status VARCHAR(10) NULL,"
          "Method VARCHAR(30) NULL,"
          "`Date` DATE NULL," 
          "FOREIGN KEY (Ref) REFERENCES BOOK(Ref),"
          "FOREIGN KEY (ID) REFERENCES OWNERINFO(ID))")


cursor.execute("SHOW TABLES")

for x in cursor:
  print(x)

cursor.execute(query19)
cnx.commit()


cursor.close()
cnx.close()

