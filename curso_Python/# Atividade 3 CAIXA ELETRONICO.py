#CAIXA ELETRONICO
SALDO = 500
while True:
    print("\n=== CAIXA ELETRÔNICO ===")
    print("1 - Ver saldo")
    print("2 - Sacar valor")
    print("3 - Depositar valor")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        print(f"Seu saldo atual é: R$ {saldo:.2f}")
    elif opcao == "2":
        valor = float(input("Digite o valor para sacar: R$ "))
        if valor <= saldo:
            saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Saldo insuficiente para essa operação.")
    elif opcao == "3":
        valor = float(input("Digite o valor para depositar: R$ "))
        saldo += valor
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
    elif opcao == "4":
        print("Encerrando o programa. Obrigado por usar nosso caixa eletrônico!")
        break  # Encerra o laço
    else:
        print("Opção inválida. Tente novamente.")
