"""
Day 33 Activity: Correlation Heatmaps
Tasks:
1) Compute correlation matrix
2) Plot heatmap with annotations
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# TODO: Load data from data/day33_corr.csv
df = pd.read_csv("day33_corr.csv")

#Task 1: Compute correlation matrix
df_corr = df.corr()

#Task 2: Plot heatmap with annotations
sns.heatmap(df_corr, annot=True)
plt.show()


# TODO: Compute df.corr() and plot heatmap
