from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.post('/webhooks')
def webhooks():
    with open('webhook.log', 'a') as log:
        params = request.get_json()
        log.write(f'{datetime.now()}\n')
        log.write(f'    {params}\n')
    return jsonify(params)
