## Documentation générale

Ce dépôt sert de journal de bord et de portfolio pour ma montée en compétence en Git et Python, dans le cadre de mon alternance en Data.


## Objectif 

1. **Centraliser**: Rassembler les diférents scripts, exercices et mini-projets que je réalise.
2. **Pratiquer Git** : Utiliser ce dépôt comme un "bac à sable " pour m'entraîner à utiliser Git de manière plus avancée (branches, merge requests, gestion des conflits , etc...)


 Contenu de ma branche actuelle (HEAD)
 
## Extensions GitLab

## Extensions GitLab ou git
 Contenu de la branche que j'essaie d'intégrer (dev)

cd existing_repo

git remote add origin https://forge.dgfip.finances.rie.gouv.fr/mousslab/git_skills.git

git branch -M main

git push -uf origin main






## Conventions Commits 

| Préfixe | Signification |
| ------ | ------ |
| `feat` | **Fonctionnalité** (Feature) : Ajoute, ajuste ou supprime une nouvelle fonctionnalité. |
| `fix` | **Correction** (Fix) : Corrige un bug dans le code (souvent après un `feat`). |
| `refactor` | **Réécriture** (Refactoring) : Réécriture de code qui ne change pas son comportement (ni n'ajoute de fonctionnalité, ni ne corrige un bug). |
| `perf` | **Performance** : Un refactor spécifique qui améliore les performances de l'application. |
| `style` | **Style de code** : Modifications liées au style de code (formatage, espaces, points-virgules, etc.) qui n'affectent pas la logique. |
| `test` | **Tests** : Ajout de nouveaux tests ou correction de tests existants. |
| `docs` | **Documentation** : Changements qui affectent uniquement la documentation (README, commentaires, etc.). |
| `build` | **Système de build** : Changements liés au processus de "build", aux dépendances (ex: npm, pom.xml), ou à l'intégration continue (CI/CD). |
| `ops` | **Opérations** : Changements liés aux opérations (infrastructure, déploiement, sauvegarde, etc.). |
| `chore` | **Corvée / Tâche** : Tâches diverses qui ne concernent pas le code source (ex: mise à jour du .gitignore, scripts internes). |

## Git command 

### 1. 🔧 Configuration (À faire une seule fois)

| Commande | Description |
|---|---|
| `git config --global user.name "Votre Nom"` | Définit votre nom pour tous vos commits. |
| `git config --global user.email "votre.email@example.com"` | Définit votre email pour tous vos commits. |
| `git config --global init.defaultBranch main` | (Recommandé) Utilise `main` comme nom de branche par défaut. |

---

### 2. 🚀 Démarrer un Projet

| Commande | Description |
|---|---|
| `git init` | Initialise un nouveau dépôt Git dans le dossier actuel. |
| `git clone <url_du_depot>` | Clone (télécharge) un projet distant et son historique. |

---

### 3. 💻 Le Travail Quotidien (La boucle essentielle)

C'est le cycle `add` -> `commit` que vous avez réussi.

| Commande | Description |
|---|---|
| `git status` | **LA PLUS IMPORTANTE.** Montre l'état de vos fichiers (modifiés, préparés, etc.). |
| `git add <fichier>` | Ajoute un fichier à la "zone de préparation" (staging area). |
| `git add .` | Ajoute *tous* les fichiers modifiés/nouveaux à la zone de préparation. |
| `git commit -m "Message"` | Crée un "snapshot" (commit) avec les fichiers préparés. |
| `git commit --amend` | (Avancé) Modifie le *dernier* commit (message ou contenu). |

---

### 4. 🌿 Travailler avec les Branches

| Commande | Description |
|---|---|
| `git branch` | Liste toutes les branches locales. |
| `git checkout -b <nom-branche>` | **Crée** une nouvelle branche ET bascule dessus. (C'est le `-b` qui vous manquait au début). |
| `git checkout <nom-branche>` | Bascule vers une branche *existante*. |
| `git switch <nom-branche>` | (Moderne) Équivalent de `git checkout`. |
| `git switch -c <nom-branche>` | (Moderne) Équivalent de `git checkout -b`. |
| `git branch -d <nom-branche>` | Supprime une branche en local (vous l'avez fait avec `dev`). |

---

### 5. 📡 Collaborer & Synchroniser (Dépôt distant `origin`)

| Commande | Description |
|---|---|
| `git push` | Envoie vos commits locaux vers le dépôt distant (`origin`). |
| `git push --set-upstream origin <nom-branche>` | **(Pour la 1ère fois)** Lie votre branche locale à la branche distante et envoie. |
| `git pull` | Récupère les changements distants et les fusionne dans votre branche. |
| `git fetch` | Récupère les changements distants (sans les fusionner). |
| `git fetch --prune` | (Utile) Fait un `fetch` et nettoie les branches locales qui n'existent plus sur le distant. |
| `git push --delete origin <nom-branche>` | Supprime une branche sur le dépôt distant (vous l'avez fait avec `dev`). |

---

### 6. 🧐 Consulter l'Historique & Annuler

| Commande | Description |
|---|---|
| `git log` | Affiche l'historique des commits. (C'est la commande qui ressemble à `ls`). |
| `git log --oneline --graph --all` | (Recommandé) Affiche un historique compact et visuel. |
| `git diff` | Montre les modifications non encore préparées (pas "add"). |
| `git diff --staged` | Montre les modifications préparées (après "add", avant "commit"). |
| `git restore <fichier>` | Annule les modifications sur un fichier (avant "add"). |
| `git restore --staged <fichier>` | Retire un fichier de la zone de préparation (l'inverse de "add"). |
