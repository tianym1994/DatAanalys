import pandas as pd
load='./data/foodInformation.csv'
df=pd.read_csv(load)
df.dropna(inplace=True)
df['food']=df['food'].str.lower()
df['ounces']=df['ounces'].apply(lambda a: abs(a))
df['ounces'].fillna(df['ounces'].mean(),inplace=True)
df.drop_duplicates('food',inplace=True)
df.reset_index(drop=True,inplace=True)
print(df)