import pandas as pd
df=pd.read_json("Practice_Data.json")
print('Display First 10 Rows ')
print(df.head())  #  If i Doesn't pass any number in paranthesis then by default 5 rows print

print('Display Last 10 Rows ')
print(df.tail())
