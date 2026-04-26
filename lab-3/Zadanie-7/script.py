def uruchom_przychodnie():
    kolejka = []
    
    menu = '''\nWybierz działanie:
1. Zarejestruj pacjenta
2. Wywołaj pacjenta do gabinetu
3. Pokaż aktualną kolejkę
4. Zakończ działanie programu'''

    while True:
        print(menu)
        wybor = input("Twój wybór: ")

        if wybor == '1':
            nazwisko = input("Podaj nazwisko pacjenta: ")
            kolejka.append(nazwisko)
            print(f"Pacjent {nazwisko} został zarejestrowany.")
        
        elif wybor == '2':
            if len(kolejka) > 0:
                pacjent = kolejka.pop(0)
                print(f"Pacjent {pacjent} proszony do gabinetu.")
            else:
                print("Kolejka jest pusta!")
        
        elif wybor == '3':
            if not kolejka:
                print("Kolejka jest aktualnie pusta.")
            else:
                print("Aktualna kolejka pacjentów:")
                for i, pacjent in enumerate(kolejka, 1):
                    print(f"{i}. {pacjent}")
        
        elif wybor == '4':
            print("Zamykanie systemu")
            break
        
        else:
            print("Nieprawidłowy wybór")

if __name__ == "__main__":
    uruchom_przychodnie()