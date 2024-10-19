import mysql.connector
__cnx=None

def get_sql_connection():
    global __cnx
    if(__cnx==None):
        __cnx = mysql.connector.connect(user='root', password='1234',
                              host='127.0.0.1',
                              database='grocery_management_system')
    return __cnx