import pandas as pd

raw_data = {'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'], 
        'last_name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze'], 
        'age': [42, 52, 36, 24, 73], 
        'preTestScore': [4, 24, 31, 2, 3],
        'postTestScore': [25, 94, 57, 62, 70]}
df = pd.DataFrame(raw_data, columns = ['first_name', 'last_name', 'age', 'preTestScore', 'postTestScore'])
df

file_name = r"pandas_dataframe_output.csv"
df.to_csv(file_name)
# df.to_csv(r'pandas_dataframe_output.csv')


df = pd.read_csv(file_name)
print(df)

print('Min', df['age'].min())
print('Max', df['age'].max())
print('Mean', df['age'].mean())


