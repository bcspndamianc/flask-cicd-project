from flask import Flask, jsonify, request
from openai import OpenAI
import os

app = Flask(__name__)

# Configuración de OpenAI (usando variable de entorno)
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY', 'demo-key'))

@app.route('/')
def home():
    return jsonify({
        "status": "success",
        "message": "API Flask con IA funcionando correctamente",
        "endpoints": ["/", "/health", "/ai"]
    })

@app.route('/health')
def health():
    return jsonify({"status": "healthy", "service": "flask-ai-app"})

@app.route('/ai', methods=['POST'])
def ai_endpoint():
    try:
        data = request.get_json()
        prompt = data.get('prompt', 'Hola, ¿cómo estás?')
        
        # Simulación de respuesta IA (para testing)
        if os.getenv('TESTING') == 'true':
            return jsonify({
                "response": "Respuesta de prueba para testing",
                "prompt": prompt
            })
        
        # Llamada real a OpenAI
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=100
        )
        
        return jsonify({
            "response": response.choices[0].message.content,
            "prompt": prompt
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)