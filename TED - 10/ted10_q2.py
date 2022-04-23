# Faça um algoritmo para ler 50 números e armazenar em um vetor VET, 
# verificar e escrever se existem números repetidos no vetor VET e em que posições se encontram.

# Ler os nº
n = 8
vet = [0] * n

for i in range (n):
    vet [i] = input ("Digite o valor {atual} de {total}: ".format(atual = i+1, total = n))

print(vet)

# Mostra os nº repetidos
rept = []
lis = []

for n in vet:
    if n not in lis:
        lis.append(n)
    else:
        rept.append(n)

print("Nº repetidos: {}".format(rept))

# Posição do nº
lis = []
for lis in rept:
    if lis not in lis:
        lis.append(lis)
print("Posição: {}".format(lis))

