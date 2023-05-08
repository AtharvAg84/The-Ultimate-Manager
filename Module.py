#import Main_Program as Main
import Module
import mysql.connector as con
path=con.connect(host="localhost", user="root",passwd="12345",database="user1")
cur=path.cursor()
global status
global manager
def start():
    status=""
    if status == "":
        print("Hello User, Welcome to DBMS")
        Module.setup()
def Editor():
        print("\nHello User, Welcome to manager")
        print("!! Setup Already completed...","\t Procedding to Management...  !! ")
        Module.Manage()
        
def setup():
    status=""
    manager=input("Please Enter the Name of the Management : ")
    tno=int(input("\n\nPlease Enter the Number of Tables : "))  
    cur.execute("create table Table_info(Table_Name varchar(30),Table_id varchar(30))")
    for i in range(1,tno+1):
        name=input(f"Input the name of table{i} : ")
        cur.execute(f"insert into table_info values('{name}','table{i}')")
        cur.execute(f"create table table{i}_info(Sno int,column_name varchar(30),column_id varchar(30),datatype varchar(30))")
        cno= int(input("\nHow many columns you want : "))
        for j in range(1,cno + 1):
            c_name=input(f"\nEnter the name of Column{j} : ")
            m=Module.datatype_ask()
            #rec=j,c_name,f"cname{j}",m
            z=f"cname{j}"
            cur.execute(f"insert into table{i}_info values({j},'{c_name}','{z}','{m}')")
            #cur.commit()
    print("\nSetup Completed !! Congo !!")
    status="completed"
    Module.Editor()

def datatype_ask():
    print("What Type of Data will it Hold:-")
    print("1. Character (Recomended for Alpha Numerical Values)","2. Integer")
    print("3. Fractional (Decimal)","4. Date          5. Time")
    n=int(input('Enter the corrosponding number : '))
    dtype=""
    if n==1:
        dtype='varchar(100)'
    elif n==2:
        dtype='int'
    elif n==3:
        dtype='float'
    elif n==4:
        dtype='date'
    elif n==5:
        dtype='time'
    else:
        print("Invalid Query")
    return dtype
            
def Manage():
    print("\n Choose the type of funtioning : ")
    print("1. DDL Options 2.DML options")
    query = int(input("Enter the corrosponding number : "))
    if query==1:
        Module.DDL()
    elif query==2:
        Module.DML()
    else:
        print("Invalid Query")

def table_no():
    cur.execute("select Table_Name from Table_info")
    num=0
    for i in cur:
        num+=1
        for j in i:
            print(j,end="\t")
        print(num)
    table_no=int(input("Please Enter the Corresponding No. to access a table : "))
    return table_no

def DDL():
    print("\n What Option do you want to execute ?? ")
    print("1. Change Table Name","2. Drop table")
    print("3. Reset Software","\n")
    n=int(input('Enter the corrosponding number : '))
    if n==1:
        table_no=Module.table_no()
        new_name=input("Enter the New Name of table : ")
        cur.execute(f"update table_info set Table_Name='{new_name}' where Table_id='table{table_no}'")
        print("Table Name changed Successfully !! ")
        #option=cur.execute(f"select * from table{numb}")
    elif n==2:
        table_no=Module.table_no()
        cur.execute("drop table table{table_no}_info")
        cur.execute("delete from table_info where table_id=table{table_no}")
    elif n==3:
        cur.execute("drop database user1")
        cur.execute("create database user1")
        print("Software Reset !! \t Please run the Setup Again !!")
    else:
        print("Invalid Query")

def DML():
    print("What Option do you want to execute ?? ","\n")
    print("1. View Data","2. Delete all Data","\n")
    n=int(input('Enter the corrosponding number : '))
    if n==1:
        table_no=2
        option=cur.execute(f"select * from table{table_no}_info")
        print(option)
    elif n==2:
        table_no=Module.table_no()
        cur.execute(f"delete from table{table_no}_info")
        print("Query Executed !! ")
    else:
        print("Invalid Query")

