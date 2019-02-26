import flask
from flask import request, jsonify

PROJECT_ID = "flask-1fa09"

response = {
      "responseId": "ea3d77e8-ae27-41a4-9e1d-174bd461b68c",
      "session": "projects/" + PROJECT_ID + "/agent/sessions/88d13aa8-2999-4f71-b233-39cbf3a824a0",
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
            "name": "projects/" + PROJECT_ID + "/agent/sessions/88d13aa8-2999-4f71-b233-39cbf3a824a0/contexts/generic",
            "lifespanCount": 5,
            "parameters": {
              "param": "param value"
            }
          }
        ],
        "intent": {
          "name": "projects/" + PROJECT_ID + "/agent/intents/29bcd7f8-f717-4261-a8fd-2d3e451b8af8",
          "displayName": "Matched Intent Name"
        },
        "intentDetectionConfidence": 1,
        "diagnosticInfo": {},
        "languageCode": "en"
      },
      "originalDetectIntentRequest": {}
    }


app = flask.Flask(__name__)

@app.route('/', methods=['GET','POST'])
def home():
    if request.method == 'POST':
        print("peticion " + str(request.form))
        print("datos" + str(request.json))
        return jsonify(response)
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
