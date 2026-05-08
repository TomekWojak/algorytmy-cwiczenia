def wyszukiwanie_liniowe(lista, szukana_wartosc):
    for i in range(len(lista)):
        if lista[i] == szukana_wartosc:
            return i
    return -1


print(wyszukiwanie_liniowe([4, 7, 2, 9, 5], 9))
print(wyszukiwanie_liniowe([10, 20, 30, 40], 25))