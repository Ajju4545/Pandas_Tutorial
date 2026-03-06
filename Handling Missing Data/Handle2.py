# fillna() = It is used to replace missing values (NaN) with a specified value in a DataFrame
# Adding value in place of NaN or None

import pandas as pd

data = {
    "Name": [None, "Yash", "Sushant"],
    "Salary": [25000, 30000, None],
    "City": ["Sangli", "Satara", "Bangalore"]
}

df = pd.DataFrame(data)

print("Original DataFrame")
print(df)

# fill missing values
df.fillna({"Name": "Unknown", "Salary": 0}, inplace=True)
print("\n")
print(df)