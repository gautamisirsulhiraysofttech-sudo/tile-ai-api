from flask import Flask, request, jsonify
import cv2
import numpy as np

app = Flask(__name__)

# 👉 ADD THIS
@app.route('/')
def home():
    return "API is running"

@app.route('/detect', methods=['POST'])
def detect():
    file = request.files['image']
    return jsonify({"msg": "ok"})

app.run(host='0.0.0.0', port=10000)