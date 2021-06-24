from flask import Flask, request, render_template
from api.db import database
from api.data import cot

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/CFTC", methods=['GET'])
def cftc():
    code = request.args.get('type')
    return database().get(code)
    
if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)
