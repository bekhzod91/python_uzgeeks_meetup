from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/welcome/<username>")
def welcome(username):
    return render_template('welcome.html', username=username)

@app.route("/welcome/<username>/many/<int:many>")
def welcome_many_time(username, many):
    return render_template(
        'welcome_many_time.html',
        username=username,
        many=range(many)
    )

if __name__ == "__main__":
    app.run()

