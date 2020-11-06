import pandas as pd
import numpy as np


def checkInList(input_list, val):
    flag = True
    for item in input_list:
        if val == item:
            flag = False
    return flag

# column_name = []
src_arr = []
formatted_arr = []
df = pd.read_csv("patient.csv")

# for clname in df.columns:
#     column_name.append(clname)
for i, name in enumerate(df.columns):
    src_arr.append(df[name])
src_arr = np.array(src_arr)
left=0
while left < src_arr.shape[1] and src_arr[2][left] > 16:
    curr_id = src_arr[0][left]
    gender = src_arr[1][left]
    age_min = src_arr[2][left]
    hadm_id = src_arr[3][left]
    icustay_avg = src_arr[4][left]
    count_hadm = 0
    flag_hadm = False
    right = left+1
    while right < src_arr.shape[1] and src_arr[0][right] == curr_id:
        right += 1
    if right - left != 1:
        hadm_id_list = []
        icustay_avg = 0
        for j in range(left, right):
            age_min = min(age_min, src_arr[2][j])
            icustay_avg += src_arr[4][j]
            # icustay_min = min(icustay_min, src_arr[4][j])
            flag_hadm = checkInList(hadm_id_list, src_arr[3][j])
            if flag_hadm:
                hadm_id_list.append(src_arr[3][j])
        count_hadm = len(hadm_id_list)
        icustay_avg = icustay_avg / (right-left)
    # for i in range(right-left):
    #     formatted_arr.append([src_arr[0][left], gender, age_min, right-left, src_arr[4][left+i]])
    if count_hadm < 6:
        formatted_arr.append([curr_id, gender, age_min, count_hadm, icustay_avg])
    left = right
formatted_arr = np.array(formatted_arr)

df_out = pd.DataFrame(data=formatted_arr, columns=df.columns)
df_out.to_csv("./patient_format_phase1.csv")

print(src_arr.shape)
# print(src_arr[0][-20:])
print("\nAfter processing......\n")
print(formatted_arr.shape)
# print(formatted_arr[-20:])
