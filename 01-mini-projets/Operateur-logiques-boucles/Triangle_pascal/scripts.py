# Initialisation et saisie utilisateur

nbre_lignes = int(input("Merci d'entrer le nombre de lignes"))
triangle = []# liste vide pour stocker toutes les lignes

# Logique de génération (boucles imbriquées)

# une noucle qui itère de 0 jusqu'à nbre_lignes -1

for lignes in range(nbre_lignes):

    ligne_actuelle = [1] # Init d'une liste avk le nbre 1 car les lignes de la triangle commence par 1

    if lignes > 0:

        """ 
        Ici c'est la condition de calcul si la personne n'est pas à la 1ere ligne
        
        """
        ligne_precedente = triangle[-1] # Afin de recup la dernière ligne stockée dans triangle
        # Boucle pour calculer les éléments intérieurs
        # Elle itère de 1 jusqu'à l'avant-dernier élément de la ligne précédente
        for elements in range(len(ligne_precedente), -1):
            """Boucle interne pour les calculs"""
            # La somme de l'élément courant et suivant dans la ligne précéd
            somme = ligne_precedente[elements] + ligne_precedente[elements+1] 
        #  Ajout cette somme à la ligne_actuelle en cours de construction. 
            ligne_actuelle.append(somme)
    ligne_actuelle.append(1)# Car toutes les lignes de terminent à 1
    triangle.append(ligne_actuelle) #Ajout de la ligne_actu complete à la liste triangle

for ligne in triangle:
    """ conversion nbre en str puis avec la, méthode pour centrer la chaine de carac à 40"""
    nbre_lignes = str(nbre_lignes)
    print(" ".join(map(str, ligne)).center(40))