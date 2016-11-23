import sqlite3
import os


# class to handle all database functions for the shooting app
class ShootDB:

    def __init__(self, db_path):
        print(ShootDB.__init__)
        # store database path in class variable
        self._db_path = db_path
        self._db_path_abs = os.path.abspath(db_path)
        # print(self._db_path_abs)

        # initialise table fields list
        # self.table_fields = []

        # create/open sql db
        if self._db_path_abs != '':
            self.db = self.init_db()
            self.cursor = self.init_cursor()

        self.init_table()

    def __del__(self):
        print(ShootDB.__del__)
        self.db.close()

    def init_db(self):
        db = sqlite3.connect(self._db_path_abs)
        return db

    def init_cursor(self):
        cursor = self.db.cursor()
        return cursor

    def init_table(self):
        print(ShootDB.init_table)

        # adds table to self.db
        shooter_sql_command = """
                    CREATE TABLE IF NOT EXISTS shoot_data (
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

        # executes the add table command
        self.cursor.execute(shooter_sql_command)

    # This method currently only uses fetchone. It needs to be configured to get a certain record based on a specified
    # index or keyword
    def get_record(self, record_index):
        # c.execute('SELECT * FROM {tn} WHERE {cn}="Hi World"'. \
        #           format(tn=table_name, cn=column_2))
        print(ShootDB.get_record)
        record_index_str = str(record_index)
        fetch_command = "SELECT * FROM shoot_data WHERE shoot_number = ?"
        self.cursor = self.db.execute(fetch_command, record_index_str)
        res = self.cursor.fetchall()
        return res

    def add_record(self, shoot_data_list):
        print(ShootDB.add_record)
        # print(shoot_data_list)
        # data must be formatted as list in order: date, fname, lname, target_breakdown,
        # total_score, fire_type, range_dist, weapon_type, stance, support
        for count in shoot_data_list:
            format_str = """INSERT INTO shoot_data (shoot_number, date, fname, lname, target_breakdown, total_score, fire_type,
                          range_dist, weapon_type, stance, support)
            VALUES (NULL, "{date}", "{first}", "{last}", "{breakdown}", "{score}", "{ammo_type}", "{range}", "{weapon}",
                          "{stance}", "{support}");"""

            add_command = format_str.format(date=count[0], first=count[1], last=count[2], breakdown=count[3], score=count[4],
                                            ammo_type=count[5], range=count[6], weapon=count[7], stance=count[8], support=[9])
            self.cursor.execute(add_command)

# TEST CODE

# create an instance of ShootDB for testing
shoot = ShootDB('db_src/shoot_db.db')
shoot_data = [("2016-11-21", "Willem", "van Hoof", "10,10,9,10,8,8,10,9,8,10", 92, "Live", "25", "Russian Scoped",
               "Sitting", "Supported")]
shoot.add_record(shoot_data)
record = shoot.get_record(0)
print('record:\n' + str(record))
