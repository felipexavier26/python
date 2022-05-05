#Enviar email automatico usando python#
import win32com.client as win32 


# criar a intergração com o outlook
outlook = win32.Dispatch('outlook.application')

# criar o email
email = outlook.CreateItem(0)

# configurar as informações do seu email

# destino para onde enviar o email
email.To = "felipexavierbraz@hotmail.com.br"
# Assunto do email
email.subject = " E-mail automatico com python"
# email que sera enviar
email.HTMLBody = """
<p>Olá Felipe, aqui é o codigo Python</p>

<p>o faturamenta da loja foi de R$ 1.000</p>
<p>vendemos 10 produtos</P>
<p>o tickes Medio foi de R$ 1.50</p>

<p>Abs,</p>
<p>Abraços Python</P.
"""

email.Send()
print("Email Enviado")
