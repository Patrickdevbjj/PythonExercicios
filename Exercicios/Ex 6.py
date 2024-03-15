#6. Média de notas:
#Leia as notas de N alunos e calcule a média da turma usando while.



cont = 1
opcao = ''
while opcao != 'nao':

    n1 = int(input("Qual a nota do primeiro aluno? "))
    n2 = int(input("Qual a nota do segundo aluno ? "))
    n3 = int(input("Qual a nota do terceiro aluno ? "))

    media = (n1 + n2 + n3) / 3

    print(f"A média dos alunos é {media:.3f}")

    opcao = input(print("Deseja calcular outras médias ? [sim/nao] "))