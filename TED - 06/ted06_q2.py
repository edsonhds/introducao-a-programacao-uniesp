# Ler o ano atual e o ano de nascimento de uma pessoa. 
# Escrever uma mensagem que diga se ela poderá ou não votar este ano 
# (não é necessário considerar o mês em que a pessoa nasceu).



print("Quer saber se você pode votar este ano?")
nascimento = int(input("Digite o ano de seu nascimento: "))
calculo = 2022 - nascimento
print("Você tem {}".format(calculo)) 

if calculo >= 18:
  print("Você pode votar")
else:
  print ("Você não pode votar")