import pandas as pd
df = pd.read_csv('2005-19_Local_Authority_CO2_emissions.csv')

#df

print(df.shape)
print(df.describe())

print(df.columns.tolist())



#print(df)