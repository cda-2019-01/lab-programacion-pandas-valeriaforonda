##
## Agregue una columna  con la suma de _c0 y _c2 a la tabla tbl0.tsv 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv("tbl0.tsv", sep="\t")
df.loc[:,'suma'] = df.loc[:,'_c0'].add(df.loc[:,'_c2'])
print(df)
## 

