"""
Created on  2025-05-08 16:33:32

@author: Sherlock
"""
import lightgbm as lgb
import numpy as np
import pandas as pd
from sklearn.model_selection import KFold
from sklearn.metrics import r2_score, mean_squared_error
import optuna
from tqdm import tqdm
import joblib

train = pd.read_csv(r"\train-wheat.csv")
X = train[['Month', 'Lon', 'Lat', 'O3', 'TA', 'VPD', 'TP', 'SWC', 'PAR', 'CO2']]
y = train['sif']

def objective(trial):
    params = {
        'learning_rate': trial.suggest_uniform('learning_rate', 0.01, 0.1),
        'n_estimators': trial.suggest_int('n_estimators', 10, 2000),
        'max_depth': trial.suggest_int('max_depth', 3, 20),
        'num_leaves': trial.suggest_int('num_leaves', 10, 100),
        'max_bin': trial.suggest_int('max_bin', 50, 150),
        'subsample': trial.suggest_uniform('subsample', 0.5, 1.0),
        'colsample_bytree': trial.suggest_uniform('colsample_bytree', 0.5, 1.0),
        'reg_alpha': trial.suggest_uniform('reg_alpha', 0, 1.5),
        'reg_lambda': trial.suggest_uniform('reg_lambda', 0, 1.5),
        'min_split_gain': trial.suggest_uniform('min_split_gain', 0, 0.5)
    }

    kf = KFold(n_splits=10, shuffle=True, random_state=42)
    r2_test_scores = []

    for train_index, test_index in kf.split(X):
        X_train, X_test = X.iloc[train_index], X.iloc[test_index]
        y_train, y_test = y[train_index], y[test_index]

        model = lgb.LGBMRegressor(**params)
        model.fit(X_train, y_train)

        y_pred_train = model.predict(X_train)
        y_pred_test = model.predict(X_test)

        r2_train = r2_score(y_train, y_pred_train)
        r2_test = r2_score(y_test, y_pred_test)

        if abs(r2_train - r2_test) > 0.08:
            return np.inf

        r2_test_scores.append(r2_test)

    return np.mean(r2_test_scores)


study = optuna.create_study(direction='maximize')

n_trials = 1000
with tqdm(total=n_trials) as pbar:
    def update_progress_bar(_study, _trial):
        pbar.update(1)


    study.optimize(objective, n_trials=n_trials, callbacks=[update_progress_bar])

best_params = study.best_params
print("最优超参数：", best_params)

kf = KFold(n_splits=10, shuffle=True, random_state=42)
r2_scores = []
rmse_scores = []

for train_index, test_index in kf.split(X):
    X_train, X_test = X.iloc[train_index], X.iloc[test_index]
    y_train, y_test = y.iloc[train_index], y.iloc[test_index]

    model = lgb.LGBMRegressor(**best_params)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    r2 = r2_score(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))

    r2_scores.append(r2)
    rmse_scores.append(rmse)

avg_r2 = np.mean(r2_scores)
avg_rmse = np.mean(rmse_scores)

params_file_path = r"\超参数-train-wheat-sif.txt"
with open(params_file_path, 'w', encoding='utf-8') as f:
    f.write("=== 最优超参数 ===\n")
    for key, value in best_params.items():
        f.write(f"{key}: {value}\n")
    f.write("\n=== 评估结果 ===\n")
    f.write(f"平均R²: {avg_r2:.4f}\n")
    f.write(f"平均RMSE: {avg_rmse:.4f}\n")
    f.write(f"各折R²: {[round(x, 4) for x in r2_scores]}\n")
    f.write(f"各折RMSE: {[round(x, 4) for x in rmse_scores]}\n")

print("\n最优参数交叉验证评估结果：")
print(f"平均R²: {avg_r2:.4f}")
print(f"平均RMSE: {avg_rmse:.4f}")
print(f"各折R²: {[round(x, 4) for x in r2_scores]}")
print(f"各折RMSE: {[round(x, 4) for x in rmse_scores]}")

best_model = lgb.LGBMRegressor(**best_params)
best_model.fit(X, y)
joblib.dump(best_model, r"\train-wheat.pkl")