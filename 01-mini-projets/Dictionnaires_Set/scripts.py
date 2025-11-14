# Rtape 1 : Création de catalogue de produits

catalogue = {
    "pomme": 0.5,
    "banane": 0.3,
    "orange": 0.4,
    "lait": 1.2,
    "pain": 0.9
}

print(f"catalogue initial {catalogue}")

# Etape 2 : Création d'un panier vide (Set)

panier = set([])

print(type(panier))

# Ici un set est recommandé car le set est immutable cad non modifiable , donc nous permet d'avoir une unicité de notre panier

# Etape 3 : Ajout des produits au panier (set)

panier.add("pomme")
panier.add("lait")
panier.add("pomme")
print(panier)

# Etape 4 : Le client cnahge d'avis 

# Il souhaite plus du lait 

panier.remove("lait")
print(panier)  # Voici le maj


# Etape 5 : Calculer le total (Dictionnaire + Set)

total = 0
for i in panier:

    prix_article = catalogue[i]
     
    total += prix_article

print(f"le total du panier est : {total:.2f} €")


# Bonus : Articles en promotion (Opérations de Set)


# Créer un nouveau set 

promo_fruits = set([
    "pomme",
    "orange",
    "banane"]
)

produits_promo = panier.intersection(promo_fruits)
"""Ou encore cette via cette méthode """
produits_promo = panier & promo_fruits

print(produits_promo)
# On voit que c'est pomme qui fait partie de la promo
