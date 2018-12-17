import mysql.connector

class UserDB():
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
    
    def insert(self,user):
        '''
        Inserts a new user into the database

        Parameters
        ----------
        user: class
            The user to be inserted

        Returns
        ------
        None
        '''

        self.connect()

        sqlFormula = "INSERT INTO userList (userID, username) VALUE (%s,%s)"
        word = (self.escapeString(user.id),self.escapeString(user.name))
        self.cursor.execute(sqlFormula,word)
        self.mydb.commit()
        self.close()

        return
    
    def fetch(self):
        '''
        Fetches users and combines them into a list

        Returns
        ------
        userArray: str[]
            A list of the users pulled from database
        '''
        self.connect()

        sqlFormula = "SELECT * FROM userList"
        self.cursor.execute(sqlFormula)
        myresults = self.cursor.fetchall()

        # Format everything
        userArray = []
        for row in myresults:
            userArray.append(row[0])

        self.close()

        return myresults
        
        # UPDATE `table_name` SET `column_name` = `new_value' [WHERE condition];
    
    def updateSwears(self, user):
    
        self.connect()

        sqlFormula = "UPDATE userList SET swearCount = swearCount + 1 WHERE userID = %s" % (user.id)
        # word = (self.escapeString(user.id))
        self.cursor.execute(sqlFormula)
        self.mydb.commit()
        self.close()

        return
