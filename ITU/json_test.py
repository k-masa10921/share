import json
import pandas as pd
import matplotlib.pyplot as plt
file_name = input("write filename:")
df = pd.read_json(file_name)
print(df)
df.describe()
target =input("target:")
df_target = df[target]
print(df_target)

