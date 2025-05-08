"""
Created on  2025-05-08 16:29:52

@author: Sherlock
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
excel_file = (r"\heat-小麦.xlsx")
df = pd.read_excel(excel_file, index_col=0)
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.weight'] = 'bold'
plt.rcParams['font.size'] = 22

plt.figure(figsize=(10, 8))
ax = sns.heatmap(df, annot=True, fmt='.2f', cmap='YlGn', linewidths=1, linecolor='black')
ax.tick_params(axis='y', rotation=0)
ax.tick_params(axis='x', rotation=45)
cbar = ax.collections[0].colorbar
cbar.set_label('ALE Normalized Percentage (%)', fontsize=20,fontweight='bold', rotation=270, labelpad=15)
cbar.outline.set_edgecolor('black')
cbar.outline.set_linewidth(1)
for _, spine in ax.spines.items():
    spine.set_visible(True)
    spine.set_color('black')
    spine.set_linewidth(1.5)
plt.tight_layout()
save_path = r"\heat-小麦.png"
plt.savefig(save_path, dpi=600)
plt.show()