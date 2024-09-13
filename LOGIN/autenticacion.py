
import bcrypt
from LOGIN.BD import BD

class Auth:
    def __init__(self):
        self.db = BD()

    def login(self, username, password):
        user = self.db.get_user(username)
        if user:
            stored_password_hash = user[1]
            if bcrypt.checkpw(password.encode('utf-8'), stored_password_hash.encode('utf-8')):
                return True
        return False

    def register(self, username, password):
        if not username or not password:
            return False
        if self.db.get_user(username) is None:
            password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            self.db.create_user(username, password_hash)
            return True
        return False
