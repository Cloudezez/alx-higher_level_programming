#!/usr/bin/python3
from flask import Flask, request, jsonify, make_response

app = Flask(__name__)

@app.route('/status', methods=['GET'])
def status():
    return "OK"

@app.route('/post_email', methods=['POST'])
def post_email():
    email = request.form.get('email')
    if not email:
        return "No email provided", 400
    return f"Your email is: {email}"

@app.route('/search_user', methods=['POST'])
def search_user():
    q = request.form.get('q', '')
    if q == 'a':
        return jsonify(id=8446, name="amnirqhtfjq")
    elif q == 'b':
        return jsonify(id=7094, name="bmofakakhke")
    else:
        return jsonify([])

@app.route('/', methods=['GET'])
def index():
    return "Index"

@app.route('/status_401', methods=['GET'])
def status_401():
    return "Unauthorized", 401

@app.route('/status_404', methods=['GET'])
def status_404():
    return "Not Found", 404

@app.route('/status_500', methods=['GET'])
def status_500():
    return "Internal Server Error", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

