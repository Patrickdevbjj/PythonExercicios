#4. Soma de números:
#Leia um número N e some todos os números de 1 a N usando while

numero = int(input("Escolhe um numero para ser somado: "))
n = 1
soma = 0  
while n <= numero:
    soma += n  
    n += 1  
print(f"A soma dos números de 1 a {numero} é {soma}")

    