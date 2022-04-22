# Faça um algoritmo para ler 50 números e armazenar em um vetor VET, 
# verificar e escrever se existem números repetidos no vetor VET e em que posições se encontram.

n = 3
vet = [0] * n

for i in range (n):
    vet [i] = input ("Digite o valor {atual} de {total}: ".format(atual = i+1, total = n))
print(vet)

