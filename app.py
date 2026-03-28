from flask import Flask, request, jsonify
import time

app = Flask(__name__)

@app.route('/')
def home():
    return "API is running"

@app.route('/detect', methods=['POST'])
def detect():
    try:
        file = request.files['image']
        
        # simulate processing delay safe
        time.sleep(1)

        return jsonify({
            "status": "success",
            "msg": "image received"
        })

    except Exception as e:
        return jsonify({
            "status": "error",
            "msg": str(e)
        })
