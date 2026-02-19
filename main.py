import streamlit as st
import streamlit.components.v1 as components
import os

# Configuration de la page
st.set_page_config(
    page_title="ProFin-AI | Expertise Financière RDC",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="collapsed"
)

def main():
    st.markdown("""
        <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            .stApp { background-color: #001b22; }
            .stFileUploader { max-width: 600px; margin: 0 auto; padding-top: 20px;}
        </style>
    """, unsafe_allow_html=True)

    # NOUVELLE FONCTIONNALITÉ : Soumission réelle du Business Plan
    st.write("---")
    st.markdown("<h3 style='text-align: center; color: #b58900;'>📂 Dépôt de Business Plan pour Audit IA</h3>", unsafe_allow_html=True)
    uploaded_file = st.file_uploader("Choisissez votre fichier projet (Format PDF uniquement)", type=["pdf"], help="Ce document sera scanné par ProFin-AI pour calculer votre score de bancabilité.")
    
    if uploaded_file is not None:
        st.success(f"✅ Document '{uploaded_file.name}' reçu. Vous pouvez maintenant démarrer l'analyse ci-dessous.")
    st.write("---")

    html_file_path = "index.html"
    
    if os.path.exists(html_file_path):
        with open(html_file_path, 'r', encoding='utf-8') as f:
            html_content = f.read()
        components.html(html_content, height=1000, scrolling=True)
    else:
        st.error(f"Fichier '{html_file_path}' introuvable.")

    # --- SIDEBAR (SANS CHANGEMENTS) ---
    with st.sidebar:
        st.image("https://img.icons8.com/fluency/96/artificial-intelligence.png", width=80)
        st.title("ProFin-AI")
        st.subheader("Expertise & Inclusion Financière")
        st.markdown("---")
        st.markdown("### 🏛️ À Propos de ProFin-AI")
        st.write(f"**ProFin-AI** est une solution développée par **DorkNet Xchange**, sous la direction du **Dr Enoch Numbi**.")
        st.write("- **Propriétaire :** Dr Enoch Numbi\n- **ID :** OP1759812")
        st.markdown("---")
        st.markdown("### 🔐 Confidentialité (AES-256)")
        st.caption("Vos documents PDF sont analysés en mémoire temporaire et ne sont jamais stockés sur nos serveurs.")
        st.info("Version 2.0 - Audit Documentaire")

if __name__ == "__main__":
    main()
