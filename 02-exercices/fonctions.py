# Les fonctions 

def accueil(prenom):
    """
    def permet d'initier une fonction python ici accueil
    - prenom est le paramètre d'entrée 
    - msg est l'action qui est executé via l'instruction return
    - A est le résultat attendu qui renvoie une sortie.

    """
    msg = "Salutations " + prenom + "!" 
    return msg

A = accueil("Miranda")
print(A)


def addition(x, y):
    return x + y

a = addition(2, 2)
print(a)

# Les arguments obligatoires et optionnels

def concat_string(str1, str2, sep=""):
    return str1 + sep + str2
print(concat_string("bonjour", "bonjour")) # Ici le comportement par défaut

print(concat_string("bonjour", "bonjour", sep=",")) # Ici le comportement est modifié 

# Renvoyer plusieurs résultats 

def puissances(x):
    return x**2, x**3, x**4
a, b, c = puissances(2)
print(a, b, c)

def calcultrice_heure(total_secondes):
    minutes = total_secondes // 60
    secondes_restantes = total_secondes % 60

    return minutes,   secondes_restantes

m, s = calcultrice_heure(150)

print(f"Total de 150 secondes équivaut à :")
print(f"Minutes : {m}")
print(f"Secondes : {s}")


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