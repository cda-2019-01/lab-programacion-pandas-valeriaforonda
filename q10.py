##
## Construya una tabla que contenga _c0 y una lista
## separada por ',' de los valores de la columna _c4
## de la tabla tbl1.tsv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv("tbl1.tsv", sep="\t")
df1 = df.sort_values(by=['_c4']).reset_index()
listado = sorted(set(df1._c0))
df2 = pd.DataFrame('',columns=['_c0','lista'],index=list(range(len(listado))))
z=0
for w in listado:
    df2._c0[z]=w
    for i in list(range(len(df._c0))):
        if df1._c0[i] == w:
            df2.lista[z] = df2.lista[z] + str(df1._c4[i])+','
    df2.lista[z]=df2.lista[z][:-1]
    z = z+1
print(df2)
##

