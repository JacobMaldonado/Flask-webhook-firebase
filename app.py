import flask
from flask import request, jsonify

app = flask.Flask(__name__)

@app.route('/', methods=['GET','POST'])
def home():
    if request.method == 'POST':
        print("peticion " + str(request.form))
        print("datos" + str(request.json))
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
