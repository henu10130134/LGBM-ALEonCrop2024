"""
Created on  2025-05-08 16:16:58

@author: Sherlock
"""

import pandas as pd
import os

folder_path = r"\w-csv-1d"
result_data = []
for filename in os.listdir(folder_path):
    if filename.endswith('.csv'):
        file_path = os.path.join(folder_path, filename)
        df = pd.read_csv(file_path)

        if 'eff' in df.columns:
            min_value = df['eff'].min()
            max_value = df['eff'].max()
            first_column_name = df.columns[0]
            row_min = df[df['eff'] == min_value].iloc[0]
            row_max = df[df['eff'] == max_value].iloc[0]
            fea_min = row_min[first_column_name]
            fea_max = row_max[first_column_name]
            file_name_without_extension = os.path.splitext(filename)[0]
            result_data.append({
                'fea': file_name_without_extension,
                'fea-min': fea_min,
                'min': min_value,
                'fea-max': fea_max,
                'max': max_value,
            })
result_df = pd.DataFrame(result_data)
output_file = r"\小麦-1d.csv"
result_df.to_csv(output_file, index=False)
print("完成，最大值和最小值已经保存到", output_file)

#==========================================================

all_rows = []
folder_path = r"\w-csv-2d"
for filename in os.listdir(folder_path):
    if filename.endswith('.csv'):
        csv_path = os.path.join(folder_path, filename)
        df = pd.read_csv(csv_path, index_col=0)
        min_val = df.min().min()
        max_val = df.max().max()
        min_pos = df.stack().idxmin()
        max_pos = df.stack().idxmax()
        min_row, min_col = min_pos
        max_row, max_col = max_pos
        new_row = {
            'fea': filename.split('.')[0],
            'min': min_val,
            'max': max_val,
            'x-min': min_row,
            'y-min': min_col,
            'x-max': max_row,
            'y-max': max_col
        }
        all_rows.append(new_row)
result_df = pd.DataFrame(all_rows)
result_df.to_csv(r"\小麦-2d.csv", index=False)
print("完成，最大值和最小值已经保存到2d")
