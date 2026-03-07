'''pd.merge(df1,df2,on="Column_name",how="type of join")
inner = An inner join returns only the rows where the key values are common in both DataFrames.
outer = An outer join returns all rows from both DataFrames.
left = A left join returns all rows from the left DataFrame and the matched rows from the right DataFrame.
right = A right join returns all rows from the right DataFrame and the matched rows from the left DataFrame.'''


import pandas as pd

df1 = pd.DataFrame({
    "ID":[1,2,3],
    "Name":["Ajay","Yash","Sushant"]
})

df2 = pd.DataFrame({
    "ID":[1,2,4],
    "Salary":[25000,30000,40000]
})

result = pd.merge(df1, df2, on="ID",how="inner")

print(result)
print("----------------------------------------------------------")

import pandas as pd

df1 = pd.DataFrame({
    "ID":[1,2,3],
    "Name":["Ajay","Yash","Sushant"]
})

df2 = pd.DataFrame({
    "ID":[1,2,4],
    "Salary":[25000,30000,40000]
})

result = pd.merge(df1, df2, on="ID",how="outer")

print(result)

print("-----------------------------------------------------------")

import pandas as pd

df1 = pd.DataFrame({
    "ID":[1,2,3],
    "Name":["Ajay","Yash","Sushant"]
})

df2 = pd.DataFrame({
    "ID":[1,2,4],
    "Salary":[25000,30000,40000]
})

result = pd.merge(df1, df2, on="ID",how="left")

print(result)

print("---------------------------------------------------------------")

import pandas as pd

df1 = pd.DataFrame({
    "ID":[1,2,3],
    "Name":["Ajay","Yash","Sushant"]
})

df2 = pd.DataFrame({
    "ID":[1,2,4],
    "Salary":[25000,30000,40000]
})

result = pd.merge(df1, df2, on="ID",how="right")

print(result)