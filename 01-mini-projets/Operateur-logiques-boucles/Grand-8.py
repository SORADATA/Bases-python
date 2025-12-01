

# Projet : Contrôleur d'Accès du Grant Huit


# Etape 1 : Collection des données

age_str = input("Quel est votre âge ?  ")
age = int(age_str)

taille_str = input(" Quel est votre taille ")
taille = int(taille_str)

Pass_VIP = input("Disposez-vous d'un pass VIP (oui/non) ?  ")

a_le_pass = (Pass_VIP.lower() == "oui")

# Etape 2 : Les règles

# Refus absolu (Taille)
if taille < 140:
    print("Accès refusé : Taille minimimale de 140 cm requise")
elif age < 12 and not a_le_pass:
    print("Accès refusé : Âge minimum 12 ans (ou Pass VIP requis).")
else:
    print("Accès autorisé. Bienvennue sur le Dragon de Feu !")
