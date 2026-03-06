# loc selects data using row label and column name.
# Row Label(Index) and Column Name

import pandas as pd
data = {
    "Name": ["Ajay", "Yash", "Sushant"],
    "Salary": [25000, 30000, 40000],
    "City": ["Sangli", "Satara", "Bangalore"]
}
df=pd.DataFrame(data)
print(df)

print(df.loc[1,"Salary"])





