
krawedzie = [("A", "B"), ("A", "C"), ("B", "C"), ("B", "D"), ("C", "D")]


wierzcholki = set()
for u, v in krawedzie:
    wierzcholki.add(u)
    wierzcholki.add(v)

wierzcholki = sorted(list(wierzcholki))


lista_sasisiedztwa = {w: set() for w in wierzcholki}


for u, v in krawedzie:
    lista_sasisiedztwa[u].add(v)


rozmiar = len(wierzcholki)

mapowanie = {w: i for i, w in enumerate(wierzcholki)}


macierz_sasedztwa = [[0] * rozmiar for _ in range(rozmiar)]

for u, v in krawedzie:
    i_start = mapowanie[u]
    i_koniec = mapowanie[v]
    macierz_sasedztwa[i_start][i_koniec] = 1


print("1. Lista sąsiedztwa (jako słownik w Pythonie):")
for wierzcholek, sasiedzi in lista_sasisiedztwa.items():
    print(f"  '{wierzcholek}': {sorted(list(sasiedzi))}")

print("\n2. Macierz sąsiedztwa (nagłówek kolumn: A, B, C, D):")
for wiersz in macierz_sasedztwa:
    print(f"  {wiersz}")