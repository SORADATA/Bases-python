# test sur la programmation orientée objet

class Fruits:
    def __init__(self, nom, couleur, poids):
        """
        __init__ défini les Attributs :
         1. nom
         2. couleur
         3. poids

         """
        self.nom = nom
        self.couleur = couleur
        self.poids = poids
    def afficher_description(self):
        return f"C'est un(e) {self.nom} de couleur {self.couleur} et pesant environ {self.poids}"
    def manger(self):
        return f"Vous mangez le/la {self.nom} , Miam! "
pomme = Fruits("pomme", "Rouge", 150)
banane = Fruits("banane", "jaune", 100)
mangue = Fruits("mangue", "orange", 90)
print(pomme.manger())
print(pomme.afficher_description())

print()

print(banane.manger())
print(banane.afficher_description())