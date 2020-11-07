import pandas as pd
import numpy as np

def groundTruth():
    dir_name = "secondHalf/"
    formatted_arr = []
    # df_1_drug = pd.read_csv(dir_name+"1drug_out.csv")
    # df_2_drug = pd.read_csv(dir_name+"2drug_out.csv")
    # df_3_drug = pd.read_csv(dir_name+"3drug_out.csv")
    df_type1_id = pd.read_csv("type1_id.csv", index_col=0)
    # df_labevents = pd.read_csv("labeventsOutput.csv")
    # df_labevents = df_labevents["subject_id"]
    # labevents_lst = []
    # labevents_lst.append(df_labevents)

    df_78552_exclude = pd.read_csv(dir_name+"exclude78552_out.csv")
    df_lactat_exclude = pd.read_csv(dir_name+"exclude_lactate_out.csv")

    # df_1_drug = df_1_drug["subject_id"]
    # df_2_drug = df_2_drug["subject_id"]
    # df_3_drug = df_3_drug["subject_id"]

    df_78552_exclude = df_78552_exclude["subject_id"]
    df_lactat_exclude = df_lactat_exclude[["subject_id", "itemid", "valuenum"]]

    # drug1_lst = []
    # drug2_lst = []
    # drug3_lst = []
    type1_lst = []
    exclude_phase1 = []
    exclude_phase2 = []
    # drug1_lst.append(df_1_drug)
    # drug2_lst.append(df_2_drug)
    # drug3_lst.append(df_3_drug)
    for name in df_type1_id.columns:
        type1_lst.append(df_type1_id[name])
    
    exclude_phase1.append(df_78552_exclude)
    exclude_phase2.append(df_lactat_exclude)

    for i, subjectid in enumerate(type1_lst[0]):
        formatted_arr.append([subjectid, type1_lst[1][i], type1_lst[2][i], type1_lst[3][i]])
    
    for i, exclu_subjectid in enumerate(exclude_phase1[0]):
        for j, type1_subjectid in enumerate(type1_lst[0]):
            if exclu_subjectid == type1_subjectid:
                formatted_arr[j][1] = 0
                formatted_arr[j][2] = 0
                formatted_arr[j][3] = 0
                break
    for i, exclu_subjectid in enumerate(exclude_phase2[0]):
        for j, type1_subjectid in enumerate(type1_lst[0]):
            if exclu_subjectid == type1_subjectid and exclude_phase2[2][i] == 0:
                formatted_arr[j][1] = 0
                formatted_arr[j][2] = 0
                formatted_arr[j][3] = 0
                break

    # for i, drug_1 in enumerate(drug1_lst[0]):
    #     for j, subject_event in enumerate(labevents_lst[0]):
    #         if drug_1 == subject_event:
    #             formatted_arr[j][1] = 1
    #             break
    # for i, drug_2 in enumerate(drug2_lst[0]):
    #     for j, subject_event in enumerate(labevents_lst[0]):
    #         if drug_2 == subject_event:
    #             formatted_arr[j][2] = 1
    #             break
    # for i, drug_3 in enumerate(drug3_lst[0]):
    #     for j, subject_event in enumerate(labevents_lst[0]):
    #         if drug_3 == subject_event:
    #             formatted_arr[j][3] = 1
    #             break
    column_label = ["subject_id", "drug_1", "drug_2", "drug_3"]
    formatted_arr = np.array(formatted_arr)
    df_out = pd.DataFrame(data=formatted_arr, columns=column_label)
    df_out.to_csv("./type2_id.csv")
    print("\nAfter processing......\n")
    print(formatted_arr.shape)
groundTruth()