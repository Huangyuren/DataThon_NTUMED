import pandas as pd
import numpy as np


def checkInList(input_list, val):
    # Return false if val is in list.
    flag = True
    for item in input_list:
        if val == item:
            flag = False
            break
    return flag

def checkInSubjectID(input_list, val):
    # Return true if val is in list.
    flag = False
    for idx, item in enumerate(input_list):
        if val == item:
            print("Hit at index: ", idx)
            flag = True
            break
        elif val < item:
            break
    return flag

src_arr = []
subjectid_valid = []
formatted_arr = []
itemid_arr = []
valuenum_arr = []

df_labevent_all = pd.read_csv("LABEVENTS.csv")
df_patient_phase1 = pd.read_csv("patient_format_phase1.csv", index_col=0)

# for i, name in enumerate(df_labevent_all.columns):
#     if name == "SUBJECT_ID" or name == "ITEMID" or name == "VALUENUM":
#         src_arr.append(df_labevent_all[name])
# for i, name in enumerate(df_patient_phase1.columns):
#     if name == "subject_id":
#         subjectid_valid = list(df_patient_phase1[name])
# print("Length of subjectid_valid: ", len(subjectid_valid))


src_arr = np.array(src_arr)
left=0
count=0


while left < src_arr.shape[1]:
    if checkInSubjectID(subjectid_valid, src_arr[0][left]) == False:
        left += 1
        continue
    print("curr_id: ", src_arr[0][left])
    print("Left: ", left)
    itemid_list = []
    valuenum_list = []
    curr_id = src_arr[0][left]
    right = left+1
    while right < src_arr.shape[1] and src_arr[0][right] == curr_id:
        right += 1
    if right - left != 1:
        for j in range(left, right):
            flag_tmp = checkInList(itemid_list, src_arr[1][j])
            if flag_tmp:
                itemid_list.append(src_arr[1][j])
        for tmp_itemid in itemid_list:
            tmp_valuenum = 0
            for j in range(left, right):
                if tmp_itemid == src_arr[1][j]:
                    # print("tmp_valuenum:%f." % (src_arr[2][j]))
                    tmp_valuenum = src_arr[2][j]
            valuenum_list.append(tmp_valuenum)
    itemid_arr.append(itemid_list)
    valuenum_arr.append(valuenum_list)
    left = right

subjectid_valid = np.array(subjectid_valid)
itemid_arr = np.array(itemid_arr)
valuenum_arr = np.array(valuenum_arr)
print("subject_id array shape: ", subjectid_valid.shape)
print("itemid_arr shape: ", itemid_arr.shape)
print("valuenum_arr shape: ", valuenum_arr.shape)
print("src_arr shape: ", np.array(src_arr).shape)