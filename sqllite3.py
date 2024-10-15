import sqlite3
con=sqlite3.connect('DBMS/students.db')

# create table
# ------------

'''try:
    con.execute('create table std(roll_no int,name text,age int)')
except:
    pass
con.execute("insert into std(roll_no,name,age)values(1,'akhil',22),(2,'appu',22),(3,'ammu',22),(4,'aro',22),(5,'achu',22)")'''
 
# Add data to sqlite3
# -------------------

'''roll=int(input('enter your roll number : '))
name=input('enter your name : ')
age=int(input('enter your age : '))

con.execute("insert into std(roll_no,name,age)values(?,?,?)",(roll,name,age))
con.commit()'''

# Pg1 (input data with a limit)
# -----------------------------

'''try:
    con.execute('create table std(roll_no int,name text,age int)')
except:
    pass

limit=int(input('enter the limit : '))

for i in range(limit):
    roll=int(input('enter your roll number : '))
    name=input('enter your name : ')
    age=int(input('enter your age : '))
    con.execute("insert into std(roll_no,name,age)values(?,?,?)",(roll,name,age))
    con.commit()'''

# Import from sqlite3
# -------------------

'''data=con.execute("select * from std")
# print(data)
for i in data:
    print(i)'''

# Search specific data in sqlite3
# -------------------------------

'''data=con.execute("select * from std where name='jith' ")
for i in data:
    print(i)'''

# Search  by a user input
# -----------------------

'''roll=int(input('enter the roll number : '))
data=con.execute("select * from std where roll_no=? ",(roll,))
for i in data:
    print(i)'''

# update command
# --------------

'''data=con.execute("update std set name='akku',age=20 where roll_no=3")
con.commit()'''

# Change name of a user
# ---------------------

'''name=input('enter your new name : ')
roll=int(input('ente your roll number : '))
con.execute("update std set name=? where roll_no=?",(name,roll))
con.commit()'''

# Delete Query
# ------------

'''con.execute("delete from std where roll_no=5")
con.commit()'''

# delete item using an user input
# -------------------------------

'''roll=int(input('enter your name : '))
con.execute('delete from std where roll_no=?',(roll,))
con.commit()'''

# like
# ----

'''data=con.execute("select * from std where name like '%n' ")  #('_' first letter anything, '%' one or more occurence)
for i in data:
    print(i)'''

# Order by (Ascending or decending)
# ---------------------------------

'''data=con.execute("select * from std order by name desc") #(desc is a attribute to set to descending order by default it works as ascending order)
for i in data:
    print(i)'''

# join 2 db
# ---------


'''l=int(input('Enter no of students : '))
for i in range(l):
    roll_no=i+1
    name=input('Enter name : ')
    age=int(input('Enter age : '))
    con.execute("insert into std(roll_no,name,age)values(?,?,?)",(roll_no,name,age))
    con.commit()
con.execute("insert into mark(roll_no,sub,mark)values(1,'cs',70),(1,'chem',49),(2,'phy',58),(4,'eng',45)")
con.commit()
data=con.execute("select std.roll_no,std.name,std.age,mark.sub,mark.mark from std cross join mark")
for i in data:
    print(i)
data=con.execute("select name,count(age) from std group by name")
for i in data:
    print(i)'''