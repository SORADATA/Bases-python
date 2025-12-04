from __future__ import annotations

class Compte:
    """
    Compte est ma classe principale avec deux attributs
    ci-dessous
    """
    def __init__(self, titulaire: str, solde: float):
        self.titulaire = titulaire
        self.solde = solde
    def __str__(self) -> str:
        """
       Pour voir la desc de la classe
        """
        return f"Le solde du compte {str(self.titulaire)} est de {str(self.solde)} €"
    def __add__(self, autre_compte: Compte) -> float:
        return self.solde + autre_compte.solde

    def depot(self, montant: float) -> None:
        self.solde += montant
    def retrait(self, montant: float) -> None:
        """
        Une méthode pour gérer les retaits
        """
      
        if montant <= self.solde:
            self.solde -= montant
            print("Retrait accepté")
        else:
            print("Retrait refusé :fonds insuffisants")

    def transfert(self, destinataire: Compte, montant: float) -> None:
        """
        Une méthode transfert avec deux paramètres

        """
        if self.solde >= montant:
            destinataire.solde += montant
            self.solde -= montant
        else:
            print("Transfert refusé : fonds insuffisants.")

# Créons deux (2) clients
client1 = Compte("Bernard", 2000)
client2 = Compte("Bianca", 5000)

print("--- Soldes initiaux ---")

print(client1)
print(client2)

print("\n--- Dépôt, Retrait et Affichage ---")

client1.depot(1000)
print(client1) # Affiche le nouveau solde

client1.retrait(10000) # Test refusé
print(client1)

client2.retrait(100)
print(client2)

print("\n--- Test de Surcharge d'Opérateur  ---")
solde_total = client1 + client2
print(f"Solde total du ménage (client1 + client2) : {solde_total:.2f} €")

print("\n--- Test de Transfert ---")
client2.transfert(client1, 200)

print(client1)
print(client2)

print("\n--- Test de Transfert Refusé ---")
client2.transfert(client1, 10000) # Test refusé