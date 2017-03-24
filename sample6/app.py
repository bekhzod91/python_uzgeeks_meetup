from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)

@app.route("/login", methods=['POST'])
def login():
    data = request.get_json()
    if data and data.get('username') == 'admin' and data.get('password') == '123':
        return jsonify(message='Welcome Admin')
    response = jsonify(message='Auth fail')
    response.status_code = 401
    return response

if __name__ == "__main__":
    app.run()

