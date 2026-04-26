def odwroc_ciag():
    wejscie = input("Podaj liczby całkowite rozdzielone spacjami: ")
    
    try:
        liczby = [int(x) for x in wejscie.split()]
    except ValueError:
        print("Podaj tylko liczby całkowite!")
        return

    print(f"\nOryginalny ciąg: {liczby}")
    
    stos = []
    
    for liczba in liczby:
        stos.append(liczba)
        
    print("Odwrócony ciąg: ", end="")
    
    while len(stos) > 0:
        ostatni_element = stos.pop()
        print(ostatni_element, end=" ")

if __name__ == "__main__":
    odwroc_ciag()