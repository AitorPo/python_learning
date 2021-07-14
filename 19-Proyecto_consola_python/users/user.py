import mysql.connector as conn

db = conn.connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    passwd = '',
    database = 'python_console'
)

cursor = db.cursor(buffered = True)

class User:

    def __init__(self, name, surname, email, password):
        self.name = name
        self.surname = surname
        self.email = email
        self.password = password

    def __str__ (self):
        return self.email + ' ' + self.name

    def register(self):
        return self.name

    def identify(self):
        return self.password
