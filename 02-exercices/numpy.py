import numpy as np

# -----------------Manipulations simples des données d'un Dataframe-----------------------

X = np.arange(10, 21)

print(X)

# Sélectionner les éléments aux positions 1, 3 et 4
print(X[[1, 3, 4]])
# Selct tous les élements sauf le premier
print(X[1:])
# select tous les élmts sauf le premier et le dernier
print(X[1:-1])
# selct les 3 premiers elmts
print(X[:3])
# selct les 5    derniers elmets
print(X[-5:])
# slct tous les élmts pairs
print(X[::2])
#slectionner tous les elmmts en les triant dans l'ordre inverse
np.flip(X)
print(X[::-1])

# -----------------Sélectionner des éléments dans une matrice -----------------------

# Una mat de taille 5x5 comprennat tous les entiers [0, 24]
# slct la valeur 19
Y = np.arange(0, 25).reshape((5, 5)) # permet de redimensionner un tableau NumPy sans modifier ses données, mais en changeant sa structure (nombre de lignes et de colonnes).
print(Y)
# selectionner la valeur 19
print(Y[3, 4])
# slct la 2e ligne
print(Y[1, :])
# slct la 4e colonne
print(Y[:, 3])
# slct la sous-matrice 3*3  centrale
print(Y[1:4, 1:4])
# slct les éléments diagonaux
print(np.diag(Y))
print(Y[np.arange(0, 5), np.arange(0, 5)])

# ----------------- Un peu de calcul --------------------------------------------------
# Deux matrices carrées de taille 3*3 sont définies sous forme d'arrays nUMPY

X = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])

Y = np.array([[10,11,12],
              [13,14,15],
              [16,17,18]])
print(X)
print()
print(Y)

# multiplier tous les élements de X par 3
print(3*X)

# diviser les éléments de Y par ceux de X
print(Y/X)
print()
# passer tous les élements de Y au log
print(np.log(Y))
# passer tous les éléments de X au carré
print()
print(np.square(X))
# faire une multiplication matricielle de X et Y
print()
print(X @ Y)
print()
# transposer la matrice Y
print(np.transpose(Y))
print()
print(Y.T)

# ----------------- Initalisation d'arrays de diverses natures --------------------------------------
# Initailisation d'arrays de diverses natures
print(np.zeros((3,2)))

# un vectuer , contenant 18 fois la valeur 1
a = np.ones(18,)
print(a)

# un array à 3 dimensions, respectivement de tailles 2, 3 et 5, contenant uniquement des zéros (fonction np.zeros)
b = np.zeros((2, 3, 5))
print(b)
print()

# une matrice (array à 2 dimensions), à 4 lignes et 3 colonnes, contenant uniquement la valeur 5 (fonction np.full)

c = np.full((4, 3), fill_value=5)
print(c)
print()

# ----------------- Tirage d’un vecteur selon une loi normale--------------------------------------
X = np.random.normal(0, np.sqrt(2), 10000)

print(np.mean(X), np.var(X))

X = np.array([[1, 1, 1, 0, 0], [0, 0, 0, 0, 1], [1, 0, 0, 0, 1],
              [1, 0, 0, 0, 0], [0, 1, 1, 1, 1]])

def shoot(x, y):
    if np.any(X == 1):
        if X[x, y] == 1:
            print("Touché !")
            X[x, y] = 2
        else:
            print("Raté !")
        print(X)
        print()
    else:
        print("Fin de partie !")

shoot(0, 1)
shoot(1, 0)
shoot(0, 2)