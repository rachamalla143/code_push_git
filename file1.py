import mysql.connector as con
mydb =con.connect(host="localhost", user="root", passwd="Gowri@143ds.")
cursor = mydb.cursor()
#query = "create table nagaraju.empyee(emp_id varchar(6),emp_name char(20),emp_mail varchar(30),emp_phone int(10))"
#query = "select *from nagaraju.empyee"
#query1 = "insert into nagaraju.empyee values('nr9988','rachamalla Gowri','rachamalla.gowri@gmail.com',12345)"
#cursor.execute(query1)
#mydb.commit()
query2 = "select emp_id,emp_name from nagaraju.empyee"
cursor.execute(query2)
l1 = []
for i in cursor.fetchall():
    l1.append(i)
    print(l1)
