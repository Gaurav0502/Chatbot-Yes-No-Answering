from flask import Flask,render_template,request,redirect
from entity_extractor import *
from intent_extractor import *
from response_generator import *

app = Flask(__name__)


def get_response_from_bot(question):
    intent = extract_intent(question)
    print(intent)
    entities = extract_entities(question)
    response = generate_response(intent,entities)
    return response

@app.route("/",methods=["GET","POST"])
def home():
    response = ""
    print("Entered")
    if request.method == "POST":
        print("entered")
        question = request.form["qs"]
        response = get_response_from_bot(question)
        print(response)
    return render_template("html/index.html",response=response)

if __name__ == "__main__":
    app.run(debug=True)