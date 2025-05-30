import pandas as pd
import regex as re

df = pd.read_csv('output/classifications.csv')

parsed = pd.read_csv('output/processed_dataset.csv')



df = df.merge(parsed[['id','cleaned_cl_marem','cleaned_cl_marco','cleaned_cl_ale']].drop_duplicates())
df.output = df.output.apply(lambda x:x.split('Output')[-1])
df['pattern'] = df.cleaned_cl_marem+'|'+df.cleaned_cl_marco+'|'+df.cleaned_cl_ale


def parse_output(a,b):
    try:
        output = re.search(a,b).group()
    except: output = None

    return output

df['parsed_output'] = df.apply(lambda x:parse_output(x.pattern,x.output),axis=1)
df = df.dropna().drop_duplicates(subset=['id','cleaned_cl_marem','cleaned_cl_marco','cleaned_cl_ale'])
df.to_csv('output/parsed_output.csv',index=False)