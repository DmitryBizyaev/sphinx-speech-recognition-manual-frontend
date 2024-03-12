from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def starting_state():

    output_text = "upload a file first!"
    return render_template('index.html', output_text=output_text)


@app.route("/upload_file", methods=['POST'])
def main_state():

    url = "http://localhost:5000"
    audio_file_data = request.files['fileData'].read()
    response = requests.post(url=url, data=audio_file_data)
    output_text = response.content.decode('utf-8')
    return render_template('index.html', output_text=output_text)