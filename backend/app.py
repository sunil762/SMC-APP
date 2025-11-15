from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
import os

# Create Flask app
app = Flask(__name__, static_folder='../frontend', static_url_path='/')
CORS(app)

@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok', 'service': 'smc-backend'})

@app.route('/api/predict', methods=['POST'])
def predict():
    # Dummy predict: echo JSON with a 'prediction' field
    data = request.get_json(force=True, silent=True) or {}
    # In real app: load model once, run inference, return result
    result = {
        'received': data,
        'prediction': 'dummy_label',
        'confidence': 0.42
    }
    return jsonify(result)

# Serve frontend static files (for single-server deployments)
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    # If path exists in frontend static, send it, otherwise serve index.html
    static_folder = os.path.join(os.path.dirname(__file__), '..', 'frontend')
    requested = os.path.join(static_folder, path)
    if path != "" and os.path.exists(requested):
        return send_from_directory(static_folder, path)
    return send_from_directory(static_folder, 'index.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
