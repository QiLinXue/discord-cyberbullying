import os
from dotenv import load_dotenv

load_dotenv(verbose=True)
DBUSER = os.getenv('DBUSER')
DBPASS = os.getenv('DBPASS')
