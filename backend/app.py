from flask import Flask, jsonify
from flask_cors import CORS

import os
import requests
app = Flask(__name__)
CORS(app)

def recomendacao(data):
    age = data.get("age")
    year = data.get("year")
    interests = data.get("interests", [])
    hobbies = data.get("hobbies", [])
    strengths = data.get("strengths", [])
    weaknesses = data.get("weaknesses", [])

    prompt = f"""
    Você é como um orientador vocacional. Analise os dados do aluno e recomende cursos e áreas.
    Idade: {age}
    Ano escolar: {year}
    Interesses: {', '.join(interests)}
    Hobbies: {', '.join(hobbies)}
    Pontos fortes: {', '.join(strengths)}
    Pontos fracos: {', '.join(weaknesses)}
    """

    use_mock = os.getenv("USE_MOCK", "true").lower() == "true"
    if use_mock:
        return {
            "recommendations": [
                {
                    "course": "Engenharia de Computação",
                    "area": "Exatas / Tecnologia",
                    "reason": "Você se destaca em matemática e lógica e gosta de programação."
                },
                {
                    "course": "Design Digital",
                    "area": "Artes / Criatividade",
                    "reason": "Seu lado criativo e interesse em artes digitais fazem deste curso uma excelente opção."
                }
            ]
        }

    hf_url = os.getenv("HFURL")
    hf_key = os.getenv("HFKEY")
    headers = {"Authorization": f"Bearer {hf_key}"}
    payload = {"inputs": prompt}
    response = requests.post(hf_url, headers=headers, json=payload)

    if response.status_code != 200:
        return {"erro": "Falha em contatar a AI."}
    return response.json()

@app.route('/', methods=["GET"])
def home():
    return jsonify({'message': 'OrientAI API funcionando!'})

@app.route("/api/recommend", methods=["POST"])
def recommend():
    try:
        data = request.get_json()
        resposta = recomendacao(data)
        return jsonify(resposta)
    except Exception as erro:
        return jsonify({"error": str(erro)}), 500

if __name__ == '__main__':
    app.run(debug=True)
