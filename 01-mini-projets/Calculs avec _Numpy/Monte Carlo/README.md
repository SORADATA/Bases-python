# Projet : Simulation de portefeuille d'Actions (Monte-Carlo)

##  Mission  

> Vous êtes un data scientist travaillant le département risque d'une banque comm, vous etes amener a faire une simulation de la valeur future d'un portefeuille boursier sur +sieurs jours.

> L'objectif est d'explorer les fonctionalités de numpy.
> ### Compétence demandée :  np.array, np.arange, for

````python

import numpy as np
# Paramètres de la simulation
NB_JOURS = 252  # Jours de trading
NB_ACTIONS = 5  # Actions dans le portefeuille
PRIX_INITIAL = 100 # Prix de départ pour chaque action
rendements = np.random.normal(loc=0.002, scale=0.01,size=(NB_JOURS, NB_ACTIONS))


