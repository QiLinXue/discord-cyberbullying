import mysql.connector

class BadWordsDB():
    from serverSetup import DBUSER,DBPASS

    def __init__(self,host,user,passwd,database,filterList=[]):
        self.host= host
        self.user = user
        self.passwd = passwd
        self.database = database
        self.filterList = filterList

    def connect(self):
        self.mydb = mysql.connector.connect(
            host=self.host,
            user=self.user,
            passwd=self.passwd,
            database=self.database
        )
        self.cursor = self.mydb.cursor()

    def close(self):
        self.cursor.close()
        self.mydb.close()

    def fetch(self):
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
    
    def insert(self,targetWord,badwordlist):
        if not targetWord.lower() in badwordlist:
            self.connect()

            sqlFormula = "INSERT INTO badwords (word, badness) VALUE (%s,%s)"
            word = (targetWord.lower(),1)

            self.cursor.execute(sqlFormula, word)
            self.close()
    
    def printAll(self):
        baddies = self.fetch()
        return ' '.join(baddies)

    def delete(self,targetWord):
        self.connect()

        sqlFormula = "DELETE FROM badwords WHERE word='%s'" % targetWord

        self.cursor.execute(sqlFormula)
        self.close()
