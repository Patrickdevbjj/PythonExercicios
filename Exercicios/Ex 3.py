#3. Tabuada:
#Imprima a tabuada de um número digitado pelo usuário usando for.

tabuada = int(input("Digite o numero que voce deseja obter a tabuada: "))

for numero in range(11):
    resultado = tabuada * numero
    print(f'{tabuada} X {numero} = {resultado}')