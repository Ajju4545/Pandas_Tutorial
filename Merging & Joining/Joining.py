#df1.join(df2)

import pandas as pd
df1 = pd.DataFrame({
    "Name":["Ajay","Yash","Sushant"]
})

df2 = pd.DataFrame({
    "Salary":[25000,30000,40000]
})

result = df1.join(df2)

print(result)