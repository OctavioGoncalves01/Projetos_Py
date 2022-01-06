import smtplib
from email.message import EmailMessage

#Email de saida
email_saida = 'email de saida'
password = 'senha do email de saida'

#Criaro email
msg = EmailMessage()
msg['Subject'] = 'Automação'
msg['From'] = 'email de saida'
msg['To'] = 'email para quem será enviado'
msg.set_content('Enviando um e-mail de forma automatica')

#enviando o email
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(email_saida, password)
    smtp.send_message(msg)