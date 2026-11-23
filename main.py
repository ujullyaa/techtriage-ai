import streamlit as st
from app.controllers.triage_controller import realizar_triagem

st.set_page_config(page_title="TechTriage AI", page_icon="🚑", layout="wide")
st.title("🚑 TechTriage AI — Triagem Inteligente N1")
st.caption("Primeira linha de defesa inteligente para suporte técnico corporativo")

aba_chat, aba_analista = st.tabs(["💬 Chat de Atendimento", "📊 Painel do Analista N2"])

if "chamados" not in st.session_state:
    st.session_state.chamados = []

with aba_chat:
    relato = st.chat_input("Descreva o que está acontecendo (ex: 'Não consigo acessar o sistema financeiro, dá erro 503')...")
    
    if relato:
        with st.spinner("Diagnosticando incidente..."):
            triagem = realizar_triagem(relato)
            st.session_state.chamados.append({"relato": relato, "dados": triagem})

    for item in st.session_state.chamados:
        d = item["dados"]
        with st.chat_message("user"):
            st.write(item["relato"])
        with st.chat_message("assistant"):
            col1, col2, col3 = st.columns(3)
            col1.metric("Categoria", d.categoria)
            col2.metric("Urgência", d.urgencia)
            col3.metric("Triagem", "✅ Autoatendimento N1" if d.resolvido_no_n1 else "🚨 Escalonado N2")

            st.markdown(d.mensagem_usuario)

            if not d.resolvido_no_n1:
                st.warning(f"**Dossiê para Escalonamento N2:** {d.resumo_escalonamento}")

with aba_analista:
    st.subheader("Visão Geral da Operação e Fila Escalonada")
    if not st.session_state.chamados:
        st.info("Nenhum chamado triado ainda. Teste enviar um relato na aba ao lado!")
    else:
        total = len(st.session_state.chamados)
        resolvidos = sum(1 for c in st.session_state.chamados if c["dados"].resolvido_no_n1)
        
        c1, c2, c3 = st.columns(3)
        c1.metric("Total de Chamados", total)
        c2.metric("Resolvidos pela IA (N1)", resolvidos)
        c3.metric("Taxa de Deflexão", f"{(resolvidos / total) * 100:.0f}%")

        st.divider()
        st.markdown("### 🚨 Chamados Escalonados para N2")
        for idx, c in enumerate(st.session_state.chamados, 1):
            if not c["dados"].resolvido_no_n1:
                st.error(f"**#{idx} [{c['dados'].urgencia}] {c['dados'].categoria}** — {c['dados'].resumo_escalonamento}")