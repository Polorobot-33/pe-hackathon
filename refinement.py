import numpy as np
import pandas as pd

def load_table() :
    df = pd.read_csv('PS_2024.10.29_06.12.44.csv', sep=',', header=96)
    df.drop_duplicates(inplace=True)
    df = df[df.default_flag == 1].drop(columns='default_flag')
    df = df[['pl_name', 'disc_year', 'discoverymethod', 'pl_orbper', 'pl_orbsmax', 'pl_rade', 'pl_bmasse', 'pl_orbeccen', 'pl_insol', 'pl_eqt', 'st_mass', 'st_teff']]
    df.set_index('pl_name', inplace=True)
    return df