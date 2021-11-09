import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

cars = pd.read_csv('Cars.csv')

plt.plot(x='County', y='Car registration count')
plt.show()