# we remove particular Columns at the dataframe

import pandas as pd
data = {
    "Name": ["Ajay", "Yash", "Sushant"],
    "Salary": [25000, 30000, 40000],
    "City": ["Sangli", "Satara", "Bangalore"]
}
df=pd.DataFrame(data)
print(df)
print("-------------------------------------")

# df.drop(columns= ["column name"],inplace=True)
df.drop(columns=["City"],inplace=True)
print(df)