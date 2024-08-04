from flask import Flask

app = Flask(__name__)

@app.route('/route_1')
def route_1():
    return 'Hello from route 1!'

@app.route('/route_3', methods=['DELETE'])
def route_3():
    return 'Hello from route 3 DELETE!'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

