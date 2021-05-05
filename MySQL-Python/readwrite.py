#!/usr/bin/python3

import pymysql

conn =pymysql.connect(database="db1",user="sai",password="sai",host="localhost")
cur=conn.cursor()

name = "user1"
age = "25"
gender = "M"
address = "Tamilnadu"

data={'name':name,'age':age,'gender':gender,'address':address}
print(data)

# Saving data to DB
cur.execute("INSERT INTO users (name,age,gender,address) VALUES (%(name)s,%(age)s,%(gender)s,%(address)s);",data)
conn.commit()
print("saved to db")

#reading data from DB
cur.execute("SELECT * FROM users;")
data1=cur.fetchone()
data2=cur.fetchall()

print(data1)
print(data2)
