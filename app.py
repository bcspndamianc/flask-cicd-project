from flask import Flask, jsonify, request
import os

app = Flask(__name__)

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
        
        # En producción, aquí iría la llamada real a OpenAI
        # Por ahora retornamos una respuesta simulada
        return jsonify({
            "response": f"Respuesta simulada para: {prompt}",
            "prompt": prompt
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)