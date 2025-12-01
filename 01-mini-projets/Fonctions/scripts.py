from typing import List, Dict, Any

# Variab globale
# CORRECTION 1: Annotation de type correcte pour 'float'
prix_penalite_jour: float = 0.50

# Inventaire global
inventaire_bibliotheque: List[Dict[str, Any]] = [
    {"titre": "L'Étranger", "auteur": "Camus", "stock": 5, "annee": 1942},
    {"titre": "1984", "auteur": "Orwell", "stock": 3, "annee": 1949},
    {"titre": "Dune", "auteur": "Herbert", "stock": 0, "annee": 1965}
]

def verifier_livre(titre_recherche: str, inventaire: List[Dict[str, Any]]) -> str:

    for livre in inventaire:
        if livre["titre"] == titre_recherche:
            if livre['stock'] > 0:
                # Note : Les guillemets internes sont des doubles "" pour éviter une erreur
                return f"Le livre {livre['titre']} est disponible en {livre['stock']} exemplaires"
            else:
                return (f"Le livre {livre['titre']} est indisponible (rupture de stock).")

    # CORRECTION 2: Si la boucle se termine, utilisez titre_recherche (pas livre)
    return f"Le livre **{titre_recherche}** n'est pas dans l'inventaire. Merci de réessayer ! "

def montant_penalite(jours_retard: int) -> str:
    penalite_totale: float = prix_penalite_jour * jours_retard
    # Utiliser :.2f pour afficher deux décimales pour l'argent
    return f"La pénalité pour {jours_retard} jours de retards est de {penalite_totale:.2f}€"

# Tests corrigés
print("--- Tests de vérification de livre ---")
# CORRECTION 3: Appel correct avec l'inventaire
A = verifier_livre("L'Étranger", inventaire_bibliotheque)
B = verifier_livre("1984", inventaire_bibliotheque)
C = verifier_livre("Dune", inventaire_bibliotheque)
# Test de livre non trouvé
E = verifier_livre("La Peste", inventaire_bibliotheque) 

print(f"A (Disponible): {A}")
print(f"B (Disponible): {B}")
print(f"C (Indisponible): {C}")
print(f"E (Non trouvé): {E}")

print("\n--- Test de pénalité ---")
D = montant_penalite(10)
print(f"D (Pénalité pour 10j): {D}")