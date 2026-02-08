#SMTP
#OUTLOOK
# SERVIÇO DE E-MAILS (TWILLIO/ SENDGRID/ MAILGUN, POSTMART)

import smtplib
import email.message
from senha_email import senha_app
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import os


def enviar_email():
   

    # bem parecido com o anterior porem muda aqui na msg pq usa a mimemultipart
    msg = MIMEMultipart()
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
    
    #Aqui vamos mudar tbm para adicionar o anexo
    msg.attach(MIMEText(corpo_email, "html"))
    #Anexar Arquivos
    with open("Emails/anexos/image.png", "rb") as arquivo:
        msg.attach(MIMEApplication(arquivo.read(), Name="image.png"))
    ## Se fosse para enviar uma lista de arquivos usaria no lugar    
    # lista arquivos = os.listdir("Emails/anexos") tudo que tiver na pasta anexos ele coloca na lista
    # ai faz um for para ler todos arquivos e anexar
    # for nome_arquivo in lista_arquivos:
        # with open(f"Emails/anexos/{nome_arquivo}", "rb") as arquivo:
            #msg.attach(MIMEApplication(arquivo.read(), Name="nome_arquivo"))
            

    
    servidor = smtplib.SMTP("smtp.gmail.com", 587)
    servidor.starttls()
    servidor.login(msg['From'], senha_app)
    servidor.send_message(msg)
    servidor.quit()
    print("Email Enviado")

enviar_email()…