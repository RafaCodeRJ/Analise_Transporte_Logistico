from flask import Flask, jsonify
from src.modelos import ModeladorCustos

app = Flask(__name__)

@app.route('/prever-custo', methods=['POST'])
def prever_custo():
    # Implementar endpoint de previsão
    return jsonify({'previsao': 2500.0})
