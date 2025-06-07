import pandas as pd
import regex as re

df = pd.read_csv('new_output/classifications_4.csv')

#parsed = pd.read_csv('output/processed_dataset_2.csv')



#df = df.merge(parsed[['id','cleaned_cl_marem','cleaned_cl_marco','cleaned_cl_ale']].drop_duplicates())
df.output = df.output.apply(lambda x:x.split('Output')[-1])
df['pattern'] = df['05']+'|'+df['01']+'|'+df['02']


def parse_output(a,b):
    try:
        output = re.search(a,b).group()
    except: output = None

    return output

df['parsed_output'] = df.apply(lambda x:parse_output(x.pattern,x.output),axis=1)
df = df.dropna().drop_duplicates(subset=['id','05','01','02'])

l = list()

for _,item in df.iterrows():
    if item.parsed_output==item['05']:
        l.append('marem')
    elif item.parsed_output==item['01']:
        l.append('marco')
    else:
        l.append('ale')

df['label'] = l
df.to_csv('new_output/parsed_output_4.csv',index=False)