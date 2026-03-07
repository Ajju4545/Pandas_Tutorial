# If you want arranging Age in descending order then firstly all Salary will be same

import pandas as pd
data = {
    "Name": ["Ajay", "Yash", "Sushant"],
    "Salary": [10000, 10000, 10000],
    "Age": [19, 70, 50]
}
df=pd.DataFrame(data)
print(df)
df.sort_values(by=["Salary","Age"],ascending=[True,False],inplace=True)
print(df)