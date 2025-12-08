import numpy as np

# on souhaite avoir la moyenne et l'ecart-type de notes

with open("notes.txt", "r") as file_in:
    """
    with : permet que le fichier soit fermé automatiquement en cas d'erreur
    'r' : essaie de lire le fichier notes.txt
    as file_in : donne lui le nom de sortie file_in

    """

    notes = file_in.read() # lit tout le contenu du fichier
notes = notes.split() # elle sépare la chaîne à chaque espace et crée une liste de chaînes de caractères.
notes_num = []
for n in notes:
    notes_num.append(int(n))
print(f"La moyenne de notes est de : {np.mean(notes_num)}")
print(f"L'ecart-type de notes est de : {np.std(notes_num)}")
        