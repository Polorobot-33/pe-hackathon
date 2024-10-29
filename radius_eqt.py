import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import refinement as rf

fulltable = rf.load_table()
df = fulltable[['pl_rade', 'pl_eqt', 'discoverymethod']].dropna(axis=0, how='any')
#df = df.pivot_table(values=['pl_rade', 'pl_eqt'], index=['discoverymethod']).unstack(level=1)
groups = df.groupby(by='discoverymethod')

fig, ax = plt.subplots()
for name, group in groups:
    group.plot(y='pl_eqt', x='pl_rade', style='.', ax=ax, label=name)

#df.plot(x='pl_eqt', y='pl_rade', style='r.', ax=ax)
#plt.yscale('log')
plt.xlabel('temperature moyenne de surface (K)')
plt.ylabel('rayon planétaire (rayon Terre)')
plt.show()