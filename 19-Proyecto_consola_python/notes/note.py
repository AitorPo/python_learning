import users.conn as connection

connect = connection.doConnect()
db = connect[0]
cursor = connect[1]


class Note:

    # title and content are optionals
    def __init__(self, idUser, title="", content=""):
        self.idUser = idUser
        self.title = title
        self.content = content

    def saveOnDB(self):
        sql = 'INSERT INTO notes VALUES (null, %s, %s, %s, NOW())'
        note = (self.idUser, self.title, self.content)

        try:
            cursor.execute(sql, note)
            db.commit()
            result = [cursor.rowcount, self]
        except:
            result = [0, self]

        return result

    def getNotes(self):
        # print(idUser)
        sql = "SELECT * FROM notes WHERE user_id = %s"
        idUser = (self.idUser, )

        cursor.execute(sql, idUser)
        result = cursor.fetchall()

        return result

    def deleteNote(self):
        sql = 'DELETE FROM notes WHERE user_id = %s AND title = ''%s'''
        data = (self.idUser, self.title)
        cursor.execute(sql, data)
        db.commit()

        return [cursor.rowcount, self]