# Projet : Gestionnaire de carte bancaire

##  Mission  

> Vous êtes un data scientist au sein d'une banque commerciale.

> L'objectif est de mettre en place un gestionnaire de compte bancaire afin de gérer la clientèle de la banque. 

- Class compte : afin d'avoir deux attributs (titulaire et solde) , une méthode(affiche_solde) etc......

Voici les données de départ  :

```python
  
class Compte:
    """ Ma class Compte avec ses attributs et objets"""
    def __init__(self, titulaire, solde):
        self.titulaire = titulaire
        self.solde = solde
