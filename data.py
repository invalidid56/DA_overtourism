import pandas as pd


df = pd.read_csv(
    '2018.csv',
    encoding='euc-kr'
)
print(df)