# As maçãs custam R$ 1,30 cada se forem compradas menos de uma dúzia, e R$ 1,00 se forem compradas pelo menos 12. 
# Escreva um programa que leia o número de maçãs compradas, calcule e escreva o custo total da compra.


macas = int(input("Digite quantas maçãs você vai levar "))

if macas <= 11:
    print(f"Vai custar R$ {macas * 1.30}")

else:
    print(f"Vai custar R$ {macas * 1}")