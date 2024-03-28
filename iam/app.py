from flask import Flask, redirect, url_for, request, render_template, jsonify
import subprocess
import urllib.request
import json
import datetime as date
import re
import pickle
import base64

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('./index.html')

@app.route('/', methods=['POST'])
def execute_command():
    command = request.form['command']
    output = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    stdout, stderr = output.communicate()
    output_text = stdout.decode()
    return render_template('index.html', output=output_text)

if __name__ == '__main__':
    app.run(debug=True)