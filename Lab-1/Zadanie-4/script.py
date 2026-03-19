import random
# Napisz program, który będzie polegał na zgadywaniu wylosowanej liczby. Ilość odgadnięć ma
# być zliczana. Program ma być zgodny z poniższym algorytmem.
# 1.1 Wybierz losowo liczbę z zakresu od 1 do 100
# 1.2 Ustaw licznik prób na 1
# 1.3 Poproś użytkownika o wpisanie liczby
# 1.3.1 Jeżeli liczba jest równa wylosowanej przerwij pętlę i przejdź do punktu 1.4
# 1.3.2 Jeżeli liczba jest większa od wylosowanej wyświetl komunikat, że liczba jest
# większa.
# 1.3.3 Jeżeli liczba jest mniejsza od wylosowanej wyświetl komunikat, że liczba jest
# mniejsza.
# 1.3.4 Zwiększ liczbę prób o 1
# 1.3.5 Powróć do punktu 1.3
# 1.4 Wyświetl komunikat przedstawiający poprawna liczbę
# 1.5 Wyświetl komunikat przedstawiający ilość prób.

    
def odgadnijLiczbe():
    licznikProb = 1
    wylosowanaLiczba = random.randint(1,100)
    
    while True:
        try:
            liczbaUzytkownika = int(input('Podaj liczbę: '))

            if(liczbaUzytkownika == wylosowanaLiczba):
                print(f'Gratulacje użytkowniku - odgadłeś liczbę, ta liczba to {wylosowanaLiczba}')
                print(f'Ilość prób: {licznikProb}')
                break
            elif(wylosowanaLiczba < liczbaUzytkownika):
                print('Wylosowana liczba jest mniejsza od podanej przez ciebie wartości')
                licznikProb += 1
            elif(wylosowanaLiczba > liczbaUzytkownika):
                print('Wylosowana liczba jest większa od podanej przez ciebie wartości')
                licznikProb += 1
        
        except ValueError:
            print('Podaj poprawną wartość')

    

odgadnijLiczbe()