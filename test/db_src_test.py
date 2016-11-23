import sqlite3
import os

abs_path = os.path.abspath('db_src/shoot_test.db')
print(abs_path)
connection = sqlite3.connect(abs_path)

shooter_sql_command = """
            CREATE TABLE shoot_data (
            shoot_number INTEGER PRIMARY KEY,
            date DATE,
            fname VARCHAR(20),
            lname VARCHAR(30),
            target_breakdown VARCHAR(40),
            total_score INT,
            fire_type VARCHAR(10),
            range_dist INT,
            weapon_type VARCHAR(30),
            stance VARCHAR(10),
            support VARCHAR(10)
            );"""

cursor = connection.cursor()
# cursor.execute(shooter_sql_command)

shooter_data = [("2016-11-21", "Willem", "van Hoof", "10,10,9,10,8,8,10,9,8,10", 92, "Live", "25", "Russian Scoped",
                 "Sitting", "Supported"),
                ("2016-11-21", "James", "Leach", "9,10,10,10,8,10,8,9,8,8", 90, "Live", "25", "Bullpup",
                 "Standing", "Unsupported")]

for p in shooter_data:
    format_str = """INSERT INTO shoot_data (shoot_number, date, fname, lname, target_breakdown, total_score, fire_type,
                  range_dist, weapon_type, stance, support)
    VALUES (NULL, "{date}", "{first}", "{last}", "{breakdown}", "{score}", "{fire_type}", "{range}", "{weapon}",
                  "{stance}", "{support}");"""

    sql_command = format_str.format(date=p[0], first=p[1], last=p[2], breakdown=p[3], score=p[4], fire_type=p[5],
                                    range=p[6], weapon=p[7], stance=p[8], support=[9])
    cursor.execute(sql_command)

cursor.execute("SELECT * FROM shoot_data")
print("fetchall:")
result = cursor.fetchall()
for r in result:
    print(r)
cursor.execute("SELECT * FROM shoot_data")
print("\nfetch one:")
res = cursor.fetchone()
print(res)
print(res[5], unicode(res[1]))

print(unicode(res[1]))

