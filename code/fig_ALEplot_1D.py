"""
Created on  2024-06-13 16:15

@author: Sherlock
"""

import matplotlib.pyplot as plt
from PyALE import ale
from joblib import load
import pandas as pd
import time
# 记录开始时间
start_time = time.time()
# 设置全局字体
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.weight'] = 'bold'  # 设置字体加粗
plt.rcParams['font.size'] = 18  # 设置默认的字体大小
train = pd.read_csv(r'\data\m-s-train.csv')
# 假设你已经准备好特征数据 X 和目标变量 y
X = train[['Month', 'Lon', 'Lat', 'O3', 'TA', 'VPD', 'TP', 'SWC', 'PAR']]
y = train['sif']
# 加载保存的模型
model = load(r'\model\bsm-m-sif.pkl')   #m是玉米，w是小麦,根据
# 创建自定义的fig和ax对象
fig, ax = plt.subplots(figsize=(8, 6))  # 创建一个12x12英寸的图形
# 筛选特征数据
q5 = X['SWC'].quantile(0.05)
q95 = X['SWC'].quantile(0.95)
X_q = X[(X['SWC'] >= q5) & (X['SWC'] <= q95)]
# 1D - continuous - with 95% CI
ale_eff = ale(X=X_q,
              model=model,
              feature=["SWC"],
              grid_size=100,
              include_CI=True,
              C=0.95,
              fig=fig,  # 传入自定义的fig
              ax=ax)    # 传入自定义的ax
# 添加图例
plt.legend(fontsize='small')
# 修改轴名和图名

ax.set_xlabel("SWC",weight='bold')


# 调整图边缘空白
plt.tight_layout()
plt.style.use('default')
# 保存图形时指定DPI
fig.savefig(r'\pic\1d-sif\m-SWC.png', dpi=600)

# 展示图形
plt.show()

# 记录结束时间
end_time = time.time()
# 计算并显示运行时间
elapsed_time = end_time - start_time
print(f"运行时间: {elapsed_time:.2f} 秒")