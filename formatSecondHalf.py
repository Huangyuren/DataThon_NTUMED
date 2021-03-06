import pandas as pd
import numpy as np

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

def computeLargest(input_list, left, right):
    ret = -100
    for i in range(left, right):
        ret = max(input_list[i], ret)
    return ret


def formating(input_list, file_name, columns_name, special_flag):
    # input list's dimension should be 2-dimensional
    if special_flag:
        print("Special flag...")
    formatted_arr = []
    left = 0
    while left < len(input_list[0]):
        left, right = getRange(input_list[0], input_list[0][left])
        if special_flag:
            val = computeLargest(input_list[2], left, right)
            if val < 2:
                formatted_arr.append([input_list[0][left], input_list[1][left], 0])
            else:
                formatted_arr.append([input_list[0][left], input_list[1][left], val])
        else:
            formatted_arr.append([input_list[0][left], input_list[1][left]])
        # print("Left: {}, Right: {}".format(left, right))
        left = right
    df_ret = pd.DataFrame(data=formatted_arr, columns=columns_name)
    df_ret.to_csv(file_name)

def combineLactate():
    dir_name = "secondHalf/"
    dir_tmp = "secondHalf/buf/"
    formatted_arr = []
    df_2_drug = pd.read_csv(dir_tmp+"intero_out_with_lactate.csv")


def combineTwoEvents():
    # first <--- second
    dir_name = "secondHalf/"
    dir_tmp = "secondHalf/buf/"
    formatted_arr = []
    # df_1_drug = pd.read_csv(dir_name+"2drug_out.csv")
    # df_2_drug = pd.read_csv(dir_name+"3drug_out.csv")
    df_1_drug = pd.read_csv(dir_tmp+"intero_out.csv")
    # df_2_drug = pd.read_csv(dir_name+"exclude78552_out.csv")
    df_2_drug = pd.read_csv(dir_name+"exclude_lactate_out.csv")
    df_1_drug = df_1_drug[["subject_id", "cardiogenetic_shock"]]
    df_2_drug = df_2_drug[["subject_id", "cardiogenetic_shock"]]
    drug1_lst = []
    drug2_lst = []
    for name in df_1_drug.columns:
        drug1_lst.append(df_1_drug[name])
    for name in df_2_drug.columns:
        drug2_lst.append(df_2_drug[name])

    # We should map first event as base, then using second event to probe.
    # If itself (second event) is new, then append, otherwise skip.
    for idx_first, subject_id_first in enumerate(drug1_lst[0]):
        formatted_arr.append([subject_id_first, drug1_lst[1][idx_first]])
    for idx_sec, subject_id_sec in enumerate(drug2_lst[0]):
        # Using second event to test new or not?
        # flag = True
        # for idx_first, subject_id_first in enumerate(drug1_lst[0]):
        #     if subject_id_sec == subject_id_first:
        #         flag = False
        #         break
        # if flag:
        #     formatted_arr.append([subject_id_sec, drug2_lst[1][idx_sec]])
        # 
        # Using exclude78552 to modify everyone
        for idx_first, subject_id_first in enumerate(formatted_arr):
            if subject_id_sec == formatted_arr[idx_first][0]:
                formatted_arr[idx_first][1] = 0
                break
    columns_name = ["subject_id", "cardiogenetic_shock"]
    formatted_arr = np.array(formatted_arr)
    df_out = pd.DataFrame(data=formatted_arr, columns=columns_name)
    # df_out.sort_values("subject_id", ascending=True, inplace=True, kind='quicksort', na_position='first') # make sure it was sorted
    df_out.to_csv(dir_tmp + "intero_out_with78552.csv")
    print("\nAfter processing......\n")
    print(formatted_arr.shape)


# df_1_drug = pd.read_csv("1_78551Drug.csv")
# df_2_drug = pd.read_csv("2_785..Drug.csv")
# df_3_drug = pd.read_csv("3_Drug.csv")
# df_exclude78552 = pd.read_csv("exclude78552_sorted.csv")
# df_exclude_lactate = pd.read_csv("exclude_lactate_sorted.csv")
# df_1_drug = df_1_drug[["subject_id", "cardiogenetic_shock"]]
# df_2_drug = df_2_drug[["subject_id", "cardiogenetic_shock"]]
# df_3_drug = df_3_drug[["subject_id", "cardiogenetic_shock"]]
# df_exclude78552 = df_exclude78552[["subject_id", "cardiogenetic_shock"]]
# df_exclude_lactate = df_exclude_lactate[["subject_id", "itemid", "valuenum"]]

# drug1_lst = []
# drug2_lst = []
# drug3_lst = []
# exclude78552_lst = []
# exclude_lactate_lst = []

# for name in df_1_drug.columns:
#     drug1_lst.append(df_1_drug[name])
# for name in df_2_drug.columns:
#     drug2_lst.append(df_2_drug[name])
# for name in df_3_drug.columns:
#     drug3_lst.append(df_3_drug[name])
# for name in df_exclude78552.columns:
#     exclude78552_lst.append(df_exclude78552[name])
# for name in df_exclude_lactate.columns:
#     exclude_lactate_lst.append(df_exclude_lactate[name])
# columns_name = ["subject_id", "cardiogenetic_shock"]

# dir_name = "secondHalf/"
# formating(drug1_lst, dir_name+"1drug_out.csv", columns_name, 0)
# formating(drug2_lst, dir_name+"2drug_out.csv", columns_name, 0)
# formating(drug3_lst, dir_name+"3drug_out.csv", columns_name, 0)
# formating(exclude78552_lst, dir_name+"exclude78552_out.csv", columns_name, 0)
# formating(exclude_lactate_lst, dir_name+"exclude_lactate_out.csv", df_exclude_lactate.columns, 1)