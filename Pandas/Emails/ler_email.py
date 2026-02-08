# instalar biblioteca pip install imap-tools
from imap_tools import MailBox, AND
from senha_email import senha_app

usuario = "paivatestes0@gmail.com"
senha = senha_app

meu_email = MailBox("imap.gmail.com").login(usuario, senha)

# Nesse for vamso puxar quais as pastas estao disponivels no email, caixa de entrada, saida etc
for pasta in meu_email.folder.list():
    print(pasta)
# meu_email.folder.set("[Gmail]/Sent Mail")   aqui estou mostrando que quero que ele leia os emails da caixa de emails enviados 

lista_emails = meu_email.fetch(AND(from_="paivatestes0@gmail.com", to="gui.dark@hotmail.com"))
#O retorno da lista email vem como um arquivo zipado. fazemos um for para pegar os arquivos zip

for i, email in enumerate(lista_emails):
    # esse if vai ser para fazer apenas em emails que tenham anexos
    if len(email.attachments) >0:
        print(email.subject)
        print(email.text)
        print(email.html)
        for anexo in email.attachments:
            with open(f"Email {i+1} - {anexo.filename}", "wb") as arquivo:
                arquivo.write(anexo.payload)
            print("Anexo:", anexo.filename)


             


    
