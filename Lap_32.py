"""
Day 32 Activity: Relationship Plots
Tasks:
1) Create scatterplot encoding >=3 variables
2) Create relplot with facet
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# TODO: Load data from data/day32_relationships.csv
df = pd.read_csv("day32_relationships.csv")

#Task 1: Create scatterplot encoding >=3 variables
sns.scatterplot(x="feature1", y="outcome", hue="segment", style="priority", data=df)
plt.show()

#Task 2: Create relplot with facet
sns.relplot(x="feature1", y="outcome", hue="segment", style="priority", col="priority", data=df)
plt.show()



# TODO: sns.scatterplot with hue/style
# TODO: sns.relplot with col or row
