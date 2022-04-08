#Importando DataSets com Pandas

import pandas as pd
file_name = 'Teoria/arquivos/binary.csv'
df = pd.read_csv(file_name)
print(df.head())


