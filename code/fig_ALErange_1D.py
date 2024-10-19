"""
Created on  2024-07-10 22:44

@author: Sherlock
"""



# 1d绘制条形图-m-玉米
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.weight'] = 'bold'  # 设置字体加粗
plt.rcParams['font.size'] = 22  # 设置默认的字体大小
plt.rcParams['mathtext.fontset'] = 'custom'
plt.rcParams['mathtext.rm'] = 'Times New Roman'
plt.rcParams['mathtext.it'] = 'Times New Roman:italic'
plt.rcParams['mathtext.bf'] = 'Times New Roman:bold'
# 读取CSV文件
df = pd.read_csv(r'\data\nor-1d-玉米%.csv')  # 玉米
# 按照列的值对数据进行排序
df_sorted = df.sort_values(by='dif', ascending=False)
# 绘制条形图
plt.figure(figsize=(8, 6))
# 检查'fea'列中'-'的数量，并根据'-'后的内容设置颜色
colors = []
for fea in df_sorted['fea']:
    if fea.count('-') == 1:
        # 获取'-'后的内容
        post_dash_content = fea.split('-')[-1]
        # 根据'-'后的内容设置颜色
        if post_dash_content in ['O3', 'TA', 'TP', 'SWC']:
            colors.append('#8ab07d')
        elif post_dash_content == 'VPD':
            colors.append('#e9c46b')
        elif post_dash_content in ['PAR']:
            colors.append('#2a9d8c')
        else:
            colors.append('grey')   # 如果不符合任何条件，设置为灰色或其他默认颜色
    else:
        colors.append('#8ECFC9')       # 如果'-'的数量不是1，设置为灰色或其他默认颜色
# 使用指定的颜色绘制条形图
bars = plt.barh(df_sorted['fea'], df_sorted['dif'], color=colors)
# 将y轴反转，使得最大值在上方
plt.gca().invert_yaxis()
# 在条形图的每个条带上添加对应的数字
for idx, bar in enumerate(bars):
    if idx in [0, 1]:  # 对于最上面的条带，将文本放在条带内部
        plt.text(bar.get_width() - bar.get_width()*0.05, bar.get_y() + bar.get_height()/2,
                 f'{bar.get_width():.2f}', va='center', ha='right', color='black')
    else:
        plt.text(bar.get_width(), bar.get_y() + bar.get_height()/2,
                 f'{bar.get_width():.2f}', va='center')
# 创建图例句柄
legend_handles = [Patch(facecolor='#2a9d8c', label='Increasing Trend'),
                  Patch(facecolor='#8ab07d', label='Non-Monotonic'),
                  Patch(facecolor='#e9c46b', label='Decreasing Trend')]
# 设置横轴名称
plt.xlabel('ALE Range (ALE$_{max}$-ALE$_{min}$, ×10$^{-4}$ W m$^{-2}$ $\mu$m$^{-1}$ sr$^{-1}$)', fontsize=20,fontweight='bold')
# 添加图例到图表，自由调整图例位置
plt.legend(handles=legend_handles, loc=(0.5, 0.05), fontsize='small')
# 调整布局以防止图例被截断
plt.tight_layout()
# 设置坐标轴框线粗细
ax = plt.gca()  # 获取当前的Axes对象ax
for spine in ax.spines.values():
    spine.set_linewidth(1.5)  # 设置边框线宽度为2
# 图片保存路径
save_path = r'\pic\1d-玉米-主效应排序.png'
# 在显示图表之前保存图表
plt.savefig(save_path, dpi=600)
# 显示图表
plt.show()




# 1d绘制条形图-w-小麦
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
# 设置全局字体为Times New Roman
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.weight'] = 'bold'  # 设置字体加粗
plt.rcParams['font.size'] = 22  # 设置默认的字体大小
plt.rcParams['mathtext.fontset'] = 'custom'
plt.rcParams['mathtext.rm'] = 'Times New Roman'
plt.rcParams['mathtext.it'] = 'Times New Roman:italic'
plt.rcParams['mathtext.bf'] = 'Times New Roman:bold'
# 读取CSV文件
df = pd.read_csv(r'\data\nor-1d-小麦%.csv')
# 按照列的值对数据进行排序
df_sorted = df.sort_values(by='dif', ascending=False)
# 绘制条形图
plt.figure(figsize=(8, 6))
# 检查'fea'列中'-'的数量，并根据'-'后的内容设置颜色
colors = []
for fea in df_sorted['fea']:
    if fea.count('-') == 1:
        # 获取'-'后的内容
        post_dash_content = fea.split('-')[-1]
        # 根据'-'后的内容设置颜色
        if post_dash_content in ['O3', 'SWC', 'TP', 'TA']:
            colors.append('#8ab07d')
        elif post_dash_content in ['VPD']:
            colors.append('#e9c46b')
        elif post_dash_content in ['PAR']:
            colors.append('#2a9d8c')
        else:
            colors.append('grey')   # 如果不符合任何条件，设置为灰色或其他默认颜色
    else:
        colors.append('#8ECFC9')       # 如果'-'的数量不是1，设置为灰色或其他默认颜色
# 使用指定的颜色绘制条形图
bars = plt.barh(df_sorted['fea'], df_sorted['dif'], color=colors)
# 将y轴反转，使得最大值在上方
plt.gca().invert_yaxis()
# 在条形图的每个条带上添加对应的数字
for idx, bar in enumerate(bars):
    if idx in [0, 1]:  # 对于最上面的条带，将文本放在条带内部
        plt.text(bar.get_width() - bar.get_width()*0.05, bar.get_y() + bar.get_height()/2,
                 f'{bar.get_width():.2f}', va='center', ha='right', color='black')
    else:
        plt.text(bar.get_width(), bar.get_y() + bar.get_height()/2,
                 f'{bar.get_width():.2f}', va='center')
# 创建图例句柄
legend_handles = [Patch(facecolor='#2a9d8c', label='Increasing Trend'),
                  Patch(facecolor='#8ab07d', label='Non-Monotonic'),
                  Patch(facecolor='#e9c46b', label='Decreasing Trend')]
# 设置横轴名称
plt.xlabel('ALE Range (ALE$_{max}$-ALE$_{min}$, ×10$^{-4}$ W m$^{-2}$ $\mu$m$^{-1}$ sr$^{-1}$)', fontsize=20,fontweight='bold')
# 添加图例到图表，自由调整图例位置
plt.legend(handles=legend_handles, loc=(0.5, 0.05), fontsize='small')
# 调整布局以防止图例被截断
plt.tight_layout()
# 设置坐标轴框线粗细
ax = plt.gca()  # 获取当前的Axes对象ax
for spine in ax.spines.values():
    spine.set_linewidth(1.5)  # 设置边框线宽度为2
# 图片保存路径
save_path = r'\pic\1d-小麦-主效应排序.png'
# 在显示图表之前保存图表
plt.savefig(save_path, dpi=600)
# 显示图表
plt.show()
