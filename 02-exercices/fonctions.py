# Les fonctions 

def accueil(prenom):
    msg = "Salutations " + prenom + "!"
    return msg

A = accueil("Miranda")
print(A)


def addition(x, y):
    return x + y

a = addition(2, 2)
print(a)

# Les variables globales
x = 5 
"""Ici x est notre var globale"""
def ajoute(y):
    return x + y
print(ajoute(6))


def ajoute(y):
    z = 5
    """Ici z est notre var locale"""
    return z + y
resultat = ajoute(6)
print(resultat)