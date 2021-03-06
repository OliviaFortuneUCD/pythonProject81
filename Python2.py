import seaborn as sns
import os
import pandas as pd
import matplotlib.pyplot as plt

activity = pd.read_csv('Fitbit.csv')
#print(activity.head(10))

# figure size
plt.figure(figsize=(15,8))

# Simple scatterplot
ax = sns.scatterplot(x='Calories', y='SedentaryMinutes', data=activity)

ax.set_title('Scatterplot of calories and intense_activities')