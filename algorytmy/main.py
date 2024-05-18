from PasswordManager import PasswordManager
from Transcations import tokenize_payment_data, display_transaction_info

password_manager = PasswordManager()

while True:
    print("\nWybierz opcję:")
    print("1. Utwórz nowe konto")
    print("2. Zaloguj się")
    print("3. Wyświetl tokenizowane hasła")
    print("4. Wyświetl token sesji")
    print("5. Wyjdź")

    choice = input("Wybór: ")

    if choice == '1':
        username = input("Podaj nazwę użytkownika: ")
        password = input("Podaj hasło: ")
        password_manager.create_user(username, password)
    elif choice == '2':
        username = input("Podaj nazwę użytkownika: ")
        password = input("Podaj hasło: ")
        if password_manager.handle_login(username, password):
            while True:
                print("\nWybierz opcję:")
                print("1. Wyświetl token sesji")
                print("2. Wyloguj się")
                print("3. Dokonaj płatności")
                user_choice = input("Wybór: ")
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
                    credit_card_number = input("Wprowadź numer karty kredytowej: ")
                    expiry_date = input("Wprowadź datę ważności karty (MM/RR): ")
                    amount = input("Wprowadź kwotę płatności: ")
                    payment_data = tokenize_payment_data(credit_card_number, expiry_date, amount)
                    display_transaction_info(payment_data)
                else:
                    print("Niepoprawny wybór. Spróbuj ponownie.")
        else:
            print("Błędne dane logowania.")
    elif choice == '3':
        password_manager.display_tokenized_passwords()
    elif choice == '4':
        username = input("Podaj nazwę użytkownika: ")
        password_manager.display_session_token(username)
    elif choice == '5':
        print("Do widzenia!")
        break
    else:
        print("Niepoprawny wybór. Spróbuj ponownie.")
