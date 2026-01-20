# 💇‍♀️ Bad Hair Index Predictor

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Pandas](https://img.shields.io/badge/Pandas-Data_Analysis-green)
![Status](https://img.shields.io/badge/Status-Completed-success)

> **Rôle :** Analytics Engineer / Data Scientist  
> **Mission :** Concevoir un pipeline ETL pour anticiper les conditions météorologiques défavorables à la coiffure via un indicateur composite : le *Bad Hair Index*.

---

## 📑 Table des matières
1. [Contexte et Objectifs](#-contexte-et-objectifs)
2. [Méthodologie](#-méthodologie--le-calcul-du-bad-hair-index)
3. [Analyses & Insights](#-analyses--insights)
4. [Stack Technique](#-stack-technique)
5. [Structure du Projet](#-structure-du-projet)
6. [Installation & Usage](#-installation--usage)

---

## 🎯 Contexte et Objectifs

L'objectif de ce projet est de transformer des données météorologiques brutes en une information actionnable pour le quotidien. Nous cherchons à répondre à la question : **Quand faut-il rester chez soi pour sauver sa coiffure ?**

Le script automatise :
* La récupération des coordonnées géographiques d'une ville (Géocodage).
* L'extraction des prévisions météo (Vent & Humidité).
* Le calcul d'un index de risque et sa visualisation.

---

## 🧪 Méthodologie : Le calcul du "Bad Hair Index"

L'indice est calculé selon une formule pondérée qui combine l'impact de l'humidité relative (frisottis) et de la force du vent (décoiffage) :

$$Bad\ Hair\ Index = Humidité\ Relative (\%) \times Vitesse\ du\ Vent (km/h)$$

> **Interprétation :**
> * **Index Faible (< 400) :** Conditions idéales.
> * **Index Élevé (> 700) :** Risque critique "Bad Hair Day".

---

## 📊 Analyses & Insights

Voici les résultats générés par le pipeline pour la semaine à venir.

### 1. Analyse Heure par Heure (Cycle Diurne)
*Identification des créneaux horaires critiques.*

![Analyse par Heure](outputs/hour.png)

**🧐 L'analyse du Data Analyst :**
* **🔴 Zone Rouge (08h00 - 09h00) :** Pic de risque (Index > 730). La combinaison de l'humidité matinale et du vent crée les pires conditions. *Action : Couvre-chef recommandé.*
* **🟢 Zone Verte (13h00 - 15h00) :** Creux favorable (Index ~610). La hausse des températures fait chuter l'humidité relative.
* **📈 Tendance Soirée :** Remontée progressive du risque après 18h00.

### 2. Analyse Jour par Jour (Tendance Hebdomadaire)
*Planification de la semaine.*

![Analyse par Jour](outputs/day.png)

---

## ⚙️ Stack Technique

Ce projet met en œuvre un pipeline **ETL** (Extract, Transform, Load) modulaire.

| Domaine | Outil | Usage |
| :--- | :--- | :--- |
| **Extraction** | `Requests` | Appels API REST (**Nominatim** & **Open-Meteo**). |
| **Transformation** | `Pandas` | Cleaning, Typage (`datetime`), Feature Engineering. |
| **Visualisation** | `Seaborn` | Graphiques statistiques (Lineplots). |
| **Système** | `OS` | Gestion automatisée des fichiers de sortie. |

---

## 📐 Structure du Projet

```text
Prediction_meteo/
├── 📂 outputs/          # 📸 Artefacts générés (Graphiques PNG)
│   ├── day.png
│   └── hour.png
├── 📄 main.ipynb        # 🧠 Notebook principal (Pipeline ETL)
├── 📄 README.md         # 📖 Documentation
└── 📄 .gitignore        # 🛡️ Exclusion des fichiers temporaires
```

## 🚀 Installation & Usage
1. Pré-requis
Cloner le projet et installer les dépendances nécessaires via le terminal :
```text
Bash
git clone https://github.com/votre-pseudo/Prediction_meteo.git
cd Prediction_meteo
pip install pandas seaborn matplotlib requests
```
2. Lancer une analyse
Ouvrez le notebook main.ipynb ou exécutez le script principal en Python :
```text
Python
from main import main
```
# Exemple 1 : Analyse fine heure par heure à Montrouge
```text
main("France", "Montrouge", agg_var="hour")

# Exemple 2 : Tendance globale à Marseille
main("France", "Marseille", agg_var="day")
