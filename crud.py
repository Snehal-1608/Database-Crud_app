import pymysql as p
def getConnection():
    return p.connect(host='localhost',user='root',password='',database='snehalkore')
    
def insertstud(t):
    db=getConnection()
    sql='insert into student values(%s,%s,%s,%s,%s)'
    cr=db.cursor()
    cr.execute(sql,t)
    db.commit()
    db.close()
    print("Data inserted successfully......")

def updatestud(t):
    db=getConnection()
    sql='update student set Name=%s,Contact=%s,Email=%s,Address=%s where Id=%s'
    cr=db.cursor()
    cr.execute(sql,t)
    db.commit()
    db.close()
    print("Data updated successfully.......")


def deletestud(id):
    db=getConnection()
    sql='delete from  student where Id=%s'
    cr=db.cursor()
    cr.execute(sql,id)
    db.commit()
    db.close()
    print("Data deleted successfully.......")

def selectallstud():
    db=getConnection()
    sql='select * from student'
    cr=db.cursor()
    cr.execute(sql)
    elist=cr.fetchall()
    i,n,q,l,p="ID","Name","Contact","Email","Address"
    print(f"{i:5} {n:10} {q:15} {l:20} {p:20}")
    for a,b,c,d,e in elist:
        print(f"{a:5} {b:10} {c:15} {d:20} {e:20}")
    db.commit()
    db.close()
    


while True:
    print("Database".center(60))
    print("1.Inserted data to Database\n2.Update data from database\n3.Delete data from database\n4.All your data from database")
    a=input("Enter Your Selection: ")
    if(a=="1"):
        ids=int(input("Enter Your Id: "))
        name=input("Enter Your Name: ")
        contact=int(input("Enter Your Contact No.: "))
        email=input("Enter Your Email Id: ")
        address=input("Enter Your address: ")
        data=[ids,name,contact,email,address]
        insertstud(data)

    elif(a=="2"):
        ids=int(input("Enter Id which you want to be change: "))
        name=input("Enter Your Name: ")
        contact=int(input("Enter Your Contact No.: "))
        email=input("Enter Your Email Id: ")
        address=input("Enter Your address: ")
        data=[name,contact,email,address,ids]
        updatestud(data)

    elif(a=="3"):
        ids=int(input("Enter Id which you want to delete: "))
        data=(ids)
        deletestud(ids)
        
    elif(a=="4"):
        selectallstud()

    else:
        print("Invalid selection")
        break

    

        
                
        
