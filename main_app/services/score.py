import pandas as pd
import numpy as np

def score(input_id,sem_name):
    dataset_23_24 = pd.read_csv("predicted_23-24.csv")

    output_dic = dict()
    sem_name = sem_name.upper()
    sem_col = pd.DataFrame(dataset_23_24[[sem_name]].values)
    email_col = pd.DataFrame(dataset_23_24.iloc[:,1].values)

    output_col = pd.concat([email_col , sem_col],axis=1)
    total_cgpa_col = output_col.to_numpy()

    required_marks = 0
    marks = 0
    average = 0

    for i in range(len(total_cgpa_col)):
        if total_cgpa_col[i][0] == input_id:
            required_marks = total_cgpa_col[i][1]

        marks += total_cgpa_col[i][1]

    average = round(marks / len(total_cgpa_col),2)

    output_dic[input_id] = required_marks
    output_dic["all_students_marks"] = total_cgpa_col
    output_dic["average_cgpa"] = average

    return output_dic