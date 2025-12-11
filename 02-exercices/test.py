import numpy as np
 
# 1. Initialisation
np.random.seed(42)  # Pour la reproductibilité
temperatures = np.random.randint(-5, 36, size=(10, 5))
stations = np.array(["Paris", "Lyon", "Marseille", "Bordeaux", "Lille"])
 
# 2. Manipulation de base
print("Températures du 3ème jour :", temperatures[2, :])
print("Températures de Lyon :", temperatures[:, 1])
 
# 3. Calculs statistiques
moyennes = np.mean(temperatures, axis=0)
print("Moyennes par station :", moyennes)
 
# 4. Algèbre linéaire
coeffs = np.random.rand(5, 3)
resultat = temperatures.T @ coeffs
 
# 5. Masques booléens
temperatures[temperatures < 0] = 0
etiquettes = np.where(temperatures > 30, "Canicule", "Normal")
 
# 6. One Hot Encoding
categories, pos = np.unique(stations, return_inverse=True)
ohe = np.zeros((len(stations), len(categories)))
ohe[np.arange(len(stations)), pos] = 1
print("One Hot Encoding :\n", ohe)