import sqlite3

connection = sqlite3.connect('company.db')

sql_command = """
CREATE TABLE employee (
staff_number INTEGER PRIMARY KEY,
fname VARCHAR(20),
lname VARCHAR(30),
gender CHAR(1),
joining DATE,
birth_date DATE);"""

cursor = connection.cursor()

staff_data = [("William", "Shakespeare", "m", "1961-10-25"),
              ("Frank", "Schiller", "m", "1955-08-17"),
              ("Jane", "Wall", "f", "1989-03-14")]

for p in staff_data:
    format_str = """INSERT INTO employee (staff_number, fname, lname, gender, birth_date)
    VALUES (NULL, "{first}", "{last}", "{gender}", "{birthdate}");"""

    sql_command = format_str.format(first=p[0], last=p[1], gender=p[2], birthdate=p[3])
    cursor.execute(sql_command)

cursor.execute("SELECT * FROM employee")
print("fetchall:")
result = cursor.fetchall()
for r in result:
    print(r)
cursor.execute("SELECT * FROM employee")
print("\nfetch one:")
res = cursor.fetchone()
print(res)

