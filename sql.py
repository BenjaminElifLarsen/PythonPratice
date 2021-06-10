import mysql.connector as mySQL

database = mySQL.connect(
    host="localhost",
    user="Me",
    password="Test123."
)

print(database)


cursor = database.cursor()
cursor.execute("SHOW DATABASES")
#print(cursor)

data = cursor.fetchall()
print(data)
databases = []
for x in data:
    print(x[0]) 
    databases.append(x[0])
print(databases)

if "pythonpratice" not in databases:
    print("Was not found and thus created")
    cursor.execute("CREATE DATABASE PythonPratice")

cursor.close()

database = mySQL.connect(
    host="localhost",
    user="Me",
    password="Test123.",
    database="pythonpratice",
)

print(database)
cursor = database.cursor()
cursor.execute("SHOW TABLES")
tableData = cursor.fetchall()
tables = []
for x in tableData:
    print(x[0]) 
    tables.append(x[0])
print(tables)
if "user" not in tables:
    print("Was not found and thus created")
    cursor.execute("CREATE TABLE User (Id INT AUTO_INCREMENT PRIMARY KEY, Name VARCHAR(50), Age Int)")

cursor.execute("INSERT INTO User (Name, Age) VALUES (%s, %s)", ("Bob",32)) #%s excapes query values 
database.commit()
print(cursor.rowcount, "record(s) inserted.")

cursor.execute("SELECT * FROM User")
results = cursor.fetchall()
for x in results:
    print(x)



