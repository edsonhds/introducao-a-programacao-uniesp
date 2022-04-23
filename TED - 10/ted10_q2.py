# Faça um algoritmo para ler 50 números e armazenar em um vetor VET, 
# verificar e escrever se existem números repetidos no vetor VET e em que posições se encontram.

# Ler os nº
n = 50
vet = [0] * n

for i in range (n):
    vet [i] = input ("Digite o valor {atual} de {total}: ".format(atual = i+1, total = n))

print(vet)

# Mostra os nº repetidos
rept = []
lis = []

for i in vet:
    if i not in lis:
        lis.append(i)
    else:
        rept.append(i)

print("Nº repetidos: {}".format(rept))

# Posição do nº
indice = []
for i in rept:
    indice.append(vet.index(i))
    
print("Posição: {}".format(indice))
