from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from chatbot.furia_bot import ChatbotFURIA

app = Flask(__name__)
CORS(app)
bot = ChatbotFURIA()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/mensagem', methods=['POST'])
def handle_message():
    try:
        data = request.get_json()
        user_message = data.get('mensagem', '').strip()
        
        if not user_message:
            return jsonify({'resposta': 'Digite uma mensagem válida.'}), 400
        
        resposta = bot.responder(user_message)
        return jsonify({'resposta': resposta})
    
    except Exception as e:
        return jsonify({'resposta': f'Erro: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)