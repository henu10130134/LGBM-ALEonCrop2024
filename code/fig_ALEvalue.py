"""
Created on  2024-07-10 22:44

@author: Sherlock
"""

# 纵向正负条形图
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.patches import Patch
# 加载CSV文件
df = pd.read_csv(r'\csv\nor-2d-玉米%.csv')  # 替换玉米/小麦
# # 设置全局字体
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.weight'] = 'bold'  # 设置字体加粗
plt.rcParams['font.size'] = 17  # 设置默认的字体大小
plt.rcParams['mathtext.fontset'] = 'custom'
plt.rcParams['mathtext.rm'] = 'Times New Roman'
plt.rcParams['mathtext.it'] = 'Times New Roman:italic'
plt.rcParams['mathtext.bf'] = 'Times New Roman:bold'

fig, ax = plt.subplots()
# 设置背景为白色
fig.patch.set_facecolor('white')
ax.set_facecolor('white')
# 绘制水平条形图
ax.barh(df['fea'], df['max'], color='#86c166', label='Positive', alpha=1)
ax.barh(df['fea'], df['min'], color='#e9cd4c', label='Negative', alpha=1)
# 在x=0的位置添加黑色竖向网格线
ax.axvline(0, color='black', linewidth=1)
# 添加图例
plt.legend(fontsize='large')

plt.xlabel(r'ALE Value (ALE$_{max/min}$, ×10$^{-4}$ W m$^{-2}$ $\mu$m$^{-1}$ sr$^{-1}$)', fontsize=17,fontweight='bold')   #(×0.0001 W m$^{-2}$ $\mu$m$^{-1}$ sr$^{-1}$)

# 设置坐标轴为黑色2
for spine in ax.spines.values():
    spine.set_color('black')
    spine.set_linewidth(1)  # 设置边框线宽度为2

# 创建图例句柄
legend_handles = [Patch(facecolor='#e9cd4c', label='Negative'),
                  Patch(facecolor='#86c166', label='Positive')]

# 添加图例到图表，自由调整图例位置
plt.legend(handles=legend_handles, loc=(0.65, 0.02), fontsize=14)
# 设置 y 轴刻度标签的字体大小
ax.tick_params(axis='y', labelsize=16)
plt.tight_layout()
# # 保存图形
fig.savefig(r'\pic\2d-玉米-正负.png', dpi=600)
# 显示图形
plt.show()











