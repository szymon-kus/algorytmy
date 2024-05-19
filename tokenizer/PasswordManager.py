import bcrypt
from uuid import uuid4
from Transcations import *
from User import User

class PasswordManager:
    def __init__(self):
        self.users = {}
        self.sessions = {}

    def create_user(self, username, password):
        if username in self.users:
            print("Użytkownik o takiej nazwie już istnieje.")
            return
        user = User(username, password)
        self.users[username] = user
        print("Użytkownik został pomyślnie utworzony.")

    def handle_login(self, username, password):
        if username not in self.users:
            print("Użytkownik o podanej nazwie nie istnieje.")
            return False
        user = self.users[username]
        if user.verify_password(password):
            print("Zalogowano pomyślnie.")
            # Generowanie tokenu sesji po udanym logowaniu
            session_token = self.generate_session_token(username)
            print(f"Token sesji: {session_token}")
            return True
        else:
            print("Błędne hasło.")
            return False

    def display_tokenized_passwords(self):
        print("Tokenizowane hasła użytkowników:")
        for username, user in self.users.items():
            print(f"{username}: {' '.join(user.password_hash)}")

    def display_session_token(self, username):
        session_token = self.get_session_token(username)
        if session_token:
            print(f"Token sesji dla użytkownika {username}: {session_token}")
        else:
            print("Brak aktywnej sesji dla podanego użytkownika.")

    def generate_session_token(self, username):
        token = str(uuid4())
        self.sessions[username] = token
        return token

    def get_session_token(self, username):
        return self.sessions.get(username)

