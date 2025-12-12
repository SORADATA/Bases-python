import pandas as pd
import numpy as np

data_list1 = [
    ['Carrefour', 'Casino', 'Lidl', 'Carrefour', 'Casino', 'Lidl'],
    ['01.1.1', '02.1.1', '01.1.1', '03.1.1', '01.1.1', '02.1.1'],
    [3, 2, 7, 5, 10, 1],
    [1.50, 2.30, 0.99, 5.00, 1.20, 3.10]
] # Sous forme d'observations(chque liste contient les donbnées d'une ligne)

data_list2 = [
    ['Carrefour', '01.1.1', 3, 1.50],
    ['Casino', '02.1.1', 2, 2.30],
    ['Lidl', '01.1.1', 7, 0.99],
    ['Carrefour', '03.1.1', 5, 5.00],
    ['Casino', '01.1.1', 10, 1.20],
    ['Lidl', '02.1.1', 1, 3.10]
] # Sous forme de var (chqe liste contient les données d'une colonne)

# L’objectif est de construire dans les deux cas un même DataFrame qui contient chacune 
# des 6 observations et des 4 variables, avec les mêmes noms dans les deux DataFrame

df_list_dic = pd.DataFrame(
    data={
        "enseigne": data_list1[0],
        "produit": data_list1[1],
        "quantite": data_list1[2],
        "prix": data_list1[3]

    }
)
print("---------------sous forme de colonne : a partir d'un dict------------------")
print(df_list_dic)

col = ["enseigne", "produit", "quantite", "prix"]
df_list_list = pd.DataFrame(data_list2, columns=col)
print("-----------------sous forme de lignes : a partir d'une liste à liste --------")
print(df_list_list)

# Vérif 
verif = df_list_dic.equals(df_list_list)
print(verif)

df = df_list_list

print(df.iloc[0])  # Sélectionner les données de la première ligne.
print()
print(df.loc[:, 'prix'])  # électionner toutes les données de la colonne “prix”.
print(df.loc[df["enseigne"]=='Carrefour']) # Sélectionner les lignes correspondant à l’enseigne “Carrefour” uniquement."
print(df.loc[df['produit']=='01.1.1', "quantite"]) # Sélectionner les quantités achetées pour les produits classifiés “01.1.1” .
print(df.loc[:, ['enseigne', 'prix']]) # col enseigne et prix pour toutes les lignes