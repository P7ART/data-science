import pandas as pd

df =pd.read_csv("employ.csv", encoding='latin1')

#iss attributes ham row*column  ki value milegi kitni rows and kitne columns
print(f"total rows and columns are {df.shape}")


# iss attributes se hame data ke andar  columns ke name milte 

print(f"column ame:{df.columns}")