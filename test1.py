import numpy as np
import pandas as pd

#df = pd.read_csv('PS_2024.10.29_06.12.44.csv', sep=',', header=96)
#print(df.pl_orbper.head(5))
#print(df.columns)

import refinement as rf

df = rf.load_table()
print(df.head(5))