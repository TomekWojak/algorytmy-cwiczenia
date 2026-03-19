import math
def obliczRownanieKwadratowe():
    a = float(input('Podaj a: '))

    if(a == 0):
        print('To nie jest równanie kwadratowe')
        return

    b = float(input('Podaj b: '))
    c = float(input('Podaj c: '))
    delta = math.pow(b,2) - 4 * a * c

    if(delta < 0):
        return 'Brak rozwiązań w zbiorze liczb rzeczywistych'
    elif(delta == 0):
        x0 = -b / (2 * a)
        return x0
    elif(delta > 0):
        x1 = (-b - math.sqrt(delta)) / (2 * a)
        x2 = (-b + math.sqrt(delta)) / (2 * a)
        return round(x1,2),round(x2,2)
    
print(obliczRownanieKwadratowe())