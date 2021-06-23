from flask import Flask, request
from api.db import database
from api.data import cot

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"

@app.route("/CFTC", methods=['GET'])
def cftc():
    code = request.args.get('type')
    return database().get(code)
    
    
if __name__ == "__main__":
    app.run(debug=True)