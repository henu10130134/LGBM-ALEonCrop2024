"""
Created on  2024-07-10 22:44

@author: Sherlock
"""


# 2d条形图
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
# 读取CSV文件
df = pd.read_csv(r'\csv\nor-2d-玉米%.csv')   # m/w
# 按照列的值对数据进行排序
df_sorted = df.sort_values(by='dif', ascending=False)
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.weight'] = 'bold'  # 设置字体加粗
plt.rcParams['font.size'] = 20  # 设置默认的字体大小
plt.rcParams['mathtext.fontset'] = 'custom'
plt.rcParams['mathtext.rm'] = 'Times New Roman'
plt.rcParams['mathtext.it'] = 'Times New Roman:italic'
plt.rcParams['mathtext.bf'] = 'Times New Roman:bold'
# 绘制条形图
plt.figure(figsize=(8, 6))
# 检查'fea'列中'-'的数量，并根据数量设置颜色
colors = []
for fea in df_sorted['fea']:
    if fea.count('-') == 1:
        colors.append('#54B345')
    elif fea.count('-') == 2:
        colors.append('#8ab07d')
    else:
        colors.append('blue')
# 使用指定的颜色绘制条形图
bars = plt.barh(df_sorted['fea'], df_sorted['dif'], color=colors)
# 将y轴反转，使得最大值在上方
plt.gca().invert_yaxis()
# 在条形图的每个条带上添加对应的数字
for idx, bar in enumerate(bars):
    if idx == 0:  # 对于最上面的条带，将文本放在条带内部
        plt.text(bar.get_width() - bar.get_width()*0.05, bar.get_y() + bar.get_height()/2,
                 f'{bar.get_width():.2f}', va='center', ha='right', color='black')
    else:
        plt.text(bar.get_width(), bar.get_y() + bar.get_height()/2,
                 f'{bar.get_width():.2f}', va='center')

plt.xlabel('ALE Range (ALE$_{max}$-ALE$_{min}$, ×10$^{-4}$ W m$^{-2}$ $\mu$m$^{-1}$ sr$^{-1}$)', fontsize=19,fontweight='bold')
# 调整布局以防止图例被截断
plt.tight_layout()
# 设置坐标轴框线粗细
ax = plt.gca()  # 获取当前的Axes对象ax
for spine in ax.spines.values():
    spine.set_linewidth(1.5)  # 设置边框线宽度为2
# 图片保存路径
save_path = r'\pic\2d-玉米-交互排序.png'
# 在显示图表之前保存图表
plt.savefig(save_path, dpi=600)
# 显示图表
plt.show()

