def tokenize_payment_data(credit_card_number, expiry_date, amount):
    formatted_credit_card_number = ' '.join([credit_card_number[i:i+4] for i in range(0, len(credit_card_number), 4)])

    months = ['styczeń', 'luty', 'marzec', 'kwiecień', 'maj', 'czerwiec', 'lipiec', 'sierpień', 'wrzesień', 'październik', 'listopad', 'grudzień']
    month, year = expiry_date.split('/')
    formatted_expiry_date = f"{months[int(month)-1]} 20{year}"

    formatted_amount = f"{amount:.2f} PLN"

    payment_data = {
        'credit_card_number': formatted_credit_card_number,
        'expiry_date': formatted_expiry_date,
        'amount': formatted_amount
    }
    return payment_data

def display_transaction_info(payment_data):
    print("Informacje o transakcji:")
    print("Numer karty kredytowej:", payment_data['credit_card_number'])
    print("Data ważności karty:", payment_data['expiry_date'])
    print("Kwota płatności:", payment_data['amount'])
