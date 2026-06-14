graf = {
    'A': {'B': -4},
    'B': {'C': 1},
    'C': {'A': -2}
}

def bellman_ford(graf, start):
    V = len(graf)
    
    odleglosci = {wierzcholek: float('inf') for wierzcholek in graf}
    odleglosci[start] = 0
    
    print(f"Stan początkowy tablicy odległości: {odleglosci}")
    print("-" * 60)
    
    for i in range(1, V):
        for u in graf:
            for v, waga in graf[u].items():
                if odleglosci[u] != float('inf') and odleglosci[u] + waga < odleglosci[v]:
                    odleglosci[v] = odleglosci[u] + waga
                    
        print(f"Po iteracji {i}: {odleglosci}")
        
    print("-" * 60)
    
    ujemny_cykl = False
    
    for u in graf:
        for v, waga in graf[u].items():
            if odleglosci[u] != float('inf') and odleglosci[u] + waga < odleglosci[v]:
                print(f"-> MOMENT WYKRYCIA CYKLU (Iteracja weryfikacyjna):")
                print(f"   Próba relaksacji krawędzi {u} -> {v} (waga: {waga})")
                print(f"   Nowy potencjalny dystans dla {v} to: {odleglosci[u]} + ({waga}) = {odleglosci[u] + waga}")
                print(f"   Aktualny dystans w tablicy dla {v} wynosi: {odleglosci[v]}")
                print(f"   Ponieważ {odleglosci[u] + waga} < {odleglosci[v]}, algorytm przerywa pracę i zgłasza ujemny cykl.")
                ujemny_cykl = True
                break
        if ujemny_cykl:
            break
            
    if ujemny_cykl:
        print("\n[WYNIK]: Graf zawiera cykl o ujemnej wadze. Najkrótsze ścieżki nie mogą zostać wyznaczone.")
    else:
        print("\n[WYNIK]: Brak ujemnych cykli. Ostateczne odległości:", odleglosci)

bellman_ford(graf, 'A')