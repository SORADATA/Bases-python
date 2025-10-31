df = "   nom: POMME GOLDEN   prix_unit : 0.99 qte: 150   "
print(f"Original: '{df}'")

#### Etape 1 : Nettoyage et standardisation 

# La correction est ici : on sauvegarde le résultat de .strip()
# puis on sauvegarde le résultat de .lower()
df_clean = df.strip()
df_clean = df_clean.lower()

# (On peut aussi l'écrire en une seule ligne :)
# df_clean = df.strip().lower()

print(f"Nettoyé : '{df_clean}'")


#### Etape 2 : Extraction des données via l'indexation et le slicing 

# 1. Trouver les positions :


start_nom = df_clean.find("nom:")
print(f"Index nom: {start_nom}")

start_prix = df_clean.find("prix_unit :")
print(f"Index prix: {start_prix}")

start_qte = df_clean.find("qte:")
print(f"Index qte: {start_qte}")


# 2. Extraire les valeurs (Slicing) :

# Pour nom : Debut = "nom:" (len 4) et Fin = start_prix
nom_brut = df_clean[start_nom + 4 : start_prix]

# Pour prix_unit : Debut = "prix_unit :" (len 11) et Fin = start_qte
# (il faut compter 11, car il y a un espace avant le :)
prix_brut = df_clean[start_prix + 11 : start_qte]

# Pour qte: Debut = "qte:" (len 4) et Fin = jusqu'au bout
qte_brut = df_clean[start_qte + 4 : ]

# Affichage dynamique
print("--- RESULTATS BRUTS ---")
print(f"Nom brut extrait: '{nom_brut}'")
print(f"Prix brut extrait: '{prix_brut}'")
print(f"Quantité brut extraite: '{qte_brut}'")


#### Etape 3 : Conversion de types 

# 1. Nettoyer les valeurs brutes 

nom_brut = nom_brut.strip()
prix_brut = prix_brut.strip()
qte_brut = qte_brut.strip()


# 2. Conversiondes variables

prix_brut = float(prix_brut)
qte_brut = int(qte_brut)

# 3. Mettre le la var nom_brut en Maj

nom_brut = nom_brut.upper()


#### Etape 4 : Calculs des opérateurs python 

# 1. definissons les taxes  :

taux_tva = 0.05

# 2. Calculons les taux 

total_ht = prix_brut * qte_brut

montant_tva = total_ht * taux_tva

total_ttc = total_ht + montant_tva

# Affichage dynamique 

print(f"Produit : '{nom_brut}'")
print(f"Total HT : '{montant_tva}'")
print(f" Total TTC : '{total_ttc}'")


#### Etape 5 : Formatage pour le rapport final : Affichez un ticket propre

# 1. Utilisez print() et f"string ou la méthode du format   :

print("******** TICKET DE CAISSE *********")
print(f"Produit :'{nom_brut}")
print(f"Quantité : '{qte_brut}")
print(f"Prix Unitaire : '{prix_brut}€")
print("-----------------------------------")
print(f"Total HT :'{total_ht:.2f}€")
print(f"TVA (5.0%) :'{montant_tva:.2f}2€")
print(f"TOTAL TTC : '{total_ttc:.2f}€")
print("***********************************")

from PIL import Image, ImageDraw, ImageFont


# SIMULATION DES VAR
nom_brut = "POMME GOLDEN"
qte_brut = 150
prix_brut = 0.99
total_ht = 148.5
montant_tva = 7.425
total_ttc = 155.925
# --- FIN : Simulation de vos variables ---



texte_ticket = f"""
******** TICKET DE CAISSE *********

Produit : {nom_brut}
Quantite : {qte_brut}
Prix Unitaire : {prix_brut:.2f} €
-----------------------------------
Total HT : {total_ht:.2f} €
TVA (5.0%) : {montant_tva:.2f} €
TOTAL TTC : {total_ttc:.2f} 

***********************************
"""

img_largeur = 400
img_hauteur = 250
img = Image.new('RGB', (img_largeur, img_hauteur), color='white')
d = ImageDraw.Draw(img)


try:
    
    font = ImageFont.truetype("DejaVuSans.ttf", size=15)
except IOError:
    # Si elle n'est pas trouvée, utiliser la police par défaut
    print("Police non trouvée, utilisation de la police par défaut.")
    font = ImageFont.load_default()

# 4. "Dessiner" le texte sur l'image
#    (10, 10) sont les coordonnées x, y où commencer
d.text((10, 10), texte_ticket, fill='black', font=font)



# 5. Sauvegarder l'image
img.save('ticket_de_caisse.png')

print("Félicitations ! L'image 'ticket_de_caisse.png' a été créée.")
print("Regardez dans l'explorateur de fichiers de VSCode.")