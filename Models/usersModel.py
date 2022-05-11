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
        conn.commit()
        conn.close()
        return data

    def update(data, newData):
        emptyArray = []
        conn = get_db_connection()
        users = conn.execute('UPDATE users SET username = ?, email=? WHERE id = ? RETURNING *', ( newData['username'],newData['email'],data['id']))
        for user in users: 
            userData = {
                "id": user["id"],
                "email": user["email"],
                "username": user["username"]
            }
            emptyArray.append(userData)
        conn.commit()
        conn.close()
        return emptyArray
    
    
    def delete(id):
        conn = get_db_connection()
        users = conn.execute('DELETE FROM users WHERE id=?', (id,))
        conn.commit()
        conn.close()
        return