from flask import Flask, request, jsonify
from flask_cors import CORS
from pprint import pprint

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


@app.route('/api/v1/payments', methods=['GET', 'POST'])
def webhook_payment_check():
    if request.method == 'POST':
        data = request.get_json()
        pprint(data)

        return jsonify({
            "success": {
                "message": "Pix's status has changed and the payment appears as paid.",
                "data": data,
                "code": 201,
            }
        }), 201

    return jsonify({
        "error": {
            "message": "This route requires calling via a Post method.",
            "type": "RequestMethodError",
            "code": 404
        }
    }), 404
