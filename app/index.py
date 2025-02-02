
from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Load the JSON data
with open('q-vercel-python.json') as f:
    data = json.load(f)

@app.route('/api', methods=['GET'])
def get_data():
    name = request.args.get('name')
    result = next((item for item in data if item['name'] == name), None)
    return jsonify(result or {"error": "Name not found"})

if __name__ == "__main__":
    app.run()
