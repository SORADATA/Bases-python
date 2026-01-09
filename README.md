<div align="center">

# 🎓 Git Skills Portfolio

**Mon journal de bord pour la maîtrise de Git & Python**

[![Git](https://img.shields.io/badge/Git-F05032?logo=git&logoColor=white)](https://git-scm.com/)
[![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-Learning-blue.svg)]()

*Alternance en Data | Progression continue*

</div>

---

## 📖 À propos

Ce dépôt constitue mon **portfolio d'apprentissage** dans le cadre de mon alternance en Data. Il trace ma progression dans la maîtrise des outils essentiels au développement collaboratif et à l'analyse de données.

### 🎯 Objectifs

| Objectif | Description | Statut |
|----------|-------------|--------|
| **📚 Centraliser** | Rassembler scripts, exercices et mini-projets réalisés | 🟢 Terminé|
| **🔧 Pratiquer Git** | Maîtriser branches, merge requests, résolution de conflits | 🟢 Terminé|
| **🐍 Développer en Python** | Améliorer mes compétences en programmation data | 🟢 Terminé|


---

## 📂 Structure du Projet

```
Bases-python/
├── 01.mini-projet/
├── 02.exercices/          # Exercices de formation
├── 03.projets finaux/       # Projets complets (POC, analyses)
├── tests/                # Prise de notes et synthèses
└── README.md             # Ce fichier
```

---

## 🚀 Quick Start

### Configuration initiale

```bash
# Cloner le dépôt
git clone https://github.com/SORADATA/Bases-python/.git
cd Bases-python

# Configurer Git (première fois)
git config --global user.name "Votre Nom"
git config --global user.email "votre.email@example.com"
git config --global init.defaultBranch main
```

### Workflow quotidien

```bash
# 1. Vérifier l'état
git status

# 2. Créer une branche pour une nouvelle fonctionnalité
git checkout -b feat/ma-nouvelle-feature

# 3. Faire des modifications, puis...
git add .
git commit -m "feat: ajout de la fonctionnalité X"

# 4. Pousser vers le dépôt distant
git push --set-upstream origin feat/ma-nouvelle-feature
```

---

## 📚 Conventions de Commits

Ce projet suit les **conventions de commits sémantiques** pour un historique clair et exploitable.

### Format

```
<type>: <emoji> <description courte>

[corps optionnel détaillant les changements]

[footer optionnel avec références]
```

### Types de commits

| Préfixe | Emoji | Signification | Exemple |
|---------|-------|---------------|---------|
| `feat` | ✨ | **Fonctionnalité** - Ajoute une nouvelle fonctionnalité | `feat: ✨ ajout du module d'analyse de données` |
| `fix` | 🐛 | **Correction** - Corrige un bug | `fix: 🐛 correction du calcul de moyenne` |
| `refactor` | ♻️ | **Refactoring** - Améliore le code sans changer le comportement | `refactor: ♻️ simplification de la logique de filtrage` |
| `perf` | ⚡ | **Performance** - Améliore les performances | `perf: ⚡ optimisation des requêtes SQL` |
| `style` | 💄 | **Style** - Formatage, indentation, conventions | `style: 💄 application de Black sur tous les fichiers` |
| `test` | ✅ | **Tests** - Ajout ou modification de tests | `test: ✅ ajout de tests unitaires pour le module X` |
| `docs` | 📝 | **Documentation** - README, commentaires, docstrings | `docs: 📝 amélioration de la documentation API` |
| `build` | 📦 | **Build** - Dépendances, configuration CI/CD | `build: 📦 mise à jour de requirements.txt` |
| `ops` | 🔧 | **Opérations** - Infrastructure, déploiement | `ops: 🔧 configuration du pipeline CI` |
| `chore` | 🧹 | **Maintenance** - Tâches diverses (.gitignore, scripts) | `chore: 🧹 nettoyage des fichiers temporaires` |

### Exemples concrets

```bash
# Bonne pratique
git commit -m "feat: ✨ ajout du script de nettoyage CSV"
git commit -m "fix: 🐛 correction du parsing de dates dans le module ETL"
git commit -m "docs: 📝 documentation de la fonction calculate_metrics()"

# À éviter
git commit -m "modifs"
git commit -m "test"
git commit -m "corrections diverses"
```

---

## 🛠️ Commandes Git Essentielles

### 1. 🔧 Configuration (Une seule fois)

```bash
git config --global user.name "Votre Nom"
git config --global user.email "votre.email@example.com"
git config --global init.defaultBranch main
git config --global core.editor "code --wait"  # Utilise VS Code comme éditeur
```

---

### 2. 🚀 Démarrer un Projet

```bash
git init                        # Initialise un nouveau dépôt
git clone <url_du_depot>        # Clone un projet existant
```

---

### 3. 💻 Le Workflow Quotidien

**Le cycle Add → Commit → Push**

```bash
git status                      # ⭐ LA COMMANDE LA PLUS IMPORTANTE
git add <fichier>               # Ajoute un fichier spécifique
git add .                       # Ajoute tous les fichiers modifiés
git commit -m "type: message"   # Crée un commit avec message
git commit --amend              # Modifie le dernier commit
git push                        # Envoie vers le dépôt distant
```

**Astuce :** Toujours faire `git status` avant et après chaque commande !

---

### 4. 🌿 Gestion des Branches

```bash
# Lister et naviguer
git branch                           # Liste les branches locales
git branch -a                        # Liste toutes les branches (locales + distantes)
git checkout <nom-branche>           # Bascule vers une branche existante
git switch <nom-branche>             # (Moderne) Équivalent de checkout

# Créer et supprimer
git checkout -b <nom-branche>        # Crée ET bascule vers une nouvelle branche
git switch -c <nom-branche>          # (Moderne) Équivalent
git branch -d <nom-branche>          # Supprime une branche en local
git push --delete origin <branche>   # Supprime une branche distante
```

**Convention de nommage des branches :**
```
feat/nom-feature          # Nouvelle fonctionnalité
fix/nom-bug              # Correction de bug
refactor/nom-refacto     # Refactoring
docs/nom-doc             # Documentation
test/nom-test            # Tests
```

---

### 5. 📡 Synchronisation avec le Dépôt Distant

```bash
# Récupérer les changements
git fetch                                # Récupère sans fusionner
git fetch --prune                        # Nettoie les branches obsolètes
git pull                                 # Récupère ET fusionne

# Envoyer les changements
git push                                 # Envoie vers origin
git push --set-upstream origin <branche> # Première fois (lie la branche)
git push -u origin <branche>             # Raccourci de la commande précédente
git push --force                         # ⚠️ À utiliser avec précaution !
```

---

### 6. 🔍 Consulter l'Historique

```bash
# Affichage standard
git log                              # Historique complet
git log --oneline                    # Historique compact (1 ligne/commit)
git log --graph --all --oneline      # ⭐ Visualisation graphique recommandée
git log --author="Votre Nom"         # Filtrer par auteur

# Comparer les versions
git diff                             # Changements non stagés
git diff --staged                    # Changements stagés (après add)
git diff <branche1> <branche2>       # Compare deux branches
```

**Alias recommandé :**
```bash
git config --global alias.lg "log --oneline --graph --all --decorate"
# Utilisation : git lg
```

---

### 7. ↩️ Annuler des Modifications

```bash
# Avant le commit
git restore <fichier>                # Annule les modifications (avant add)
git restore --staged <fichier>       # Retire de la staging area (après add)
git reset HEAD <fichier>             # Équivalent ancien de restore --staged

# Après le commit
git reset --soft HEAD~1              # Annule le dernier commit (garde les modifs)
git reset --hard HEAD~1              # ⚠️ Annule ET supprime les modifications
git revert <commit-hash>             # Crée un nouveau commit qui annule un ancien
```

⚠️ **Attention :** `--hard` supprime définitivement les modifications !

---

### 8. 🔀 Fusion et Résolution de Conflits

```bash
# Fusionner une branche
git merge <branche-source>           # Fusionne branche-source dans la branche courante
git merge --no-ff <branche>          # Force un commit de merge

# En cas de conflit
git status                           # Voir les fichiers en conflit
# Éditer manuellement les fichiers marqués
git add <fichiers-résolus>
git commit -m "fix: résolution des conflits"

# Annuler un merge en cours
git merge --abort
```

**Résolution de conflits :**
```
<<<<<<< HEAD (votre branche)
Votre code
=======
Code de la branche à fusionner
>>>>>>> nom-de-la-branche
```

---

## 🎯 Bonnes Pratiques

### ✅ À faire

- ✅ **Commit fréquemment** avec des messages clairs
- ✅ **Une branche = une fonctionnalité**
- ✅ **Toujours `git pull` avant de commencer à travailler**
- ✅ **Tester avant de commit**
- ✅ **Utiliser `.gitignore`** pour exclure les fichiers inutiles
- ✅ **Faire des merge requests** pour le code review

### ❌ À éviter

- ❌ Commit directement sur `main` (travailler sur des branches)
- ❌ Messages de commit vagues ("fix", "update", "modifs")
- ❌ Commits trop gros (>500 lignes de changements)
- ❌ `git push --force` sur des branches partagées
- ❌ Commit de fichiers sensibles (mots de passe, clés API)

---

## 📊 Progression & Jalons

### Compétences acquises

- [x] Configuration de Git
- [x] Création et gestion de branches
- [x] Commits et messages conventionnels
- [x] Push/Pull vers dépôt distant
- [x] Suppression de branches locales et distantes
- [x] Résolution de conflits de merge
- [x] Rebase interactif
- [x] Git hooks et automatisation
- [x] Gestion avancée des tags et releases

---

## 🔗 Ressources Utiles

### Documentation officielle
- [Git Documentation](https://git-scm.com/doc)
- [Pro Git Book (gratuit)](https://git-scm.com/book/fr/v2)
- [GitHub Guides](https://guides.github.com/)
- [Conventionnal Commits](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13#types)

### Tutoriels interactifs
- [Learn Git Branching](https://learngitbranching.js.org/?locale=fr_FR)
- [Git Immersion](https://gitimmersion.com/)
- [Exercism - Git Track](https://exercism.org/tracks/git)

### Outils
- [GitKraken](https://www.gitkraken.com/) - Interface graphique
- [Oh My Zsh Git Plugin](https://github.com/ohmyzsh/ohmyzsh/tree/master/plugins/git) - Alias Git
- [Git Cheat Sheet (PDF)](https://education.github.com/git-cheat-sheet-education.pdf)

---

## 📝 Notes Personnelles

### Erreurs courantes rencontrées et solutions

**Problème 1 : `error: failed to push some refs`**
```bash
# Solution : Pull d'abord, puis push
git pull origin main
git push origin main
```

**Problème 2 : Oubli de créer une branche**
```bash
# Solution : Créer une branche avec les modifications actuelles
git stash                    # Sauvegarde les modifications
git checkout -b nouvelle-branche
git stash pop               # Récupère les modifications
```

**Problème 3 : Modifier le dernier commit**
```bash
# Solution : Amender le commit
git add fichier-oublie.py
git commit --amend --no-edit
```

---

## 🤝 Contribution

Ce dépôt est personnel, mais les suggestions d'amélioration sont bienvenues !

Pour proposer une amélioration :
1. Créer une branche `feat/amelioration-xxx`
2. Faire vos modifications
3. Soumettre une merge request avec description détaillée

---

## 📜 License

Ce projet est à usage éducatif dans le cadre de mon alternance.

---

<div align="center">

**Développé avec 💙 dans le cadre de mon alternance Data**

*Dernière mise à jour : Janvier 2025*

[![Git](https://img.shields.io/badge/Keep-Learning-success)]()

</div>
