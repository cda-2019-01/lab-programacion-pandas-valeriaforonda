
##
## Si la columna _c0 es la clave en las tablas tbl0.tsv
## y tbl2.tsv, compute la suma de tbl2._c5b por cada
## valor en tbl0._c1.
import pandas as pd
import numpy as np
import datetime
df =  pd.read_csv("tbl0.tsv", sep="\t")
df1 =  pd.read_csv("tbl2.tsv", sep="\t")
Mix = df =  pd.read_csv("tbl0.tsv", sep="\t")
Cons =  pd.merge(df, df1, on='_c0')
Final = df2 = Cons.groupby('_c5a').agg({'_c5b': np.sum})
print(Final.iloc[:,0])


