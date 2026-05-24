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
