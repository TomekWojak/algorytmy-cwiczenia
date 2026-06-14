moj_graf = {
    'A': {'B', 'C'},
    'B': {'A', 'C', 'D'},
    'C': {'A', 'B', 'D', 'E'},
    'D': {'B', 'C', 'E'},
    'E': {'C', 'D'}
}

def wypisz_sasiadow(graf, wierzcholek):
    if wierzcholek in graf:
        sasiedzi = graf[wierzcholek]
        if sasiedzi:
            print(f"Sąsiedzi wierzchołka '{wierzcholek}': {', '.join(sorted(sasiedzi))}")
        else:
            print(f"Wierzchołek '{wierzcholek}' nie ma żadnych sąsiadów.")
    else:
        print(f"Błąd: Wierzchołek '{wierzcholek}' nie istnieje w tym grafie!")



print("Prezentacja działania funkcji dla różnych wierzchołków:\n")

wypisz_sasiadow(moj_graf, 'C')

wypisz_sasiadow(moj_graf, 'A')

wypisz_sasiadow(moj_graf, 'Z')