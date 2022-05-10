import sqlite3

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


class Users:
    def __init__(self, id, username, email):
        self.id = id
        self.username = username
        self.email = email

    @staticmethod
    def getAll():
        data = []
        conn = get_db_connection()
        users = conn.execute('SELECT * FROM users').fetchall()
        for user in users:
            # userData = Users(user["id"], user["username"], user["email"])
            userData = {
                "id": user["id"],
                "email": user["email"],
                "username": user["username"]
            }
            data.append(userData)
        print(data)
        conn.close()
        return data

    @classmethod
    def show(self, username):
        data = []

        conn = get_db_connection()
        users = conn.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchall()
        for user in users:
            userData = {
                "id": user["id"],
                "email": user["email"],
                "username": user["username"]
            }
            data.append(userData)
        conn.close()
        return data
    
    @classmethod
    def create(self, userData):
        # print(userData)
        data = []
        conn = get_db_connection()
        users = conn.execute('INSERT INTO users (username, email) VALUES (?,?) RETURNING *', (userData["username"],userData["email"])).fetchall()
        for user in users:
            print(user["id"],user["email"], user["username"] )
            userData = {
                "id": user["id"],
                "email": user["email"],
                "username": user["username"]
            }
            data.append(userData)
        # print(data)
        conn.close()
        return data

    def update(data):
        print(data)
        conn = get_db_connection()
        users = conn.execute('DELETE FROM users WHERE id=?', (id,))
        conn.close()
        return
    
    
    def delete(id):
        print(id)
        conn = get_db_connection()
        users = conn.execute('DELETE FROM users WHERE id=?', (id,))
        conn.close()
        return