graf = {
    'A': {'B', 'C'},
    'B': {'C', 'D'},
    'C': {'D'},
    'D': {}
}

wierzcholki = sorted(list(graf.keys()))
rozmiar = len(wierzcholki)

mapowanie = {wierzcholek: indeks for indeks, wierzcholek in enumerate(wierzcholki)}


macierz = [[0] * rozmiar for _ in range(rozmiar)]


for u, sasiedzi in graf.items():
    for v in sasiedzi:
        indeks_start = mapowanie[u]
        indeks_koniec = mapowanie[v]
        macierz[indeks_start][indeks_koniec] = 1


lista_krawedzi = []

for u, sasiedzi in graf.items():
    for v in sasiedzi:
        lista_krawedzi.append((u, v))


lista_krawedzi.sort()



print("a) Macierz sąsiedztwa:")
for wiersz in macierz:
    print(wiersz)

print("\nb) Lista krawędzi:")
print(lista_krawedzi)