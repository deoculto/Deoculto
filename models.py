from pony.orm import *

db = Database()

class User(db.Entity):
    username = Required(str)
    password = Required(str)
