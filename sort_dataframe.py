import pandas as pd
import numpy as np

# df_labevent_all = pd.read_csv("LABEVENTS_dict.csv")
# df_labevent_all = df_labevent_all[["MIMIC LABEL", "ITEMID"]]
# df_labevent_all.sort_values("ITEMID", ascending=True, inplace=True, kind='quicksort', na_position='first')
# df_labevent_all.to_csv("./LABEVENTS_dict_sorted.csv")

# df_labevent_all = pd.read_csv("exclude78552.csv")
# df_labevent_all = df_labevent_all[["subject_id", "cardiogenetic_shock"]]
# df_labevent_all.sort_values("subject_id", ascending=True, inplace=True, kind='quicksort', na_position='first')
# df_labevent_all.to_csv("./exclude78552_sorted.csv")

df_labevent_all = pd.read_csv("exclude_lactate.csv")
# df_labevent_all = df_labevent_all[["subject_id", "cardiogenetic_shock"]]
df_labevent_all.sort_values("subject_id", ascending=True, inplace=True, kind='quicksort', na_position='first')
df_labevent_all.to_csv("./exclude_lactate_sorted.csv")