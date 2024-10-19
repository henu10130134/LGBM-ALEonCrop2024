"""
Created on  2024-08-05 18:08

@author: Sherlock
"""

import pickle
import pandas as pd
from sklearn.model_selection import KFold
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import numpy as np

# 加载模型
model_path = r'\model\bsm-m-sif.pkl'
with open(model_path, 'rb') as file:
    model = pickle.load(file)

# 读取数据
data = pd.read_csv(r'\data\m-s-train.csv')
X = data[['Month', 'Lon', 'Lat', 'O3', 'TA', 'VPD', 'TP', 'SWC', 'PAR']]
y = data['sif']

# 设置10折交叉验证
kf = KFold(n_splits=10, shuffle=True, random_state=42)

# 初始化存储分数的列表
r2_scores_train = []
r2_scores_test = []
rmse_scores = []
mse_scores = []
mae_scores = []

# 执行10折交叉验证
for fold, (train_index, test_index) in enumerate(kf.split(X), start=1):
    X_train, X_test = X.iloc[train_index], X.iloc[test_index]
    y_train, y_test = y[train_index], y[test_index]

    # 训练模型
    model.fit(X_train, y_train)

    # 预测
    y_pred_train = model.predict(X_train)
    y_pred_test = model.predict(X_test)

    # 计算分数
    r2_train = r2_score(y_train, y_pred_train)
    r2_test = r2_score(y_test, y_pred_test)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred_test))
    mse = mean_squared_error(y_test, y_pred_test)
    mae = mean_absolute_error(y_test, y_pred_test)

    # 存储分数
    r2_scores_train.append(r2_train)
    r2_scores_test.append(r2_test)
    rmse_scores.append(rmse)
    mse_scores.append(mse)
    mae_scores.append(mae)

    # 打印每个折的结果
    print(f"Fold {fold} Results:")
    print(f"Train R² Score: {r2_train:.4f}")
    print(f"Val R² Score: {r2_test:.4f}")
    print(f"RMSE: {rmse:.4f}")
    print(f"MSE: {mse:.4f}")
    print(f"MAE: {mae:.4f}")

# 计算并打印平均分数
print("Average Scores:")
print(f"Average Train R²: {np.mean(r2_scores_train):.4f}")
print(f"Average Val R²: {np.mean(r2_scores_test):.4f}")
print(f"Average RMSE: {np.mean(rmse_scores):.4f}")
print(f"Average MSE: {np.mean(mse_scores):.4f}")
print(f"Average MAE: {np.mean(mae_scores):.4f}")