from flask import Flask, request, jsonify
from datetime import datetime
import logging

# DEBUG, INFO, WARNING (default), 'ERROR', 'CRITICAL'

logging.basicConfig(level=logging.DEBUG, filename='webhook.log',
        format='%(levelname)s:%(asctime)s:%(message)s')

app = Flask(__name__)

@app.post('/webhooks')
def webhooks():
    logging.debug(request.get_json())
    logging.debug(request.headers)
    return jsonify({'status': 'Push signal received'})
