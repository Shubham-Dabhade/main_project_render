import pandas as pd
import numpy as np

def find_prediction():
    dataset_21_22 = pd.read_csv("predicted_21-22.csv")
    dataset_22_23 = pd.read_csv("predicted_22-23.csv")
    dataset_23_24 = pd.read_csv("predicted_23-24.csv")


    actual_21_22 = dataset_21_22.iloc[:,-2].values
    prediction_21_22 = dataset_21_22.iloc[:,-1].values
    actual_22_23 = dataset_22_23.iloc[:,-2].values
    prediction_22_23 = dataset_22_23.iloc[:,-1].values
    prediction_23_24 = dataset_23_24.iloc[:,-1].values

    prediction_dict = dict()
    actual = 0
    predict = 0

    for i in range(len(actual_21_22)):
        if actual_21_22[i] == "yes":
            actual += 1
        if prediction_21_22[i] == 'yes':
            predict += 1

        perc_actual = round((actual/len(actual_21_22)) *100,2)
        perc_predict = round((predict/len(actual_21_22)) *100,2)

    prediction_dict['prediction_21-22'] = {"actual_percentage": perc_actual,"predicted_percentage":perc_predict}


    actual = 0
    predict = 0

    for i in range(len(actual_22_23)):
        if actual_22_23[i] == "yes":
            actual += 1
        if prediction_22_23[i] == 'yes':
            predict += 1

        perc_actual = round((actual/len(actual_22_23)) *100,2)
        perc_predict = round((predict/len(actual_22_23)) *100,2)

    prediction_dict['prediction_22-23'] = {"actual_percentage": perc_actual,"predicted_percentage":perc_predict}


    predict = 0

    for i in range(len(prediction_23_24)):
        if prediction_23_24[i] == 'yes':
            predict += 1

        perc_predict = round((predict/len(prediction_23_24)) *100,2)

    prediction_dict['prediction_23-24'] = {"predicted_percentage":perc_predict}

    return prediction_dict


