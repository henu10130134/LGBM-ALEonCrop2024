"""
Created on  2025-05-08 16:34:00

@author: Sherlock
"""
import matplotlib.pyplot as plt
from PyALE import ale
from joblib import load
import pandas as pd
import itertools

plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.weight'] = 'bold'
plt.rcParams['font.size'] = 18

train = pd.read_csv(r"\train-wheat.csv")
X = train[['Month', 'Lon', 'Lat', 'O3', 'TA', 'VPD', 'TP', 'SWC', 'PAR', 'CO2']]
y = train['sif']
model = load(r"\bsm-wheat-sif.pkl")
features = ['O3', 'CO2', 'PAR', 'TA', 'VPD', 'SWC', 'TP']
feature_pairs = list(itertools.combinations(features, 2))
for feature_x, feature_y in feature_pairs:
    fig, ax = plt.subplots(figsize=(8, 6))
    q5_x = X[feature_x].quantile(0.05)
    q95_x = X[feature_x].quantile(0.95)
    q5_y = X[feature_y].quantile(0.05)
    q95_y = X[feature_y].quantile(0.95)
    X_q = X[(X[feature_x] >= q5_x) & (X[feature_x] <= q95_x) &
            (X[feature_y] >= q5_y) & (X[feature_y] <= q95_y)]
    ale_eff = ale(
        X=X_q,
        model=model,
        feature=[feature_x, feature_y],
        grid_size=100,
        fig=fig,
        ax=ax
    )
    x_range = ax.get_xlim()[1] - ax.get_xlim()[0]
    y_range = ax.get_ylim()[1] - ax.get_ylim()[0]
    ax.set_aspect(abs(x_range / y_range))
    ax.set_xlabel(feature_y, weight='bold')
    ax.set_ylabel(feature_x, weight='bold')
    import matplotlib.colors as mcolors
    for im in ax.get_images():
        data_min, data_max = im.get_clim()
        norm = mcolors.TwoSlopeNorm(vmin=data_min, vcenter=0., vmax=data_max)
        im.set_cmap('rainbow')
        im.set_norm(norm)
        colorbar = plt.colorbar(im, ax=ax)
        colorbar.set_label('ALE Effect')
    plt.tight_layout()
    fig.savefig(rf"\w-pic-2d\w-{feature_x}-{feature_y}.png", dpi=600)
    ale_eff.to_csv(rf"\w-csv-2d\w-{feature_x}-{feature_y}.csv", index=True)
    plt.close(fig)
