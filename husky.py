#!/usr/bin/env python
from flask import *

app = Flask(__name__, template_folder='husky_web_ui')

@app.route('/')
def index():
    return render_template("husky.html")

if __name__ == "__main__":
    app.run()