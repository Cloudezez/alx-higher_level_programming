from flask import Flask

app = Flask(__name__)

@app.route('/route_3', methods=['DELETE'])
def handle_delete():
    return "I'm a DELETE request", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

