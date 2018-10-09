import mysql.connector
from serverSetup import DBUSER,DBPASS

def run(badWord):

    mydb = mysql.connector.connect(
        host="us-cdbr-iron-east-01.cleardb.net",
        user=DBUSER,
        passwd=DBPASS,
        database="heroku_5e695080c7ef107"
    )

    mycursor = mydb.cursor()

    sqlFormula = "INSERT INTO badwords (word, badness) VALUE (%s,%s)"
    word = (badWord,1)

    mycursor.execute(sqlFormula, word)
    mydb.commit()
    mycursor.close()

def fetch():

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
