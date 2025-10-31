


# Etape 1 : Creation de ma bibliothèque

ma_biblio = []  # Une liste vide


# Création des tuples

livre1 = ("Pensez pour moi même", "Marc Aurele")

livre2 = ("Les damnés de la terre", "Franz fanon")

livre3 = ("Les miserables", "Victor hugo")

# Ajout des trois livres à ma biblio

ma_biblio.append(livre1)

ma_biblio.append(livre2)

ma_biblio.append(livre3)

# Etape 2 : Affichage de ma collection

print(".......Ma bibliotèque.......")

print(ma_biblio)

print(f"J'ai dispose {len(ma_biblio)} livres")


# Etape 3 : Sélection de livres spécifiques

premier_livre = ma_biblio[0]

print(f"mon premier livre est {premier_livre}")

deuxieme_livre = ma_biblio[1][1]

print(f"L'auteur de mon deuxième livre est {deuxieme_livre}")

# Etape 4 : Rétirer un livre

# Vous avez prêté un livre et il n'est jamais revenu. Utilisez la méthode .pop() ou

# .remove() pour supprimer l'un des livres de votre liste.

 

livre_prete = ma_biblio.pop(2)


print(f"Mon livre preté est {livre_prete}")

 

print(ma_biblio)

 

# Bonus : Immutabilité

 

# ma_biblio[0][0] = "Un autre titre"

# print(ma_biblio)  # Erreur car il s'agit d'un tupples donc impossible de'être modifier

 

# Bonus 2 : Trier ma biblio

 

# La biblio est en désordre alors met la en ordre par alphabet

ma_biblio.append(("Fondation", "Isaac Asimov"))

ma_biblio.sort()

print("*********BIBLIOTHEQUE*****************")

print(f"Je vous présente ma bibliothèque {ma_biblio}")