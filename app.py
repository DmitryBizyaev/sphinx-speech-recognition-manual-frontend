from flask import Flask
from flask import render_template
import requests

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def starting_state():

    url = "http://localhost:5000"
    output_text = "upload a file first!"
    return render_template('index.html', output_text=output_text, url=url)


@app.route("/test", methods=['POST'])
def main_state():

    url = "http://localhost:5000"
    output_text = "upload a file first!"
    # r = requests.post(url)
    print("received POST request")
    return render_template('index.html', output_text=output_text, url=url)
    