import numpy as np
import matplotlib.pyplot as plt
import refinement as rf

fulldata = rf.load_table()
df = fulldata[['disc_year', 'discoverymethod']]

df['col'] = 1
grouped = df.groupby(by=['discoverymethod', 'disc_year']).count()
#year = grouped.resample('1y', on='disc_year')
#print(grouped.count().head(5))
pivot = grouped.pivot_table(values='col', index=['discoverymethod', 'disc_year'], aggfunc='sum').unstack(level=0)

fig, ax = plt.subplots()
pivot.plot(ax=ax, stacked=True, kind='bar')
plt.title('nombre de découvertes d\'exoplanètes par année et par méthode')
plt.show()