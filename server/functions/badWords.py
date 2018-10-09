import mysql.connector
from serverSetup import DBUSER,DBPASS

# TODO move mydb to main.py and combine it with the fetch method there to minimize time
mydb = mysql.connector.connect(
    host="us-cdbr-iron-east-01.cleardb.net",
    user=DBUSER,
    passwd=DBPASS,
    database="heroku_5e695080c7ef107"
)

def getCursor():
    try:
        cursor = mydb.cursor()
    except:
        mydb = mysql.connector.connect(
            host="us-cdbr-iron-east-01.cleardb.net",
            user=DBUSER,
            passwd=DBPASS,
            database="heroku_5e695080c7ef107"
        )
        cursor = mydb.cursor()
    return cursor

def fetch():
    try:
        mycursor = mydb.cursor()
    except:
        mydb = mysql.connector.connect(
            host="us-cdbr-iron-east-01.cleardb.net",
            user=DBUSER,
            passwd=DBPASS,
            database="heroku_5e695080c7ef107"
        )
        mycursor = mydb.cursor()

    sqlFormula = "SELECT * FROM badwords"
    mycursor.execute(sqlFormula)
    myresults = mycursor.fetchall()

    # Format everything
    badWordArray = []
    for row in myresults:
        badWordArray.append(row[0])

    mycursor.close()
    return badWordArray

def run(badWord,baddies):

    if not badWord.lower() in baddies:
        try:
            mycursor = mydb.cursor()
        except:
            mydb = mysql.connector.connect(
                host="us-cdbr-iron-east-01.cleardb.net",
                user=DBUSER,
                passwd=DBPASS,
                database="heroku_5e695080c7ef107"
            )
            mycursor = mydb.cursor()
        
        sqlFormula = "INSERT INTO badwords (word, badness) VALUE (%s,%s)"
        word = (badWord.lower(),1)

        mycursor.execute(sqlFormula, word)
        mydb.commit()
        mycursor.close()

def printAll():
    
    baddies = fetch()
    return ' '.join(baddies)

def delete(badWord):
    try:
        mycursor = mydb.cursor()
    except:
        mydb = mysql.connector.connect(
            host="us-cdbr-iron-east-01.cleardb.net",
            user=DBUSER,
            passwd=DBPASS,
            database="heroku_5e695080c7ef107"
        )
        mycursor = mydb.cursor()
    
    sqlFormula = "DELETE FROM badwords WHERE word='%s'" % badWord

    mycursor.execute(sqlFormula)
    mydb.commit()
    mycursor.close()