import Module as mo
import mysql.connector as con
path=con.connect(host="localhost", user="root",passwd="12345",database="user1")
cur=path.cursor()
#cur.execute("drop database user1")
#cur.execute("create database user1")
#mo.start()
def DML():
    print("What Option do you want to execute ?? ","\n")
    print("1. View Data","2. Delete all Data","\n")
    n=int(input('Enter the corrosponding number : '))
    if n==1:
        table_no=2
        cur.execute(f"select * from table{table_no}_info")
        for i in cur:
            print(i)
    elif n==2:
        table_no=Module.table_no()
        cur.execute(f"delete from table{table_no}_info")
        print("Query Executed !! ")
    else:
        print("Invalid Query")
DML()
