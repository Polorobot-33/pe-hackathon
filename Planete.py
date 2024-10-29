import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import refinement as rf
df=rf.load_table()
categories=df['discoverymethod'].unique()
couleur=['green','orange','blue','brown','purple','red','lightblue','yellow']
j=0
couleur=couleur+couleur
nombre=[]
identifiant=[]
for i in categories:
    df_i=df[df['discoverymethod']==i]
    annee=df_i['disc_year']
    a=df_i.max()['disc_year']-df_i.min()['disc_year']+1
    plt.hist(annee,bins=a,color=couleur[j])
    j=j+1
    identifiant.append(j)
    plt.title('Method : '+i)
    plt.show()
    nombre.append(df_i.shape[0])
plt.bar(identifiant,nombre,color='purple')
plt.title('Nombre de planètes découvertes par méthode')
plt.legend()
