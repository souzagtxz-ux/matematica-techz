import streamlit as st
from groq import Groq

# Configuração da página
st.set_page_config(
    page_title="Matematica Tech", 
    page_icon="🧪", 
    layout="centered",
    initial_sidebar_state="collapsed"
)

# CSS Estilo Hacker (Preto e Verde)
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stApp { background-color: #000000; }
    
    h1, h2, h3, p, span, label, .stMarkdown { 
        color: #00FF41 !important; 
        font-family: 'Courier New', Courier, monospace; 
    }
    
    .stButton>button { 
        background-color: #000000; 
        color: #00FF41; 
        border: 2px solid #00FF41;
        width: 100%;
        border-radius: 8px;
        font-weight: bold;
        height: 3.5em;
    }
    .stButton>button:hover { 
        background-color: #00FF41 !important; 
        color: #000000 !important; 
    }
    
    .stTextInput>div>div>input { 
        background-color: #050505; 
        color: #00FF41; 
        border: 1px solid #00FF41; 
    }

    .souza-footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #000;
        color: #00FF41;
        text-align: center;
        padding: 15px;
        font-family: 'Courier New', Courier, monospace;
        border-top: 1px solid #00FF41;
        font-size: 14px;
        z-index: 999;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'>⚡ MATEMATICA TECH ⚡</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>🧬 DATABASE GLOBAL ATIVA</p>", unsafe_allow_html=True)

# NOVA API KEY ATUALIZADA
client = Groq(api_key="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")

pergunta = st.text_input("📝 INSIRA O CÁLCULO:", placeholder="Ex: Resolva 2x + 5 = 15")

st.markdown("<br>", unsafe_allow_html=True)

c1, c2 = st.columns(2)

if pergunta:
    with c1:
        if st.button("🎯 RESPOSTA DIRETA"):
            with st.spinner("🔢 CALCULANDO..."):
                try:
                    prompt = f"Dê apenas o resultado direto de: {pergunta}"
                    resp = client.chat.completions.create(messages=[{"role":"user","content":prompt}], model="llama3-8b-8192")
                    st.success(f"✅ **RESULTADO:** {resp.choices[0].message.content}")
                except Exception as e:
                    st.error(f"❌ ERRO: {str(e)}")

    with c2:
        if st.button("👨‍🏫 MODO PROFESSOR"):
            with st.spinner("📚 ANALISANDO..."):
                try:
                    prompt = f"Explique o passo a passo de: {pergunta}"
                    resp = client.chat.completions.create(messages=[{"role":"user","content":prompt}], model="llama3-8b-8192")
                    st.info(f"📖 **PASSO A PASSO:**\n\n{resp.choices[0].message.content}")
                except Exception as e:
                    st.error(f"❌ ERRO: {str(e)}")

st.markdown('<div class="souza-footer">🛠️ CRIADO POR: SOUZA 🛠️</div>', unsafe_allow_html=True)
