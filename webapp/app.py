from flask import Flask,render_template,request,redirect,jsonify
from entity_extractor import *
from intent_extractor import *
from response_generator import *

app = Flask(__name__)


def get_response_from_bot(question):
    try:
     intent = extract_intent(question)
     print(intent)
     entities = extract_entities(question)
     response = generate_response(intent,entities)
    except KeyError:
     response = "Seems like an error occurred while answering this question"
    return response

@app.route("/",methods=["GET","POST"])
def home():
    return render_template("html/index.html")

@app.route("/chatbot_response/<string:qs>",methods=["GET"])
def respond(qs):
    response = ""
    print("Entered",qs)
    if request.method == "GET":
        print("entered")
        response = get_response_from_bot(qs)
        print(response)
    return jsonify({"response":response})

if __name__ == "__main__":
    app.run(debug=True)