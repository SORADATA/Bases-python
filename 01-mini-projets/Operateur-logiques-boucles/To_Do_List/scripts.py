taches = []  # structure pour stocker les tâches

while True:
    print("\n ---- GESTIONNAIRE DE TÂCHES ----")
    print("1. Ajouter une tâche")
    print("2. Afficher les tâches")
    print("3. Supprimer une tâche")
    print("4. Quitter")

    choix = input("Quel est votre choix (1-4) ? ")
    
    # Option (choix 1)
    if choix == '1':
        A = input("Entrer une nouvelle tâche: ")
        taches.append(A)

    # Option (choix 2)
    elif choix == '2':
        if not taches:
            print("La liste des tâches est vide.")
        else:
            print("\n----LISTE DES TÂCHES----")
            for index, tache in enumerate(taches, start=1):
                print(f"{index}. {tache}")
    # Option supprimer (choix 3)
    elif choix == '3':
        if not taches:
            print("Aucune tâche à supprimer.")
            continue
        for index, tache in enumerate(taches, start=1):
            print(f"{index}. {tache}")
        # Saisie sécurisée
        try:
            num_tache_sup = int(input("Entrez le numéro de la tâche à supprimer : "))
            
            if 1 <= num_tache_sup <= len(taches): 
                """
                1 <= num_tache_sup : Limite inférieeure : pas de nbre neg ou 0
                num_tache_sup <= len(taches) : Limite supérieure , user ne doit pas entre un nbre sup à len (total élement dans tache)

                """
                tache_supprimee = taches.pop(num_tache_sup - 1)   # Puisqu'on a dit de start à 1 alorsque l'index noraml est 0
                print(f"La tâche '{tache_supprimee}' a été supprimée")
            else:
                print("Le numéro entré est invalide")
        except ValueError:
            print("Veuillez entrer un nombre valide")

    elif choix == '4':
        print("Bonne journée et au revoir !")
        break
    else:
        print("Choix non valide. Veuillez réessayer.")
