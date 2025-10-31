#  Projet : Gestionnaire de Bibliothèque Personnelle

## L'objectif

Vous allez créer un petit script pour gérer votre collection de livres. Vous devrez ajouter des livres, les supprimer, et les afficher. Ce projet vous forcera à utiliser des **listes** pour ce qui peut changer, et des **tuples** pour ce qui est fixe.

---

## Le Contexte

* **Un livre :** Un livre a un **Titre** et un **Auteur**. Une fois qu'un livre est écrit, son titre et son auteur ne changent pas. C'est donc une donnée parfaite pour un **tuple** (immutable).
    * Exemple : `("1984", "George Orwell")`
* **La bibliothèque :** Votre bibliothèque (l'étagère) est une collection de livres. Vous pouvez y **ajouter** de nouveaux livres ou en **retirer**. C'est donc un conteneur parfait pour une **liste** (mutable).
    * Exemple : `[ ("1984", "George Orwell"), ("Le Hobbit", "J.R.R. Tolkien") ]`

---

## Les Étapes à suivre

Voici les tâches à réaliser : 

1.  **Créer votre bibliothèque**
    Créez une liste vide appelée `ma_bibliotheque`.
2.  **Ajouter vos premiers livres**
    * Créez trois tuples représentant trois de vos livres préférés.
    * Utilisez la méthode `.append()` pour ajouter ces trois tuples (livres) à votre liste `ma_bibliotheque`.
3.  **Afficher votre collection**
    * Affichez le contenu de `ma_bibliotheque`.
    * Affichez le nombre de livres que vous possédez en utilisant la fonction `len()`.
4.  **Accéder à un livre spécifique**
    * Affichez le **premier** livre de votre liste (titre et auteur).
    * Affichez seulement l'**auteur** du **deuxième** livre de votre liste (cela vous oblige à utiliser la double indexation).
5.  **Retirer un livre**
    * Vous avez prêté un livre et il n'est jamais revenu. Utilisez la méthode `.pop()` ou `.remove()` pour supprimer l'un des livres de votre liste.
    * Affichez à nouveau votre bibliothèque pour voir le changement.
6.  **(Bonus) L'épreuve de l'immutabilité**
    * Essayez de corriger une "faute de frappe" sur le titre de votre premier livre.
        * Par exemple, essayez de faire : `ma_bibliotheque[0][0] = "Un autre titre"`
    * Que se passe-t-il ? Notez bien l'erreur (c'est le but de l'exercice !).
7.  **(Bonus 2) Trier votre bibliothèque**
    * Votre bibliothèque est en désordre. Triez-la par ordre alphabétique de titre.
        * *Indice :* La méthode `.sort()` fonctionne très bien sur une liste de tuples. Elle trie par défaut en utilisant le premier élément de chaque tuple.
    * Affichez la liste triée.