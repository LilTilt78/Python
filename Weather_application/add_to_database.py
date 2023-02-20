import mysql.connector

class Database:
    """Obsahuje konfiguraci připojení k databázi a funkci addToDB"""
    mydb = mysql.connector.connect(host = "localhost", user = "root", passwd = "123password", database = "database1")
    mycursor = mydb.cursor()
    jednou = True
    while(jednou == True):
        id = 1
        jednou = False


    def addToDB(id, source, time, city, tempc, tempf, desc, feels, wind, humi, visi):
        """Funkce provádí samotný proces zapsání vložených dat do databáze"""
        sqlFormula = "INSERT INTO weather_data (weatherID, source, sample_time, city, temp_celsius, temp_fahrenheit, description, feels_like, wind_speed, humidity, visibility) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)" #%s funguje jako place holder
        data = (id, source, time, city, tempc, tempf, desc, feels, wind, humi, visi)
        Database.mycursor.execute(sqlFormula, data)
        Database.mydb.commit()
