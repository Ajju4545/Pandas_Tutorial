# interpolate() is a Pandas function used to fill missing values (NaN) by estimating values from nearby data points.
# None = Fill estimate value

import pandas as pd
data = {
    "Time": [1,2,3],
    "Value": [25000,None, 40000],
    
}
df=pd.DataFrame(data)
print("Before interpolate")
print(df)
df['Value'] = df['Value'].interpolate(method="linear")
print('\n After interpolate')
print(df)
