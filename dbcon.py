import pyodbc

try:
    con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\Tareq\Documents\pydbc.accdb;'
    conn = pyodbc.connect(con_string)
    print("connected to database")
except pyodbc.Error as e:
    print("Error in connection", e)