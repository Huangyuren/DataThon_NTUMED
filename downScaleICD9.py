import pandas as pd
import numpy as np

def getRange(input_list, val):
    left = 0
    right = 0
    for i, item in enumerate(input_list):
        if item[0] == val:
            left = i
            right = left + 1
            while right < len(input_list) and input_list[right][0] == val:
                right += 1
            break
    return left, right

df_icd9_feature = pd.read_csv("ICD9_feature.csv")
df_icd9_feature_lst = df_icd9_feature.values.tolist()
df_icd9_dictionary = pd.read_csv("ICD9CSV_sorted.csv")
df_icd9_dictionary_lst = df_icd9_dictionary["ICD9_code"].values.tolist()
df_icd9_dictionary_lst_name = df_icd9_dictionary["Name"].values.tolist()
df_labevent_all = pd.read_csv("labeventsOutput.csv", index_col=0)
df_labevent_subjectID_lst = df_labevent_all["subject_id"].values.tolist()

formatted_arr=[]
for i, id_name in enumerate(df_labevent_subjectID_lst):
    formatted_arr.append([id_name])
    for j in range(len(df_icd9_dictionary_lst)):
        formatted_arr[i].append(0)

column_labels = []
column_labels.append("subject_id")
for i in df_icd9_dictionary_lst_name:
    column_labels.append(i)
for i, icd9code in enumerate(df_icd9_dictionary_lst):
    column_labels[i+1] = str(icd9code)+"_"+column_labels[i+1]

left=0
counter=0
while left < len(df_icd9_feature_lst):
    counter += 1
    curr_subjectID = df_icd9_feature_lst[left][0]
    left, right = getRange(df_icd9_feature_lst, curr_subjectID)
    for i in range(left, right):
        curr_icd9_code = df_icd9_feature_lst[i][1]
        offset_idx=0
        try:
            offset_idx = df_labevent_subjectID_lst.index(curr_subjectID)
        except ValueError:
            continue
        formatted_arr[offset_idx][df_icd9_dictionary_lst.index(curr_icd9_code)+1] = curr_icd9_code
    left = right

df_out = pd.DataFrame(data=formatted_arr, columns=column_labels)
df_out.to_csv("./ICD9Formatted.csv", index=False)
# df_out.to_csv("./TEST.csv", index=False)