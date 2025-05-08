"""
Created on  2025-05-08 16:33:49

@author: Sherlock
"""
import matplotlib.pyplot as plt
from PyALE import ale
from joblib import load
import pandas as pd
import time

start_time = time.time()

plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.weight'] = 'bold'
plt.rcParams['font.size'] = 18

train = pd.read_csv(r"\train-wheat.csv")
X = train[['Month', 'Lon', 'Lat', 'O3', 'TA', 'VPD', 'TP', 'SWC', 'PAR', 'CO2']]
y = train['sif']

model = load(r"\bsm-wheat-sif.pkl")

features = ['O3', 'TA', 'VPD', 'TP', 'SWC', 'PAR', 'CO2']

for feature in features:
    fig, ax = plt.subplots(figsize=(8, 6))
    q5 = X[feature].quantile(0.05)
    q95 = X[feature].quantile(0.95)
    X_q = X[(X[feature] >= q5) & (X[feature] <= q95)]
    ale_eff = ale(
        X=X_q,
        model=model,
        feature=[feature],
        grid_size=100,
        include_CI=True,
        C=0.95,
        fig=fig,
        ax=ax
    )
    ax.legend(fontsize=13)
    ax.set_xlabel(feature, weight='bold')
    ax.set_ylabel('ALE Effect (centered)', weight='bold')
    plt.tight_layout()
    fig.savefig(rf"\w-pic-1d\w-{feature}.png", dpi=600)
    ale_eff.to_csv(rf"\w-csv-1d\w-{feature}.csv", index=True)
    plt.close(fig)
end_time = time.time()
elapsed_time = end_time - start_time
print(f"运行时间: {elapsed_time:.2f} 秒")
