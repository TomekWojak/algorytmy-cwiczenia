def czy_nawiasy_poprawne(wyrazenie):
    stos = []
    
    for znak in wyrazenie:
        if znak == '(':
            stos.append(znak)
        elif znak == ')':
            if not stos:
                return False
            stos.pop()
    return len(stos) == 0

wynik = 'nawiasy poprawne' if czy_nawiasy_poprawne('(()()(()))') else 'nawiasy niepoprawne'
wynik2 = 'nawiasy poprawne' if czy_nawiasy_poprawne('(()') else 'nawiasy niepoprawne'
print(wynik, wynik2)
