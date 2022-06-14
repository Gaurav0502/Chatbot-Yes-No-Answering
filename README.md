# RailBot
## Requirements needed to be installed
- Open a terminal and install all the required modules of python from requirements.txt using pip or equivalent.
```
pip install requirements.txt
```
- Having met all the requirements, the code in this repository shall work fine.
## Problem Statement
Development and Deployment of a simple chatbot which gives a Yes or No reply for the given question.
## Components
Every chatbot development process comprises of three key components as follows:

 1. Intent Classification
 2. Entity Extraction
 3. Question Answering
 4. Deployment using Flask

### Intent Classification
Generally, a chatbot is made to cater a specific domain and each domain has some specific number of intents. An intent is resembles the significance of the question.   In this particular case, there two types of intents:

1. TrainCheck - Enquiry about the train name and numbers.
2. RouteCheck - Enquiry regarding the existence of a route between a source and destination.

Here, for intent classification each intent had two questions and for an new question, the following steps where followed:

1. Calculating the similiarity of the new question with all questions under each intent.
2. Averaging out the similiarities for question under each intent.
3. The intent with maximum average similiarity is alloted.

**<u>Note:</u>** For calculating similiarity between two word embeddings, spacy by defualt uses the Cosine Similiarity. Moreover, for use cases with higher number intents and question training examples machine learning models like Decision Trees and Neural Networks would be more appropriate.
     
### Entity Extraction
After obtaining the intent behind the question, we shall extract the entities from the question. Here, the entities are mainly train numbers, train names, source and destination and they are mapped to existing named entities as follows:
<table>
    <tr>
        <th>Entity Type</th>
        <th>Its Meaning</th>
        <th>Used for</th>
    </tr>
    <tr>
        <td>CARDINAL</td>
        <td>Numerical Values that are not dates, 
            times, percent, money or quantity</td>
        <td>Train Number</td>
    </tr>
    <tr>
        <td>GPE</td>
        <td>Geo-Political Entity</td>
        <td>Stations</td>
    </tr>
    <tr>
        <td>FAC</td>
        <td>Facilites</td>
        <td>Train Name</td>
    </tr>
</table>

For entity extraction, Named Entity Recognition(NER) model from spacy was used with fine-tuning the above mentioned entities using Transfer Learning.

### Question Answering
Having acquired the intent and entities, now we answer the question from a knowledge-base or a database. For this chatbot, the types of answers are as follows:

1. Yes
2. No
3. Seems like an error occurred while answering question.

Since, the knowledge of the chatbot was confined to a dataset, the questions were answering by querying a Pandas DataFrame. 

### Deployment using Flask
Having a fully functional chatbot, the next task is to integrate it with the web application. The major steps involved in deploying a chatbot are as follows:

1. Creating User Interface for the chatbot.
2. Building a restful-API to get the response of the chatbot on receiving the question.
3. Dynamically adding the questions and responses to User Interface.
4. Testing the chatbot and maintaining a log for it.

