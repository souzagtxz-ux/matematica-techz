import streamlit as st
from groq import Groq

# Configuração da página
st.set_page_config(
    page_title="Matematica Tech", 
    page_icon="🧪", 
    layout="centered",
    initial_sidebar_state="collapsed"
)

# CSS Estilo Hacker + Emojis
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
        background-color: #00FF41; 
        color: #000000; 
        box-shadow: 0 0 20px #00FF41;
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
        letter-spacing: 2px;
    }
    </style>
    """, unsafe_allow_stdio=True)

# Cabeçalho com Emojis
st.markdown("<h1 style='text-align: center;'>⚡ MATEMATICA TECH ⚡</h1>", unsafe_allow_stdio=True)
st.markdown("<p style='text-align: center;'>🧬 UNIVERSO DE CÁLCULOS INFINITOS</p>", unsafe_allow_stdio=True)

# Inicializar Groq
client = Groq(api_key="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")

# Entrada
pergunta = st.text_input("📝 INSIRA SUA PERGUNTA OU CONTA:", placeholder="Ex: Baskara, Derivada, 2+2...")

st.markdown("<br>", unsafe_allow_stdio=True)

# Colunas para botões com Emojis
c1, c2 = st.columns(2)

if pergunta:
    with c1:
        if st.button("🎯 RESPOSTA DIRETA"):
            with st.spinner("🔢 CALCULANDO..."):
                try:
                    prompt = f"Resolva e dê apenas o resultado final: {pergunta}"
                    resp = client.chat.completions.create(messages=[{"role":"user","content":prompt}], model="llama3-8b-8192")
                    st.success(f"✅ **RESULTADO:** {resp.choices[0].message.content}")
                except:
                    st.error("⚠️ ERRO NO SISTEMA")

    with c2:
        if st.button("👨‍🏫 MODO PROFESSOR"):
            with st.spinner("📚 ANALISANDO..."):
                try:
                    prompt = f"Explique detalhadamente o passo a passo desta questão: {pergunta}"
                    resp = client.chat.completions.create(messages=[{"role":"user","content":prompt}], model="llama3-8b-8192")
                    st.info(f"📖 **PASSO A PASSO:**\n\n{resp.choices[0].message.content}")
                except:
                    st.error("⚠️ ERRO NA ANÁLISE")

# Rodapé Souza
st.markdown('<div class="souza-footer">🛠️ CRIADO POR: SOUZA 🛠️</div>', unsafe_allow_stdio=True)
