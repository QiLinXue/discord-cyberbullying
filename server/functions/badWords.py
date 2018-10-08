import mysql.connector

import os
from dotenv import load_dotenv

load_dotenv(verbose=True)
DBUSER = os.getenv('DBUSER')
DBPASS = os.getenv('DBPASS')

mydb = mysql.connector.connect(
    host="us-cdbr-iron-east-01.cleardb.net",
    user=DBUSER,
    passwd=DBPASS,
    database="heroku_5e695080c7ef107"
)

mycursor = mydb.cursor()

def run(badWord):

    sqlFormula = "INSERT INTO badwords (word, badness) VALUE (%s,%s)"
    word = (badWord,1)

    mycursor.execute(sqlFormula, word)
    mydb.commit()

def fetch():

    sqlFormula = "SELECT * FROM badwords"
    mycursor.execute(sqlFormula)
    myresults = mycursor.fetchall()

    # Format everything
    badWordArray = []
    for row in myresults:
        badWordArray.append(row[0])

    return badWordArray



    