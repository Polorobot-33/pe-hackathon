import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import refinement as rf
df=rf.load_table()
df.drop(index='TOI-1694 c',inplace=True) #suppression d'un point abérant
un_sur_M=1/df['st_mass']
T2=df['pl_orbper']**2
a3=df['pl_orbsmax']**3
F=T2/a3
plt.plot(un_sur_M,F,marker='+',linewidth=0)
plt.xlabel('1/M_soleil')
plt.ylabel('T^2/a^3')
plt.title('Validation expérimentale de la 3ème loi de Kepler')
