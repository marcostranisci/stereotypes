import pandas as pd
import random
import csv

#file = open('classifications_2.csv',mode='w')

'''writer = csv.DictWriter(file,fieldnames=['id','output'])
writer.writeheader()'''
def create_prompt(row):

  text = row["tweet"]
  opt_marem = row['cleaned_cl_marem']
  opt_marco = row['cleaned_cl_marco']
  opt_ale = row['cleaned_cl_ale']
  random.seed(16)
  list_options = [opt_marem, opt_marco, opt_ale]
  random.shuffle(list_options)

  instruction = {"prelude": "Ti viene fornita in input (Input) una frase estratta dai social media, insieme a tre possibili stereotipi (Opzioni).",
        "task": "Il tuo compito è individuare quale stereotipo è implicito nella frase, scegliendo tra le opzioni fornite." ,
        "instr": "Restituisci in output (Output) una singola opzione, sotto forma di lista Python (es. ['Opzione 1']).",
        "input": f"Input: {text}",
        "options": f"Opzioni: {list_options}",
        "output": "Output:"}

  prompt = f"{instruction['prelude']} {instruction['task']} {instruction['instr']}\n {instruction['input']}\n {instruction['options']}\n {instruction['output']}"

  return prompt


df = pd.read_csv("./data/data_on5.csv")
df = df[df["cluster_5_nome_ale"] != 'None/Doubt']
df = df[df["cluster_5_nome_ale"] != 'None/Doubt']

dict_marem =  {'SonoSfruttatori': "Sono degli sfruttatori",
               'SonoMinaccia': "Sono una minaccia",
               'RovinanoItalia': "Rovinano l'Italia",
               'SonoTutelati': "Sono tutelati",
               'SonoEstremistiReligiosi': "Sono degli estremisti religiosi"}

dict_marco =  {'SonoParassiti': "Sono dei parassiti",
               'SonoSubdoli': "Sono subdoli",
               'SonoImmorali': "Sono immorali",
               'SonoIncompatibiliConNoi': "Sono incompatibili con noi",
               'SonoProblema': "Sono un problema"}

dict_ale = {'FannoQuelloCheVoglionoSenzaContribuire':  "Fanno quello che vogliono senza contribuire",
            'SonoPericolosi': "Sono pericolosi",
            'PeggioranoLeNostreCondizioniDiVita': "Peggiorano le nostre condizioni di vita",
            'HannoCulturaDiversaDallaNostra': "Hanno una cultura diversa dalla nostra",
            'PortanoDegrado': "Portano degrado"}

df["cleaned_cl_marem"] = df["cluster_5_nome_marem"].map(dict_marem)
df["cleaned_cl_marco"] = df["cluster_5_nome_marco"].map(dict_marco)
df["cleaned_cl_ale"] = df["cluster_5_nome_ale"].map(dict_ale)


df = df [['id', 'annotatore', 'tweet', 'chunk', 'annotazione','annotazioni_parsate',
          'cleaned_cl_marem', 'cleaned_cl_marco', 'cleaned_cl_ale']]

dataset = df
print(len(dataset))

dataset["prompt"] = dataset.apply(create_prompt, axis=1)

dataset.to_csv('output/processed_dataset_2.csv',index=False)

'''import transformers
import torch
from tqdm import tqdm

model_id = "sapienzanlp/Minerva-7B-instruct-v1.0"  # Replace with a compatible model ID



# Initialize the pipeline.
pipeline = transformers.pipeline(
    "text-generation",
    model=model_id,
    device_map="auto",
    model_kwargs={"torch_dtype": torch.bfloat16},
)

# Input text for the model.
input_conv = [{"role": "user", "content": "Che tipo di stereotipo c'è in questo testo 'i migranti non vogliono lavorare'? Scegli tra: 1. sono pigri, 2. sono sfruttatori e 3. sono un fardello? Rispondi alla domanda con un numero tra 1 e 3"}]

for _,item in tqdm(dataset.iterrows(),total=len(dataset)):
  output = pipeline(
    item.prompt,
    max_new_tokens=15,
  )


  writer.writerow({'id':item.id,'output':output})'''