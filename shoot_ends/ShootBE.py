from db import ShootDB
from analysis import ShootAnalysis
import cPickle as pickle


class ShootBE:

    def __init__(self, db_path):
        # type: (object) -> object
        print(ShootBE.__init__)

        current_db = db_path

        if current_db == '':
            self.current_db_path = '/db_src/shoot_db.db'
        # create a class variable instance of the ShootDB class

        # add call to get user options from file (default db, working directory, etc)
        # self.get_usr_options

        self.menu_options = ['Add record(s)', 'Show all records', 'Parameter search', 'Exit']
        self.shootdb = ShootDB.ShootDB('/db_src/shoot_db.db')

        self.column_heading_list = self.get_column_headings_shootdb()
        # self.menu()

    # def close(self):
    #     print(self.close)
    #     self.__del__
    #
    # def __del__(self):
    #     print(ShootBE.__del__)

    # menu loop (used for command line version)
    # def menu(self):
    #
    #     print(ShootBE.menu_loop)
    #     menu_loop_stat = True
    #     for menu_count in range(len(self.menu_options)):
    #         print(menu_count, '. ', self.menu_options[menu_count])
    #
    #     # start menu loop
    #     while menu_loop_stat:
    #         usr_in = raw_input("Please select an option by typing in it's number and pressing enter")
    #
    #         if usr_in == 1:
    #             self.add_record_shootdb()
    #         elif usr_in == 2:
    #             self.get_record_shootdb()
    #         elif usr_in == 3:
    #             self.search_shootdb()
    #         elif usr_in == 4:
    #             break
    #         else:
    #             print('You have not entered a valid response.')
    #
    #         # for usr_in_count in range(len(self.menu_options)):
    #         #     if str(usr_in_count) == usr_in:
    #         #         if

    # saves db data to file for use later
    def dump_db(self):
        print(ShootBE.dump_db)
        pickle.dump(self.shootdb, open('dbdata.sdb'))

    def get_column_headings_shootdb(self):
        names = self.shootdb.get_headings()
        return names

    def get_all_records_shootdb(self):
        data_values = self.shootdb.get_all_records()
        return data_values

    # adding records to shootdb
    # records parameter is list of tuples
    def add_record_shootdb(self, records):
        print(ShootBE.add_record_shootdb)

        # for loop to add records to db
        for record_count in range(len(records)):
            print('Adding record:\n' + records[record_count])
            self.shootdb.add_record(records[record_count])

        print('SUCCESS: All records added successfully.')

    def get_record_shootdb(self):
        print(ShootBE.get_record_shootdb)

    def search_shootdb(self):
        print(ShootBE.search_shootdb)
