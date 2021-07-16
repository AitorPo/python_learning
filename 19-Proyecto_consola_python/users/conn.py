import mysql.connector as conn

def doConnect():
    db = conn.connect(
        host = 'localhost',
        port = 3306,
        user = 'root',
        passwd = '',
        database = 'python_console'
    )

    cursor = db.cursor(buffered = True)

    return [db, cursor]
