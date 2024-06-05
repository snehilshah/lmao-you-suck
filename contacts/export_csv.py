import pandas as pd

# read a csv file into a DataFrame

df = pd.read_csv('contacts/OG.csv')


# read the NewMnNo column into a array
# agg_functions = {'NewMNo': 'first', 'MMobile': 'sum'}
# df_new = df.groupby(df['NewMNo']).aggregate(agg_functions)
df = df.groupby("ID", as_index=False).agg(lambda x: ','.join(x.tolist()))


new = df["MMobile"].str.split(" ", n=2, expand=True)
df["mobile_1"] = new[0]
df["mobile_2"] = new[1]


# series = pd.Series(df.MMobile)
# df_new = df_new[2].str.split(',', expand=True)


# df[['ID', 'model_0', 'model_1', 'model_2', 'model_3', 'model_4', 'model_5']]

print(df)
