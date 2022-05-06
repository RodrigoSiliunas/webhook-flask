from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


@app.route('/api/v1/payments', methods=['GET', 'POST'])
def webhook_payment_check():
    pass
