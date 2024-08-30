import os

clientes = [
    {"nome": "Ana Silva", "categoria": "Novo Cliente", "ativo": True},
    {"nome": "Vitória Pereira", "categoria": "Cliente Frequente", "ativo": False},
    {"nome": "Maria Oliveira", "categoria": "Cliente Frequente", "ativo": True}
]

def mostra_titulo():
    print("""
    

██╗░░██╗░█████╗░██╗██████╗░    ███████╗██╗░░░░░███████╗░██████╗░░█████╗░███╗░░██╗░█████╗░███████╗
██║░░██║██╔══██╗██║██╔══██╗    ██╔════╝██║░░░░░██╔════╝██╔════╝░██╔══██╗████╗░██║██╔══██╗██╔════╝
███████║███████║██║██████╔╝    █████╗░░██║░░░░░█████╗░░██║░░██╗░███████║██╔██╗██║██║░░╚═╝█████╗░░
██╔══██║██╔══██║██║██╔══██╗    ██╔══╝░░██║░░░░░██╔══╝░░██║░░╚██╗██╔══██║██║╚████║██║░░██╗██╔══╝░░
██║░░██║██║░░██║██║██║░░██║    ███████╗███████╗███████╗╚██████╔╝██║░░██║██║░╚███║╚█████╔╝███████╗
╚═╝░░╚═╝╚═╝░░╚═╝╚═╝╚═╝░░╚═╝    ╚══════╝╚══════╝╚══════╝░╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝░╚════╝░╚══════╝""")

def mostra_escolhas():
    print("1. Cadastrar Cliente")
    print("2. Listar Clientes")
    print("3. Atualizar Informações do Cliente")
    print("4. Sair")

def escolhe_opcao():
    def exibir_subtitulo(texto):
        os.system("clear")
        print(texto)
        print(" ")

    def retorna_menu():
        input("Digite uma tecla para voltar ao menu principal ")
        main()

    def cadastrar_cliente():
        exibir_subtitulo("Cadastrar Cliente")

        nome_cliente = input("Digite o nome do cliente que deseja cadastrar: ")
        categoria_cliente = input("Digite a categoria do cliente: ")
        dados_do_cliente = {"nome": nome_cliente, "categoria": categoria_cliente, "ativo": True}
        clientes.append(dados_do_cliente)
        print(f"O cliente {nome_cliente} foi cadastrado com sucesso\n")

        retorna_menu()

    def listar_clientes():
        exibir_subtitulo("Lista de Clientes Cadastrados")
        if clientes:
            for cliente in clientes:
            nome_cliente = cliente["nome"]
            categoria_cliente = cliente["categoria"]
            ativo = "Ativo" if cliente["ativo"] else "Inativo"
            print(f" - {nome_cliente} | {categoria_cliente} | {ativo}")
        retorna_menu()

    def ativar_cliente():
        exibir_subtitulo("Ativar cliente")
        nome_cliente = input("Digite o nome do cliente que deseja ativar: ")
        cliente_encontrado = False

        for cliente in clientes:
            if nome_cliente == cliente['nome']:
                cliente_encontrado = True
                cliente['ativo'] = not cliente['ativo']
                mensagem = f'A categoria {nome_cliente} foi ativado/desativado com sucesso' if cliente['ativo'] else f'A categoria {nome_cliente} foi desativado'
                print(mensagem)
        if not cliente_encontrado:
            print('Não encontrado')        

    def atualizar_cliente():
        exibir_subtitulo("Atualizar Informações do Cliente")
        listar_clientes()
        if clientes:
            nome_cliente = input("Digite o nome do cliente para atualizar informações: ")
            for cliente in clientes:
                if cliente["nome"].lower() == nome_cliente.lower():
                    nova_categoria = input("Digite a nova categoria do cliente: ")
                    cliente["categoria"] = nova_categoria
                    cliente["ativo"] = True
                    print(f"As informações do cliente {nome_cliente} foram atualizadas com sucesso\n")
                    break
            else:
                print("Cliente não encontrado.")
        retorna_menu()

    def finalizar_programa():
        os.system("cls" if os.name == 'nt' else 'clear')
        print("Finalizando o programa\n")
        exit()

    def opcao_invalida():
        print("Opção inválida! Tente novamente.")
        input("Aperte qualquer tecla para voltar")
        main()

    try:
        opcao_escolhida = int(input("Escolha uma opção: "))
        if opcao_escolhida == 1:
            cadastrar_cliente()
        elif opcao_escolhida == 2:
            listar_clientes()
        elif opcao_escolhida == 3:
            atualizar_cliente()
        elif opcao_escolhida == 4:
            finalizar_programa()
        else:
            opcao_invalida()
    except ValueError:
        opcao_invalida()

def main():
    mostra_titulo()
    mostra_escolhas()
    escolhe_opcao()

if __name__ == "__main__":
    main()
