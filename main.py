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
    initial_sidebar_state="collapsed"
)

# Fonction réelle d'envoi de mail via le serveur (Optionnelle)
def send_server_email(user_email, subject, body):
    try:
        # Configuration SMTP (ex: Gmail)
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = "votre-email@gmail.com"
        msg['To'] = user_email
        # smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        # smtp.login("votre-email@gmail.com", "votre-mot-de-passe")
        # smtp.sendmail(msg['From'], msg['To'], msg.as_string())
        # smtp.quit()
        return True
    except:
        return False

def main():
    st.markdown("""
        <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            .stApp { background-color: #001b22; }
        </style>
    """, unsafe_allow_html=True)

    html_file_path = "index.html"
    
    if os.path.exists(html_file_path):
        with open(html_file_path, 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        # Injection du pont HTML avec défilement fluide
        components.html(html_content, height=1000, scrolling=True)
    else:
        st.error(f"Fichier '{html_file_path}' introuvable.")

    with st.sidebar:
        st.image("https://img.icons8.com/fluency/96/artificial-intelligence.png", width=80)
        st.title("ProFin-AI")
        st.info("Propriété de Dr Enoch Numbi. IA dédiée à la bancabilité RDC.")
        st.write("---")
        st.caption("Version 1.0 - Full Production")

if __name__ == "__main__":
    main()
