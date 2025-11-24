class Compte:
    """
    Compte est ma classe principale avec deux attributs 
    ci-dessous
    """
    def __init__(self, titulaire, solde):
        self.titulaire = titulaire
        self.solde = solde
    def affiche_solde(self):
        """
        Une méthode affiche_solde
        """
        print(f"Le solde du compte {str(self.titulaire)} est de {str(self.solde)} €")
    def depot(self, montant):
        self.solde += montant
    def retrait(self, montant):
        """
        Une méthode pour gérer les retaits
        """
      
        if montant <= self.solde:
            self.solde -= montant
            print("Retrait accepté")
        else:
            print("Retrait refusé :fonds insuffisants")

    def transfert(self, destinataire, montant):
        """
        Une méthode transfert avec deux paramètres

        """
        if self.solde >= montant:
            destinataire.solde += montant
            self.solde -= montant
        else:
            print("Transfert refusé : fonds insuffisants.")

# Créons deux (2) clients afin de tester que les diff fonctionnalités
# à implémenter marchent comme prévu

client1 = Compte("Bernard", 2000)
client2 = Compte("Bianca", 5000)

client1.affiche_solde()
client2.affiche_solde()

print()  # Afin d'avoir un saut de page

client1.depot(1000)
client1.affiche_solde()

print()   

client2.affiche_solde()
 

print()

client1.retrait(10000)
client1.affiche_solde()

print()

client2.retrait(100)
client2.affiche_solde()

print()

client2.transfert(client1, 200)
client2.affiche_solde()

print()

client2.transfert(client1, 10000)
client2.affiche_solde()
client1.affiche_solde()