import smtplib
import ssl
import os
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()

SMTP_SERVER = os.getenv("EMAIL_SMTP_HOST")
PORT = int(os.getenv("EMAIL_SMTP_PORT", 587))


def send_email(matricula: str):
    sender_email = os.getenv("EMAIL_SENDER")
    password = os.getenv("EMAIL_PASSWORD")
    receiver_email = os.getenv("EMAIL_RECEIVER")

    if not SMTP_SERVER:
        raise RuntimeError("EMAIL_SMTP_HOST não configurado")

    if not sender_email or not password or not receiver_email:
        raise RuntimeError("Variáveis de email não configuradas")

    msg = EmailMessage()
    msg["Subject"] = "Usuário removido"
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg.set_content(
        f"O usuário de matrícula {matricula} foi removido com sucesso do sistema."
    )

    context = ssl.create_default_context()

    with smtplib.SMTP(SMTP_SERVER, PORT, timeout=10) as server:
        server.starttls(context=context)
        server.login(sender_email, password)
        server.send_message(msg)
