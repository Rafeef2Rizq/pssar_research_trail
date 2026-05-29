import pandas as pd
import json
# Load the dataset
df_researchers = pd.read_csv('Session_data/researchers.csv')
#CP1 researcher cleaning
# Explore
# print(df.head())
# print(df.info())
# print(df.isnull().sum())
# print(df.duplicated().sum())

#cleaning
#Filter
filtered = df_researchers[(df_researchers["is_active"] == True) & (df_researchers["h_index"] > 15)]
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
# df_funding_excel['amount_cad_clean']=pd.to_numeric(df_funding_excel['amount_cad'],errors='coerce')
# valid_funding=df_funding_excel[df_funding_excel['amount_cad_clean']>0]
# total_funding=valid_funding['amount_cad_clean'].sum()
# print('total funding in CAD:',total_funding)

# print('total funding in CAD:',str(total_funding))

# Merge all 3 files
merged=(
     df_researchers.merge(df_publication,on='researcher_id',how='left').merge(df_funding_excel,on='researcher_id',how='left')
)
inner_merged=(
     df_researchers.merge(df_publication,on='researcher_id',how='inner').merge(df_funding_excel,on='researcher_id',how='inner')
)
print('Left merged:',{len(merged)})
print('Inner merged:',{len(inner_merged)})

# cleaning function 
def clean_funding(df):
    df = df.copy()
    df["amount_cad"] = pd.to_numeric(df["amount_cad"], errors='coerce')
    df = df[df["amount_cad"] > 0]
    return df

def total_funding(df):
    cleaned = clean_funding(df)
    return cleaned["amount_cad"].sum()

df_funding_cleaning = clean_funding(df_funding_excel)
print('Total funding in CAD:', total_funding(df_funding_cleaning))

#Q1
real_publications=df_publication[df_publication["pub_id"] != "P_HIDDEN"]
top= (
     real_publications.
     groupby("researcher_id")["citations"].sum()
     .reset_index()
     .merge(df_researchers[["researcher_id","first_name","last_name"]],on="researcher_id",how="left")
     .sort_values(by="citations",ascending=False)
     .iloc[0]
)
print("Top Researcher:",top["first_name"],top["last_name"],"with",top["citations"],"citations")

# Q2
funding_by_field = (
    df_funding_cleaning
    .merge(df_researchers[["researcher_id","field"]], on="researcher_id")
    .groupby("field")["amount_cad"].sum()
    .sort_values(ascending=False)
)
print(f"Q2: ${funding_by_field.iloc[0]} — {funding_by_field.index[0]}")

# Q3
earliest_researcher =(
     df_researchers[df_researchers["is_active"] == True]
     .sort_values(by="joined_year")
     .iloc[0]
)
print("Q3: Earliest Active Researcher:",earliest_researcher["first_name"],earliest_researcher["last_name"],"joined in",earliest_researcher["joined_year"])