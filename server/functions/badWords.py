import mysql.connector

class BadWordsDB():
    '''
    A bad words object that hold the database information, allowing it to access the bad words

    Attributes
    ----------
    host: string
        The host name of the server (could be local or external)
    user: string
        The user connecting to the server
    password: string
        The password to authenticate access to server
    database: string
        The database name user wants to connect to
    mydb: mysql.connector.connection_cext.CMySQLConnection
        The generated connection for the server
    cursor: mysql.connector.cursor_cext.CMySQLCursor
        The generated cursor for the server

    Methods
    -------
    connect() -> None
        Intializes mydb and cursor
    close() -> None
        Disconencts mydb and cursor
    escapeString(sqlString: string) -> str
        Escapes apostrophe to prevent sql injections
    fetch() -> str[]
        Fetches bad words and combines them into a list
    printAll() -> str
        combines bad word list into string
    insert(targetWord: str, badWordArray: str[]) -> None
        Inserts a new bad word into the database
    delete(targetWord: str) -> None
        Deletes the given bad word from the database
    
    ----------
    '''

    # Import database username and password
    from serverSetup import DBUSER,DBPASS

    def __init__(self,host,user,password,database):
        '''
		Constructor to build the bad words object

		Parameters
		----------
        host: string
            The host name of the server (could be local or external)
        user: string
            The user connecting to the server
        password: string
            The password to authenticate access to server
        database: string
            The database name user wants to connect to
		'''

        self.host= host
        self.user = user
        self.password = password
        self.database = database

    def connect(self):
        '''
        Intializes mydb and cursor

        Returns
        ------
        None
        '''
        self.mydb = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.mydb.cursor()

        return

    def close(self):
        '''
        Disconencts mydb and cursor

        Returns
        ------
        None
        '''
        self.cursor.close()
        self.mydb.close()

        return

    def escapeString(self,sqlString):
        '''
        Escapes apostrophe to prevent sql injections

        Parameters
        ----------
        sqlString: str
            The injection string that may include apostrophes

        Returns
        ------
        sqlString: str
            The cleaned up version without the aopstrophes
        '''
        sqlString.replace('\'','')
        return sqlString

    def fetch(self):
        '''
        Fetches bad words and combines them into a list

        Returns
        ------
        badWordArray: str[]
            A list of the bad words pulled from database
        '''
        self.connect()

        sqlFormula = "SELECT * FROM badwords"
        self.cursor.execute(sqlFormula)
        myresults = self.cursor.fetchall()

        # Format everything
        badWordArray = []
        for row in myresults:
            badWordArray.append(row[0])

        self.close()

        return badWordArray
    
    def printAll(self):
        '''
        Combines bad word list into string

        Returns
        ------
        str
            A concatted list of bad words
        '''
        baddies = self.fetch()
        return ' '.join(baddies)

    def insert(self,targetWord,badWordArray):
        '''
        Inserts a new bad word into the database

        Parameters
        ----------
        targetWord: str
            The bad word to be inserted
        badWordArray: str[]
            A list which checks if the bad word is inserted already

        Returns
        ------
        None
        '''
        if not targetWord.lower() in badWordArray:
            self.connect()

            sqlFormula = "INSERT INTO badwords (word, badness) VALUE (%s,%s)"
            word = (self.escapeString(targetWord.lower()),1)
            self.cursor.execute(sqlFormula,word)
            self.mydb.commit()
            self.close()

        return

    def delete(self,targetWord):
        '''
        Deletes the given bad word from the database

        Parameters
        ----------
        targetWord: str
            The bad word to be deleted from database

        Returns
        ------
        None
        '''
        self.connect()

        sqlFormula = "DELETE FROM badwords WHERE word='%s'" % targetWord
        sqlFormula = self.escapeString(sqlFormula)

        self.cursor.execute(sqlFormula)
        self.mydb.commit()

        self.close()

        return
