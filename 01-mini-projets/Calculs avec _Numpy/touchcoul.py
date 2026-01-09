import numpy as np
# Touché-coulé
# Grille de 5*5 est définie dans la cellule svte comme etant un array

X = np.array([[1, 1, 1, 0, 0], [0, 0, 0, 0, 1], [1, 0, 0, 0, 1],
              [1, 0, 0, 0, 0], [0, 1, 1, 1, 1]])
print(X)

def shoot(x, y):
    """
    x = indice de la ligne
    y = indice de la conne
    """
    if np.any(X == 1):
        if X[x, y] == 1:
            print("Touché !")
            X[x, y] == 2
        else:
            print("Raté !")
        print(X)
        print()
    else:
        print("Fin de partie ! ")
shoot(0, 1)
shoot(1, 0)
shoot(0, 2)

