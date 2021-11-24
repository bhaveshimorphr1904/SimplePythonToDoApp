import pyodbc

# Define Connection String

sqlDbConn = pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=DESKTOP-BQC6PN7\SQLEXPRESS;"
    "Database=SampleProduct;"
    "Trusted_Connection=yes;")

def getData(sqlDbConn):
    print("Read")
    cursor = sqlDbConn.cursor()
    cursor.execute("select * from  ProductMaster")
    for row in cursor:
        print(f"{row}")

def insertData(sqlDbConn):
    print("Insert")
    cursor = sqlDbConn.cursor()
    cursor.execute(f"insert into ProductMaster (Product,Cost) values('Laser Mouse', 500.00)")
    sqlDbConn.commit()

def updateData(sqlDbConn):
    print("Update")
    cursor = sqlDbConn.cursor()
    cursor.execute(f"update ProductMaster set Cost = 75000.00 where Id = 1")
    sqlDbConn.commit()
    
def deleteData(sqlDbConn):
    print("Delete")
    cursor = sqlDbConn.cursor()
    cursor.execute(f"delete from ProductMaster where Id = 3")
    sqlDbConn.commit()

# insertData(sqlDbConn)
# updateData(sqlDbConn)
deleteData(sqlDbConn)
getData(sqlDbConn)