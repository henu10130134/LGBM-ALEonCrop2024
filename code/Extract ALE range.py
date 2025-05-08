"""
Created on  2025-05-08 16:20:56

@author: Sherlock
"""
import pandas as pd
# df = pd.read_csv(r"F:\1biye\re10\0330\ALE\csv_极值\小麦-2d.csv")
df = pd.read_csv(r"F:\1biye\re10\0330\CATE_ALE\小麦-1d.csv")
# 计算差值
df['dif'] = df['max'] - df['min']
print(df)
df.to_csv(r"\差值-小麦-1d.csv", index=False)

df = pd.read_csv(r"\差值-小麦-1d.csv")
total_sum = df['dif'].sum()
df['nor_dif'] = (df['dif'] / total_sum)*100
df.to_csv(r"\nor-小麦-1d%.csv", index=False)
