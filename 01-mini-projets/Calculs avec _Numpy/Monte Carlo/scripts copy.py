import numpy as np



# Paramètres de la simulation
NB_JOURS: int = 252
NB_ACTIONS: int = 5
PRIX_INITIAL: float = 100 # car une val monétaire

# Création de la matrice des rendements
rendements = np.random.normal(loc=0.002, scale=0.01, size=(NB_JOURS, NB_ACTIONS))

# Transformation des rendements en multiplicateurs
multiplicateurs = 1 + rendements

# Calcul de l'évolution des prix au fil des jours (CORRIGÉ)
prix_simules = PRIX_INITIAL * np.cumprod(multiplicateurs, axis=0)

print("\n--- MATRICE DE PRIX SIMULÉS (Prem. 5 Jours) ---")
print(prix_simules[:5])

# -----------------------------------------------------------------
# CALCULS STATISTIQUES
# -----------------------------------------------------------------

print("\n-------------CALCULS GENERAUX (Sur tous les rendements)------------------")
moyenne = np.mean(rendements)
ecart_type = np.std(rendements)
print(f"Moyenne Globale: {moyenne:.6f}")
print(f"Écart-type Global: {ecart_type:.6f}")

print("\n-------------ANALYSES PAR ACTION (axis=0)------------------")
# Moyenne par colonne (performance de chaque action)
moy_par_action = np.mean(rendements, axis=0) 
# Écart-type par colonne (volatilité/risque de chaque action)
sd_par_action = np.std(rendements, axis=0) 
print(f"Moyenne par action (5 résultats): {moy_par_action}")
print(f"Volatilité par action (5 résultats): {sd_par_action}")

# -----------------------------------------------------------------
# ANALYSE DE RISQUE (Masques Booléens)
# -----------------------------------------------------------------

print("\n----------- ANALYSES DU RISQUE (Masques Booléens)------------")

# 1. Création du Masque Booléen 
SEUIL_RISQUE: float = -0.02 # Perte de plus de 2%
masque_risque = rendements < SEUIL_RISQUE

# 2. Compter le nombre total de jours de risque (True est compté comme 1)
jours_risque_total = np.sum(masque_risque)
print(f"Masque créé (True si rendement < -0.02) : {masque_risque.shape}")
print(f"Nombre total de jours de krach (rendement < -2%) : {jours_risque_total}")

# 3. Identifier l'action la plus risquée (axis=0)
# On somme verticalement (axis=0) pour compter les "True" par colonne
jours_risque_par_action = np.sum(masque_risque, axis=0)
action_plus_risquee_index = np.argmax(jours_risque_par_action)

print(f"Jours de risque par action : {jours_risque_par_action}")
print(f"Action la plus risquée (Index): {action_plus_risquee_index}")


