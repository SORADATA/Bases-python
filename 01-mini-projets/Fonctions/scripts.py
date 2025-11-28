# Variab globale
prix_penalite_jour = 0.50

def verifier_livre(titre_recherche, jours_retard=0):
    inventaire_bibliotheque = [
       {"titre": "L'Étranger", "auteur": "Camus", "stock": 5, "annee": 1942},
       {"titre": "1984", "auteur": "Orwell", "stock": 3, "annee": 1949},
       {"titre": "Dune", "auteur": "Herbert", "stock": 0, "annee": 1965}
    ]
    """
    Ici 2 arguments (parametre):
     1. Argument obligatoire
     2. Argument optionnel

    """
    # Ici commence la boucle intern
    for livre in inventaire_bibliotheque:
        if livre["titre"] == titre_recherche:
            """
            Si le titre_livre = titr recherché alors vérifie le stock (ci-dessous)

            """

            if livre['stock'] > 0:
                return f"le livre {livre["titre"]} est disponible en {livre["stock"]} exemplaires"
            else:
                """
                Si la condit° du haut pas respecté : stock_livre == 0 alors
                calcul la pena_totale et return que le divre est indispo
                
                """
                penalite_totale = prix_penalite_jour * jours_retard
                return (f"le livre {livre['titre']} est indisponible (rupture de stock)."
                        f"la pénalité de {jours_retard} jours de retards est de {penalite_totale}€")             
    return f"le livre {livre['titre']}, n'est pas dans l'inventaire.Merci de réessayer ! "
# Tests 
A = verifier_livre("L'Étranger", 10)
B = verifier_livre("1984")
C = verifier_livre("Dune", 5)
print(A)

print()

print(B)

print()

print(C)