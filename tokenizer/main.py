from PasswordManager import PasswordManager
from Transcations import tokenize_payment_data, display_transaction_info

password_manager = PasswordManager()

def get_input(prompt):
    try:
        return input(prompt)
    except KeyboardInterrupt:
        print("\nAnulowano operację.")
        return None

def handle_new_account():
    username = get_input("Podaj nazwę użytkownika: ")
    if not username:
        return
    password = get_input("Podaj hasło: ")
    if not password:
        return
    password_manager.create_user(username, password)

def handle_login():
    username = get_input("Podaj nazwę użytkownika: ")
    if not username:
        return
    password = get_input("Podaj hasło: ")
    if not password:
        return
    if password_manager.handle_login(username, password):
        while True:
            print("\nWybierz opcję:")
            print("1. Wyświetl token sesji")
            print("2. Wyloguj się")
            print("3. Dokonaj płatności")
            user_choice = get_input("Wybór: ")
            if user_choice == '1':
                session_token = password_manager.get_session_token(username)
                if session_token:
                    print("Token sesji:", session_token)
                else:
                    print("Brak aktywnej sesji dla użytkownika.")
            elif user_choice == '2':
                print("Wylogowano.")
                break
            elif user_choice == '3':
                handle_payment()
            else:
                print("Niepoprawny wybór. Spróbuj ponownie.")
    else:
        print("Błędne dane logowania.")

def handle_payment():
    try:
        credit_card_number = get_input("Wprowadź numer karty kredytowej: ")
        if not credit_card_number or not credit_card_number.isdigit() or len(credit_card_number) not in [13, 16]:
            raise ValueError("Nieprawidłowy numer karty kredytowej.")
        expiry_date = get_input("Wprowadź datę ważności karty (MM/RR): ")
        if not expiry_date or not expiry_date.count('/') == 1 or not all(part.isdigit() for part in expiry_date.split('/')):
            raise ValueError("Nieprawidłowy format daty ważności.")
        month, year = expiry_date.split('/')
        if not (1 <= int(month) <= 12):
            raise ValueError("Nieprawidłowy miesiąc.")
        amount = get_input("Wprowadź kwotę płatności: ")
        amount = float(amount)  # Pozwoli zgłosić wyjątek, jeśli amount nie jest liczbą
        payment_data = tokenize_payment_data(credit_card_number, expiry_date, amount)
        display_transaction_info(payment_data)
    except ValueError as e:
        print(f"Błąd: {e}")
    except Exception as e:
        print(f"Nieoczekiwany błąd: {e}")

def main():
    while True:
        print("\nWybierz opcję:")
        print("1. Utwórz nowe konto")
        print("2. Zaloguj się")
        print("3. Wyświetl tokenizowane hasła")
        print("4. Wyświetl token sesji")
        print("5. Wyjdź")

        choice = get_input("Wybór: ")

        if choice == '1':
            handle_new_account()
        elif choice == '2':
            handle_login()
        elif choice == '3':
            password_manager.display_tokenized_passwords()
        elif choice == '4':
            username = get_input("Podaj nazwę użytkownika: ")
            if username:
                password_manager.display_session_token(username)
        elif choice == '5':
            print("Do widzenia!")
            break
        else:
            print("Niepoprawny wybór. Spróbuj ponownie.")

if __name__ == "__main__":
    main()