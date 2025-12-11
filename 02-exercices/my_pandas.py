import pandas as pd
import numpy as np
import csv

# Les series : un conteneur de données unidimensionnel pouvant acceuillir n'importe quel type de données

l = [1, "X", 3]
s = pd.Series(l)
print(s)
print(s[2])
s = pd.Series(1, index=["a", "b", "c"])
print(s)
s["b"]

s.values

# Dataframe : consiste en une collection de Series, alignées par les index.abs

df = pd.DataFrame(
    data = {
        "var1": [1.3, 5.6, np.nan, np.nan, 0, np.nan],
        "var2": np.random.randint(-10, 10, 6),
        "experiment": ["test", "train", "test", "train", "train", "validation"],
        "date": ["2022-01-01", "2022-01-02", "2022-01-03", "2022-01-04", "2022-01-05", "2022-01-06"],
        "sample": "sample1"
    }
)
df
print(df)

# Index 
print(df.index)
print(df.columns)

# Méthode set_index
df = df.set_index("date")
print(df)

# Sélectionner des données
# selectionner une seule colonne
select_col = df["var1"]
print(select_col)
print(type(select_col)) # est une Series
print(select_col.shape) # dimension de l'objet. 

# Selectionner plusieures colonnes
select_col = df[["var1", "var2", "experiment"]]
print(select_col)
print(select_col.shape)

# Selectionner des lignes 

# Utilisation de loc : fonctionne avec des labels
print(df.loc["2022-01-01":"2022-01-03", :])
# iloc : permet de sélectionner des lignes et des col par leur position
print(df.iloc[0:3, :])

# Filtrage des données selon des conditions

print(df[df["var2"] >= 0])

# Apartenance avec isin : i on veut filtrer les données basées sur une liste de valeurs possibles
print(df[df["experiment"].isin(["train", "validation"])])


# Explorer des données tabulaires

# importer et exporter des données
rows = []
with open