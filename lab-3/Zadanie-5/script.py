from collections import deque

def symulacja_kolejki():
    kolejka = deque()

    for i in range(1, 4):
        try:
            liczba = int(input(f"Podaj liczbę nr {i}: "))
            kolejka.append(liczba)
        except ValueError:
            print("To nie jest liczba całkowita!")
            return

    
    while len(kolejka) > 0:
        element = kolejka.popleft()
        print(f"Pobrano z kolejki: {element}")

if __name__ == "__main__":
    symulacja_kolejki()