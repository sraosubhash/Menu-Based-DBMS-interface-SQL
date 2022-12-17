import mysql.connector
import matplotlib.pyplot as plt
import numpy as nm
mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234",database="mock")
mycursor=mydb.cursor()
def menu():
    c='y'
    while(c=='y'):
        print("\t\t1. add record")
        print("\t\t2. display records")
        print("\t\t3. update record")
        print("\t\t4. delete data")
        print("\t\t5. Search data")
        print("\t\t6. Bar graph of marks")
        print("\t\t7. Exit")
        choice=int(input("enter your choice:"))
        if choice==1:
            adddata()
        elif choice==2:
            fetchdata()
        elif choice==3:
            updatedata() 
        elif choice==4:
            deldata()
        elif choice==5:
            search()
        elif choice==6:
            graph()
        elif choice==7:
            print("exiting")
            break
        else:
            print("INVALID INPUT ")
            c=input("want to continue?")
    
def adddata():
    rno=int(input("Enter Rollno"))
    s="Select rollno from smug"
    p=[]
    l=[]
    mycursor.execute(s)
    m=mycursor.fetchall()
    for x in m:
        p.append(x)
    for i in range (len(p)):
        if p[i]==(rno,):
            l.append(p[i])
            print("Roll Number Exists")
            break
    if l==[]:
        nm=input("enter name : ")
        age=int(input("enter age : "))
        city=input("enter city : ")
        mrk=int(input("enter marks : "))
        sql="insert into smug (rollno,name,age,city,marks) values(%s,%s,%s,%s,%s)"
        val=(rno,nm,age,city,mrk)
        mycursor.execute(sql,val)
        print("\nRECORD INSERTED\n")
    mydb.commit()
    
def fetchdata():
    mycursor.execute("select*from smug")
    myresult=mycursor.fetchall()
    for x in myresult:
        print(x)
def updatedata():
    print("\t1. update name : ")
    print("\t2. update age : ")
    print("\t3. update city : ")
    print("\t4. update marks : ")
    c=int(input("enter your choice : "))

    if c==1:
        upnm()
    elif c==2:
        upage()
    elif c==3:
        upcity() 
    elif c==4:
        upmar()
       
def deldata():
    n=int(input("Enter roll number to be deleted"))
    l=[]
    s="select rollno from smug"
    p=[]
    mycursor.execute(s)
    m=mycursor.fetchall()
    for x in m:
         l.append(x)
    z=len(l)
    for i in range (z):
        if l[i]==(n,):
            p.append(l[i])
            sql = "delete from smug where rollno=%s"
            rn=(n,)
            mycursor.execute(sql,rn)
            print("Record Deleted")
    if p==[]:
        print("Roll number not found")
    mydb.commit()

def search():
    print("\t1. search throgh roll number")
    print("\t2. search throgh name")
    print("\t3. search throgh city")
    print("\t4. search throgh age")
    print("\t5. search through marks") 
    choice=int(input("enter your choice:"))
    if choice==1:
        searchroll()
    elif choice==2:
        searchname()
    elif choice==3:
        searchcity() 
    elif choice==4:
        searchage()
    elif choice==5:
        searchmar()

def searchroll():
    n=int(input("Enter roll number whose data to be searched :"))
    sql = "select * from smug where rollno=%s"
    rn=(n,)
    l=[]
    mycursor.execute(sql,rn)
    myresult=mycursor.fetchall()
    for x in myresult:
        print(x)
        l.append(x)
    if l==[]:
        print("RECORD NOT FOUND")
    mydb.commit()

def searchname():
    n=str(input("Enter name whose data to be searched :"))
    sql = "select * from smug where name=%s"
    rn=(n,)
    l=[]
    mycursor.execute(sql,rn)
    myresult=mycursor.fetchall()
    for x in myresult:
        print(x)
        l.append(x)
    if l==[]:
        print("RECORD NOT FOUND")
    mydb.commit()

def searchage():
    n=str(input("Enter age whose data to be searched :"))
    sql = "select * from smug where age=%s"
    rn=(n,)
    l=[]
    mycursor.execute(sql,rn)
    myresult=mycursor.fetchall()
    for x in myresult:
        print(x)
        l.append(x)
    if l==[]:
        print("RECORD NOT FOUND")
    mydb.commit()
    
def searchcity():
    n=str(input("Enter city whose data to be searched :"))
    sql = "select * from smug where city=%s"
    rn=(n,)
    l=[]
    mycursor.execute(sql,rn)
    myresult=mycursor.fetchall()
    for x in myresult:
        print(x)
        l.append(x)
    if l==[]:
        print("RECORD NOT FOUND")
    mydb.commit()

def searchmar():
    n=int(input("Enter marks whose data to be searched :"))
    sql = "select * from smug where marks=%s"
    rn=(n,)
    l=[]
    mycursor.execute(sql,rn)
    myresult=mycursor.fetchall()
    for x in myresult:
        print(x)
        l.append(x)
    if l==[]:
        print("RECORD NOT FOUND")
    mydb.commit()
    

def upnm():
    nm=int(input("Enter roll number to update Name"))
    s="select rollno from smug"
    l=[]
    p=[]
    mycursor.execute(s)
    m=mycursor.fetchall()
    for x in m:
         l.append(x)
    z=len(l)
    for i in range (z):
        if l[i]==(nm,):
            p.append(l[i])
            sql = "Update smug set name=%s where rollno=%s"
            m=str(input("Enter Name"))
            val=(m,nm)
            mycursor.execute(sql,val)
            print("")
            print("DATA SUCESSFULLY UPDATED")
    if p==[]:
        print("Roll number not found")
    mydb.commit()
    
def upage():
    nm=int(input("Enter roll number to update Age"))
    s="select rollno from smug"
    l=[]
    p=[]
    mycursor.execute(s)
    m=mycursor.fetchall()
    for x in m:
         l.append(x)
    z=len(l)
    print(l)
    for i in range (z):
        if l[i]==(nm,):
            p.append(l[i])
            sql = "Update smug set age=%s where rollno=%s"
            m=int(input("Enter Age"))
            val=(m,nm)
            mycursor.execute(sql,val)
            print("")
            print("DATA SUCESSFULLY UPDATED")
    if p==[]:
        print("Roll number not found")
    mydb.commit()
  
def upcity():
    nm=int(input("Enter roll number to update City"))
    s="select rollno from smug"
    l=[]
    p=[]
    mycursor.execute(s)
    m=mycursor.fetchall()
    for x in m:
         l.append(x)
    z=len(l)
    for i in range (z):
        if l[i]==(nm,):
            p.append(l[i])
            sql = "Update smug set city=%s where rollno=%s"
            m=str(input("Enter new City"))
            val=(m,nm)
            mycursor.execute(sql,val)
            print("")
            print("DATA SUCESSFULLY UPDATED")
    if p==[]:
        print("Roll number not found")
    mydb.commit()

    
def upmar():
    nm=int(input("Enter roll number to update Marks"))
    s="select rollno from smug"
    l=[]
    p=[]
    mycursor.execute(s)
    m=mycursor.fetchall()
    for x in m:
         l.append(x)
    z=len(l)
    for i in range (z):
        if l[i]==(nm,):
            p.append(l[i])
            sql = "Update smug set marks=%s where rollno=%s"
            m=int(input("Enter new Marks"))
            val=(m,nm)
            mycursor.execute(sql,val)
            print("")
            print("DATA SUCESSFULLY UPDATED")
    if p==[]:
        print("Roll number not found")
    mydb.commit()

def graph():
    a="select marks from smug"
    i=[]
    mycursor.execute(a)
    m=mycursor.fetchall()
    for x in m:
         i.append(x)
    z=[]
    for j in range (len(i)):
        for q in range (0,100):
            if i[j]==(q,):
                z.append(q)
    mydb.commit()
    w=[]
    for i in range (len(i)):
        w.append(i+1)
    f="select name from smug"
    t=[]
    mycursor.execute(f)
    m=mycursor.fetchall()
    for x in m:
         t.append(x)
    plt.title("Marks of students")
    plt.ylabel("Marks")
    plt.xlabel("Students (Roll no)")
    plt.bar(w,z,width=0.4,label=t)
    plt.legend()
    plt.show()
    mydb.commit()

menu()

