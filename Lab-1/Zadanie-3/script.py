# 1. Podaj ilość elementów, jeśli mniejsza lub równa 0 => podaj ponownie
# 2. Wczytaj n-tą liczbę całkowią
# 3. Podaj liczbę, którą należy wyszukać w tym ciągu
# 4. Jeśli liczba występuje => pokaż jej indeks pierwszego wystąpnenia
# 5. Jeśli liczba nie występuje => wyświetl odpowiedni komunikat


def wyszukaj(lista, cel):
    for indeks, element in enumerate(lista):
        if element == cel:
            return indeks
    return -1

def stworzCiagIZnajdzLiczbe():
    while True:
        try:
            ciag = []
            licznik = 1
            n = int(input('Podaj liczbę elementów: '))

            if n <= 0:
                print('Ilość nie może być mniejsza ani równa 0!')
                continue
            
            while licznik <= n:
                a = int(input(f'Podaj liczbę nr {licznik}: '))
                ciag.append(a)
                licznik += 1

            szukanaLiczba = int(input('Podaj liczbę, którą chcesz znaleźć: '))

            indeks = wyszukaj(ciag, szukanaLiczba)

            if indeks != -1:
                print(f'Indeks znalezionej liczby: {indeks}')
            else:
                print('Szukanej liczby nie ma w ciągu')

        except ValueError:
            print('Podaj poprawną wartość')

stworzCiagIZnajdzLiczbe()