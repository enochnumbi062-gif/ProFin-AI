import streamlit as st
import streamlit.components.v1 as components
import os

# 1. Configuration de la page Streamlit (Apparence et Titre)
st.set_page_config(
    page_title="ProFin-AI | Expertise Financière RDC",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="collapsed"
)

def main():
    # Style CSS pour cacher les éléments inutiles de Streamlit et centrer l'app
    st.markdown("""
        <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            .stApp {
                background-color: #001b22;
            }
        </style>
    """, unsafe_allow_html=True)

    # 2. Lecture du fichier HTML que nous avons créé ensemble
    # Assurez-vous que index.html est dans le même dossier que app.py
    html_file_path = "index.html"
    
    if os.path.exists(html_file_path):
        with open(html_file_path, 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        # 3. Injection du composant HTML (Le Pont)
        # On définit une hauteur de 900px pour éviter les barres de défilement internes
        components.html(html_content, height=900, scrolling=True)
    else:
        st.error(f"Erreur : Le fichier '{html_file_path}' est introuvable. Veuillez le placer à la racine du projet.")

    # 4. Sidebar (Optionnelle, pour donner du crédit ou des instructions)
    with st.sidebar:
        st.image("https://img.icons8.com/fluency/96/artificial-intelligence.png", width=80)
        st.title("ProFin-AI")
        st.info("Propriété de Dr Enoch Numbi. Solution d'IA dédiée à la bancabilité des projets en RDC.")
        st.write("---")
        st.caption("Version 1.0 - Déploiement Stable")

if __name__ == "__main__":
    main()
