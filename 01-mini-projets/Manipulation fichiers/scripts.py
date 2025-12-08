import numpy as np

# on souhaite avoir la moyenne et l'ecart-type de notes

with open("notes.txt", "r") as file_in:
    """
    with : permet que le fichier soit fermé automatiquement en cas d'erreur
    'r' : essaie de lire le fichier notes.txt
    as file_in : donne lui le nom de sortie file_in

    """

    notes_brutes = file_in.read() # lit tout le contenu du fichier
notes_str = notes_brutes.split() # elle sépare la chaîne à chaque espace et crée une liste de chaînes de caractères.
notes_num = []
for n in notes_str:
    notes_num.append(int(n))

moyenne = np.mean(notes_num)
ecart_type = np.std(notes_num)

print(f"La moyenne de notes est de : {moyenne}")
print(f"L'ecart-type de notes est de : {ecart_type}")

# ---------------------------------------------------------
# Sauvegarde des notes propres dans le fichier clean_notes.txt
# ---------------------------------------------------------- 

notes_clean_str = "\n".join(map(str, notes_num))
with open("clean_notes.txt", 'w') as file_out:
    file_out.write(notes_clean_str + "\n")


# ---------------------------------------------------------
# Sauvegarde des outputs dans le fichier statistics.txt
# ----------------------------------------------------------   

ligne_moyenne = f"La moyenne de notes est de : {moyenne}\n"
ligne_ecart_type = f"L'ecart-type de notes est de : {ecart_type}\n"

# on ouvre le fichier clean_notes
with open("statistics.txt", 'w') as file_out:
    file_out.write(ligne_moyenne)
    file_out.write(ligne_ecart_type)
