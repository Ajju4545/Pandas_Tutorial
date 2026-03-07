'''df['Column name].mean()
   df['Column name].mean()
   df['Column name].mean()
   df['Column name].mean()'''


import pandas as pd
data = {
    "Name": ["Ajay", "Yash", "Sushant"],
    "Salary": [10000, 10000, 10000],
    "Age": [19, 70, 50]
}
df=pd.DataFrame(data)
print(df)

avg_Age=df['Age'].mean()
Min_values=df['Age'].min()
Max_values=df['Age'].max()
Sum=df['Age'].sum()

print(avg_Age)
print(Min_values)
print(Max_values)
print(Sum)