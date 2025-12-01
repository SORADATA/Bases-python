# La  programmation orientée objet (poo) nous permet de structurer des programmes autour
# d'une abstraction , l'objet qui contient des attributs de des méthodes qui agissent sur lui-même.

# Admettons que le jus contenu dans un citron soit une fonction proportionnelle de sa masse,
# défini de la manière suivante : jus = masse / 4

class Citron:
    def __init__(self, couleur, masse):
        self.saveur = "acide"
        self.couleur = couleur
        self.masse = masse
        self.jus = masse / 4
    def recup_masse(self):
        print(f"La masse du citron est  {str(self.masse)} grammes")
            
    def recup_qte_jus(self):
        print(f"Il reste {str(self.jus)} mL de jus dans le citron.")
    def extraire_jus(self, quantite):
        if quantite > self.jus:
            print("Il n'ya pas assez de jus dans le citron pour la quantité demandée.")
        else:
                self.jus = max(0, self.jus - quantite) # Afin déviter toute valeur négative de jus
citron = Citron("jaune", 500)

citron.recup_masse()
citron.recup_qte_jus()