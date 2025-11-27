# Projet : Gestionnaire de  Livres

##  Mission  

> Vous êtes un data scientist au sein de la biblio nationale François Mitterand. 

> L'objectif est de créer une fonction pour gérer l'inventaire des livres, en utilisant la variable globale du prix de pénalité de retard. 

> ### Compétence demandée :  def , if/elif/else, dictionnaire  

Voici les données de départ  :

```python

# Variab globale 

inventaire_bibliotheque = [
    {"titre": "L'Étranger", "auteur": "Camus", "stock": 5, "annee": 1942},
    {"titre": "1984", "auteur": "Orwell", "stock": 3, "annee": 1949},
    {"titre": "Dune", "auteur": "Herbert", "stock": 0, "annee": 1965}
]
def verifier_livre(titre_recherche, jours_retard=0 ):
    """
    Ici 2 arguments (parametre):
     1. Argument obligatoire
     2. Argument optionnel

    """