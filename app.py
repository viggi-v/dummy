from flask import Flask, render_template, request

#from app import app

from trial import solve

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/q/', methods = ["POST"])
def render_questionfile():
    return solve(request.form)
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
