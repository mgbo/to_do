
import mysql.connector
import pymysql
import random

def mydata():
    val = []
    for i in range(300):
        for j in range(300):
            val.append((i, j, random.randint(6, 15)))

    return val

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database='deepwater'
)

# print(mydb)
# mycursor = mydb.cursor()

# my_cursor.execute("CREATE DATABASE deepwater")
# my_cursor.execute("SHOW DATABASES")


# mycursor.execute("CREATE TABLE test3_deeps (x INTEGER(10), y INTEGER(10),d INTEGER(10))")
# mycursor.execute("SHOW TABLES")
# for i in mycursor:
#     print(i)

# sql = "INSERT INTO test3_deeps (x, y, d) VALUES (%s, %s, %s)"
# val = (3, 4, 5)
# mycursor.execute(sql, val)

# val = mydata()
# mycursor.executemany(sql, val)
# mydb.commit()

# print(mycursor.rowcount, "was inserted")
# print(mycursor.lastrowid)


# mycursor.execute("SELECT * FROM test3_deeps")
# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x)


# sql = "SELECT * FROM deeps WHERE x = %s AND y = %s"
# adr = (0, 3)
# mycursor.execute(sql, adr)

# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x)






