"""
Day 31 Activity: Seaborn Visualizations
Tasks:
1) Load dataset
2) Recreate histplot, kdeplot, boxplot, countplot
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


#Task 1: Load dataset
df = pd.read_csv("day31_seaborn.csv")


#Task 2: Recreate histplot, kdeplot, boxplot, countplot

#histplot
sns.histplot(x="age", data=df)
plt.show()

#kdeplot
sns.kdeplot(x="age", data=df)
plt.show()

#boxplot
sns.boxplot(x="age", data=df)
plt.show()

#countplot
sns.countplot(x="age", data=df)
plt.show()

# TODO: sns.histplot, sns.kdeplot, sns.boxplot, sns.countplot
