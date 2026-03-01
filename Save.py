import pandas as pd

data={
    "Name":['Ajay','Yash','Sushant'],
    "Salary":[250000,33333,44444],
    "Place":['Sangli','Satara','Bengluru']
}

df=pd.DataFrame(data)

# df.to_csv("TEST.csv", index=False)
# df.to_json("TEST.json", index=False)
df.to_excel("TEST.xlsx", index=False)

print(df)