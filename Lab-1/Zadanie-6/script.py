macierz = [[5,2,9,8],[1,7,3,4],[6,0,2,5]]
def znajdz_min_max(macierz):
    min_val = macierz[0][0]
    max_val = macierz[0][0]
    
    min_pos = (0, 0)
    max_pos = (0, 0)

    for i in range(len(macierz)):
        for j in range(len(macierz[i])):
            if macierz[i][j] < min_val:
                min_val = macierz[i][j]
                min_pos = (i, j)
            if macierz[i][j] > max_val:
                max_val = macierz[i][j]
                max_pos = (i, j)

    for i in range(len(macierz)):
        for j in range(len(macierz[i])):
            if (i, j) == min_pos:
                print("MIN", end=" ")
            elif (i, j) == max_pos:
                print("MAX", end=" ")
            else:
                print(macierz[i][j], end=" ")
        print()


znajdz_min_max(macierz)