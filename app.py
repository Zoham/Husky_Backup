from flask import Flask, render_template, request
import requests
app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")

def get_bot_response():
    message = request.args.get('msg')
    sender = "hrishabh"
    r = requests.post('http://localhost:5002/webhooks/rest/webhook', json={"sender": sender, "message": message})
    s = ""
    for i in r.json():
        print(i)
        if i.get('text'):
            s = s +"\n" + i['text']
        if i.get('image'):
            s = s + "\n" + i['image']
    return s


if __name__ == "__main__":
    app.run()
