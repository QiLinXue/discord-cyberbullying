from server.objects.user import User
class seidelions(User):
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
    reportStats: int
        The number of times the seidelon reported a message

    Methods
    -------
    display() -> str
        Outputs the user's name and role
    insert() -> None
        inserts the user info into its respective user database
    updateSwears() -> None
        updates the user database on number of swears by user
    report(messageId: str) -> void
        reports the message to administrators
    '''
    def __init__(self,identification,name,userDB,swearCount,reportStats):
        super().__init__(identification,name,userDB,swearCount)
        self.reportStats = reportStats

    def display(self):
        '''
        Returns the name of the user
        
        Returns
        ----------
        description: str
            The user's name + rle 
        '''
        description = "Name: %s Role: 'Seidelion'" % self.name 
        return description

    def report(self,messageID):
        '''
        Reports the message to the specific channel

        Parameters
        ----------
        messageID: str
            the id of the message that is reported
        
        Returns
        -------
        message: str
            the message to be sent
        '''
        message = "There has been an instance of cyberbullying. Message id is %s" % messageID
        self.reportStats += 1
        return message
