import spacy
def extract_entities(question):
    nlp = spacy.load("../models/railways_ner")
    entities = nlp(question).ents
    entities_with_labels = []
    for i in entities:
        entities_with_labels.append((i.label_,i.text))
    return entities_with_labels
