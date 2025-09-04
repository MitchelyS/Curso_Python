#mostrando o MENU
nomes = [] #cria uma lista vazia, ou seja, uma lista que não contém nenhum elemento LISTA
while True:# LOOP DE REPETIÇÃO
    print("1 - Menu")
    print("2 - Adicionar nomes")
    print("3 - Sair")
    opcao = input("Escolha uma opção:")
# CONDIÇÕES
    if opcao == "1": # SE
        nome = input("Digite um nome para adicionar")
        nomes.append(nome)# É um comando que adiciona o valor armazenado na variável nome ao final da lista nomes
        print(f"Nome '{nome}' adicionado com sucesso! :)")
        
    elif opcao == "2": #Se então
        print("\nLista de nomes:")
        if len(nomes) == 0:#serve para retornar o número de itens em um objeto
            print("Nenhum nome foi adicionado ainda.")
        else: #ou
            for nome in nomes:
                print(f"- {nome}")

    elif opcao == "3":
        print("Saindo do programa. Até mais!")
        break  # encerra o while

    else:
        print("Opção inválida. Tente novamente.")