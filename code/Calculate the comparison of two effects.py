"""
Created on  2025-05-08 16:30:52

@author: Sherlock
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"\差值-小麦-2d.csv")
new_df = df[['fea', 'max', 'min','dif']]
new_df.to_csv(r"\热图-小麦-2d.csv", index=False)
#================================================================
file1 = r"\热图-小麦-1d.csv"
df1 = pd.read_csv(file1)
file2 = r"\热图-小麦-2d.csv"
df2 = pd.read_csv(file2)
merged_df = pd.merge(df1, df2, on=['fea', 'max', 'min','dif'], how='outer')
merged_df.to_csv(r"\heat-小麦.csv", index=False)
print('CSV files have been merged successfully!')
#===============================================================

df = pd.read_csv(r"F:\\1biye\\re10\\0328\\ALE\\csv_极值\\heat-小麦.csv")
df['dif_log_temp'] = np.log(df['dif'])
total = df['dif_log_temp'].sum()
df['dif_log'] = df['dif_log_temp'] / total * 100
df['dif_log-2'] = df['dif_log'].round(2)
df.drop('dif_log_temp', axis=1, inplace=True)
df.to_csv(r"\heat-小麦-ln%.csv", index=False)
