import mysql.connector

import os
from dotenv import load_dotenv

load_dotenv(verbose=True)
MYSQLPW = os.getenv('MYSQLPW')
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=MYSQLPW,
    database="cyberbullying"
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



    