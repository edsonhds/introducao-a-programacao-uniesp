# Desenvolva um sistema de autenticação, no qual se verifica o login e a senha. 
# O usuário deverá digitar o seu nome de usuário e sua senha. 
# Se os dois valores estiverem correto, imprima uma mensagem de boas-vindas para para o usuário, 
# se não imprima que o login ou a senha estão incorretos. Utilize nome de usuário e senhas fictícias dentro da estrutura de seleção.

login_cadastrado = 'Edson123'
senha_cadastrada ='1234'

login = str(input("Login:"))
senha = str(input("Senha:"))


if login == login_cadastrado and senha == senha_cadastrada:
  print("Seja bem vindo!")

else:
  print("Usuário ou senha incorreto")