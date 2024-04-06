def czy_liczba_pierwsza(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def test_czy_liczba_pierwsza():
    cases = ((1, False), (2, True), (13, True), (64, False), (997, True), (1001*1001, False))
    for case in cases:
        n = case[0]
        expected_result = case[1]
        result = czy_liczba_pierwsza(n)
        print(f"Liczba {n}: oczekiwano {expected_result}, otrzymano {result}")
        assert result == expected_result, f"Błąd dla liczby {n}"

# Wywołanie funkcji testującej
test_czy_liczba_pierwsza()
def liczby_pierwsze_z_zakresu():
    start = int(input("Podaj początek zakresu: "))
    koniec = int(input("Podaj koniec zakresu: "))

    print(f"Liczby pierwsze w zakresie od {start} do {koniec}:")
    for liczba in range(start, koniec + 1):
        if czy_liczba_pierwsza(liczba):
            print(liczba)


# Wywołanie funkcji
liczby_pierwsze_z_zakresu()
