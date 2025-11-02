# ai/pipeline.py
import os
import json
import requests

HF_BASE = "https://router.huggingface.co/v1"
# IMPORTANTE: o ID é case-sensitive. Este está correto.
MODEL_ID = os.getenv("HF_MODEL_ID", "meta-llama/Meta-Llama-3-8B-Instruct").strip()
HF_TIMEOUT = int(os.getenv("HF_TIMEOUT", "45"))  # segundos

def _build_prompt(d: dict) -> str:
    def join(xs): return ", ".join(x for x in xs if x)
    return f"""
Você é um orientador vocacional para ensino médio no Brasil.
Analise o perfil do estudante e recomende 3 cursos com área e justificativa curta.
Priorize cursos coerentes com interesses, matérias favoritas, habilidades e objetivos.
Se útil, considere modalidade preferida e estilo de trabalho.

Importante:
- Fale **diretamente com o estudante**, usando "você".
- Nunca use expressões como "para Fulano" ou "para o estudante".
- Use frases como "Os cursos mais recomendados para você são:".

Responda em JSON exatamente no formato:
{{"recommendations":[{{"course":"...", "area":"...", "reason":"..."}}, ...]}}

Dados básicos
- Nome: {d.get("name") or ""}
- Idade: {d.get("age") or ""}
- Ano escolar: {d.get("year") or ""}
- Cidade/Estado/País: {join([d.get("city"), d.get("state"), d.get("country")])}

Interesses e preferências
- Áreas de interesse: {join(d.get("interest_areas", []))}
- Matérias favoritas: {join(d.get("favorite_subjects", []))}
- Matérias menos favoritas: {join(d.get("least_subjects", []))}
- Hobbies/atividades: {d.get("hobbies") or ""}

Desempenho e habilidades
- Pontos fortes: {join(d.get("strengths", []))}
- Pontos a melhorar: {join(d.get("improvements", []))}

Objetivos e estilo de aprendizado
- Modalidade preferida: {d.get("study_modality") or ""}
- Curso dos sonhos / objetivo de carreira: {d.get("dream_course") or ""}

Perfil de personalidade
- Preferência: {d.get("team_pref") or ""} | Estilo de trabalho: {d.get("work_style") or ""}
- Tolerância a desafios (1–5): {d.get("challenge_tolerance") or ""}
- Preferência por rotina (1–5): {d.get("routine_preference") or ""}
""".strip()

def _call_hf_chat(prompt: str, hf_key: str):
    url = f"{HF_BASE}/chat/completions"
    headers = {
        "Authorization": f"Bearer {hf_key}",
        "Content-Type": "application/json",
        "Accept": "application/json",
    }
    payload = {
        "model": MODEL_ID,  # ex.: "meta-llama/Meta-Llama-3-8B-Instruct"
        "messages": [
            {"role": "system", "content": "Você é um orientador vocacional."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.3,
        "max_tokens": 1000,
        "stream": False
    }
    try:
        resp = requests.post(url, headers=headers, json=payload, timeout=HF_TIMEOUT)
    except requests.exceptions.Timeout:
        return None, {"error": "Timeout ao contatar a Hugging Face."}
    except requests.exceptions.RequestException as e:
        return None, {"error": f"Falha de rede ao contatar a Hugging Face: {e}"}

    if resp.status_code != 200:
        # Retorna detalhe para debug
        try:
            return None, resp.json()
        except Exception:
            return None, {"raw": resp.text}

    data = resp.json()
    text = (data.get("choices") or [{}])[0].get("message", {}).get("content")
    if not text:
        return None, {"error": "Retorno sem 'message.content'.", "raw": data}
    return text, None

def generate_recommendations(data: dict):
    # Ative mock só se quiser (USE_MOCK=true). Default: IA real.
    use_mock = os.getenv("USE_MOCK", "false").strip().lower() in ("1","true","yes","on")
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

    hf_key = os.getenv("HF_KEY", "").strip()
    if not hf_key:
        return {"error": "HF_KEY não configurada no ambiente."}

    prompt = _build_prompt(data)
    text, err = _call_hf_chat(prompt, hf_key)
    if err:
        return {"error": "Falha ao contatar a Hugging Face.", "detail": err}

    # Tenta parsear JSON como instruído
    try:
        parsed = json.loads(text)
        if isinstance(parsed, dict) and "recommendations" in parsed:
            return parsed
    except Exception:
        pass

    # Fallback: encapsula texto livre
    return {
        "recommendations": [
            {"course": "Resultado gerado pela IA", "area": "IA", "reason": text}
        ]
    }
