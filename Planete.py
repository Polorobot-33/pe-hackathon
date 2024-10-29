import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import refinement as rf
df=rf.load_table()
categories=df['discoverymethod'].unique()
for i in categories:
    df_i=df[df['discoverymethod']==i]
    annee=df_i['disc_year']
    a=df_i.max()['disc_year']-df_i.min()['disc_year']+1
    plt.hist(annee,bins=a)
    plt.title('Method : '+i)
    plt.show()
