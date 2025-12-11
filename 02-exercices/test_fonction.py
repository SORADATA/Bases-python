# Super calcumatrice de statistiques

def analyse_rapide(liste_nombres):
    # liste_nombres = int(liste_nombres)
    somme = sum(liste_nombres)
    compte = len(liste_nombres)
    Moyenne = somme / compte
    return (somme, compte, Moyenne)
notes = [10, 15, 8, 17, 20]
A = analyse_rapide(notes)
print(A)


# Convertisseur de température

def convertir_temps(valeur, vers="C"):
    if vers == "C":
        """
        La fonction doit convertir la température de Fahrenheit en Celsius.


        """
        resultat = (valeur - 32)*(5/9)
        return resultat
    elif vers == "F":
        resultat = (valeur*9/5)+32
        return resultat
    else:
        return "Erreur : Spécifiez 'C' ou 'F' pour la conversion."

A = convertir_temps(68, vers="C")
print(f"68°F équivaut à {A:.2f}°C") # Résultat : 20.00°C

# Test 2 : De Celsius à Fahrenheit
B = convertir_temps(25, vers="F")
print(f"25°C équivaut à {B:.2f}°F") # Résultat : 77.00°F

