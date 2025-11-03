from flask import Flask, jsonify, request
from flask_cors import CORS
from ai.pipeline import generate_recommendations
import os

import os
import requests
app = Flask(__name__)

# Ex.: CORS_ORIGINS=http://localhost:5173,https://orientai.vercel.app
CORS(app, resources={r"/api/*": {"origins": os.getenv("CORS_ORIGINS", "*").split(",")}})

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "OrientAI API funcionando!"})

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})

def _to_list(v):
    if v is None: 
        return []
    if isinstance(v, list):
        return [str(x).strip() for x in v if str(x).strip()]
    # aceita "ia, matemática" => ["ia","matemática"]
    return [s.strip() for s in str(v).split(",") if s.strip()]

def _to_str(v):
    return "" if v is None else str(v).strip()

def _to_int(v, default=None):
    try:
        return int(v)
    except Exception:
        return default

def _clamp(v, lo=1, hi=5):
    if v is None: 
        return None
    return max(lo, min(hi, v))

def _normalize_form(raw: dict) -> dict:
    return {
        # Dados básicos
        "name": _to_str(raw.get("name")),
        "age": _to_int(raw.get("age")),
        "year": _to_str(raw.get("year")),
        "city": _to_str(raw.get("city")),
        "state": _to_str(raw.get("state")),
        "country": _to_str(raw.get("country")),

        # Interesses e preferências
        "interest_areas": _to_list(raw.get("interest_areas")),          # ["Exatas","Humanas",...]
        "favorite_subjects": _to_list(raw.get("favorite_subjects")),    # ["Matemática","Física",...]
        "least_subjects": _to_list(raw.get("least_subjects")),          # ["Química","Geografia",...]
        "hobbies": _to_str(raw.get("hobbies")),

        # Desempenho e habilidades
        "strengths": _to_list(raw.get("strengths")),
        "improvements": _to_list(raw.get("improvements")),

        # Objetivos e estilo de aprendizado
        "study_modality": _to_str(raw.get("study_modality")),           # "Presencial" | "Online" | "Híbrido"
        "dream_course": _to_str(raw.get("dream_course")),

        # Perfil de personalidade
        "team_pref": _to_str(raw.get("team_pref")),                     # "Trabalho em equipe" | "Trabalho sozinho"
        "work_style": _to_str(raw.get("work_style")),                   # "Presencial" | "Remoto" | "Híbrido"
        "challenge_tolerance": _clamp(_to_int(raw.get("challenge_tolerance"))),  # 1..5
        "routine_preference": _clamp(_to_int(raw.get("routine_preference"))),    # 1..5
    }

@app.route("/api/recommend", methods=["POST"])
def recommend():
    raw = request.get_json(silent=True) or {}
    data = _normalize_form(raw)   # << usa o normalizado
    result = generate_recommendations(data)
    has_error = isinstance(result, dict) and ("error" in result or "erro" in result)
    return jsonify(result), (502 if has_error else 200)

@app.route("/debug/env", methods=["GET"])
def debug_env():
    return {
        "USE_MOCK": os.getenv("USE_MOCK", "MISSING"),
        "HF_KEY_present": bool(os.getenv("HF_KEY")),
        "HF_KEY_len": len(os.getenv("HF_KEY", "")),
        "HF_KEY_preview": os.getenv("HF_KEY", "")[:6] + "..." if os.getenv("HF_KEY") else None
    }

if __name__ == "__main__":
    debug = os.getenv("FLASK_DEBUG", "true").lower() == "true"
    port = int(os.getenv("PORT", "5000"))
    app.run(host="0.0.0.0", port=port, debug=debug)
