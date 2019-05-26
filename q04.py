##
## Imprima los valores unicos e la columna _c4 de 
## de la tabla tbl1 en mayusculas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df1 = pd.read_csv("tbl1.tsv", sep="\t")
aux1 = df1.applymap(lambda s:s.upper() if type(s) == str else s)
aux = aux1['_c4'].unique()
aux2 = sorted(aux)
print(aux2)
## 


