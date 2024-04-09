agenda2024 = {}

while True:
    print("\n1. Adicionar evento")
    print("2. Ver eventos")
    print("3. Excluir evento")
    print("4. Sair")
    
    opcao = int(input("\nEscolha uma opção: "))
    
    if opcao == 1:
        data = input("\nDigite a data do evento (DD/MM): ")
        evento = input("Digite o nome do evento: ")
        if data in agenda2024:
            agenda2024[data].append(evento)
        else:
            agenda2024[data] = [evento]
        print(f"\nEvento '{evento}' adicionado na data {data}!")
        
    elif opcao == 2:
        data = input("\nDigite a data que deseja ver os eventos (DD/MM): ")
        if data in agenda2024:
            print(f"\nEventos na data {data}:")
            for evento in agenda2024[data]:
                print(evento)
        else:
            print("\nNada nesta data. Tá de boa! :D")
            
    elif opcao == 3:
        data = input("\nDigite a data do evento que deseja excluir (DD/MM): ")
        if data in agenda2024:
            evento = input("Digite o nome do evento que deseja excluir: ")
            if evento in agenda2024[data]:
                agenda2024[data].remove(evento)
                print(f"\nEvento '{evento}' excluído da data {data}!")
            else:
                print("\nNada marcado nesta data.")
        else:
            print("\nTem nada. Tá de boa! :D")
            
    elif opcao == 4:
        break
        
    else:
        print("\nOpção inválida. Tente novamente.")