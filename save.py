import pandas as pd

data = {
    "name": ["John", "Jane", "Jim", "Jill"],
    "age": [25, 30, 35, 40],
    "city": ["New York", "Los Angeles", "Chicago", "Houston"]
}
# hame raw given data ko dataframe me convert karega
df = pd.DataFrame(data)
print(df)

# save the dataframe to a csv,excel,json file 
df.to_csv("employee.csv")
df.to_json("employee.json")
df.to_excel("employee.xlsx")
print(df)

#agar dataframe me index use nahi karna hai tuh index false karega
df.to_csv("employ.csv",index=False)
df.to_json("employ.json", index=False)
df.to_excel("employ.xlsx",index=False)
print(df)


