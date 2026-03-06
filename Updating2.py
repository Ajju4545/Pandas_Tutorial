import pandas as pd
data = {
    "Name": ["Ajay", "Yash", "Sushant"],
    "Salary": [25000, 30000, 40000],
    "City": ["Sangli", "Satara", "Bangalore"]
}
df=pd.DataFrame(data)
print(df)
print("-------------------------------------")

#Increasing Salary By 5 %
df["Salary"] = df["Salary"] * 5
print(df)