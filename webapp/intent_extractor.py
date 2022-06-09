import json
import spacy
import numpy as np
def question_similiarity(sentence,question):
    nlp = spacy.load("en_core_web_sm")
    sent = nlp(sentence)
    q = nlp(question)
    return sent.similarity(q)

def extract_intent(question):
    file = open(r"C:\Users\mitug\Chatbot-Yes-No-Answering\data\intent_classification_data.json")
    questions = json.load(file)
    intent_similiarity = dict()
    for i in questions:
        intent_similiarity[i] = np.mean(list(map(question_similiarity,questions[i],[question]*len(questions[i]))))
    return max(zip(intent_similiarity.values(), intent_similiarity.keys()))[1]
    
