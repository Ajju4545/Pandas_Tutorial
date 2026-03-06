import pandas as pd
data = {
    "Name": [None, "Yash", "Sushant"],
    "Salary": [25000, 30000,None],
    "City": ["Sangli", None, "Bangalore"]
}
df=pd.DataFrame(data)
print(df)
print("---------------------------")
print(df.isnull())
print("---------------------------")
print(df.isnull().sum())