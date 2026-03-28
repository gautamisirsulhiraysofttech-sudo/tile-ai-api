from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "API is running"

@app.route('/detect', methods=['POST'])
def detect():

    if 'image' not in request.files:
        return jsonify({"status": "error", "msg": "No image uploaded"})

    file = request.files['image']

    return jsonify({
        "status": "success",
        "msg": "image received",
        "filename": file.filename
    })
