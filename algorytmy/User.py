import bcrypt

class User:
    def __init__(self, username, password):
        self.username = username
        self.password_hash = self._hash_password(password)

    def _hash_password(self, password):
        salt = bcrypt.gensalt()
        password_hash = bcrypt.hashpw(password.encode('utf-8'), salt)
        return password_hash.decode('utf-8')

    def verify_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password_hash.encode('utf-8'))
