import random
import time
ran = random.randint(1, 20)
print('Spróbuj odgadnąć liczbę!')
print("Liczba o której myślę jest pomiędzy 1 i 20")
time.sleep(0.10)

input1 = int(input())
if input1 > ran:
    print('Liczba o której myślę jest mniejsza niż', input1)
    print("Zostały ci dwie szansy!")

if input1 < ran:
    print("Liczba o której myślę jest większa niż", input1)
    print("Zostały ci dwie szansy!")

if input1 == ran:
    print('Liczba o której myślałem to była', ran)
    print("Wygrałeś!")
    time.sleep(2)
    exit()

time.sleep(0.10)

input2 = int(input())
if input2 > ran:
    print('Liczba o której myślę jest mniejsza niż', input2)
    print("Została ci jedna szansa!")

if input2 < ran:
    print("Liczba o której myślę jest większa niż", input2)
    print("Została ci jedna szansa!")

if input2 == ran:
    print('Liczba o której myślałem to była', ran)
    print("Wygrałeś!")
    time.sleep(2)
    exit()

time.sleep(0.10)

input3 = int(input())
if input3 != ran:
    print('Liczba o której myślałem to była', ran)
    print("Przegrałeś!")
    time.sleep(2)
    exit()

if input3 == ran:
    print('Liczba o której myślałem to była', ran)
    print("Wygrałeś!")
    time.sleep(2)
    exit()
