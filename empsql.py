import pymysql.cursors

connection = pymysql.connect(host="localhost",
                             user="root",
                             password="",
                             db="TestEM")

try:
    with connection.cursor()as cursor:
        #cursor.execute ('CREATE DATABASE TestEM')
        #sql = """CREATE TABLE EMPLYEE(
                # FIRST_NAME CHAR(20) NOT NULL,
                # LAST_NAME CHAR(20),
                 #AGE INT,
                 #SEX CHAR(1),
                 #INCOME FLOAT)"""
        #cursor.execute('SELECT * FROM EMPLYEE')
        
         sql = """INSERT INTO EMPLYEE(FIRST_NAME,LAST_NAME,AGE,SEX,INCOME)
                  VALUES('SRI','GANESH',20,'M',2000),
                  ('rks','r',30,'F',5000)"""

         sql = "SELECT * FROM EMPLYEE"

         cursor.execute(sql)
         
        
except:
    print("Error:unable to fetch data")
                    
         #cursor.execute(sql)

    connection.commit()

finally:
    connection.close()
