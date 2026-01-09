
listes_notes = []

with open("clean_notes.txt", 'r') as file_in:
    lignes = file_in.readlines()  # retourne chaque élément avec une ligne du fichier

for n in lignes:
    listes_notes.append(int(n))
#-------------------------------------------------------
# # Réecriture des notes dans un fichier notes_mentions.txt
#--------------------------------------------------------

with open("notes_mentions.txt", 'w') as file_out:
    notes_triees = sorted(listes_notes, reverse=True)
    for note in notes_triees:
        if note >= 10:
            mention = "admis"
        else:
            mention = "recalé"
        file_out.write(f"{note} {mention}\n")
    









    
