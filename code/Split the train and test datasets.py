"""
Created on  2025-05-08 16:33:20

@author: Sherlock
"""
import pandas as pd
import math

df = pd.read_csv(r"\wheat.csv")

train_dfs = []
test_dfs = []

for city in df['Month'].unique():
    city_data = df[df['Month'] == city]
    n = len(city_data)

    if n == 0:
        continue
    test_num = math.ceil(0.1 * n)
    test_num = min(test_num, n - 1) if n > 1 else 0

    if test_num <= 0:
        train_dfs.append(city_data)
        continue

    test_data = city_data.sample(n=test_num, random_state=42)
    train_data = city_data.drop(test_data.index)

    train_dfs.append(train_data)
    test_dfs.append(test_data)

# 合并数据并保存
train_df = pd.concat(train_dfs)
test_df = pd.concat(test_dfs)

train_df.to_csv(r"\train-wheat.csv", index=False)
test_df.to_csv(r"\test-wheat.csv", index=False)