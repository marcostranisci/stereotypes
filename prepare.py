import pandas as pd
import numpy as np

ale_stereotypes = pd.read_csv("./data/stereotipi_parsati_clusterizzati_ALE - stereotipi_parsati_clusterizzati_ALE.csv")
joined = pd.read_csv("./data/joinedClusterizzatiHS.csv")

ale_stereotypes = ale_stereotypes.rename(columns={"cluster N=10":"cluster_10_nome_ale", "cluster N=5":"cluster_5_nome_ale", "stereotipi":"annotazioni_parsate"})

print("joined shape before merging: ", joined.shape)
joined = joined.merge(ale_stereotypes[["annotazioni_parsate", "cluster_10_nome_ale", "cluster_5_nome_ale"]], on="annotazioni_parsate", how="left")
print("joined shape after merging: ",joined.shape)
joined.to_csv("./data/datasetStereotype.csv")

# Information about the dataset
print("\n")
print("Number of annotations:", joined.shape)
print("Number of texts:",len(set(joined["id"].tolist())))
print("Number of annotations per annotator")
print(joined["annotatore"].value_counts())
print()
print("Number of texts annotate by each annotator")
print(joined.groupby("annotatore")["id"].count())


print("\n")
count_empty_unique = (ale_stereotypes["occorrenze"] == 1).sum()
count_full_unique = (len((ale_stereotypes["occorrenze"].tolist())))
count_empty = (joined["cluster_10_marem"].isnull()).sum()

print("Number texts where the parsed annotations had 1 occurrence:",count_empty_unique, "on a total of: ", count_full_unique)
print("Number empty clusters:",count_empty)


df = joined.dropna(subset=["cluster_10_marem"])
df = df[df["cluster_10_nome_ale"] !='None/Doubt']
df = df[df["cluster_5_nome_ale"] !='None/Doubt']

print("Dataframe without empty clusters", df.shape)
df_on10 = df.drop_duplicates(subset=["id", "cluster_10_nome_marem", "cluster_10_nome_ale", "cluster_10_nome_marco"])
print("Dataframe based on 10 clusters", df_on10.shape)
df_on10.to_csv("./data/data_on10.csv")
df_on5 = df.drop_duplicates(subset=["id", "cluster_5_nome_marem", "cluster_5_nome_ale", "cluster_5_nome_marco"])
print("Dataframe based on 5 clusters", df_on5.shape)
df_on5.to_csv("./data/data_on5.csv")






