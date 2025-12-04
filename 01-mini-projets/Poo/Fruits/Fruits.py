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
    def __str__(self):
       return f"C'est un(e) {self.nom} de couleur {self.couleur} et pesant environ {self.poids}"
    def __repr__(self):
        return f"Vous mangez le/la {self.nom} , Miam! "
pomme = Fruits("pomme", "Rouge", 150)
banane = Fruits("banane", "jaune", 100)
mangue = Fruits("mangue", "orange", 90)
print(pomme.__repr__())
print(pomme.__str__())

print()

print(banane.__repr__())
print(banane.__str__())

