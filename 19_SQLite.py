# Here I'll show you how to work with SQLite databases
# in Python

# A database makes it easy for you to organize your
# data for storage and fast searching

# I show how to install SQLite and use it in this
# tutorial https://youtu.be/QjICgmk31js

# You need the SQLite module to use it
import sqlite3
import sys
import csv


# ---------- FUNCTIONS ----------

def printDB():
    # To retrieve data from a table use SELECT followed
    # by the items to retrieve and the table to
    # retrieve from

    try:
        result = theCursor.execute("SELECT id, FName, LName, Age, Address, Salary, HireDate FROM Employees")

        # You receive a list of lists that hold the result
        for row in result:
            print("ID :", row[0])
            print("FName :", row[1])
            print("LName :", row[2])
            print("Age :", row[3])
            print("Address :", row[4])
            print("Salary :", row[5])
            print("HireDate :", row[6])

    except sqlite3.OperationalError:
        print("The Table Doesn't Exist")

    except:
        print("Couldn't Retrieve Data From Database")


# ---------- END OF FUNCTIONS ----------

# connect() will open an SQLite database, or if it
# doesn't exist it will create it
# The file appears in the same directory as this
# Python file
db_conn = sqlite3.connect('test.db')

print("Database Created")

# A cursor is used to traverse the records of a result
theCursor = db_conn.cursor()

# execute() executes a SQL command
# We organize our data in tables by defining their
# name and the data type for the data

# We define the table name
# A primary key is a unique value that differentiates
# each row of data in our table
# The primary key will auto increment each time we
# add a new Employee
# If a piece of data is marked as NOT NULL, that means
# it must have a value to be valid

# NULL is NULL and stands in for no value
# INTEGER is an integer
# TEXT is a string of variable length
# REAL is a float
# BLOB is used to store binary data

# You can delete a table if it exists like this
# db_conn.execute("DROP TABLE IF EXISTS Employees")
# db_conn.commit()

try:
    db_conn.execute("CREATE TABLE Employees(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, FName TEXT NOT NULL, LName TEXT NOT NULL, Age INT NOT NULL, Address TEXT, Salary REAL, HireDate TEXT);")

    db_conn.commit()

    print("Table Created")

except sqlite3.OperationalError:
    print("Table couldn't be Created")

# To insert data into a table we use INSERT INTO
# followed by the table name and the item name
# and the data to assign to those items

db_conn.execute("INSERT INTO Employees (FName, LName, Age, Address, Salary, HireDate)"
                "VALUES ('Derek', 'Banas', 41, '123 Main St', '500,000', date('now'))")

db_conn.commit()

print("Employee Entered")

# Print out all the data in the database
printDB()

# You can update a value in a table by referencing
# something unique like the ID or anything else
# with the UPDATE command

try:
    db_conn.execute("UPDATE Employees SET Address = '121 Main St' WHERE ID=2")
    db_conn.commit()

except sqlite3.OperationalError:
    print("Database couldn't be Updated")

printDB()

# Delete matching data from the database by
# referencing the table name and something unique

try:
    db_conn.execute("DELETE FROM Employees WHERE ID=2")
    db_conn.commit()

except sqlite3.OperationalError:
    print("Data couldn't be Deleted")

printDB()

# Undo the last commit()
db_conn.rollback()

printDB()

# You can add a new column to a table with ALTER

try:
    db_conn.execute("ALTER TABLE Employees ADD COLUMN 'Image' BLOB DEFAULT NULL")

    db_conn.commit()

except sqlite3.OperationalError:
    print("Table couldn't be Altered")

# Retrieve table column names
theCursor.execute("PRAGMA TABLE_INFO(Employees)")

# fetchall() returns all remaining rows of a query result
# as a list
rowNames = [nameTuple[1] for nameTuple in theCursor.fetchall()]
print(rowNames)

# Get the total number of rows
theCursor.execute('SELECT COUNT(*) FROM Employees')

numOfRows = theCursor.fetchall()

print("Total Rows :", numOfRows[0][0])

# Get SQLite version
theCursor.execute('SELECT SQLITE_VERSION()')

# fetchone() returns one result
print("SQLite Version :", theCursor.fetchone())

# Use the dictionary cursor to retrieve data in a dictionary
with db_conn:
    db_conn.row_factory = sqlite3.Row

    theCursor = db_conn.cursor()

    theCursor.execute("SELECT * FROM Employees")

    rows = theCursor.fetchall()

    for row in rows:
        print("{} {}".format(row["FName"], row["LName"]))

# Write data to File

with open('dump.sql', 'w') as f:
    # iterdump() returns an iterator to dump the database
    # in SQL format
    for line in db_conn.iterdump():
        f.write('%s\n' % line)

# Closes the database connection
db_conn.close()