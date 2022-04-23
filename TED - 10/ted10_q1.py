# Faça um algoritmo para ler 20 números e armazenar em um vetor. 
# Após a leitura total dos 20 números, o algoritmo deve escrever esses 20 números lidos na ordem inversa.

n = 20
vet = [0] * n

for i in range (n):
    vet [i] = input ("Digite o valor {atual} de {total}: ".format(atual = i+1, total = n))
print(vet)
print(list(reversed(vet)))