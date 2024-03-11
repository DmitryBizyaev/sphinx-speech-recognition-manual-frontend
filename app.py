from flask import Flask, render_template, request
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
    audio_file_data = request.form['file']
    print(audio_file_data)
    return render_template('index.html', output_text=output_text, url=url)
    