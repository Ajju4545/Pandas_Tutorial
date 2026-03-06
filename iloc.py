# iloc uses row position and column position.
# Row No and Column No

import pandas as pd
data = {
    "Name": ["Ajay", "Yash", "Sushant"],
    "Salary": [25000, 30000, 40000],
    "City": ["Sangli", "Satara", "Bangalore"]
}
df=pd.DataFrame(data)
print(df)

print(df.iloc[0,2])