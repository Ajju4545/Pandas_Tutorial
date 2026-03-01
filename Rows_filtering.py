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
print('-----------------------------------')

# 1st Salary Rows Filtering
high_salary = df[df['Salary']>50000]['Salary']
print('Salary is greater than 50k ')
print(high_salary)
print('-------------------------------------------')

# 2nd Score Rows Filtering
low_score = df[df['Score']<50]['Score']
print('The Lowest score')
print(low_score)
print('--------------------------------------------------')

# This is AND Condition
# Filtering Rows Salary>50k and Score<80
filtered = df[(df['Salary']>50000) & (df['Score']<80)]
print('Salary>50k   + Score<50')
print(filtered)
print('------------------------------------------------------------------')

# This is OR Condition
# Filtering Rows 
filtered_or = df[(df['Age']>24) | (df['Score']>80)]
print('Employees Age Greater Than 24 and Score is Greater Than 80')
print(filtered_or)
print('---------------------------')
