from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Welcome to the Flask app!"})

@app.route("/add", methods=["POST"])
def add():
    data = request.json
    if "a" in data and "b" in data:
        return jsonify({"result": data["a"] + data["b"]})
    else:
        return jsonify({"error": "Missing parameters 'a' and 'b'"}), 400

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))  # Use the PORT provided by Render
    app.run(debug=True, host="0.0.0.0", port=port)
