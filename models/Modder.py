from models.User import User
from models.enums.Levels import Level
import datetime 

class Modder(User):
    def __init__(self, firstName, lastName, age, email, usn, pwd):
        super().__init__(firstName, lastName, age, email, usn, pwd)
        
        self.level = Level.SILVER

    def __repr__(self):
        return f"{{Email: {self.email}, Usn: {self.usn}, Livello: {self.level.name}}}"

    def calcAge(self):
        return (datetime.datetime.now().year)-self.age
