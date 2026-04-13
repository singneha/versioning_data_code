import pandas as pd
from path import Path

data_dir=Path.cwd()/'data'/'data.csv'
print(data_dir)
df = pd.read_csv(data_dir)
print(df.head())