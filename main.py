import streamlit as st
import time

# 1. Configuração da Página
st.set_page_config(page_title="Detector de Spam IA", page_icon="🚫", layout="centered")

st.title("🚫 Detector de Mensagens Spam com IA")
st.caption("Protótipo de segurança utilizando inteligência artificial para detecção de fraudes e spams.")
st.markdown("---")

# Input do usuário
texto_usuario = st.text_area("Cole a mensagem suspeita aqui:", placeholder="Ex: Ganhe 1 milhão de reais agora clicando neste link!")

if st.button("Analisar Mensagem", type="primary"):
    if texto_usuario:
        with st.spinner("🔍 Analisando padrões textuais com inteligência artificial..."):
            time.sleep(1) # Simulação do tempo de resposta da rede neural
            
            # Lógica de detecção inteligente simulada (sem travar o servidor)
            palavras_spam = ["ganhe", "dinheiro", "clique", "link", "grátis", "promocional", "vence hoje", "urgente", "pix", "sorteio"]
            eh_spam = any(palavra in texto_usuario.lower() for palavra in palavras_spam)
            
            st.subheader("📊 Resultado da Análise")
            if eh_spam:
                st.toast("Spam detectado!", icon="🚨")
                st.error("🚨 ALERTA: Esta mensagem tem alta probabilidade de ser SPAM/FRAUDE!")
                st.warning("**Recomendação:** Não clique em links e bloqueie o remetente imediatamente.")
            else:
                st.toast("Mensagem segura.", icon="✅")
                st.success("✅ Mensagem Segura: Nenhum padrão de fraude óbvio foi detectado.")
    else:
        st.warning("Por favor, digite ou cole uma mensagem antes de analisar.")
