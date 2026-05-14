import pandas as pd 
import numpy as np 

data_multi = {
    "Paese": ["Italia", "Italia"],
    "Anno": [2023, 2024, 2023, 2024],
    "Ventide": [120, 135, 110, 118]
}

df_multi = pd.Dataframe(data_multi)

df_multi = df_multi.set_index(["Paese", "Anno"])
print("\nDataFrame con MultiIndex")
print(df_multi)

print("\nTutte le righe")
print(df_multi.loc['Italia'])

print("\nValore vendite Francia 2024")
print(df_multi.loc[("Francia", 2024), "Vendite"])