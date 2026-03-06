#dropna() = removes all rows containing missing values (None or NaN).
# Deleting rows and columns value 

import pandas as pd
data = {
    "Name": [None, "Yash", "Sushant"],
    "Salary": [25000, 30000,None],
    "City": ["Sangli","Satara","Bangalore"]
}
df=pd.DataFrame(data)
print(df)

df.dropna(inplace=True)
print(df)