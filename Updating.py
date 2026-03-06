# We update Some information at particular Row and Column wise

import pandas as pd
data = {
    "Name": ["Ajay", "Yash", "Sushant"],
    "Salary": [25000, 30000, 40000],
    "City": ["Sangli", "Satara", "Bangalore"]
}
df=pd.DataFrame(data)
print(df)
print("-------------------------------------")
# .loc[]
# df.loc[Row_index,"Column_name"] = New value
df.loc[0,"Salary"] = 111111
print(df)