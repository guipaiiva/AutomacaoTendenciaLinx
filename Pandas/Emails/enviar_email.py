#SMTP
#OUTLOOK
# SERVIÇO DE E-MAILS (TWILLIO/ SENDGRID/ MAILGUN, POSTMART)

import smtplib
import email.message
from senha_email import senha_app


def enviar_email():
   
    msg = email.message.Message()
    msg['From'] = "paivatestes0@gmail.com"
    msg['To'] = "gui.dark@hotmail.com"
    msg['Subject'] = "Email enviado com Python"
    msg["Cc"] = "paivatestes0+copia@gmail.com"

    link_img_assinatura = "https://beecrowd.com/wp-content/uploads/2024/04/2022-07-19-Melhores-cursos-de-Python.jpg"
    corpo_email = f"""<p>Boa tarde</p>
    <p>Esse é meu primeiro email enviando com Python</p>
    <p>Att,</p>
    <p>Guilherme</p>
    <img src='{link_img_assinatura}'>
    """
    
    corpo_email = corpo_email.encode("utf-8")
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)
    
    servidor = smtplib.SMTP("smtp.gmail.com", 587)
    servidor.starttls()
    servidor.login(msg['From'], senha_app)
    servidor.send_message(msg)
    servidor.quit()
    print("Email Enviado")

enviar_email()
