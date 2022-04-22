# Crie um programa para verificar se a média aritmética de uma disciplina atingiu a nota 7,0. 
# Considere três notas, e aplique a fórmula da média aritmética, se o aluno atingiu a nota mínima ou maior, 
# imprima uma mensagem de parabéns, se não uma mensagem de que ele precisa estudar um pouco mais.

nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
nota3 = float(input("Digite a nota 3: "))
media = ((nota1 + nota2) + nota3) / 3 

if media >= 7:
    print("Parabéns!  Você tirou {}, esta na média.".format(media))
else:
    print("Você tirou {}, precisa estudar um pouco mais.".format(media))
