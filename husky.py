#!/usr/bin/env python
from flask import *

app = Flask(__name__, template_folder='husky_web_ui')

@app.route('/')
def index():
    return render_template("husky.html")

@app.route('/response', methods=['POST'])
def response():
    message = request.form.get("message")
    reply = husky(message)
    return render_template("husky.html", reply=reply)

if __name__ == "__main__":
    app.run()

def husky(message):
    return "Huksy says :: " + message