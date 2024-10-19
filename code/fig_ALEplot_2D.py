"""
Created on  2024-06-13 17:21

@author: Sherlock
"""

import matplotlib.pyplot as plt
from PyALE import ale
from joblib import load
import pandas as pd
# 设置全局字体
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.weight'] = 'bold'  # 设置字体加粗
plt.rcParams['font.size'] = 18  # 设置默认的字体大小
train = pd.read_csv(r'\data\m-s-train.csv')
# 假设你已经准备好特征数据 X 和目标变量 y
X = train[['Month', 'Lon', 'Lat', 'O3', 'TA', 'VPD', 'TP', 'SWC', 'PAR']]
y = train['sif']
features = ['O3', 'TA', 'VPD', 'TP', 'SWC', 'PAR']
# 加载保存的模型
model = load(r'\model\bsm-m-nirv.pkl')   #m是玉米，w是小麦 4次
# 创建自定义的fig和ax对象
fig, ax = plt.subplots(figsize=(8, 6))  # 创建一个12x12英寸的图形
# 筛选特征数据
q5_y = X['VPD'].quantile(0.05)      #8次
q95_y = X['VPD'].quantile(0.95)
q5_x = X['SWC'].quantile(0.05)
q95_x = X['SWC'].quantile(0.95)
X_q = X[(X['VPD'] >= q5_y) & (X['VPD'] <= q95_y) &
                (X['SWC'] >= q5_x) & (X['SWC'] <= q95_x)]
ale_eff = ale(X=X_q,
              model=model,
              feature=["VPD", "SWC"],        #1
              grid_size=100,
              fig=fig,  # 传入自定义的fig
              ax=ax)    # 传入自定义的ax

# 获取x轴和y轴的数据范围
x_range = ax.get_xlim()[1] - ax.get_xlim()[0]
y_range = ax.get_ylim()[1] - ax.get_ylim()[0]
# 设置轴的长宽比，使得横轴和纵轴长度相同
ax.set_aspect(abs(x_range/y_range))

# 修改轴名称和图名      #2
ax.set_ylabel("VPD")  # 设置y轴标签，对应feature前面那个
ax.set_xlabel("SWC")  # 设置x轴标签
#fig.suptitle("2D-ALE Plot of ", weight='bold')  # 设置图表标题       #3
# 获取ax中的Image对象，并设置色带
import matplotlib.colors as mcolors
for im in ax.get_images():
    # 获取数据的最大值和最小值
    data_min, data_max = im.get_clim()
    # 创建TwoSlopeNorm对象，以0为中心
    norm = mcolors.TwoSlopeNorm(vmin=data_min, vcenter=0., vmax=data_max)
    # 应用新的色彩映射和规范化
    im.set_cmap('rainbow')#'BrBG'
    im.set_norm(norm)
# 调整图边缘空白
plt.tight_layout()
# 保存图形时指定DPI
fig.savefig(r'\pic\2d-sif\m-VPD-SWC.png', dpi=600)

# 展示图形
plt.show()