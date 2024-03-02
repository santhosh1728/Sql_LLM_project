import sqlite3

# Connect to SQLite
connection = sqlite3.connect("student.db")

# Create a cursor object to insert records, create table, retrieve
cursor = connection.cursor()

# Create the table
table_info = """
CREATE TABLE STUDENT (
    NAME VARCHAR(25),
    CLASS VARCHAR(25),
    SECTION VARCHAR(25),
    MARKS INT
);
"""
cursor.execute(table_info)

# Insert some records
cursor.execute('''INSERT INTO STUDENT VALUES('Santhosh', 'IOT', 'A', 90)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Dhanavath', 'HCI', 'A', 50)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Mahesh', 'CSE', 'A', 90)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Ram', 'DS', 'A', 60)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Teja', 'AIML', 'A', 70)''')

# Display all the records
print('The inserted records are:')
data = cursor.execute('''SELECT * FROM STUDENT''')
for row in data:
    print(row)

# Commit changes and close the connection
connection.commit()
connection.close()
