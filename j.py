from google import genai

client = genai.Client(api_key="AIzaSyCPQAuzzBxNX8vlR3Nvfj9PVE-3Pbqzt38")

response = client.models.generate_content(  

model = "gemini-2.0-flash",contents="Hello, how are you?"
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    prompt = data['prompt']
    response = model.generate_content(prompt)
    return jsonify({'response': response.text})

if __name__ == '__main__':
    app.run(debug=True)