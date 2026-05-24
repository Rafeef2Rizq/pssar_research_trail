import pandas as pd

# Load the dataset
df = pd.read_csv('Session_data/researchers.csv')

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

#publication cleaning
df_json=pd.read_json('Session_data/publications.json')
# print(df_json.head())
# print(df_json.info())
# print(df_json.isnull().sum())
# print(df_json.duplicated().sum())

#cleaning publication
top_result = df_json.loc[df_json["citations"].idxmax()]
print(top_result)