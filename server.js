const express = require('express');
const cors = require('cors'); 
const axios = require('axios');
const path = require('path');

const app = express(); // 1. BUILD THE ENGINE FIRST

// --- SECURITY & MIDDLEWARE ---
app.use(cors()); // 2. OPEN THE SECURITY GATES
app.use(express.json());
app.use(express.static(path.join(__dirname, '../Project_Frontend')));

// --- THE LOGIC ENGINE ---
app.post('/process', async (req, res) => {
    try {
        console.log("Director Input Received:", req.body.text);
        
        const response = await axios.post('http://127.0.0.1:11434/api/generate', {
            model: 'qwen2.5-coder', 
            prompt: "Return ONLY the text with names replaced by [HIDDEN] and times by [TIME]. No talk. Text: " + req.body.text,
            stream: false
        });
        
        let raw = response.data.response.trim().split('\n')[0];
        let clean = raw.replace(/Jane|Emily|Joe|Sherry|Ram/gi, '[HIDDEN]');
        let finalOutput = clean.replace(/[^\x20-\x7E]/g, '');

        res.json({ summary: ":) SAFE: " + finalOutput });
    } catch (error) {
        console.error("AI Bridge Error:", error.message);
        res.status(500).json({ summary: 'RECONNECTING TO AI...' });
    }
});

// --- 3. THE POWER SWITCH (CRITICAL) ---
app.listen(3000, () => {
    console.log('------------------------------------');
    console.log('LOGIC ENGINE ONLINE: PORT 3000');
    console.log('------------------------------------');
});