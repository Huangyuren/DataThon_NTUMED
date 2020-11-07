import pandas as pd
import numpy as np

df_labevent_all = pd.read_csv("ICD9CSV.csv")
df_labevent_all.sort_values("ICD9_code", ascending=True, inplace=True, kind='quicksort', na_position='first')
df_labevent_all.to_csv("./ICD9CSV_sorted.csv")