import flask
from flask import request, jsonify

PROJECT_ID = "flask-1fa09"




app = flask.Flask(__name__)

@app.route('/', methods=['GET','POST'])
def home():
    if request.method == 'POST':
        print("peticion " + str(request.form))
        print("datos" + str(request.json))
        return jsonify(generateResponse(request.json["session"]))
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

def generateResponse(sessionPath):
    return {
              "fulfillmentText": "This is a text response",
              "fulfillmentMessages": [
                {
                  "card": {
                    "title": "card title",
                    "subtitle": "card text",
                    "imageUri": "https://assistant.google.com/static/images/molecule/Molecule-Formation-stop.png",
                    "buttons": [
                      {
                        "text": "button text",
                        "postback": "https://assistant.google.com/"
                      }
                    ]
                  }
                }
              ],
              "source": "example.com",
              "payload": {
                "google": {
                  "expectUserResponse": True,
                  "richResponse": {
                    "items": [
                      {
                        "simpleResponse": {
                          "textToSpeech": "this is a simple response"
                        }
                      }
                    ]
                  }
                },
                "facebook": {
                  "text": "Hello, Facebook!"
                },
                "slack": {
                  "text": "This is a text response for Slack."
                }
              },
              "outputContexts": [
                {
                  "name": sessionPath + "/contexts/contextName",
                  "lifespanCount": 5,
                  "parameters": {
                    "param": "param value"
                  }
                }
              ],
              "followupEventInput": {
                "name": "event name",
                "languageCode": "en-US",
                "parameters": {
                  "param": "param value"
                }
              }
            }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
