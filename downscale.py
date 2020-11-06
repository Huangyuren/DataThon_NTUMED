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
        if item == val:
            left = i
            right = left + 1
            while right < len(input_list) and input_list[right] == val:
                right += 1
            break
    return left, right

def setupValueNum(input_lst_1, left, right, val):
    ret = 0
    for i in range(left, right):
        if val == input_lst_1[i]:
            ret = i
    return ret


# df_labevent_all = pd.read_csv("LABEVENTS.csv")
# df_labevent_all = df_labevent_all[["SUBJECT_ID", "ITEMID", "VALUENUM"]]
# df_labevent_all.sort_values("SUBJECT_ID", ascending=True, inplace=True, kind='quicksort', na_position='first')
# df_labevent_all.to_csv("./LABEVENTS_sorted.csv")

df_labevent_all = pd.read_csv("LABEVENTS_dict_sorted.csv")
df_itemid_all = df_labevent_all["ITEMID"] # dataFrame for itemid
df_mimic_label_all = df_labevent_all["MIMIC LABEL"] # dataFrame for alphabetical representation of items
itemid_dictionary = df_itemid_all.tolist()
mimic_label_dictionary = df_mimic_label_all.tolist()
final_column_labels = []
final_column_labels.append("subject_id")
for alphas in mimic_label_dictionary:
    final_column_labels.append(alphas)


formatted_arr = [] # array for return, should formatted
df_patient_phase1 = pd.read_csv("patient_format_phase1.csv", index_col=0)
df_patient_phase1 = df_patient_phase1["subject_id"]

df_labevent_sorted = pd.read_csv("LABEVENTS_sorted.csv")
src_arr = []
for i, name in enumerate(df_labevent_sorted.columns):
    if i == 0:
        continue
    src_arr.append(df_labevent_sorted[name]) # sorce array be like: [[subject_id...], [item_id...], [valuenum...]] with shape (3, 27854055)
subjectid_valid = df_patient_phase1.values.tolist() # subject valid array be like: [..] with length 3170

for i, curr_subjectID in enumerate(subjectid_valid):
    print("i: {}, curr_subjectID: {}".format(i, curr_subjectID))
    left, right = getRange(src_arr[0], curr_subjectID)
    itemid_list = []
    valuenum_list = []
    # Now we should first compose itemid list
    for j in range(left, right):
        curr_itemid = src_arr[1][j]
        if checkInList(itemid_list, curr_itemid) == False:
            itemid_list.append(curr_itemid)
    # Then we can complete valuenum list
    for k, tmp in enumerate(itemid_list):
        valuenum_idx = setupValueNum(src_arr[1], left, right, tmp)
        valuenum_list.append(src_arr[2][valuenum_idx])
    # Finally, we can form our per-row content!
    rowtmp = []
    rowtmp.append(curr_subjectID)
    for l, mimic_numeric in enumerate(itemid_dictionary):
        flag = True
        for m in range(len(itemid_list)):
            if mimic_numeric == itemid_list[m]:
                rowtmp.append(valuenum_list[m])
                flag = False
                break
        if flag:
            rowtmp.append(0)
    formatted_arr.append(rowtmp)

formatted_arr = np.array(formatted_arr)
df_out = pd.DataFrame(data=formatted_arr, columns=final_column_labels)
df_out.to_csv("./labeventsOutput.csv")

print("\nAfter processing......\n")
print(formatted_arr.shape)
