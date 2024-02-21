# Un peu de pratique

Maintenant que l'on sait tout ça, pourquoi ne pas passer à la partie pratique ?

## Les instructions utiles :
- SELECT : sert à sélectionner des données dans une base de données
- FROM : sert à désigner de quelle base de données on va prendre les données
- WHERE : sert à filtrer les données que l'on veut récupérer de notre base de données
- ORDER BY : sert à ordonner nos données sélectionnées

# Exercice

Nous avons une base de données bien remplie et plutôt que de regarder les mots de passe pour chaque `id`, je peux juste récupérer le mot de passe `password` de l'utilisateur `FLAG`.
On utilisera ici la base de données `users`.
*Ecris la requête SQL qui va permettre de récupérer le Flag*

<script src="https://cdn.jsdelivr.net/npm/alasql"></script>

<script src="resources/script/script.js"></script>

<input type="text" id="sqlTable" required minlength="4" maxlength="64" size="64" />
<button onclick="request()">Envoyer la requête SQL</button>

<input type="text" id="sqlFlag" required minlength="4" maxlength="32" size="32" />
<button onclick="validate()">Valider le Flag</button>