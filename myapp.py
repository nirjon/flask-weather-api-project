from flask import Flask
import requests, json 

app = Flask(__name__)
        
@app.route("/", methods=["GET"])
def message():
    resp = requests.get("http://www.7timer.info/bin/api.pl?lon=113.17&lat=23.09&product=astro&output=json").json()
    #resp = requests.get("https://v2.jokeapi.dev/joke/Programming?type=single")
    return resp

if __name__=='__main__':
    app.run(debug=True)