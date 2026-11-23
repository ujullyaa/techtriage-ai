# 🚑 TechTriage AI — Triagem Inteligente para Suporte Técnico N1

![Python](https://img.shields.io/badge/Python-3.14-blue?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Interface-FF4B4B?logo=streamlit&logoColor=white)
![Gemini API](https://img.shields.io/badge/Google%20Gemini-Structured%20Outputs-8E75B2?logo=googlegemini&logoColor=white)
![Arquitetura](https://img.shields.io/badge/Arquitetura-MVC-success)

**TechTriage AI** é uma solução de primeira linha de defesa inteligente (N1) para suporte técnico corporativo. Projetado sob a metáfora de um *"Paramédico de Resgate"*, o sistema acolhe relatos ambíguos de usuários, realiza o diagnóstico técnico instantâneo, guia resoluções de autoatendimento e consolida dossiês estruturados para escalonamento ágil ao time de N2.

---

## 🎯 Problema & Proposta de Valor

Equipes de Service Desk (N1) sofrem com alto volume de chamados repetitivos (redefinição de senhas, falhas de VPN, limpeza de cache), gerando gargalos no atendimento e desviando analistas de incidentes críticos. 

O **TechTriage AI** resolve esse atrito por meio de três pilares:
1. **Absorção de Ansiedade:** Comunicação empática e adaptada ao nível técnico do solicitante.
2. **Deflexão Inteligente (N1):** Resolução imediata de problemas recorrentes via tutoriais passo a passo.
3. **Escalonamento Cirúrgico (N2):** Envio de incidentes graves já classificados por categoria e severidade, eliminando o retrabalho de triagem manual.

---

## 🏗️ Arquitetura do Projeto (Padrão MVC)

O sistema foi estruturado seguindo o padrão **Model-View-Controller (MVC)** para separar responsabilidades entre regras de validação, integração com IA e interface visual:

- `app/models/triage_schema.py` — **Model:** Schemas Pydantic (Structured Outputs)
- `app/controllers/triage_controller.py` — **Controller:** Orquestração com Google Gemini e fallback resiliente
- `main.py` — **View:** Interface Streamlit (Chat N1 + Painel N2)
- `requirements.txt` — Dependências do ambiente Python
- `.env.example` — Template de configuração da API Key
- `.gitignore` — Proteção de credenciais e ambiente virtual

---

## 📊 Matriz de Classificação e Triagem

A IA utiliza **Structured Outputs** (via Pydantic) para garantir que toda resposta siga estritamente o contrato de dados esperado pela aplicação:

| Campo | Valores / Tipo | Função no Sistema |
| :--- | :--- | :--- |
| **`categoria`** | `Rede/VPN`, `Acesso/Senha`, `Hardware`, `Software`, `Infraestrutura Crítica` | Roteamento técnico do incidente |
| **`urgencia`** | `P1 - Crítico`, `P2 - Alto`, `P3 - Médio`, `P4 - Baixo` | Priorização baseada no impacto operacional |
| **`resolvido_no_n1`** | `True` / `False` | Define se o chamado é encerrado em autoatendimento ou enviado à fila N2 |
| **`mensagem_usuario`** | `str` | Orientação humanizada e passo a passo numerado para o colaborador |
| **`resumo_escalonamento`** | `str` | Dossiê técnico objetivo exibido no **Painel do Analista N2** |

---

## 🚀 Como Executar Localmente

### Pré-requisitos
- Python 3.10 ou superior
- Uma chave de API gratuita do [Google AI Studio](https://aistudio.google.com/)

### Passo a passo

1. **Clone o repositório e acesse a pasta:**
   `git clone https://github.com/ujullyaa/techtriage-ai.git && cd techtriage-ai`
2. **Crie e ative o ambiente virtual:**
   `python3 -m venv .venv && source .venv/bin/activate`
3. **Instale as dependências:**
   `pip install -r requirements.txt`
4. **Configure as variáveis de ambiente:**
   `cp .env.example .env` *(abra o `.env` e adicione sua `GEMINI_API_KEY`)*
5. **Inicie a aplicação:**
   `streamlit run main.py`

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python
- **Inteligência Artificial:** Google GenAI SDK (`gemini-3.8-flash` com fallback automático para modelos Flash)
- **Validação de Dados:** Pydantic
- **Interface Web:** Streamlit

---

## 👩‍💻 Autoria

Desenvolvido por **Jullya Conceição** — Estudante de Sistemas de Informação (UFSC) & Suporte Técnico N1.