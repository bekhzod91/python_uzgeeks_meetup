from flask import Flask
from flask import jsonify
app = Flask(__name__)

@app.route("/welcome/<username>")
def welcome(username):
    return jsonify(username=username)

@app.route("/welcome/<username>/show_id/<int:user_id>")
def welcome_and_show_id(username, user_id):
    return jsonify(
            username=username,
            user_id=user_id
    )

if __name__ == "__main__":
    app.run()

