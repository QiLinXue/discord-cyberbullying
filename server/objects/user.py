class User:
    def __init__(self,identification,name,userDB):
        self.id  = identification
        self.name = name
        self.userDB = userDB

    def display(self):
        return self.name

    def insert(self):
        self.userDB.insert(self)
