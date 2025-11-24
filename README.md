## Documentation générale

Ce dépôt sert de journal de bord et de portfolio pour ma montée en compétence en Git et Python, dans le cadre de mon alternance en Data.


## Objectif 

1. **Centraliser**: Rassembler les diférents scripts, exercices et mini-projets que je réalise.
2. **Pratiquer Git** : Utiliser ce dépôt comme un "bac à sable " pour m'entraîner à utiliser Git de manière plus avancée (branches, merge requests, gestion des conflits , etc...)


## Extensions GitLab

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

## Integrate with your tools

- [ ] [Set up project integrations](https://forge.dgfip.finances.rie.gouv.fr/mousslab/git_skills/-/settings/integrations)

## Collaborations

- [ ] [Invite team members and collaborators](https://docs.gitlab.com/ee/user/project/members/)
- [ ] [Create a new merge request](https://docs.gitlab.com/ee/user/project/merge_requests/creating_merge_requests.html)
- [ ] [Automatically close issues from merge requests](https://docs.gitlab.com/ee/user/project/issues/managing_issues.html#closing-issues-automatically)
- [ ] [Enable merge request approvals](https://docs.gitlab.com/ee/user/project/merge_requests/approvals/)
- [ ] [Set auto-merge](https://docs.gitlab.com/user/project/merge_requests/auto_merge/)

## Test and deployments

Use the built-in continuous integration in GitLab.

- [ ] [Get started with GitLab CI/CD](https://docs.gitlab.com/ee/ci/quick_start/)
- [ ] [Analyze your code for known vulnerabilities with Static Application Security Testing (SAST)](https://docs.gitlab.com/ee/user/application_security/sast/)
- [ ] [Deploy to Kubernetes, Amazon EC2, or Amazon ECS using Auto Deploy](https://docs.gitlab.com/ee/topics/autodevops/requirements.html)
- [ ] [Use pull-based deployments for improved Kubernetes management](https://docs.gitlab.com/ee/user/clusters/agent/)
- [ ] [Set up protected environments](https://docs.gitlab.com/ee/ci/environments/protected_environments.html)


