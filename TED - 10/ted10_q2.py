# Faça um algoritmo para ler 50 números e armazenar em um vetor VET, 
# verificar e escrever se existem números repetidos no vetor VET e em que posições se encontram.

import random

n = 50
vet = []

for i in range(0, n):
    vet.append(random.randint(1, 10))

print(vet)

checked = []

for i in vet:
    positions = []

    if i not in checked:
        checked.append(i)

        for j in range(0, len(vet)):
            if vet[j] == i:
                positions.append(j)

        if len(positions) > 1:
            print("O número {numero} aparece nas posições: {posicoes}".format(numero=i, posicoes=positions))
 
