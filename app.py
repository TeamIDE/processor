from flask import Flask, redirect, url_for, request, render_template, jsonify
from flask_cors import CORS, cross_origin
import pdb
import requests
import subprocess

app = Flask(__name__)
CORS(app)


@app.route('/processor', methods=['POST'])
def process():
    """
        Handles the request and creates a file for the executor to run
    """
    data = request.get_json()
    create_file(data)
    # incredibly dangerous command and not suitable for prod
    output = subprocess.check_output(['python', 'file.py'])
    return jsonify(output)

def create_file(data):
    new_file = open('file.py', 'w')
    new_file.write(data['value'])
    new_file.close()

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=5002, debug=True)
