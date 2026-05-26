import pandas as pd
import json
# Load the dataset
df = pd.read_csv('Session_data/researchers.csv')
#CP1 researcher cleaning
# Explore
# print(df.head())
# print(df.info())
# print(df.isnull().sum())
# print(df.duplicated().sum())

#cleaning
#Filter
filtered = df[(df["is_active"] == True) & (df["h_index"] > 15)]
#sort
filtered=filtered.sort_values(by="joined_year",ascending=True)
letters=filtered["last_name"].str[0]
word="".join(letters)
print(word)

#CP2  publication cleaning


# print(df_json.head())
# print(df_json.info())
# print(df_json.isnull().sum())
# print(df_json.duplicated().sum())

#cleaning publication
with open('Session_data/publications.json') as f:
     publication=json.load(f)
     
df_publication=pd.json_normalize(publication)
top=df_publication.loc[df_publication['citations'].idxmax()]
     
print(top['title'])
print(top['citations'])
print(top['researcher_id'])

#CP3 funding cleaning
df_funding_excel=pd.read_excel('Session_data/funding.xlsx',dtype={'amount_cad':str})
df_funding_excel['amount_cad_clean']=pd.to_numeric(df_funding_excel['amount_cad'],errors='coerce')
valid_funding=df_funding_excel[df_funding_excel['amount_cad_clean']>0]
total_funding=valid_funding['amount_cad_clean'].sum()
print('total funding in CAD:',total_funding)

print('total funding in CAD:',str(total_funding))
