import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import refinement as rf

fulltable = rf.load_table()
df = fulltable[['pl_orbsmax', 'pl_eqt']].dropna(axis=0, how='any')
#df = df[(df.pl_orbsmax < 10)]

#df['pl_orbsmax'] = np.log(df.pl_orbsmax)


df.plot(x='pl_orbsmax', y='pl_eqt', style='r.')
plt.xlabel('rayon orbital maximal (unité astronomique, échelle logarithmique)')
plt.ylabel('Températude d\'équilibre (°K)')
plt.xscale('log')
plt.show()