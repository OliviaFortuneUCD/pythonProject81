import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
cars = pd.read_csv('Cars.csv')


sns.histplot(data=cars, x="Engine type")
plt.show()