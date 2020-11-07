import pandas as pd
import numpy as np

def checkInList(input_list, val):
    # Return true if val is in list.
    if len(input_list) == 0:
        return False
    flag = False
    for item in input_list:
        if val == item:
            flag = True
            break
    return flag

def checkInSubjectID(input_list, val):
    # Return true if val is in list.
    if len(input_list) == 0:
        return False
    flag = False
    for idx, item in enumerate(input_list):
        if val == item:
            flag = True
            break
        elif val < item:
            break
    return flag

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

def getTimeRange(input_lst):
    ret = []
    down = len(input_lst) - 1
    while down >= 0:
        curr_hour = int(input_lst[down][2].split()[1].split(":")[0])
        j = down - 1
        if j<0:
            ret.append((down, down))
            break
        else:
            while j >= 0 and int(input_lst[j][2].split()[1].split(":")[0]) == curr_hour:
                j -= 1
                # print(int(input_lst[j][2].split()[1].split(":")[0]))
            ret_j = j+1
            ret_down = down + 1
            ret.append((ret_j, ret_down))
            down = j
    return ret
def choseGroup(grouped_time):
    count = 0
    idx = 0
    ret = []
    while idx < len(grouped_time) and count < 6:
        count += 1
        ret.append(grouped_time[idx])
        idx += 4
    return ret

df_icd9_feature = pd.read_csv("ICD9_feature.csv")
df_icd9_feature_lst = df_icd9_feature[]
df_icd9_dictionary = pd.read_csv("ICD9.xlsx")
df_icd9_dictionary_lst = df_icd9_dictionary["ICD9_code"].values.tolist()
df_labevent_all = pd.read_csv("labeventsOutput.csv", index_col=0)
df_labevent_subjectID_lst = df_labevent_all["subject_id"].values.tolist()

formatted_arr=[]
for i in df_labevent_subjectID_lst:
    formatted_arr.append(i)

left=0
counter=0
while left < len(df_vital_sign_lst):
    counter += 1
    curr_subjectID = df_vital_sign_lst[left][0]
    left, right = getRange(df_vital_sign_lst, df_vital_sign_lst[left][0])
    # Now we get this patient's information.
    grouped_time = getTimeRange(df_vital_sign_lst[left:right])
    picked_grouped_time = choseGroup(grouped_time)
    for i in range(len(picked_grouped_time)):
        i_tmp = 5-i
        curr_time = 5-i
        offset_idx=0
        try:
            offset_idx = df_labevent_subjectID_lst.index(curr_subjectID)
        except ValueError:
            continue
        offset = i_tmp*3170 + offset_idx
        formatted_arr[offset][1] = curr_time
        first = picked_grouped_time[i][0]
        second = picked_grouped_time[i][1]
        for j in range(first, second):
            tmp_itemID = df_vital_sign_lst[j][1]
            formatted_arr[offset][itemID_table.index(tmp_itemID)+2] = df_vital_sign_lst[j][3]
            if i_tmp == 5:
                formatted_arr[offset][8] = df_type_2_drug_lst[offset_idx][0]
                formatted_arr[offset][9] = df_type_2_drug_lst[offset_idx][1]
    left = right

df_out = pd.DataFrame(data=formatted_arr, columns=column_labels)
df_out.to_csv("./vitalSignFormatted.csv")
# df_out.to_csv("./TEST.csv")