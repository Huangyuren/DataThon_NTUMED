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


# df_labevent_all = pd.read_csv("LABEVENTS.csv")
# df_labevent_all = df_labevent_all[["SUBJECT_ID", "ITEMID", "VALUENUM"]]
# df_labevent_all.sort_values("SUBJECT_ID", ascending=True, inplace=True, kind='quicksort', na_position='first')
# df_labevent_all.to_csv("./LABEVENTS_sorted.csv")

# df_icd9_feature = pd.read_csv("ICD9_feature.csv")
df_type_2 = pd.read_csv("type2_id.csv", index_col=0)
df_vital_sign = pd.read_csv("vital_sign.csv")
df_vital_sign_lst = df_vital_sign.values.tolist() # dataframe in 2d list shape (#rows, 4)
df_labevent_all = pd.read_csv("labeventsOutput.csv", index_col=0)
df_labevent_subjectID = df_labevent_all["subject_id"]
df_labevent_subjectID_lst = df_labevent_subjectID.values.tolist()
df_type_2_drug = df_type_2[["drug_1", "drug_2"]]
df_type_2_drug_lst = df_type_2_drug.values.tolist()
# df_icd9_feature_lst = df_icd9_feature[]
formatted_arr=[]
for i in range(6):
    for j in df_labevent_subjectID_lst:
        formatted_arr.append([j, i, "","","","","","",0,0,"",""])
column_labels = ["subject_id", "Time", "heart_rate_220045", "ABP_systolic_220050", "NIBP_systolic_220179", \
                        "SPO2_220277", "Respiratory_rate_220210", "Respiratory_rate_224690", "drug_1", "drug_2",\
                        "Lactate", "TroponinT"]
itemID_table = [220045, 220050, 220179, 220277, 220210, 224690, 50813, 51003]



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

# 50813 part
left=0
counter=0
df_50813 = pd.read_csv("50813.csv")
df_50813_lst = df_50813.values.tolist()
while left < len(df_50813_lst):
    counter += 1
    curr_subjectID = df_50813_lst[left][0]
    left, right = getRange(df_50813_lst, curr_subjectID)
    # Now we get this patient's information.
    grouped_time = getTimeRange(df_50813_lst[left:right])
    picked_grouped_time = choseGroup(grouped_time)
    for i in range(len(picked_grouped_time)):
        i_tmp = 5-i
        offset_idx=0
        try:
            offset_idx = df_labevent_subjectID_lst.index(curr_subjectID)
        except ValueError:
            continue
        offset = i_tmp*3170 + offset_idx
        formatted_arr[offset][1] = i_tmp
        first = picked_grouped_time[i][0]
        second = picked_grouped_time[i][1]
        for j in range(first, second):
            if df_50813_lst[j][3] != "NULL":
                formatted_arr[offset][10] = df_50813_lst[j][3]
    left = right

# 51003 part
left=0
counter=0
df_51003 = pd.read_csv("51003.csv")
df_51003_lst = df_51003.values.tolist()
while left < len(df_51003_lst):
    counter += 1
    curr_subjectID = df_51003_lst[left][0]
    left, right = getRange(df_51003_lst, curr_subjectID)
    # Now we get this patient's information.
    grouped_time = getTimeRange(df_51003_lst[left:right])
    picked_grouped_time = choseGroup(grouped_time)
    for i in range(len(picked_grouped_time)):
        i_tmp = 5-i
        offset_idx=0
        try:
            offset_idx = df_labevent_subjectID_lst.index(curr_subjectID)
        except ValueError:
            continue
        offset = i_tmp*3170 + offset_idx
        formatted_arr[offset][1] = i_tmp
        first = picked_grouped_time[i][0]
        second = picked_grouped_time[i][1]
        for j in range(first, second):
            if df_51003_lst[j][3] != "NULL":
                formatted_arr[offset][11] = df_51003_lst[j][3]
    left = right

df_out = pd.DataFrame(data=formatted_arr, columns=column_labels)
df_out.to_csv("./vitalSignFormatted.csv")
# df_out.to_csv("./TEST.csv")