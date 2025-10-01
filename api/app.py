from flask import Flask, request
import json
from flask_cors import CORS
import requests

app = Flask(__name__)

CORS(app)

@app.post('/get_code')
def get_code():
    username = "mihaiciorobitca007@gmail.com"
    password = "9T6wNEtKDAFTv3"
    file_path = request.json.get('file_path')

    payload = {
        "username": username,
        "password": password,
        "path": file_path
    }

    response = requests.post("https://eapi.pcloud.com/getfilepublink", json=payload)
    return json.dumps(response.json())
