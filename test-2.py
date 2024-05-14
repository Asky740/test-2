import random

pole = []

body = 0
body = int(body)

for i in range(random.randint(1, 15)):

    print(" ")
    print("Kolo č.",i+1)
    print(" ")

    for j in range(random.randint(1, 10)):
        pole.append(random.randint(1, 10))

    print(pole)
    print(" ")

    delka = int(len(pole))

    odpoved = input("napiš délku pole:")
    odpoved = int(odpoved)

    print(" ")

    if odpoved == delka:
       body = body + 1
       print("správně, získáváš bod, tvé body:",body)
    else:
       body = body - 1
       print("špatně, ztrácíš bod, tvé body:",body)

print("Konec hry, tvé body:",body)