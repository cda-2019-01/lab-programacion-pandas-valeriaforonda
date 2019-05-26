##
## Agregue el año como una columna a la tabla tbl0.tsv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv("tbl0.tsv", sep="\t")
df['ano'] = [i.split('-')[0] for i in df['_c3']]
print(df)
##

