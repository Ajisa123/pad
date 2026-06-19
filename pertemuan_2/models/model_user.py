from database import get_connection

class UserModel:
    @staticmethod
    def authenticate(username, password):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT id, username, role, nama FROM users WHERE username = ? AND password = ?', (username, password))
        row = cursor.fetchone()
        conn.close()
        
        if row:
            return {'id': row['id'], 'username': row['username'], 'role': row['role'], 'nama': row['nama']}
        return None