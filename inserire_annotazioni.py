import owlready2
import rdflib
import pandas as pd
import spacy_udpipe

df = pd.read_csv('joinedClusterizzatiHS.csv')
onto = owlready2.get_ontology('stereotypes_KG.owl').load()
s = set()
df = df.fillna(0)


'''for row in df.iloc[:].values:
    txt = rdflib.BNode()
    tweet = onto['Tweet'](txt)
    tweet.hasId = row[0]
    tweet.hasText = row[2]
    tweet.containsHateSpeech = row[-7]
    tweet.containsIrony = row[-2]
    tweet.containsSarcasm = row[-1]
    x = onto['Cluster'](row[7]) if row[7] != 0 else None
    x = onto['Cluster'](row[8]) if row[8] != 0 else None
    x = onto['Cluster'](row[12]) if row[12] != 0 else None
    x = onto['Cluster'](row[13]) if row[13] != 0 else None
    #print(x)
    #print(tweet,tweet.hasId,tweet.hasText,tweet.containsHateSpeech)



onto.save('stereotypes_KG.owl')'''






#onto.save('stereotypes_KG.owl')

for item in onto.individuals():
    if item.chunk is not None:
        annot = df[df['annotazione']==item.hasFrame]
        for x in annot.iloc[:].values:
            item.includesAgent = onto[x[-2]] if x[-2] !=0 else None
            item.includesPatient = onto[x[-1]] if x[-1] !=0 else None

onto.save('stereotypes_KG.owl')




'''for item in onto.individuals():
    sliced = df[df['id']==item.hasId] if item.hasId else None
    if sliced is not None:
        for row in sliced.iloc[:].values:
            bnode = rdflib.BNode()
            ster = onto['Stereotype'](bnode)
            item.expresses.append(ster)
            ster.chunk = row[3]
            ster.hasFrame = row[4]
            ster.wasDerivedFrom = onto[row[1]]
            if row[7]!=0:
                ster.wasClusterizedAs.append(onto[row[7]])
                print(ster.wasClusterizedAs,ster.chunk,ster.hasFrame,ster.wasDerivedFrom)
            if row[8]!=0:
                ster.wasClusterizedAs.append(onto[row[8]])
            if row[12]!=0:
                ster.wasClusterizedAs.append(onto[row[12]])
            if row[13]!=0:
                ster.wasClusterizedAs.append(onto[row[13]])

onto.save('stereotypes_KG.owl')'''