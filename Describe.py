import pandas as pd
data={
    "Name":['Ajay','Sushant','Yash','Neha','Sanika','Krishna','Rohit','Virat','ABD','Jassi'],
    'Age':[19,20,21,22,23,24,38,37,36,29],
    'Score':[99,23,45,65,67,66,90,78,89,91],
    'Salary':[10000,20000,30000,40000,50000,60000,70000,80000,90000,100000]
}
df=pd.DataFrame(data)
print('Sample Data')
print(df)

print('Descriptive Statistics')
print(df.describe())