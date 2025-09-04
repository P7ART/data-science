import pandas as pd

df =pd.read_csv("employ.csv", encoding='latin1')
print(df)

# cel=df["name"]#single column ko select karne ke liye
# print(cel)

# multiple column selection
cel=df[["name","age"]]#multiple column ko select karne ke liye
print(cel)

