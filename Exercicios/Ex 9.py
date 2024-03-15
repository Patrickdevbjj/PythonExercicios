print("=" * 30)
print("{:^30}".format("CAIXA ELETRÔNICO"))
print("=" * 30)

notas_disponiveis = [100, 50, 20, 10, 5, 2]

saldo = 0

while True:
    print("\nEscolha uma operação:")
    print("1. Ver saldo")
    print("2. Sacar")
    print("3. Depositar")
    print("4. Sair")

    opcao = int(input("Digite o número da operação desejada: "))

    if opcao == 1:
        print(f"Seu saldo atual é R${saldo}")
    elif opcao == 2:
        valor_do_saque = int(input("Digite o valor do saque: R$"))
        for notas in notas_disponiveis:
            while valor_do_saque >= notas:
                valor_do_saque -= notas
                saldo -= notas
                print(f"Total de R${notas} sacado... [OK]")
        if valor_do_saque == 0:
            print(f"Saque no valor total de R${saldo} realizado com sucesso!")
        else:
            print("As cédulas disponíveis neste caixa não permitem concluir esta transação.")
    elif opcao == 3:
        valor_do_deposito = int(input("Digite o valor do depósito: R$"))
        saldo += valor_do_deposito
        print(f"Depósito de R${valor_do_deposito} realizado com sucesso! Saldo atual: R${saldo}")
    elif opcao == 4:
        print("Obrigado por utilizar nosso caixa eletrônico. Volte sempre!")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")

