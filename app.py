from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

import os

# Initialize Flask app
app = Flask(__name__)

# Gemini API setup (make sure your API key is in a secure place)
genai.configure(api_key="AIzaSyCPQAuzzBxNX8vlR3Nvfj9PVE-3Pbqzt38")
model = genai.GenerativeModel('gemini-2.0-flash')

@app.route('/')
def home():
    return render_template("index.html")
@app.route('/scriptchat')
def scriptchat():
    return render_template('scriptchat.html')


@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    prompt = data.get('prompt')
    
    if not prompt:
        return jsonify({'response': 'No prompt provided'}), 400

    response = model.generate_content(prompt)
    return jsonify({'response': response.text})

if __name__ == '__main__':
    app.run(debug=True)
