# Consutra uma matriz A de tamanho 10 x 10 com valores inteiros e randômicos. 
# Depois Imprima o resultado da soma de todos os valores da matriz no terminal, depois;
# Depois construa uma nova matriz B, no qual cada item seja o valor da matriz A * 3.

import random
n = 2
m = []
b = []

for x in range(n):
    list_aux = []
    
    for y in range(n):
        list_aux.append(random.randint(1, 10))
    m.append(list_aux)

soma = 0

print(m)

for i in range(len(m)):
    list_aux = []
    for j in range(len(m[i])):
       soma = soma + m[i][j]
       list_aux.append(m[i][j] * 3)
    b.append(list_aux)
print(soma)

print(b)
   