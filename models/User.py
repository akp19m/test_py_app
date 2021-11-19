from models.Person import Person
from models.enums.Levels import Level
import datetime 

class User(Person):
    def __init__(self, firstName, lastName, age, email, usn, pwd):
        super().__init__(firstName, lastName, age)
        self.email = email
        self.usn = usn
        self.pwd = pwd
        self.level = Level.BRONZE
   
    def __repr__(self):
        return f"{{Email: {self.email}, Usn: {self.usn}, Livello: {self.level.name}}}"

    def calcAge(self):
        return (datetime.datetime.now().year)-self.age
