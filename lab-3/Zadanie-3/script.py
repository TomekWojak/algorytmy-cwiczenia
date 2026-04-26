def symulacja_undo():
    stos_akcji = []
    print("Wpisz tekst, aby go dodać; wpisz 'undo', aby cofnąć; 'exit', aby wyjść")

    while True:
        wybor = input("\n[Stos: {}] > ".format(stos_akcji)).strip()

        if wybor.lower() == 'exit':
            print("Zamykanie programu...")
            break
        
        elif wybor.lower() == 'undo':
            if len(stos_akcji) > 0:
                usuniety = stos_akcji.pop()
                print(f"Cofnięto '{usuniety}'")
            else:
                print("Brak operacji do cofnięcia!")
        
        else:
            stos_akcji.append(wybor)
            print(f"Dodano: '{wybor}'")

if __name__ == "__main__":
    symulacja_undo()