import mysql.connector
cnx = mysql.connector.connect(user='root', password='Glover98', host="127.0.0.1", database='CATTERY')

cursor = cnx.cursor()

query = "INSERT INTO CATINFO( `Name`, Sex, DOB, Charac, Vac, Pref_Vet, Checked_In) VALUES( %s, %s, %s, %s, %s, %s, %s )"


values = [
    ('Aatrox', 'm', '2018-11-1', 'jolly', '2019-01-1', 'danny Bank', "0"),
    ('Ahri', 'f', '2016-08-04', 'quiet', '2019-04-25', 'brenda Burk', "0"),
    ('Blitz', 'm', '2013-09-13', 'quiet', '2019-08-11', 'paris Vamb', "1"),
    ('Curley', 'm', '2017-06-04', 'playfull', '2017-05-02', 'hila Klein', "1"),
    ('Mandy', 'm', '2015-11-02', 'reserved', '2016-09-08', 'sally Broker', "1"),
    ('Nami', 'f', '2012-05-11', 'playfull', '2016-11-22', 'charley Bruff', "1"),
    ('Kog', 'm', '2018-05-12', 'contempt', '2018-08-15', 'barry	Chole', "1"),
    ('Caitlyn', 'f', '2019-04-02', 'underactive', '2019-05-06', 'felicity Smoke', "0"),
    ('Barney', 'm', '2013-08-15', 'jolly', '2017-10-19', 'harry Bank', "0"),
    ('Gnar', 'm', '2016-05-17', 'contempt', '2018-06-05', 'ari Milner', "0"),
    ('Charley', 'f', '2018-05-11', 'quiet', '2019-09-22', 'grace Rodgers', "0"),
    ('Bundy', 'm', '2013-09-05', 'jolly', '2019-08-02', 'bethaney Evans', "0"),
    ('Ringo', 'm', '2011-11-12', 'underactive', '2019-11-02', 'orion Derrik', "0"),
    ('Smiley', 'm', '2016-05-09', 'playfull', '2019-10-15', 'sally Broker', "0"),
    ('Bentley', 'f', '2017-05-31', 'contempt', '2018-08-20', 'harry Bank', "0"),
    ('Barney', 'm', '2018-06-01', 'jolly', '2019-10-11', 'harry Bank', "0"),
    ('Yuumi', 'f', '2013-09-11', 'jolly', '2019-08-01', 'orion Derrik', "0"),
    ('Rammus', 'm', '2013-08-21', 'overactive', '2016-09-10', 'harry Bank', "0"),
    ('Viktor', 'm', '2012-09-27', 'contempt', '2017-06-06', 'ari Milner', "0"),
    ('Xerath', 'm', '2017-09-12', 'reserved', '2019-05-12', 'paris Vamb', "0"),
    ('Azir', 'm', '2014-05-14', 'contempt', '2019-11-01', 'orion Derrik', "0"),
    ('Reginald', 'm', '2013-06-09', 'overactive', '2017-11-05', 'brenda Burk', "0"),
    ('Harry', 'm', '2016-09-02', 'overactive', '2019-09-05', 'brenda Burk', "0"),
    ('Indie', 'f', '2019-06-02', 'playfull', '2019-11-11', 'orion Derrik', "0"),
    ('Dotty', 'f', '2011-06-29', 'jolly', '2018-08-21', 'bethaney Evans', "0"),
    ('Wesley', 'm', '2019-10-13', 'quiet', '2019-12-19', 'hila Klein', "0"),
    ('Karma', 'f', '2016-05-22', 'overactive', '2017-12-22', 'sally Broker', "0"),
    ('Nami', 'f', '2018-09-02', 'contempt', '2019-06-19', 'harry Bank', "0"),
    ('Nautalus', 'm', '2015-12-11', 'jolly', '2016-09-01', 'hila Klein', "0"),
    ('Tristy', 'f', '2016-09-08', 'overactive', '2016-11-15', 'bethaney Evans', "0"),
    ('Kaisa', 'f', '2013-05-21', 'quiet', '2019-09-19', 'sally Broker', "0"),
    ('Baron', 'm', '2012-07-17', 'reserved', '2019-06-19', 'charley Bruff', "0"),
    ('Braum', 'm', '2015-09-01', 'overactive', '2019-08-02', 'harry Bank', "0"),
    ('Alistar', 'm', '2017-08-14', 'reserved', '2017-08-05', 'paris Vamb', "0"),
    ('Ahri', 'f', '2012-12-31', 'reserved', '2017-11-19', 'bethaney Evans', "0")
    ]




cursor.executemany(query, values)


cnx.commit()

print(cursor.rowcount, "was inserted.")

cursor.close()
cnx.close()