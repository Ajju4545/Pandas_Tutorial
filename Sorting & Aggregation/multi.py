import pandas as pd
data = {
    "Name": ["Ajay", "Yash", "Sushant","Ram","AK"],
    "Salary": [100000,200000,30000,200000,100000],
    "Age": [19, 70, 50,70,19]
}
df=pd.DataFrame(data)
print(df)
multi_grouped = df.groupby(['Name','Salary'])['Age'].sum()
print(multi_grouped)