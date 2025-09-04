import pandas as pd

df = pd.read_csv("sales_data_sample.csv", encoding='latin1')

print(df.head(10))
print(df.tail(10))
print(df.head())#by default hame koi argu nahi diya tu 5 line tak value dega.
print(df.tail())#by default hame koi argu nahi diya tu 5 line tak value dega.