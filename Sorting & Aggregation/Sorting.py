#Sorting Data
#Sorting Data 1 Column sort_values()
#df.sort_values(by="column name",True/False,inplace=True)

import pandas as pd
data = {
    "Name": ["Ajay", "Yash", "Sushant"],
    "Salary": [25000, 10000, 40000],
    "City": ["Sangli", "Satara", "Bangalore"]
}
df=pd.DataFrame(data)
print(df)
df.sort_values(by="Salary",ascending=False,inplace=True)
print(df)