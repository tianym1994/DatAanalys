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

load2='./data/accountMessage.csv'
df2=pd.read_csv(load2)
df2['2'].fillna(int(df2['2'].mean()),inplace=True)
df2.dropna(inplace=True)
row_with_lbs=df2['3'].str.contains('lbs').fillna(False)
for i,lbs_row in df2[row_with_lbs].iterrows():
    weight=int(float(lbs_row['3'][:-3])/2.2)
    df2.at[i,'3']='{}kgs'.format(weight)
df2[['first_name','last_name']] = df2['1'].str.split(expand=True)
df2.drop('1', axis=1, inplace=True)
df2['first_name'].replace({r'[^\x00-\x7F]+':''}, regex=True, inplace=True)
df2['last_name'].replace({r'[^\x00-\x7F]+':''}, regex=True, inplace=True)
df2.drop_duplicates(['first_name','last_name'],inplace=True)
df2.drop('0',axis=1,inplace=True)
df2.drop('\t',axis=1,inplace=True)
df2.reset_index(drop=True,inplace=True)
print(df2)