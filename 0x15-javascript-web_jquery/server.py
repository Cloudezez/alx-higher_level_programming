from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to the Flask Server!"

@app.route('/header_color', methods=['POST'])
def header_color():
    color = request.json.get('color', '#FF0000')
    return jsonify({"color": color})

@app.route('/add_item', methods=['POST'])
def add_item():
    item = request.json.get('item', 'Item')
    return jsonify({"item": item})

@app.route('/update_header', methods=['POST'])
def update_header():
    header_text = request.json.get('header_text', 'New Header!!!')
    return jsonify({"header_text": header_text})

@app.route('/character', methods=['GET'])
def character():
    import requests
    response = requests.get('https://swapi-api.alx-tools.com/api/people/5/?format=json')
    return jsonify(response.json())

@app.route('/movies', methods=['GET'])
def movies():
    import requests
    response = requests.get('https://swapi-api.alx-tools.com/api/films/?format=json')
    return jsonify(response.json())

@app.route('/hello', methods=['GET'])
def hello():
    lang = request.args.get('lang', 'fr')
    import requests
    response = requests.get(f'https://hellosalut.stefanbohacek.dev/?lang={lang}')
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True, port=5001)

