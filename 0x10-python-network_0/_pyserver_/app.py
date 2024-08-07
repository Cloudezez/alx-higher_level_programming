from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/route_1', methods=['GET'])
def route_1():
    return 'Route 1 Response', 200

@app.route('/route_2', methods=['GET'])
def route_2():
    return 'Route 2 Response', 200

@app.route('/route_3', methods=['DELETE'])
def route_3():
    return 'I\'m a DELETE request', 200

@app.route('/route_4', methods=['OPTIONS'])
def route_4():
    return '', 200, {'Allow': 'OPTIONS, HEAD, PUT'}

@app.route('/route_5', methods=['GET'])
def route_5():
    return 'Hello School!', 200

@app.route('/route_6', methods=['POST'])
def route_6():
    email = request.form.get('email')
    subject = request.form.get('subject')
    return jsonify({'message': f'Received email: {email} with subject: {subject}'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

