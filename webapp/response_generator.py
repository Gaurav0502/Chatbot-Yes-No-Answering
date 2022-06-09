import pandas as pd
import numpy as np

def generate_response(intent,entities_with_labels):
    trains = pd.read_csv(r"C:\Users\mitug\Chatbot-Yes-No-Answering\data\All_Indian_Trains.csv")
    column_intent_mapping = {
    "TrainCheck":["Train no.","Train name"],
    "RouteCheck":["Starts","Ends"]
    }
    relevant_columns = column_intent_mapping[intent]
    search_space = trains[relevant_columns]
    if intent == "RouteCheck":
       search_results = search_space.loc[(search_space['Starts'] == entities_with_labels[0][1]) & (search_space['Ends'] == entities_with_labels[1][1])]
    else:
       entities_with_labels = dict(entities_with_labels)
       search_results = search_space.loc[(search_space['Train no.'] == int(entities_with_labels["CARDINAL"])) & (search_space['Train name'] == entities_with_labels["FAC"])]
    response = "No"
    if len(search_results) > 0:
       response = "Yes"
    return response