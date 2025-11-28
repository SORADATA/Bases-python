# Listes de ref 
  
produits = ["Aspirateur", "Mixeur", "Casserole"]
mois = ["janv", "Fév", "Mars", "Avr", "Mai", "Juin"]
ventes_aspirateur = [100, 120, 230, 240, 1500, 1600]
ventes_mixeur = [200, 300, 100, 120, 130, 300]
ventes_casserole = [123, 1400, 474, 700, 560, 300]

toutes_les_ventes = [ventes_aspirateur, ventes_mixeur, ventes_casserole]
resultats_analyse = {} # dict vide afin de stocker les résultats agrégés pour chaque produit

# Boucle principale

print("*************** ANALYSES DES VENTES **********************")

for i,  prd in enumerate(produits):
    """ Afin d'obtenir l'indice i et le nom du produit pour l'iteration actuelle"""
    ventes_actuelles = toutes_les_ventes[i]
    total_ventes = 0
    meilleure_vente_montant = -1 # Afin de s'assurer que le 1er mtnt soit enrégistré
    meilleure_vente_mois = " "

# Boucle interne 

    for montant, nom_mois in zip(ventes_actuelles, mois):
        """ Associe et traite le mntnt et le n.mois corrpdnd à chaque tour"""
        # 1. Calcul du total des ventes

        total_ventes += montant

        # 2. Trouver le mois avec la meilleure vente

        if montant > meilleure_vente_montant:
            """
            Si cette cond est vraie :
            alors maj meilleure_vente_mtnt et
             meilleure_ventes_mois par les valeurs actuelles
             
             """

            meilleure_vente_montant = montant
            meilleure_vente_mois = nom_mois
    # Stockage des résultats dans le dic resultats analyse

    resultats_analyse[prd] = {
      "Total": total_ventes,
      "Meilleur mois": meilleure_vente_mois,
      "Montant Max":  meilleure_vente_montant
    }

    resultats_triers = sorted(
        resultats_analyse.items(),
        key=lambda item: item[1]['Total'], # Tri-moi en regardant la Valeur du Total
        reverse=True  #Classe du grand au plus petit
    )


# Afiichage des results

for produit, donnees in resultats_triers:
    print(f"\nproduit : **{produit}**")
    print(f" Ventes totales (6 mois) : {donnees['Total']} unités ")
    print(f" Meilleures mois de vente: {donnees["Meilleur mois"]} ({donnees["Montant Max"]} unités)")







