##
## Imprima la suma de la _c2 por cada letra de la _c1 
## de la tabla tbl0
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv("tbl0.tsv", sep="\t")
print(df.groupby('_c1').sum()['_c2'])
## 

