from flask import Flask, render_template, request, jsonify
from pathlib import Path
import cv2
import numpy as np
from scripts.deploy_model import WasteDetectionDeployer
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max

# Create uploads folder
Path(app.config['UPLOAD_FOLDER']).mkdir(exist_ok=True)

# Load model once
print("[INFO] Loading waste detection model...")
deployer = WasteDetectionDeployer('models/best_model.pth')
print("[INFO] Model loaded successfully!")

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'bmp'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file provided'}), 400
        
        file = request.files['file']
        
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        if not allowed_file(file.filename):
            return jsonify({'error': 'File type not allowed'}), 400
        
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        print(f"[INFO] Predicting on: {filename}")
        result = deployer.detect_waste(filepath)
        
        response = {
            'filename': filename,
            'waste_detected': result['detected'],
            'confidence': float(result['confidence']),
            'class_id': int(result['class_id']),
            'message': 'Waste detected!' if result['detected'] else 'No waste detected'
        }
        
        return jsonify(response), 200
    
    except Exception as e:
        print(f"[ERROR] {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/health', methods=['GET'])
def health():
    return jsonify({
        'status': 'READY',
        'model': 'SmartWaste Detection v1.0',
        'device': 'CPU'
    }), 200

if __name__ == '__main__':
    print("\n" + "=" * 70)
    print("🚀 STARTING SMARTWASTE WEB APPLICATION")
    print("=" * 70)
    print("\n📱 Open your browser and go to: http://localhost:5000")
    print("\n" + "=" * 70 + "\n")
    
    app.run(debug=True, host='localhost', port=5000)