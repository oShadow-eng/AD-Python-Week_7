"""
Day 34 Activity: Pattern Discovery
Tasks:
1) Create faceted plots (row/col)
2) Add trend overlays or grouped plots
3) Identify non-obvious pattern
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# TODO: Load data from data/day34_patterns.csv
df = pd.read_csv("day34_patterns.csv")

#Task 1: Create faceted plots (row/col)
sns.relplot(x="time", y="value", hue="segment", style="season", col="season",row="segment", data=df)
plt.show()

#Task 2: Add trend overlays or grouped plots
sns.lmplot(x="time", y="value", hue="segment", col="season", data=df)
plt.show()

#Task 3: Identify non-obvious pattern
"""Insight:
# Although the overall values increase with time, there is a subtle pattern in the distribution of segments.
# Segment B appears only at higher time points (time ≥ 3), while Segment A is present at both early and later times.
# This indicates that different segments behave differently over time and are not evenly distributed across seasons.
# Such a pattern is not immediately obvious from a simple line or scatter plot."""



# TODO: Faceted relplot or catplot
# TODO: Trend overlay
