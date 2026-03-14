import pandas as pd

df =pd.read_csv("https://archive.ics.uci.edu/static/public/186/data.csv")

print(df.head())

subconjunto =df[df['quality'].isin([5,6,7])]

print(subconjunto.shape)