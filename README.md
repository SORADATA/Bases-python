<div align="center">

# 🎓 Git Skills and Python Portfolio

**Mon journal de bord pour la maîtrise de Git & Python**

[![Git](https://img.shields.io/badge/Git-F05032?logo=git\&logoColor=white)](https://git-scm.com/)
[![Python](https://img.shields.io/badge/Python-3776AB?logo=python\&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-Learning-blue.svg)]()

*Alternance en Data | Progression continue*

</div>

---

## 📖 À propos

Ce dépôt constitue mon **portfolio d'apprentissage** dans le cadre de mon alternance en Data. Il trace ma progression dans la maîtrise des outils essentiels au développement collaboratif et à l'analyse de données.

### 🎯 Objectifs

| Objectif                    | Description                                                       | Statut     |
| --------------------------- | ----------------------------------------------------------------- | ---------- |
| **📚 Centraliser**          | Rassembler scripts, DAGs et modèles de données                    | 🟢 Terminé |
| **🔧 Pratiquer Git**        | Maîtriser branches, rebase, cherry-pick et résolution de conflits | 🟢 Terminé |
| **🐍 Développer en Python** | Améliorer mes compétences en ingénierie de données                | 🟢 Terminé |

---

## 📂 Structure du Projet

```text
Bases-python/
├── 01.mini-projet/
├── 02.exercices/          # Scripts ETL/ELT
├── 03.projets finaux/     # Pipelines complets, modèles dbt, DAGs Airflow
├── tests/                 # Tests unitaires et requêtes de validation
└── README.md              # Ce fichier
```

## 🚀 Quick Start

### Configuration initiale

```bash
# Cloner le dépôt
git clone https://github.com/SORADATA/Bases-python.git
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

# 2. Créer une branche pour un nouveau modèle ou pipeline
git checkout -b feat/stg-nouveau-modele

# 3. Faire des modifications, puis...
git add .
git commit -m "feat: ajout du staging pour les données d'activité"

# 4. Pousser vers le dépôt distant
git push --set-upstream origin feat/stg-nouveau-modele
```

---

## 📚 Conventions de Commits

Ce projet suit les **conventions de commits sémantiques** pour un historique clair, indispensable pour les déploiements automatisés.

### Types de commits

| **Préfixe** | **Emoji** | **Signification**                                  | **Exemple**                                               |
| ----------- | --------- | -------------------------------------------------- | --------------------------------------------------------- |
| `feat`      | ✨         | **Fonctionnalité** - Nouveau modèle ou DAG         | `feat: ✨ ajout du DAG d'orchestration`                    |
| `fix`       | 🐛        | **Correction** - Bug SQL ou Python                 | `fix: 🐛 correction de la jointure sur l'id_projet`       |
| `refactor`  | ♻️        | **Refactoring** - Optimisation de code             | `refactor: ♻️ optimisation de la macro dbt`               |
| `perf`      | ⚡         | **Performance** - Amélioration des temps de calcul | `perf: ⚡ ajout d'un partitionnement sur import_timestamp` |
| `style`     | 💄        | **Style** - Formatage (Flake8, SQLFluff)           | `style: 💄 formatage SQL du modèle de reporting`          |
| `test`      | ✅         | **Tests** - Ajout de tests dbt ou Pytest           | `test: ✅ ajout de tests not_null sur la clé primaire`     |
| `docs`      | 📝        | **Documentation** - README, YAML dbt               | `docs: 📝 ajout des descriptions de colonnes`             |
| `build`     | 📦        | **Build** - Dépendances                            | `build: 📦 mise à jour de dbt-core`                       |
| `ops`       | 🔧        | **Opérations** - CI/CD, Docker                     | `ops: 🔧 maj du workflow GitHub Actions`                  |
| `chore`     | 🧹        | **Maintenance** - Tâches mineures                  | `chore: 🧹 nettoyage des logs locaux`                     |

---

## 🛠️ Commandes Git Essentielles pour l'Analytics Engineer

### 1. 💻 Le Workflow Quotidien

**Le cycle Add → Commit → Push**

```bash
git status                      # ⭐ LA COMMANDE LA PLUS IMPORTANTE
git add models/mon_modele.sql   # Ajoute un fichier spécifique
git add -p                      # Ajoute interactivement (bout par bout)
git commit -m "type: message"   # Crée un commit avec message
git commit --amend -m "nouveau" # Modifie le dernier commit (message ou fichiers oubliés)
git push                        # Envoie vers le dépôt distant
```

### 2. 🌿 Gestion des Branches & Changement de Contexte (Stash)

```bash
# Mettre de côté son travail en cours
git stash                       # Sauvegarde les modifs non commitées
git stash list                  # Liste les sauvegardes en attente
git stash pop                   # Applique et supprime la dernière sauvegarde
git stash apply                 # Applique sans supprimer la sauvegarde
git stash drop                  # Supprime une sauvegarde spécifique

# Créer et naviguer
git switch -c <nom-branche>         # (Moderne) Crée et bascule
git push origin --delete <branche>  # Supprime une branche distante
```

### 3. 🔀 Intégration Continue : Merge vs Rebase

```bash
# Le Rebase (Réécrire l'historique pour l'aligner sur main)
git fetch origin
git rebase origin/main          # Place tes commits au-dessus de main
git rebase -i HEAD~3             # Rebase interactif : fusionner (squash) ou modifier les 3 derniers commits

# Le Merge classique
git merge main                  # Fusionne main dans ta branche
```

### 4. 🚑 Débogage et Secours (Les commandes "Sauve-moi")

```bash
# Qui a écrit cette ligne de code (et quand) ?
git blame models/core/mon_modele.sql

# Trouver quel commit précis a introduit un bug (recherche binaire)
git bisect start
git bisect bad                  # Le code actuel est cassé
git bisect good <commit-hash>   # Ce vieux commit fonctionnait
# Git va tester les commits un par un pour trouver l'erreur

# Récupérer un commit spécifique (hotfix) depuis une autre branche
git cherry-pick <commit-hash>

# La machine à voyager dans le temps (historique de TOUTES tes actions)
git reflog
git reset --hard HEAD@{2}       # Annule une erreur de rebase ou de reset !
```

### 5. 🏷️ Gestion des Versions (Tags)

```bash
git tag -a v1.0.0 -m "Release initiale du data warehouse"
git push origin v1.0.0          # Pousse un tag spécifique
git push origin --tags          # Pousse tous les tags locaux
```

### 6. ↩️ Annuler des Modifications

```bash
git restore <fichier>                # Annule les modifications (avant add)
git restore --staged <fichier>       # Retire de la staging area (après add)
git reset --soft HEAD~1              # Annule le dernier commit (garde les modifs)
git reset --hard HEAD~1              # ⚠️ Annule ET supprime les modifications
git revert <commit-hash>             # Crée un nouveau commit qui annule un ancien (sûr pour le travail partagé)
```

---

## 🎯 Bonnes Pratiques de l'Analytics Engineer

* ✅ **Tester avant de commit** (ex: `dbt build` ou run local d'Airflow).
* ✅ **Squasher ses commits** via rebase interactif avant de merger une grosse PR pour garder l'historique propre.
* ✅ **Utiliser `.gitignore`** pour exclure `dbt_packages/`, `logs/`, `target/` et les credentials `.env`.
* ❌ **Ne jamais utiliser `git push --force` sur `main`** (utiliser `--force-with-lease` sur ses propres branches après un rebase).
* ❌ **Ne jamais commiter de données brutes (`.csv`, `.parquet`)** ou de secrets (fichiers `profiles.yml`).

---

## 📝 Notes Personnelles : Résolution d'Erreurs Fréquentes

### Problème 1 : Conflit lors d'un rebase (`CONFLICT (content)`)

```bash
# Solution : Résoudre manuellement dans l'éditeur, puis :
git add fichier_resolu.py
git rebase --continue

# (Ne PAS faire git commit pendant un rebase)
```

### Problème 2 : J'ai commité sur la mauvaise branche (main au lieu d'une feature branch)

```bash
git branch feat/nouvelle-table      # 1. Copier l'état actuel dans une nouvelle branche
git reset --hard HEAD~1             # 2. Reculer main d'un commit
git switch feat/nouvelle-table      # 3. Aller sur la bonne branche (le commit y est !)
```

---

**Développé avec 💙 dans le cadre de mon alternance Analytics Engineer**

*Dernière mise à jour : Janvier 2025*
