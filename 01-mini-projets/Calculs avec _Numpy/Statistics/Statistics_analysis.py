import numpy as np
data = np.random.normal(size=(1000, 5))
# Afficha init
print("-----1. Matrice des données (Array)-----")
print(data)
print(type(data))

# Calculs globaux
moyenne = np.mean(data)
ecart_type = np.std(data)
minimum = np.min(data)
maximum = np.max(data)

print("\n--- 2. Statistiques Globales ---")

print(f"Moyenne Globale : {moyenne: .4f}")
print(f"ecart-type Global : {ecart_type:.4f}")
print(f"Minimum: {minimum: .4f}")
print(f"Maximum: {maximum: .4f}")

# Analyse par variable (colonne)
# Calculons la moyenne de chaque colonne : 5 col
moy_col = np.mean(data, axis=0)
# Moyenne de chaque observation (ligne) : 1000 résultats
moy_obs = np.mean(data, axis=1)
print("\n--- 3. Analyse par Axe (Axis) ---")
print(f"Moyenne par colonne (axis=0, 5 résultats) : {moy_col}")
print(f"Moyenne par ligne (axis=1, 1000 résultats, affichage des 5 premiers) : {moy_obs[:5]}")