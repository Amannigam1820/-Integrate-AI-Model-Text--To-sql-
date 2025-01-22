import sqlite3

connection = sqlite3.connect("student.db")

cursor = connection.cursor()

create_table_query="""
CREATE TABLE IF NOT EXISTS STUDENT (
    ID INT,
    NAME    VARCHAR(25),
    COURSE   VARCHAR(25),
    SECTION VARCHAR(25),
    MARKS   INT
);
"""

cursor.execute(create_table_query)

sql_query = """INSERT INTO STUDENT (ID, NAME, COURSE, SECTION, MARKS) VALUES (?,?, ?, ?, ?)"""
values = [
    (1,'Student1', 'Data Science', 'A', 90),
    (2,'Student2', 'Data Science', 'B', 100),
    (3,'Student3', 'Data Science', 'A', 86),
    (4,'Student4', 'DEVOPS', 'A', 50),
    (5,'Student5', 'DEVOPS', 'A', 35),
    (6,'Student6', 'Python', 'A', 90),
    (7,'Student7', 'Python', 'B', 100),
    (8,'Student8', 'AI', 'A', 86),
    (9,'Student9', 'AI', 'A', 50),
    (10,'Student10', 'MERN', 'A', 35)
]

cursor.executemany(sql_query,values)
connection.commit()

data = cursor.execute("""Select * from STUDENT""")

for row in data:
    print(row)

if connection:
    connection.close()