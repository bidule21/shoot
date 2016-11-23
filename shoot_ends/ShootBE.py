from db import ShootDB
from analysis import 
import cPickle as pickle


class ShootBE:

    def __init__(self, db_path):
        print(ShootBE.__init__)

        if db_path == '':
            self.current_db_path = '/db_src/shoot_db.db'
        # create a class variable instance of the ShootDB class
        self.shootdb = ShootDB.ShootDB()

    # saves db data to file for use later
    def dump_db(self):
        print(ShootBE.dump_db)
        pickle.dump(self.shootdb, open('dbdata.sdb'))
