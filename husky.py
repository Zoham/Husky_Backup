#!/usr/bin/env python
from flask import *

app = Flask(__name__, template_folder='husky_web_ui')

thread = {"Hey", "Hi !", "How is the weather today?", "You might need an umbrella today."}

@app.route('/')
def index():
    global thread
    return render_template("husky.html", thread=thread)

@app.route('/response', methods=['POST'])
def response():
    global thread
    message = request.form.get("message")
    thread.append(message)
    index()

    reply = husky(message)
    thread.append(reply)
    return index()

if __name__ == "__main__":
    app.run()

def husky(message):
    return "Huksy says :: " + message