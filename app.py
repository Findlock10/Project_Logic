from flask import Flask, send_from_directory, jsonify, request
import os
import requests # You might need to run 'pip install requests'

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory(os.getcwd(), 'index.html')

@app.route('/guard.js')
def serve_guard():
    return send_from_directory(os.getcwd(), 'guard.js')

# The 5-day expiry API
@app.route('/api/user-status')
def get_status():
    return jsonify({"expiry_date": "2026-01-08"}) 

# THE NEW AI ROUTE
@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    
    # Talking to Ollama
    ollama_response = requests.post('http://localhost:11434/api/generate', 
        json={
            "model": "qwen", # Ensure you have run 'ollama pull qwen'
            "prompt": user_message,
            "stream": False
        })
    
    return jsonify(ollama_response.json())

if __name__ == '__main__':
    print("--------------------------------------------------")
    print("LOGIC AI ONLINE: http://127.0.0.1:3001")
    print("--------------------------------------------------")
    app.run(host='127.0.0.1', port=3001, debug=True)