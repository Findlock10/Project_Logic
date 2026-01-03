from flask import Flask, send_from_directory, jsonify
import os

app = Flask(__name__)

# Logic Protocol: Serve the Frontend
@app.route('/')
def index():
    # 'send_from_directory' is the correct modern function
    return send_from_directory(os.getcwd(), 'index.html')

# Serve guard.js for the expiry alert logic
@app.route('/guard.js')
def serve_guard():
    return send_from_directory(os.getcwd(), 'guard.js')

# API for the 5-day expiry check
@app.route('/api/user-status')
def get_status():
    # Return 5 days from Jan 3, 2026 for testing
    return jsonify({"expiry_date": "2026-01-08"}) 

if __name__ == '__main__':
    print("--------------------------------------------------")
    print("LOGIC ENGINE ONLINE: http://127.0.0.1:3001")
    print("--------------------------------------------------")
    # Explicitly binding to 127.0.0.1
    app.run(host='127.0.0.1', port=3001, debug=True)