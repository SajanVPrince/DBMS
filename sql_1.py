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
'''roll=int(input('enter your roll number : '))
name=input('enter your name : ')
age=int(input('enter your age : '))

cur.execute("insert into std (roll_no,name,age)values(%s,%s,%s)",(roll,name,age))'''

# cur.execute("select * from std order by name desc")
'''cur.execute("select * from std where name like '_k%'")
data=cur.fetchall()
for i in data:
    print(i)'''
try:
    cur.execute("create table mark (roll_no int,sub text,mark int)")
except:
    pass
cur.execute("insert into mark(roll_no,sub,mark)values(1,'cs',70),(1,'chem',49),(2,'phy',58),(4,'eng',45)")
cur.execute("select std.roll_no,std.name,std.age,mark.sub,mark.mark from std cross join mark")
data=cur.fetchall()
for i in data:
    print(i)
cur.execute("select name,count(age) from std group by name")
data=cur.fetchall()
for i in data:
    print(i)