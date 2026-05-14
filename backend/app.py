from flask import Flask, request, jsonify
from flask_cors import CORS

from database import create_table
from model import ai_response

app = Flask(__name__)
CORS(app)

create_table()

@app.route('/chat', methods=['POST'])
def chat():

    user_message = request.json['message']

    response = ai_response(user_message)

    return jsonify({
        "reply": response
    })

@app.route('/')
def home():
    return "AI Backend Running 🚀"

if __name__ == '__main__':
    app.run(debug=True)