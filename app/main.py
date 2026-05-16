from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/v1/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"}), 200

@app.route('/api/v1/data', methods=['POST'])
def process_data():
    data = request.get_json()
    if not data or 'input' not in data:
        return jsonify({"error": "Missing 'input' field"}), 400
    
    user_input = str(data['input'])
    if len(user_input) > 100:
        return jsonify({"error": "Input too long"}), 400

    return jsonify({"message": "Data processed successfully", "processed": user_input.upper()}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)