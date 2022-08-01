from flask import Flask, render_template
from flask import request
from functions import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/rnlproccess', methods=['POST','GET'])
def process_text():
    message = request.form['base_msj']
    doc = evaluate_language(message)
    ents = get_information(message)
    return render_template('result.html',messages = message, docs_lang = doc, ents = ents)