# algorytmy


Wybrałem implementację tokenizacji danych płatniczych i tworzenie uzytkowników ze zhaszowanymi hasłami, ponieważ opisywałem haszowanie w artykule i interesuje mnie szeroko pojęty temat finansów i płatności.  W moim przypadku projekt tak naprawdę nie jest właściwą tokenizacją poprawiającą bezpieczeństwo transakcji, a jest on związany z formatowaniem danych wejściowych na bardziej czytelny format tokenów (formatowanie i przetwarzanie danych). 

Formatowanie numeru karty kredytowej: numer karty kredytowej jest dzielony na grupy po 4 cyfry. Formatowanie daty ważności: data ważności karty jest zamieniana na bardziej czytelny format (np. "12/24" staje się "grudzień 2024"). Formatowanie kwoty: kwota płatności jest formatowana jako wartość z dwoma miejscami po przecinku i dodaniem waluty PLN.

# Problemy przy implementacji:
## Czytelność danych
Surowe dane płatnicze, takie jak numer karty kredytowej lub data ważności, mogą być trudne do odczytania i weryfikacji przez użytkowników lub systemy.
## Rozwiązanie
Dzielenie numeru karty kredytowej na grupy po 4 cyfry i formatowanie daty ważności w bardziej czytelny sposób poprawia czytelność i zmniejsza ryzyko błędów.
## Spójność formatowania
Brak jednolitego formatu danych wejściowych i wyjściowych może prowadzić do niespójności w wyświetlaniu i przetwarzaniu danych, co może powodować błędy.
## Rozwiązanie
Implementacja standardowego formatowania zapewnia, że dane są zawsze prezentowane w spójny i przewidywalny sposób.
