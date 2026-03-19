lista = [1,2,3,4,5,5,5]

def znajdzDrugaNajwieksza():
    najwieksza = max(lista)
    
    for numer in sorted(lista, reverse=True):
        if numer < najwieksza:
            return numer

    return None

print(znajdzDrugaNajwieksza())