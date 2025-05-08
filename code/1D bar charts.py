"""
Created on  2025-05-08 16:23:35

@author: Sherlock
"""

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.weight'] = 'bold'
plt.rcParams['font.size'] = 22
plt.rcParams['mathtext.fontset'] = 'custom'
plt.rcParams['mathtext.rm'] = 'Times New Roman'
plt.rcParams['mathtext.it'] = 'Times New Roman:italic'
plt.rcParams['mathtext.bf'] = 'Times New Roman:bold'

df = pd.read_csv(r"F:\1biye\re10\0328\ALE\csv_极值\nor-小麦-1d%.csv")
custom_order = ['O3', 'CO2', 'PAR', 'TA', 'VPD', 'SWC', 'TP']
def get_sort_key(feature):
    parts = feature.split('-')
    if len(parts) > 1:
        post_dash = parts[-1].upper()
        try:
            return custom_order.index(post_dash)
        except ValueError:
            return len(custom_order)
    return len(custom_order)
df_sorted = df.copy()
df_sorted['sort_key'] = df_sorted['fea'].apply(get_sort_key)
df_sorted = df_sorted.sort_values('sort_key')
df_sorted = df_sorted.drop('sort_key', axis=1)
plt.figure(figsize=(8, 6))
colors = []
for fea in df_sorted['fea']:
    if fea.count('-') == 1:
        post_dash_content = fea.split('-')[-1].upper()
        if post_dash_content in ['O3', 'TA', 'TP', 'SWC', 'CO2','VPD']:
            colors.append('#8ab07d')
        elif post_dash_content in []:
            colors.append('#e9c46b')
        elif post_dash_content in ['PAR']:
            colors.append('#2a9d8c')
        else:
            colors.append('grey')
    else:
        colors.append('#8ECFC9')
bars = plt.barh(df_sorted['fea'], df_sorted['dif'], color=colors)
plt.gca().invert_yaxis()
for idx, bar in enumerate(bars):
    if idx in [2]:
        plt.text(bar.get_width() - bar.get_width()*0.05, bar.get_y() + bar.get_height()/2,
                 f'{bar.get_width():.2f}', va='center', ha='right', color='black')
    else:
        plt.text(bar.get_width(), bar.get_y() + bar.get_height()/2,
                 f'{bar.get_width():.2f}', va='center')
legend_handles = [Patch(facecolor='#2a9d8c', label='Increasing Trend'),
                  Patch(facecolor='#8ab07d', label='Non-Monotonic'),
                  Patch(facecolor='#e9c46b', label='Decreasing Trend')]
plt.xlabel('ALE Range (ALE$_{max}$-ALE$_{min}$, ×10$^{-4}$ W m$^{-2}$ $\mu$m$^{-1}$ sr$^{-1}$)', fontsize=20,fontweight='bold')
plt.legend(handles=legend_handles, loc=(0.5, 0.01), fontsize='small')
plt.tight_layout()
ax = plt.gca()
for spine in ax.spines.values():
    spine.set_linewidth(1.5)
save_path = r"\1d-主效应-小麦.png"
plt.savefig(save_path, dpi=600)
plt.show()