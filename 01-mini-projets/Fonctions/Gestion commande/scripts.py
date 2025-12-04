# Typage pour la Gestion de Commande
#from typing import Dict, List, Any : Pas nécessaire ici 

# 1. Fonction de calcul
def calculer_prix_total(quantite: int, prix_unitaire: float) -> float:
    prix_total: float = quantite * prix_unitaire
    return prix_total

# 2. Fonction de vérification
def verifier_statut_commande(statut_client: str, commande_terminee: bool) -> str:
    if commande_terminee and statut_client == "Premium":
        return "Commande prête : Envoi prioritaire."
    elif commande_terminee:
        return "Commande prête : Envoi standard."
    else:
        return "Commande en attente de préparation."


# --- Tests (Ces lignes sont nécessaires pour l'affichage !) ---
print("--- Test de prix total ---")
# Appel de fonction et affichage du résultat
resultat_prix = calculer_prix_total(5, 12.50)
print(f"Prix total (5x12.50): {resultat_prix}")

print("\n--- Tests de statut de commande ---")
# Appel de fonction et affichage du résultat
print(f"Premium: {verifier_statut_commande('Premium', True)}")
print(f"Basic: {verifier_statut_commande('Basic', True)}")
print(f"Premium: {verifier_statut_commande('Premium', False)}")