import numpy as np
import pandas as pd

def load_table() :
    df = pd.read_csv('PS_2024.10.29_06.12.44.csv', sep=',', header=96)
    df.drop_duplicates(inplace=True)
    return df[df.default_flag == 1].drop(columns='default_flag')

#print(load_table().describe())