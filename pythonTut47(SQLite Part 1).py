import sqlite3
import sys

def printDB():
    try:
        result = theCursor.execute("SELECT ID, FName, LName, Age, Address, Salary,              HireDate FROM Employees")
        for row in result:
           print("ID: ", row[0])
           print("FName: ", row[1])
           print("LName: ", row[2])
           print("Age: ", row[3])
           print("Address: ", row[4])
           print("Salary: ", row[5])
           print("HireDate: ", row[6])
    except sqlite3.OperationalError:
        print("The table doesn't exist")
    except:
        print("Couldn't retrieve data from employees")



db_conn = sqlite3.connect('test.db')

print("Created the database")

theCursor = db_conn.cursor()

try:
    db_conn.execute("CREATE TABLE Employees(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT        NULL, FName TEXT NOT NULL, LName TEXT NOT NULL, Age INTEGER, Address TEXT, Salary REAL, HireDate TEXT);")
except sqlite3.OperationalError:
    print("Table couldn't be created")

db_conn.commit()
print("Table Created")
db_conn.execute("INSERT INTO Employees (FName, LName, Age, Address, Salary, HireDate) VALUES ('Michael', 'Dee', 24, '123 Main St', 200000, date('now'))")
db_conn.commit()

printDB()

# Grab names of all the rows in the database
theCursor.execute("PRAGMA TABLE_INFO(Employees)")
rowNames = [nameTuple[1] for nameTuple in theCursor.fetchall()]
print(rowNames)

# Grab number of rows in the db
theCursor.execute("SELECT COUNT(*) FROM Employees")
numOfRows = theCursor.fetchall()
print("The number of rows: ", numOfRows[0][0])

# Print out just first and last names
with db_conn:
    db_conn.row_factory = sqlite3.Row
    theCursor = db_conn.cursor()
    theCursor.execute("SELECT * FROM Employees")
    rows = theCursor.fetchall()

    for row in rows:
        print("{} {}".format(row["FName"], row["LName"]))
db_conn.close()
print("Database closed")
