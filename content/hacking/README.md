---
hidden: true
---

# How it works ?



## Part 1 : Check

Source code

Il n'y a pas de flag ici, il suffit juste de regarder le code source et d'activer le boutton


## Part 2 : Check

Ascii to Flag

On nous donne explicitement le flag et en plus on nous dit qu'il faut convertir ce qui est à l'intérieur grâce à la table ASCII

Flag : Prologin


## Part 3
http://alasql.org/


On utilise la lib : *Alasql*

On génère une BDD
Et comme le sujet nous donne si bien la réponse, on doit entrer la requête `SELECT val FROM users WHERE id="FLAG"`

Flag : PostgreSQL


## Part 4 : Pas implem
Bon je peux rajouter cette partie en vrai 

But de l'exo : on a aussi une base de donnée mais bizarrement, quand on order by X, on peut lire un flag 

Enter that SQL statement : "SELECT id FROM USER ORDER BY"

## Part 5


Stégano :D

On nous donne un échange entre George Sand et Alfred de Musset et le but des de décoder leurs petits messages
Indice : lire les premiers mots de chaque vers

Flag : Cette nuit (peut-importe l'ecriture, la fonction de verif met la string en MAJ)


## Part 6 : Check
Enter a command in the web-browser

Petit jeu de piste pour revenir en arrière : Revenir à la première URL de SQL -> start et la réponse est là

Flag : Keanu_Reeves

## Part 7 : Check
Read the local-Storage
```
++++++++++[>+>+++>+++++++>++++++++++<<<<-]>>>>+++++++++++++++++++++++.------------.++++.----------.+++++.++++++.+++++++++.
```
Indice : Meep Meep ;)

C'est du RoadRunner, et il faut chercher comment le convertir en brainfuck pour ensuite l'exec et trouver le flag

Here is a converted brainfuck code to RoadRunner :(
Expected Output : 
- {osint}
Flag : osint

## Part 8 : Check
Osint
OMG IT IS KRAKOW
Indice : EXIF_DATA

Flag : Dorks

## Part 9
Osint

## Part 10
