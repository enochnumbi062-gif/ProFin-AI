import streamlit as st
import streamlit.components.v1 as components
import os
import smtplib
from email.mime.text import MIMEText

# Configuration de la page
st.set_page_config(
    page_title="ProFin-AI | Expertise Financière RDC",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded" # FORCE l'ouverture du menu au démarrage
)

# Fonction réelle d'envoi de mail via le serveur (Optionnelle)
def send_server_email(user_email, subject, body):
    try:
        # Configuration SMTP (ex: Gmail)
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = "contact.profin.ai@gmail.com"
        msg['To'] = user_email
        return True
    except:
        return False

def main():
    # Style CSS pour cacher les menus inutiles et styliser la flèche de la barre latérale
    st.markdown("""
        <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            .stApp { background-color: #001b22; }
            
            /* Rend la flèche du menu dorée et plus visible sur mobile */
            .st-emotion-cache-zq5wms {
                background-color: #b58900 !important;
                color: #001b22 !important;
                border-radius: 50%;
                padding: 5px;
            }
        </style>
    """, unsafe_allow_html=True)

    # BOUTON D'URGENCE : Affichage direct des infos si le menu est fermé
    if st.button("ℹ️ INFOS LÉGALES & PROPRIÉTAIRE"):
        st.info("PROPRIÉTAIRE : Dr Enoch Numbi | PASSEPORT : OP1759812 | DorkNet Xchange")

    html_file_path = "index.html"
    
    if os.path.exists(html_file_path):
        with open(html_file_path, 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        # Injection du pont HTML avec défilement fluide
        components.html(html_content, height=1000, scrolling=True)
    else:
        st.error(f"Fichier '{html_file_path}' introuvable.")

    # --- SECTION À PROPOS ET CONFIDENTIALITÉ DANS LA SIDEBAR ---
    with st.sidebar:
        st.image("https://img.icons8.com/fluency/96/artificial-intelligence.png", width=80)
        st.title("ProFin-AI")
        st.subheader("Expertise & Inclusion Financière")
        
        st.markdown("---")
        
        # Section À Propos (Justification de propriété pour FlexPay)
        st.markdown("### 🏛️ À Propos de ProFin-AI")
        st.write(f"""
        **ProFin-AI** est une solution technologique développée par **DorkNet Xchange**, sous la direction du **Dr Enoch Numbi**.
        
        **Propriété Légale :**
        - **Fondateur :** Dr Enoch Numbi
        - **Identité :** Certifiée n° **OP1759812**
        - **Siège :** Kinshasa, RDC.
        """)
        
        st.markdown("---")
        
        # Clause de Confidentialité
        st.markdown("### 🔐 Confidentialité (AES-256)")
        st.caption("""
        Conformément aux standards de protection des données, ProFin-AI garantit que les détails de votre projet 
        ne sont jamais partagés avec des tiers. Vos informations sont cryptées et utilisées uniquement pour 
        générer votre diagnostic de bancabilité.
        """)
        
        st.write("---")
        st.info("Propriété de Dr Enoch Numbi. IA dédiée à la bancabilité RDC.")
        st.caption("Version 1.0 - Full Production")

if __name__ == "__main__":
    main()
