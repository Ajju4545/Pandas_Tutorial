# DataFrame = Multiple Columns (Table Format)
# Rows + Column Wise Data

import pandas as pd

data = {
    "Name": ["Ajay", "Yash", "Sushant"],
    "Salary": [25000, 30000, 40000],
    "City": ["Sangli", "Satara", "Bangalore"]
}

df = pd.DataFrame(data)
print(df)