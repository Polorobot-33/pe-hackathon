import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import refinement as rf

fulltable = rf.load_table()
df = fulltable[['pl_orbsmax', 'disc_year', 'discoverymethod']].dropna(axis=0, how='any')
df = df.pivot_table(values='pl_orbsmax', index=['disc_year', 'discoverymethod']).unstack(level=1)

fig, ax = plt.subplots()
df.plot(kind='bar', ax=ax, width=1.5)
plt.yscale('log')
plt.xlabel('année de découverte')
plt.ylabel('distance (unité astronomique, échelle logarithmique)')
plt.show()