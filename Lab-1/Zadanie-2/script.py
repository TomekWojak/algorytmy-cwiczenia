# 1. Podaj ilość liczb ciągu
# 2. Jeśli liczba ta jest ujemna lub równa 0 => wyświetl odpowiednią informację i zapytaj użytkownika jeszcze raz
# 3. Jeśli wszystko się zgadza => podaj pierwszy wyraz ciągu i n kolejnych wyrazów
# 5. Przejdź po wszystkich elementach ciagu podanych przez użytkownika i przy pomocy modulo określ, która liczba jest parzysta.
# 6. Jeśli liczba jest parzysta => zwiększ liznik o 1, jeśli nie => nie rób nic


def wyznaczLiczbyParzyste():
    try:
        while True:
            licznikWyrazow = 1
            licznikParzystych = 0
            n = int(input('Podaj ilość liczb ciągu: '))
            if(n <= 0):
                print('Ilość nie może być mniejsza ani równa 0!')
                continue

            while licznikWyrazow <= n:
                wyraz = int(input(f'Podaj wyraz nr {licznikWyrazow}: '))
                if(wyraz % 2 == 0): licznikParzystych += 1
                licznikWyrazow += 1
            print(f'Ilość liczb parzystych: {licznikParzystych}')
            break
    except ValueError:
        print('Podaj poprawne dane')
wyznaczLiczbyParzyste()