from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def main():
    url = "http://127.0.0.1:5000"
    output_text = "transcribed text will be here"
    return render_template('index.html', output_text=output_text, url=url)
    