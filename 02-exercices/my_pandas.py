import pandas as pd # ON MET l'alias pd afin de faciliter les futures appels aux objets et autres..
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




#--------------------------------------------- Plusieures façons de créer de Dataframe-----------------------------------------

data_list1 = [
    ['Carrefour', 'Casino', 'Lidl', 'Carrefour', 'Casino', 'Lidl'],
    ['01.1.1', '02.1.1', '01.1.1', '03.1.1', '01.1.1', '02.1.1'],
    [3, 2, 7, 5, 10, 1],
    [1.50, 2.30, 0.99, 5.00, 1.20, 3.10]
]

data_list2 = [
    ['Carrefour', '01.1.1', 3, 1.50],
    ['Casino', '02.1.1', 2, 2.30],
    ['Lidl', '01.1.1', 7, 0.99],
    ['Carrefour', '03.1.1', 5, 5.00],
    ['Casino', '01.1.1', 10, 1.20],
    ['Lidl', '02.1.1', 1, 3.10]
]

# Si les données sont sous forme de colonnes : à partir d'un dictionnaire
data_dict = {
    'enseigne': data_list1[0],
    'produit': data_list1[1],
    'quantite': data_list1[2],
    'prix': data_list1[3]
}

df_from_dict = pd.DataFrame(data_dict)
print(df_from_dict)
# Si les données sont sous forme de lignes : à partir d'une liste de listes
columns = ['enseigne', 'produit', 'quantite', 'prix']
df_from_list = pd.DataFrame(data_list2, columns=columns)
print(df_from_list)
# Vérification
df_from_dict.equals(df_from_list)



data = {
    'enseigne': ['Carrefour', 'Casino', 'Lidl', 'Carrefour', 'Casino', 'Lidl'],
    'produit': ['01.1.1', '02.1.1', '01.1.1', '03.1.1', '01.1.1', '02.1.1'],
    'quantite': [3, 2, 7, 5, 10, 1],
    'prix': [1.50, 2.30, 0.99, 5.00, 1.20, 3.10],
    'date_heure': pd.to_datetime(["2022-01-01 14:05", "2022-01-02 09:30", 
                                  "2022-01-03 17:45", "2022-01-04 08:20", 
                                  "2022-01-05 19:00", "2022-01-06 16:30"])
}

df = pd.DataFrame(data)
# loc 
print(df.iloc[0])
print()
print(df.loc[:, 'prix'])

df = df.set_index("prix")

print(df)

