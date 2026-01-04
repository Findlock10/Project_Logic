from flask import Flask, send_from_directory, jsonify, request
import os
import sqlite3
import datetime
import ollama
from fpdf import FPDF
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# --- SETTINGS [cite: 2026-01-04] ---
OUTPUT_DIR = r"C:\Scripts\Project_Logic\output"

def get_db():
    conn = sqlite3.connect('users.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    if not os.path.exists(OUTPUT_DIR): os.makedirs(OUTPUT_DIR)
    with get_db() as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE,
            password_hash TEXT,
            role TEXT DEFAULT 'User')''')
        conn.commit()

# --- AGENT TOOLS [cite: 2026-01-04] ---
def save_logic_pdf(content):
    try:
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=10)
        clean_text = content.encode('latin-1', 'replace').decode('latin-1')
        pdf.multi_cell(0, 10, txt=clean_text)
        
        filename = f"Logic_Auth_{datetime.datetime.now().strftime('%H%M%S')}.pdf"
        full_path = os.path.join(OUTPUT_DIR, filename)
        pdf.output(full_path)
        return full_path
    except:
        return None

# --- ROUTES ---
@app.route('/')
def index():
    return send_from_directory(os.getcwd(), 'Index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        user_msg = request.json.get("message", "")
        
        # Call Ollama Llama3.2 [cite: 2026-01-02]
        res = ollama.chat(model='llama3.2', messages=[
            {'role': 'system', 'content': 'You are a Senior Architect. Provide clean SQL/Python.'},
            {'role': 'user', 'content': user_msg}
        ])
        
        response_text = res['message']['content']
        saved_path = save_logic_pdf(response_text)

        # KEY FIX: We must return 'saved_at' so the UI doesn't say 'undefined'
        return jsonify({
            "response": response_text,
            "file_saved": True if saved_path else False,
            "saved_at": saved_path  # This fixes the UI error
        })
    except Exception as e:
        return jsonify({"response": f"SYSTEM_ERROR: {str(e)}", "file_saved": False})

if __name__ == '__main__':
    init_db()
    app.run(host='127.0.0.1', port=3001, debug=False)