import pymysql.cursors

connection = pymysql.connect(host="localhost",
                            user="root",
                            port=3306,
                            password="",
                            db="student1")

try:
    with connection.cursor()as cursor:
       # cursor.execute('CREATE DATABASE student1')
        #sql = """ CREATE TABLE studentdetails(
                   #name char(20) NOT NULL,
                   #age int)"""

        sql ="""INSERT INTO studentdetails(
                name,age)
                VALUES('sri',20)"""
    
        #ver = cursor.fetchone()
        #print ("Database version: %s" %ver)
        
        cursor.execute("SELECT * FROM studentdetails")
        rows = cursor.fetchall()

        #for row in cursor.fetchall():
            #print (row[0], "",row[1])

        for row in rows:
            print (row)
      

                       
        connection.commit()
           
        

finally:
    connection.close()
