"""
Created on  2025-05-08 16:26:26

@author: Sherlock
"""
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv(r"\nor-小麦-2d%.csv")
var_order = ['O3', 'CO2', 'PAR', 'TA', 'VPD', 'SWC', 'TP']
def custom_sort(feature):
    if '-' not in feature:
        return (len(var_order), feature)
    parts = feature.split('-')
    idx1 = var_order.index(parts[0]) if parts[0] in var_order else len(var_order)
    idx2 = var_order.index(parts[1]) if parts[1] in var_order else len(var_order)
    return (min(idx1, idx2), max(idx1, idx2))
df_sorted = df.copy()
df_sorted['sort_key'] = df_sorted['fea'].apply(custom_sort)
df_sorted = df_sorted.sort_values('sort_key').drop('sort_key', axis=1)

plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.weight'] = 'bold'
plt.rcParams['font.size'] = 16
plt.rcParams['mathtext.fontset'] = 'custom'
plt.rcParams['mathtext.rm'] = 'Times New Roman'
plt.rcParams['mathtext.it'] = 'Times New Roman:italic'
plt.rcParams['mathtext.bf'] = 'Times New Roman:bold'
plt.figure(figsize=(8, 6))
colors = []
for fea in df_sorted['fea']:
    if fea.count('-') == 1:
        colors.append('#54B345')
    elif fea.count('-') == 2:
        colors.append('#8ab07d')
    else:
        colors.append('blue')

bars = plt.barh(df_sorted['fea'], df_sorted['dif'], color=colors)
plt.gca().invert_yaxis()
for idx, bar in enumerate(bars):
    if idx in [8]:
        plt.text(bar.get_width() - bar.get_width() * 0.05, bar.get_y() + bar.get_height() / 2,
                 f'{bar.get_width():.2f}', va='center', ha='right', color='black')
    else:
        plt.text(bar.get_width(), bar.get_y() + bar.get_height() / 2,
                 f'{bar.get_width():.2f}', va='center')

plt.xlabel('ALE Range (ALE$_{max}$-ALE$_{min}$, ×10$^{-4}$ W m$^{-2}$ $\mu$m$^{-1}$ sr$^{-1}$)', fontsize=17,
           fontweight='bold')
plt.tight_layout()
ax = plt.gca()
for spine in ax.spines.values():
    spine.set_linewidth(1.5)
save_path = r"\2d-交互-小麦.png"
plt.savefig(save_path, dpi=600)
plt.show()


#=========================================================================================
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.patches import Patch
df = pd.read_csv(r"\nor-小麦-2d%.csv")
var_order = ['O3', 'CO2', 'PAR', 'TA', 'VPD', 'SWC', 'TP']
def custom_sort(feature):
    if '-' not in feature:
        return (len(var_order), feature)
    parts = feature.split('-')
    idx1 = var_order.index(parts[0]) if parts[0] in var_order else len(var_order)
    idx2 = var_order.index(parts[1]) if parts[1] in var_order else len(var_order)
    return (min(idx1, idx2), max(idx1, idx2))
df_sorted = df.copy()
df_sorted['sort_key'] = df_sorted['fea'].apply(custom_sort)
df_sorted = df_sorted.sort_values('sort_key').drop('sort_key', axis=1)

plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.weight'] = 'bold'
plt.rcParams['font.size'] = 14
plt.rcParams['mathtext.fontset'] = 'custom'
plt.rcParams['mathtext.rm'] = 'Times New Roman'
plt.rcParams['mathtext.it'] = 'Times New Roman:italic'
plt.rcParams['mathtext.bf'] = 'Times New Roman:bold'
fig, ax = plt.subplots()
fig.patch.set_facecolor('white')
ax.set_facecolor('white')
ax.barh(df['fea'], df['max'], color='#86c166', label='Positive', alpha=1)
ax.barh(df['fea'], df['min'], color='#e9cd4c', label='Negative', alpha=1)
ax.axvline(0, color='black', linewidth=1)
plt.legend(fontsize='large')
plt.xlabel(r'ALE Value (ALE$_{max/min}$, ×10$^{-4}$ W m$^{-2}$ $\mu$m$^{-1}$ sr$^{-1}$)', fontsize=15,fontweight='bold')   #(×0.0001 W m$^{-2}$ $\mu$m$^{-1}$ sr$^{-1}$)
for spine in ax.spines.values():
    spine.set_color('black')
    spine.set_linewidth(1)
legend_handles = [Patch(facecolor='#e9cd4c', label='Negative'),
                  Patch(facecolor='#86c166', label='Positive')]
plt.legend(handles=legend_handles, loc=(0.02, 0.01), fontsize=14)
ax.tick_params(axis='y', labelsize=13)
plt.tight_layout()
fig.savefig(r"\2d-小麦-正负.png", dpi=600)
plt.show()