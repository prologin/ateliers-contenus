from random import randint

nombre_secret = randint(1, 1000)
nombre = 0
score = 0

while nombre != nombre_secret:
    nombre = int(input("Entre un nombre : "))
    score = score + 1
    if nombre_secret < nombre:
        print("Moins !")
    elif nombre_secret > nombre:
        print("Plus !")
    else:
        print("Gagné !")

print("Le nombre secret était :", nombre_secret)
print("Score :", score)
