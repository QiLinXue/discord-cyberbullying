class User:
    def __init__(self,identification,name,userDB,swearCount):
        self.id  = identification
        self.name = name
        self.userDB = userDB
        self.swearCount = swearCount

    def display(self):
        return self.name

    def insert(self):
        self.userDB.insert(self)

    def updateSwears(self):
        self.userDB.updateSwears(self)
        self.swearCount = self.swearCount + 1
        return