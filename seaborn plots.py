import numpy as np
import os
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd
import folium

NYC= pd.read_csv('Accidents_2018.csv')

count_table = pd.crosstab(index=NYC["BOROUGH"], columns=NYC["NUMBER OF PERSONS INJURED"])

count_table.plot(kind="bar",
                 figsize=(8,8),
                 stacked=True)
plt.xticks(rotation=0)

#sns.catplot(x="BOROUGH", y="Bldg.Type", data=NYC)
#NYC['BOROUGH'].value_counts().plot(kind='bar')
plt.show()