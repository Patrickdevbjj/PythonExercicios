#5. Fatorial:
#Calcule o fatorial de um número digitado pelo usuário usando while


numero = int(input("Digite um número inteiro positivo: "))
resultado = 1
cont = 1
while cont <= numero:
    resultado *= cont
    cont += 1
print(f"O fatorial de {numero} é {resultado}")
