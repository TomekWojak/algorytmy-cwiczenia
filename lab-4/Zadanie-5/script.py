wagi_paczek = [18, 5, 12, 3, 9]

n = len(wagi_paczek)
porownania = 0

print("Stan początkowy:", wagi_paczek)

for i in range(n - 1):
    min_index = i

    for j in range(i + 1, n):
        porownania += 1

        if wagi_paczek[j] < wagi_paczek[min_index]:
            min_index = j

    wagi_paczek[i], wagi_paczek[min_index] = wagi_paczek[min_index], wagi_paczek[i]

    print(f"Krok {i + 1}: {wagi_paczek}")

print("\nWynik końcowy:", wagi_paczek)
print("Liczba porównań:", porownania)