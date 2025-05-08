"""
Created on  2025-05-08 16:33:41

@author: Sherlock
"""
from sklearn.model_selection import train_test_split, KFold
import pickle
import lightgbm as lgb
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from tqdm import tqdm

train = pd.read_csv(r"\train-wheat.csv")
X = train[['Month', 'Lon', 'Lat', 'O3', 'TA', 'VPD', 'TP', 'SWC', 'PAR', 'CO2']]
y = train['sif']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

n_splits = 10
kf = KFold(n_splits=n_splits, shuffle=True, random_state=42)

best_score = -np.inf
best_model = None

r2_scores = []
rmse_scores = []
mse_scores = []
mae_scores = []

for train_idx, test_idx in tqdm(kf.split(X), total=n_splits, desc="KFold Progress"):
    X_train_fold, X_test_fold = X.iloc[train_idx], X.iloc[test_idx]
    y_train_fold, y_test_fold = y.iloc[train_idx], y.iloc[test_idx]

    model = lgb.LGBMRegressor(objective='regression',
                              boosting_type='gbdt',
                              random_state= 1234,
                              learning_rate= 0.5,
                              n_estimators= 100,
                              max_depth= 5,
                              num_leaves= 10,
                              max_bin= 10,
                              subsample= 0.5,
                              colsample_bytree= 0.7,
                              reg_alpha= 0.3,
                              reg_lambda= 1.0,
                              min_split_gain= 0.01
                              )

    early_stopping_callback = lgb.early_stopping(stopping_rounds=1234, verbose=False)

    model.fit(X_train_fold, y_train_fold,
              eval_set=[(X_test_fold, y_test_fold)],
              eval_metric='rmse',
              callbacks=[early_stopping_callback])

    y_pred = model.predict(X_test_fold)
    r2 = r2_score(y_test_fold, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test_fold, y_pred))
    mse = mean_squared_error(y_test_fold, y_pred)
    mae = mean_absolute_error(y_test_fold, y_pred)

    r2_scores.append(r2)
    rmse_scores.append(rmse)
    mse_scores.append(mse)
    mae_scores.append(mae)

    if r2 > best_score:
        best_score = r2
        best_model = model

model_save_path = r"\bsm-wheat-sif.pkl"
with open(model_save_path, 'wb') as file:
    pickle.dump(best_model, file)

result_path = r"\model-wheat-10cv.txt"

output_content = f"""=== 10折交叉验证结果 ===
最佳单折R²: {best_score:.4f}

各折详细结果:
R²:  {[round(x, 4) for x in r2_scores]}
RMSE: {[round(x, 4) for x in rmse_scores]}
MSE:  {[round(x, 4) for x in mse_scores]}
MAE:  {[round(x, 4) for x in mae_scores]}

平均指标:
平均R²:   {np.mean(r2_scores):.4f}
平均RMSE: {np.mean(rmse_scores):.4f}
平均MSE:  {np.mean(mse_scores):.4f}
平均MAE:  {np.mean(mae_scores):.4f}"""

with open(result_path, 'w', encoding='utf-8') as f:
    f.write(output_content)

print(f"\nBest R² Score: {best_score:.4f}")
print("决定系数 R² (每折):", [round(x, 4) for x in r2_scores])
print("均方根误差 RMSE (每折):", [round(x, 4) for x in rmse_scores])
print("均方误差 MSE (每折):", [round(x, 4) for x in mse_scores])
print("绝对误差 MAE (每折):", [round(x, 4) for x in mae_scores])
print("\n平均结果:")
print(f"平均R²:  {np.mean(r2_scores):.4f}")
print(f"平均RMSE: {np.mean(rmse_scores):.4f}")
print(f"平均MSE:  {np.mean(mse_scores):.4f}")
print(f"平均MAE:  {np.mean(mae_scores):.4f}")


