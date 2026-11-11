
import streamlit as st
from avu_chatbot import repondre

st.set_page_config(
    page_title="AVU-BOT",
    page_icon="🎓",
    layout="centered"
)

# ==========================================
# DESIGN PREMIUM AVU-BOT
# ==========================================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

:root {
    --navy: #10152F;
    --purple: #7957FF;
    --purple-dark: #25245B;
    --turquoise: #20D6C7;
    --white: #F4F6FF;
}

/* FOND PRINCIPAL */
.stApp {
    background:
        radial-gradient(ellipse at top left, rgba(121,87,255,0.16), transparent 45%),
        radial-gradient(ellipse at bottom right, rgba(32,214,199,0.10), transparent 40%),
        linear-gradient(135deg, #10152F, #151B3B 55%, #10152F);
    color: var(--white);
    font-family: 'Inter', sans-serif;
}

.block-container {
    max-width: 1050px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

/* BARRE SUPERIEURE STREAMLIT */
[data-testid="stHeader"] {
    background: #0F766E !important;
}

[data-testid="stAppDeployButton"] {
    background: transparent !important;
    color: white !important;
}

[data-testid="stToolbar"] {
    color: white !important;
}

/* BARRE LATERALE */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #151B3B, #10152F);
    border-right: 1px solid rgba(121,87,255,0.25);
}

section[data-testid="stSidebar"] * {
    color: var(--white);
}

/* TITRES */
h1, h2, h3, h4 {
    color: var(--white) !important;
    font-family: 'Inter', sans-serif !important;
    font-weight: 800 !important;
}

p, label {
    color: #C8CEE8;
}

/* EN-TETE PREMIUM */
.avu-header {
    text-align: center;
    padding: 42px 20px;
    margin-bottom: 28px;
    background: linear-gradient(125deg, #25245B, #7957FF, #20D6C7);
    border: 1px solid rgba(255,255,255,0.2);
    border-radius: 26px;
    box-shadow: 0 15px 45px rgba(0,0,0,0.30);
}

.avu-logo {
    font-size: 58px;
    margin-bottom: 5px;
}

.avu-title {
    color: white !important;
    font-size: 44px;
    font-weight: 800;
    letter-spacing: 3px;
    margin: 5px 0;
}

.avu-subtitle {
    color: #F4F6FF !important;
    font-size: 17px;
    margin-bottom: 20px;
}

.avu-status {
    display: inline-block;
    background: rgba(16,21,47,0.25);
    border: 1px solid rgba(255,255,255,0.3);
    color: white;
    padding: 9px 20px;
    border-radius: 30px;
    font-size: 13px;
    font-weight: 600;
}

/* BULLES DE DISCUSSION */
[data-testid="stChatMessage"] {
    border-radius: 20px;
    padding: 19px;
    margin-bottom: 16px;
    border: 1px solid rgba(255,255,255,0.10);
    box-shadow: 0 8px 25px rgba(0,0,0,0.18);
}

[data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-user"]) {
    background: linear-gradient(135deg, #25245B, #42358A);
    border: 1px solid rgba(121,87,255,0.55);
}

[data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-assistant"]) {
    background: linear-gradient(135deg, #123C55, #164C62);
    border: 1px solid rgba(32,214,199,0.35);
}

[data-testid="stChatMessage"] p {
    color: #F4F6FF !important;
}

/* ZONE DE SAISIE */
[data-testid="stChatInput"] {
    border-radius: 18px;
}

[data-testid="stChatInput"] textarea {
    background: #1B2345 !important;
    color: white !important;
    -webkit-text-fill-color: white !important;
    caret-color: #20D6C7 !important;
    border: 1px solid #7957FF !important;
    border-radius: 15px !important;
}

[data-testid="stChatInput"] textarea::placeholder {
    color: #C8CEE8 !important;
    -webkit-text-fill-color: #C8CEE8 !important;
    opacity: 1 !important;
}

[data-testid="stChatInput"] textarea:focus {
    border: 1px solid #20D6C7 !important;
    box-shadow: 0 0 0 2px rgba(32,214,199,0.15) !important;
}

/* BOUTONS */
.stButton > button {
    background: linear-gradient(110deg, #7957FF, #20D6C7);
    color: white !important;
    border: none;
    border-radius: 13px;
    padding: 11px 18px;
    font-weight: 700;
    transition: all 0.25s ease;
}

.stButton > button:hover {
    background: linear-gradient(110deg, #9278FF, #42E9D9);
    transform: translateY(-2px);
    box-shadow: 0 8px 24px rgba(121,87,255,0.3);
}

/* ==========================================
   SELECTEUR DE LANGUE - TEXTE BIEN VISIBLE
   ========================================== */

/* Titre du sélecteur */
[data-testid="stSelectbox"] label,
[data-testid="stSelectbox"] label p {
    color: #20D6C7 !important;
    -webkit-text-fill-color: #20D6C7 !important;
    font-weight: 700 !important;
    font-size: 15px !important;
}

/* Fond du menu */
[data-testid="stSelectbox"] [data-baseweb="select"] {
    background: #25245B !important;
    border: 1px solid #20D6C7 !important;
    border-radius: 14px !important;
    box-shadow: 0 4px 15px rgba(121,87,255,0.15);
}

/* Texte sélectionné */
[data-testid="stSelectbox"] [data-baseweb="select"] * {
    color: #FFFFFF !important;
    -webkit-text-fill-color: #FFFFFF !important;
}

/* Flèche du menu */
[data-testid="stSelectbox"] svg {
    fill: #20D6C7 !important;
    color: #20D6C7 !important;
}

/* Fond du menu déroulant */
[data-baseweb="popover"],
[data-baseweb="menu"],
[data-baseweb="popover"] ul {
    background: #25245B !important;
}

/* Options Français et English */
[data-baseweb="menu"] li,
[data-baseweb="menu"] li * {
    color: #FFFFFF !important;
    -webkit-text-fill-color: #FFFFFF !important;
}

/* Survol des options */
[data-baseweb="menu"] li:hover {
    background: #7957FF !important;
}

/* INTENTIONS RECONNUES */
[data-testid="stCaptionContainer"] {
    color: #20D6C7 !important;
}

/* LIENS */
a {
    color: #20D6C7 !important;
}

/* CARTE SIDEBAR */
.sidebar-card {
    text-align: center;
    padding: 24px 12px;
    margin-bottom: 22px;
    background: linear-gradient(135deg, #25245B, #7957FF, #147D83);
    border: 1px solid rgba(255,255,255,0.15);
    border-radius: 20px;
    box-shadow: 0 8px 25px rgba(0,0,0,0.20);
}

.sidebar-card h2 {
    color: white !important;
    margin: 5px 0;
}

.sidebar-card p {
    color: #F4F6FF !important;
    font-size: 13px;
}

/* MOBILE */
@media (max-width: 768px) {
    .block-container {
        padding: 1rem;
    }

    .avu-header {
        padding: 30px 15px;
    }

    .avu-title {
        font-size: 34px;
    }
}
</style>
""", unsafe_allow_html=True)


# ==========================================
# CHOIX DE LA LANGUE
# ==========================================

langue = st.selectbox(
    "Choisissez votre langue / Choose your language:",
    ["Français", "English"]
)

if langue == "Français":
    code_langue = "fr"
else:
    code_langue = "en"


# ==========================================
# INITIALISATION DE LA CONVERSATION
# ==========================================

if "messages" not in st.session_state:
    st.session_state.messages = []

if "bienvenue_affichee" not in st.session_state:
    st.session_state.bienvenue_affichee = False

if "langue_precedente" not in st.session_state:
    st.session_state.langue_precedente = code_langue

if st.session_state.langue_precedente != code_langue:
    st.session_state.langue_precedente = code_langue
    st.session_state.messages = []
    st.session_state.bienvenue_affichee = False


# ==========================================
# EN-TETE AVU-BOT
# ==========================================

st.markdown("""
<div class="avu-header">
    <div class="avu-logo">🎓</div>
    <h1 class="avu-title">AVU-BOT</h1>
    <p class="avu-subtitle">Assistant de Vie Universitaire</p>
    <span class="avu-status">
        ● Assistant en ligne | IRGIB Africa
    </span>
</div>
""", unsafe_allow_html=True)


# ==========================================
# PRESENTATION
# ==========================================

if code_langue == "fr":
    st.write("Bienvenue ! Je suis AVU-BOT, votre assistant universitaire.")
else:
    st.write("Welcome! I am AVU-BOT, your university assistant.")


# ==========================================
# BARRE LATERALE
# ==========================================

if code_langue == "fr":
    titre_sidebar = "Votre compagnon universitaire"
    titre_parametres = "⚙️ Paramètres"
    texte_bouton = "🗑️ Effacer la conversation"
else:
    titre_sidebar = "Your university companion"
    titre_parametres = "⚙️ Settings"
    texte_bouton = "🗑️ Clear conversation"

st.sidebar.markdown(f"""
<div class="sidebar-card">
    <div style="font-size: 42px;">🎓</div>
    <h2>AVU-BOT</h2>
    <p>{titre_sidebar}</p>
    <span style="color: #B9FFF5; font-size: 12px;">
        ● En ligne
    </span>
</div>
""", unsafe_allow_html=True)

st.sidebar.markdown(f"### {titre_parametres}")

if st.sidebar.button(texte_bouton):
    st.session_state.messages = []
    st.session_state.bienvenue_affichee = False
    st.rerun()


# ==========================================
# MESSAGE DE BIENVENUE
# ==========================================

if not st.session_state.bienvenue_affichee:

    if code_langue == "fr":
        message_bienvenue = (
            "Bonjour ! 👋 Je suis AVU-BOT, votre assistant "
            "de vie universitaire à IRGIB Africa. "
            "Comment puis-je vous aider ?"
        )
    else:
        message_bienvenue = (
            "Hello! 👋 I am AVU-BOT, your university life "
            "assistant at IRGIB Africa. How can I help you?"
        )

    st.session_state.messages.append({
        "role": "assistant",
        "content": message_bienvenue
    })

    st.session_state.bienvenue_affichee = True


# ==========================================
# AFFICHAGE DES MESSAGES
# ==========================================

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.write(message["content"])

        if message["role"] == "assistant" and "intention" in message:
            if code_langue == "fr":
                st.caption("Intention reconnue : " + message["intention"])
            else:
                st.caption("Recognized intent: " + message["intention"])


# ==========================================
# ZONE DE DISCUSSION
# ==========================================

if code_langue == "fr":
    question = st.chat_input("Posez votre question ici...")
else:
    question = st.chat_input("Ask your question here...")


# ==========================================
# TRAITEMENT DE LA QUESTION
# ==========================================

if question:

    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    reponse, intention = repondre(question, code_langue)

    st.session_state.messages.append({
        "role": "assistant",
        "content": reponse,
        "intention": intention
    })

    st.rerun()
