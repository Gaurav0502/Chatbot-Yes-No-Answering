import json
import os
import datetime

def update_log(question,intent,entities,response,tag):
    log = json.load(open(os.path.abspath(r"..\Chatbot-Yes-No-Answering\data\log.json"),"r"))
    time = str(datetime.datetime.now())
    log[time] = {
        "Question":question,
        "Intent": intent,
        "Entities":entities,
        "Response":response,
        "Tag":tag
    }
    json.dump(log,open(os.path.abspath(r"..\Chatbot-Yes-No-Answering\data\log.json"),"w"),indent=4,sort_keys=True)
