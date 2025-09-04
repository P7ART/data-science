import pandas as pd

# data = pd.read_csv('sales_data_sample.csv', encoding='latin1')
da = pd.read_json('sample_Data.json')
print(da)
f = pd.read_excel("SampleSuperstore.xlsx")
print(f)

