from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app) # Crucial: This allows the browser to talk to Port 3001

@app.route('/process', methods=['POST'])
def process():
    try:
        data = request.json
        user_text = data.get('text', '')
        print(f"Logic received: {user_text}")

        # Talking to the Engine (Ollama)
        payload = {
            "model": "qwen2.5-coder",
            "prompt": "Return ONLY text. Text: " + user_text,
            "stream": False
        }
        
        # We use localhost and a 60-second timeout to prevent 'OFFLINE' flickers
        response = requests.post('http://localhost:11434/api/generate', json=payload, timeout=60)
        
        if response.status_code == 200:
            ai_text = response.json().get('response', '')
            return jsonify({"summary": ":) SAFE: " + ai_text})
        else:
            return jsonify({"summary": "ENGINE ERROR"}), 500

    except Exception as e:
        print(f"Error detail: {e}")
        return jsonify({"summary": "AI DISCONNECTED"}), 500

if __name__ == '__main__':
    print("------------------------------------")
    print("LOGIC ENGINE ONLINE: PORT 3001")
    print("------------------------------------")
    app.run(port=3001, debug=True)

