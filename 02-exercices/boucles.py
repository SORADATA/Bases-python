# Exercices boucle for :

B = [1, 2, 3, 4, 5]
for i in B:
    print(f"voici mes numéros : {i}")
print()

C = 10
for i in range(10):
    print(f"voici tes numéros : {i}")

for annee in range(1, 11):
    print(f"Année : {annee}")

for nombre_pair in range(0, 10, 2):
    """compter par pas de 2"""
    print(f"voici le boucle for avec 3 éléments : {nombre_pair}")

for decompte in range(10, 0, -1):
    """ Compter à rebours cad compter du plus grand au plus petit"""
    print(f"voici {decompte}")

villes = ["Lille", "Metz", "Angers", "Paris", "Toulouse"]
for index, ville in enumerate(villes):
    """ Méthode built-in : fonction enumerate"""
    print(f"A l'indice {index}, la ville est {ville}")

 
for rang, produit in enumerate(["cafe", "chocolat", "thé"], start=1):
    print(f"Le produit n° {rang} est le {produit}")

noms = ["Alice", "Benoit", "Cedric"]
scores = [95, 80, 10]
statuts = ["Validé", "En cours de validation", "Echec"]

for nom, score in zip(noms, scores):
    """la fonction zip permet d'avoir 2 conditions a l'intérieur d'une boucle"""
    print(f"{nom} a obtenu un score de {score} / 100 ")

for nom, score, statut in zip(noms, scores, statuts):
    """Avec trois conditions a l'intérieur d'une boucle for"""
    print(f"{nom} a obtenu un socre de {score}/100, a donc le statut {statut} ")

# Boucle While
i = 1 
while i <= 5:
    print(i)
    i = i+1

votre_prenom = "Romain"
while True:
    #print("-------Veuillez entrer votre prénom------")
    prenom = input()
    if prenom == votre_prenom:
        break
#print(f"Bienvenue {votre_prenom}")

i = 0
while i <= 5:
    for j in range(5):
        if j == 2:
            print("Break.")
            break
    i += 1


votre_prenom = "Romain"

while True:
    print("Veuillez entrer votre prénom")
    prenom = input()
    if prenom != votre_prenom:
        continue
    print("Veuillez entrer votre mot de passe")
    mdp = input()
    if mdp == "lemotpasse":
        break
print(f"Bonjour {votre_prenom}, bienvenue !")



