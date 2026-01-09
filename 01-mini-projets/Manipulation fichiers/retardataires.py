# 3 éleves n'avaient pas rendu leur copie dans le temps :

supp = [
    (16, 3),  # Miranda a obtenu 16 et rendu son devoir avec 3 jours de rtard
    (11, 1),  # Paolo a obtenu 11 et a rendu son devoir avec 1 jour de rtard
    (3, 5)   # Isidore a obtenu 3 et a rendu son devoir avec 5 jour de retard
]

# A savoir que chaque élève aura une note finale = à la note obtenue - le nombre de jours de retard.

#-------------------------------------------------------------------------------------------
# A l’aide d’une boucle sur cette liste, ajouter (sans réécrire complètement le fichier !). 
# les notes au fichier notes_clean.txt (sans la mention).
#--------------------------------------------------------------------------------------------

supp = [(16, 3), (11, 1), (3, 5)]

with open("clean_notes.txt", "a") as file_out:
    for elem in supp:
        note_finale = elem[0] - elem[1]
        note_finale = max(0, note_finale)
        file_out.write(str(note_finale) + "\n")

      