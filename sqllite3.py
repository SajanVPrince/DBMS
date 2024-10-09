import sqlite3
con=sqlite3.connect('DBMS/students.db')
# try:
#     con.execute('create table std(roll_no int,name text,age int)')
# except:
#     pass
# # con.execute("insert into std(roll_no,name,age)values(1,'akhil',22),(2,'appu',22),(3,'ammu',22),(4,'aro',22),(5,'achu',22)")
 
# roll=int(input('enter your roll number : '))
# name=input('enter your name : ')
# age=int(input('enter your age : '))

# con.execute("insert into std(roll_no,name,age)values(?,?,?)",(roll,name,age))
# con.commit()
try:
    con.execute('create table std(roll_no int,name text,age int)')
except:
    pass

limit=int(input('enter the limit : '))

for i in range(limit):
    roll=int(input('enter your roll number : '))
    name=input('enter your name : ')
    age=int(input('enter your age : '))
    con.execute("insert into std(roll_no,name,age)values(?,?,?)",(roll,name,age))
    con.commit()


