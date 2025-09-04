import pandas as pd

df =pd.read_csv("employ.csv", encoding='latin1')
print(df)

#filter rows by applying condition for single row

fil = df[df["age"]>40]
print(fil)

#filter rows by applying condition for multiple rows
fil1 = df[(df["age"]>30) & (df["salary"]>5000)]
print(fil1)
 