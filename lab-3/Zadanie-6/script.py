from collections import deque

def pobierz_n_elementow(kolejka, n):
    if not kolejka:
        return "Kolejka jest pusta"
    
    wynik = []
    
    while len(wynik) < n and kolejka:
        element = kolejka.popleft()
        wynik.append(element)
        
    return wynik


moja_kolejka = deque(["A", "B", "C", "D", "E"])

print(pobierz_n_elementow(moja_kolejka, 3))
print(pobierz_n_elementow(moja_kolejka, 10))
print(pobierz_n_elementow(moja_kolejka, 1))