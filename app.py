import flask
from flask import request, jsonify

PROJECT_ID = "flask-1fa09"




app = flask.Flask(__name__)

@app.route('/', methods=['GET','POST'])
def home():
    if request.method == 'POST':
        print("peticion " + str(request.form))
        print("datos" + str(request.json))
        return jsonify(generateResponse(request.json["responseId"],
                                        request.json["queryResult"]["intent"]["name"],
                                        request.json["queryResult"]["intent"]["displayName"]))
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

def generateResponse(responseId, intentPath, intentName):
    return {
      "responseId": responseId,
      "session": "projects/" + PROJECT_ID + "/agent/sessions/" + responseId,
      "queryResult": {
        "queryText": "user's original query to your agent",
        "parameters": {
          "param": "param value"
        },
        "allRequiredParamsPresent": True,
        "fulfillmentText": "Text defined in Dialogflow's console for the intent that was matched",
        "fulfillmentMessages": [
          {
            "text": {
              "text": [
                "Text defined in Dialogflow's console for the intent that was matched"
              ]
            }
          }
        ],
        "outputContexts": [
          {
            "name": "projects/" + PROJECT_ID + "/agent/sessions/" + responseId + "/contexts/generic",
            "lifespanCount": 5,
            "parameters": {
              "param": "param value"
            }
          }
        ],
        "intent": {
          "name": intentPath,
          "displayName": intentName
        },
        "intentDetectionConfidence": 1,
        "diagnosticInfo": {},
        "languageCode": "es"
      },
      "originalDetectIntentRequest": {}
    }



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
