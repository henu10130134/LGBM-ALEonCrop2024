"""
Created on  2024-07-10 22:38

@author: Sherlock
"""


# 绘制热图
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 读取Excel文件
excel_file = (r'\csv\heat-玉米.xlsx')  # 替换为你的Excel文件路径
df = pd.read_excel(excel_file, index_col=0)  # 假设第一列是索引列，也就是变量名
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.weight'] = 'bold'  # 设置字体加粗
plt.rcParams['font.size'] = 22  # 设置默认的字体大小

# 使用Seaborn绘制热图
plt.figure(figsize=(10, 8))  # 设置画布大小
ax = sns.heatmap(df, annot=True, fmt='.2f', cmap='YlGn', linewidths=1, linecolor='black')  # annot=True显示数值，fmt='.2f'设置数值格式，添加格线
# 设置轴刻度标签的位置
ax.tick_params(axis='y', rotation=0)  # 设置y轴标签水平显示
ax.tick_params(axis='x', rotation=0)  # 设置x轴标签垂直显示
# 添加颜色条标题
cbar = ax.collections[0].colorbar
cbar.set_label('ALE Normalized Percentage (%)', fontsize=20,fontweight='bold', rotation=270, labelpad=15)  # 设置颜色条标题，旋转270度，距离颜色条15
# 给颜色条添加黑色边框
cbar.outline.set_edgecolor('black')
cbar.outline.set_linewidth(1)
# 添加边框线，使图形封闭
for _, spine in ax.spines.items():
    spine.set_visible(True)
    spine.set_color('black')
    spine.set_linewidth(1.5)

# 保存图片到指定路径，设置分辨率为600dpi
plt.tight_layout()
save_path = r'\pic\heat-玉米.png'  # 替换为你想要保存图片的路径
plt.savefig(save_path, dpi=600)
# 显示图形
plt.show()