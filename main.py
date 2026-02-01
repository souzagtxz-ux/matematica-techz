import streamlit as st
from groq import Groq
from PIL import Image

# Configuração da página para remover margens e menu
st.set_page_config(
    page_title="Matematica Tech", 
    page_icon="🧮", 
    layout="centered",
    initial_sidebar_state="collapsed"
)

# CSS Mestre: Interface Hacker + Modo Tela Cheia
st.markdown("""
    <style>
    /* Esconder Menu e Rodapé padrão do Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Fundo preto total e margens zero */
    .stApp {
        background-color: #000000;
    }
    
    /* Estilização de Textos */
    h1, h2, h3, p, span, label, .stMarkdown { 
        color: #00FF41 !important; 
        font-family: 'Courier New', Courier, monospace; 
    }
    
    /* Botões Estilo Matrix */
    .stButton>button { 
        background-color: #000000; 
        color: #00FF41; 
        border: 2px solid #00FF41;
        width: 100%;
        border-radius: 5px;
        font-weight: bold;
        transition: 0.3s;
    }
    .stButton>button:hover { 
        background-color: #00FF41; 
        color: #000000; 
        box-shadow: 0 0 15px #00FF41;
    }
    
    /* Input de texto */
    .stTextInput>div>div>input { 
        background-color: #111; 
        color: #00FF41; 
        border: 1px solid #00FF41; 
    }

    /* Rodapé Personalizado do SOUZA */
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
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_stdio=True)

# Título do App
st.markdown("<h1 style='text-align: center;'>📟 MATEMATICA TECH</h1>", unsafe_allow_stdio=True)
st.markdown("<p style='text-align: center;'>SISTEMA DE CÁLCULO AVANÇADO</p>", unsafe_allow_stdio=True)

# Inicializar Groq
client = Groq(api_key="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")

# Interface de Entrada
opcao = st.radio("MÉTODO DE ENTRADA:", ["✍️ TEXTO", "📸 CÂMERA"])

pergunta = ""

if opcao == "✍️ TEXTO":
    pergunta = st.text_input("DIGITE A EXPRESSÃO:")
else:
    foto = st.camera_input("SCANNER ATIVADO")
    if foto:
        pergunta = "Resolva este problema matemático da imagem."

st.markdown("<br>", unsafe_allow_stdio=True)

# Botões de Ação
c1, c2 = st.columns(2)

with c1:
    if st.button("⚡ DIRETA"):
        if pergunta:
            with st.spinner("PROCESSANDO..."):
                prompt = f"Responda apenas o resultado final: {pergunta}"
                resp = client.chat.completions.create(messages=[{"role":"user","content":prompt}], model="llama3-8b-8192")
                st.success(f"R: {resp.choices[0].message.content}")

with c2:
    if st.button("👨‍🏫 PROFESSOR"):
        if pergunta:
            with st.spinner("ANALISANDO..."):
                prompt = f"Explique o passo a passo didaticamente: {pergunta}"
                resp = client.chat.completions.create(messages=[{"role":"user","content":prompt}], model="llama3-8b-8192")
                st.info(f"EXPLICAÇÃO:\n\n{resp.choices[0].message.content}")

# Rodapé Fixo
st.markdown('<div class="souza-footer">CRIADO POR: SOUZA 🛠️</div>', unsafe_allow_stdio=True)
