import os
from google import genai
from google.genai import types
from google.genai.errors import ServerError
from dotenv import load_dotenv
from app.models.triage_schema import ResultadoTriagem

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

SYSTEM_INSTRUCTION = """
Você é o TechTriage AI, a primeira linha de defesa inteligente para o suporte técnico corporativo (N1).
Sua metáfora de atuação é ser um 'Paramédico de Resgate': absorva a ansiedade do usuário com empatia,
diagnostique relatos mesmo que ambíguos e estabilize a crise técnica rapidamente.

Regras:
- Se for um problema simples de N1 (reset de senha, configuração básica, limpar cache, reconectar VPN),
  marque 'resolvido_no_n1' como True e forneça um tutorial curto e direto em passos numerados.
- Se for queda de servidor, falha de hardware físico, incidente de segurança ou problema persistente,
  marque 'resolvido_no_n1' como False e gere um resumo técnico preciso para o analista N2.
"""

MODELOS_DISPONIVEIS = [
    "gemini-3.8-flash",
    "gemini-3.7-flash",
    "gemini-3.5-flash",
    "gemini-3.5-flash-lite",
]

def realizar_triagem(relato_usuario: str) -> ResultadoTriagem:
    ultimo_erro = None

    for modelo in MODELOS_DISPONIVEIS:
        try:
            response = client.models.generate_content(
                model=modelo,
                contents=relato_usuario,
                config=types.GenerateContentConfig(
                    system_instruction=SYSTEM_INSTRUCTION,
                    response_mime_type="application/json",
                    response_schema=ResultadoTriagem,
                    temperature=0.2,
                ),
            )
            return response.parsed
        except ServerError as e:
            ultimo_erro = e
            continue

    raise ultimo_erro