from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def front_server():

    url = "http://localhost:5000"
    output_text = "upload a file first!"
    return render_template('index.html', output_text=output_text, url=url)
    