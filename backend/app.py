from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/add", methods=["POST"])
def add():
    data = request.json
    return jsonify({"result": data["a"] + data["b"]})

