from flask import Flask, jsonify, request
from flask_cors import CORS
from ai.pipeline import generate_recommendations
import os
import sqlite3
import json
import requests
app = Flask(__name__)

# Ex.: CORS_ORIGINS=http://localhost:5173,https://orientai.vercel.app
CORS(app, resources={r"/api/*": {"origins": os.getenv("CORS_ORIGINS", "*").split(",")}})

DB_PATH = os.getenv("DB_PATH", "orientai.db")
# Banco de Dados 
def connect_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def create_tables():
    with connect_db() as conn:
        conn.executescript("""
        CREATE TABLE IF NOT EXISTS student_forms (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER,
            year TEXT,
            city TEXT,
            state TEXT,
            country TEXT,
            interest_areas TEXT,
            favorite_subjects TEXT,
            least_subjects TEXT,
            hobbies TEXT,
            strengths TEXT,
            improvements TEXT,
            study_modality TEXT,
            dream_course TEXT,
            team_pref TEXT,
            work_style TEXT,
            challenge_tolerance INTEGER,
            routine_preference INTEGER,
            motivations TEXT,
            recommendations_json TEXT
        );
        """)
        conn.commit()

def save_form(data: dict, recommendations: dict):
    with connect_db() as conn:
        conn.execute("""
            INSERT INTO student_forms (
                name, age, year, city, state, country,
                interest_areas, favorite_subjects, least_subjects, hobbies,
                strengths, improvements, study_modality, dream_course,
                team_pref, work_style, challenge_tolerance, routine_preference,
                motivations, recommendations_json
            ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
        """, (
            data.get("name"),
            data.get("age"),
            data.get("year"),
            data.get("city"),
            data.get("state"),
            data.get("country"),
            ", ".join(data.get("interest_areas", [])),
            ", ".join(data.get("favorite_subjects", [])),
            ", ".join(data.get("least_subjects", [])),
            data.get("hobbies"),
            ", ".join(data.get("strengths", [])),
            ", ".join(data.get("improvements", [])),
            data.get("study_modality"),
            data.get("dream_course"),
            data.get("team_pref"),
            data.get("work_style"),
            data.get("challenge_tolerance"),
            data.get("routine_preference"),
            data.get("motivations"),
            json.dumps(recommendations)
        ))
        conn.commit()

def fetch_forms(limit=20):
    with connect_db() as conn:
        cur = conn.execute("SELECT * FROM student_forms ORDER BY id DESC LIMIT ?", (limit,))
        return [dict(row) for row in cur.fetchall()]
    

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

@app.route("/initdb", methods=["GET"])
def initdb():
    create_tables()
    return jsonify({"status": "ok", "message": "Database initialized successfully!"})

@app.route("/api/forms", methods=["GET"])
def get_forms():
    forms = fetch_forms(limit=20)
    return jsonify(forms)

@app.route("/api/recommend", methods=["POST"])
def recommend():
    raw = request.get_json(silent=True) or {}
    data = _normalize_form(raw)   # << usa o normalizado
    result = generate_recommendations(data)
    try:
        save_form(data, result)
    except Exception as e:
        print("Error saving to database:", e)
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
    create_tables()
    app.run(host="0.0.0.0", port=port, debug=debug)
