n = int(input("Podaj liczbę graczy: "))

wyniki = []

for i in range(n):
    wynik = int(input(f"Podaj wynik gracza {i+1}: "))
    wyniki.append(wynik)

for i in range(n):
    for j in range(0,n-i-1):
        if wyniki[j] > wyniki[j + 1]:
            wyniki[j], wyniki[j + 1] = wyniki[j + 1], wyniki[j]

print("Wyniki po sortowaniu", wyniki)
print("Najniższy wynik:", wyniki[0])
print("Najwyższy wynik:", wyniki[-1])