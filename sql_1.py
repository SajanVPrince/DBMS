# sudo apt update && sudo apt upgrade -Y

# install xampp

# download xampp for linux version

# in cmd use command cd Downloads

# us ls to list the directories in that File

# to set a permission(chmod +x ---filename---)('enter first letter and use tab for full file name')

# pip install mysql-connector-python

import mysql.connector
con=mysql.connector.connect(user='SajanVPrince',host='localhost',password='Sajan@2002',database='demo')
con.autocommit=True
cur=con.cursor()
# cur.execute("create database demo")
try:
    cur.execute("create table std (roll_no int,name text,age int)")
except:
    pass

# cur.execute("insert into std (roll_no,name,age)values(1,'akhil',22),(2,'appu',22),(3,'ammu',22),(4,'aro',22),(5,'achu',22)")
roll=int(input('enter your roll number : '))
name=input('enter your name : ')
age=int(input('enter your age : '))

cur.execute("insert into std (roll_no,name,age)values(%s,%s,%s)",(roll,name,age))