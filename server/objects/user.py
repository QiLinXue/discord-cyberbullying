class User:
    '''
    A User object that holdS information about a specific user in a specific server

    Attributes
    ----------
    id: string
        The discord id of the user
    name: string
        The user's discord username for specific server
    userDB: userDB object
        The database in which the user is connected to
    swearCount: int
        The number of times the user swore

    Methods
    -------
    display() -> str
        Outputs the user's name
    insert() -> None
        inserts the user info into its respective user database
    updateSwears() -> None
        updates the user database on number of swears by user    
    '''
    def __init__(self,identification,name,userDB,swearCount):
        '''
		Constructor to build the bad words object

        Parameters
        ----------
        id: string
            The discord id of the user
        name: string
            The user's discord username for specific server
        userDB: userDB object
            The database in which the user is connected to
        swearCount: int
            The number of times the user swore
		'''
        self.id  = identification
        self.name = name
        self.userDB = userDB
        self.swearCount = swearCount
        print(type(self.id),type(self.name),type(self.userDB),type(swearCount))

    def display(self):
        '''
        Returns the name of the user
        
        Returns
        ----------
        self.name: str
            The user's name 
        '''
        return self.name

    def insert(self):
        '''
        Inserts the user information into its respective database

        Returns
        -------
        None
        ''''
        self.userDB.insert(self)

    def updateSwears(self):
        '''
        Increments the number of swears made by the user to its
        respective database

        Returns
        -------
        None
        '''
        self.userDB.updateSwears(self)
        self.swearCount = self.swearCount + 1
