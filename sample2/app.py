from flask import Flask
app = Flask(__name__)

@app.route("/welcome/<username>")
def welcome(username):
    return "Hi %s" % username

@app.route("/show_id/<int:user_id>")
def show_id(user_id):
    return "Your id is: %d" % user_id

@app.route("/welcome/<username>/show_id/<int:user_id>")
def welcome_and_show_id(username, user_id):
    return "Hi %s. Your id is: %d" % (username, user_id)

if __name__ == "__main__":
    app.run()

