def dodawnie(x, y):
    return x + y

def odejmwowanie(x, y):
    return x - y

def mnozenie(x, y):
    return x * y

def dzielenie(x, y):
    return x / y

print("Wybierz operacje:")

while True:
    choice = input("Napisz skrot dzialania ktore chcesz wykonać\n (DOD - dodawnie/ ODE - odejmowanie / MNO - monożenie/DZI - dzielenie):\n")

    if choice in ('DOD', 'ODE', 'MNO', 'DZI'):
        try:
            num1 = float(input("Podaj pierwsza liczbe: "))
            num2 = float(input("Podaj druga liczbe: "))
        except ValueError:
            print("Niepoprawny argument, musisz wprowadzic liczbe")
            continue

        if choice == 'DOD':
            print(num1, "+", num2, "=", dodawnie(num1, num2))

        elif choice == 'ODE':
            print(num1, "-", num2, "=", odejmwowanie(num1, num2))

        elif choice == 'MNO':
            print(num1, "*", num2, "=", mnozenie(num1, num2))

        elif choice == 'DZI':
            print(num1, "/", num2, "=", dzielenie(num1, num2))

        next_calculation = input("Czy chcesz pracowac dalej? (tak/nie): ")
        if next_calculation == "nie":
            break
    else:
        print("Niepoprawny parametr!")
