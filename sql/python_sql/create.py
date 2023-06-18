import pyodbc

server = '.'
database = 'anahit'
username = 'postgres'
password = 'postgres'
# ENCRYPT defaults to yes starting in ODBC Driver 18. It's good to always specify ENCRYPT=yes on the client side to avoid MITM attacks.
cnxn = pyodbc.connect('DRIVER={DEVART ODBC Driver for POSTGRESQL};SERVER=localhost:5432;DATABASE=anahit;ENCRYPT=yes;UID=postgres;PWD=postgres')
cursor = cnxn.cursor()