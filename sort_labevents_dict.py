import pandas as pd
import numpy as np

df_labevent_all = pd.read_csv("LABEVENTS_dict.csv")
df_labevent_all = df_labevent_all[["MIMIC LABEL", "ITEMID"]]
df_labevent_all.sort_values("ITEMID", ascending=True, inplace=True, kind='quicksort', na_position='first')
df_labevent_all.to_csv("./LABEVENTS_dict_sorted.csv")
