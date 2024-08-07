from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/route_6', methods=['POST'])
def handle_post():
    email = request.form.get('email')
    subject = request.form.get('subject')
    return jsonify({"message": f"Received email: {email} with subject: {subject}"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

