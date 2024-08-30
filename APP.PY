import os
import platform

clientes = [
    {"nome": "Cliente 1", "classe": "Novo Cliente", "ativo": True},
    {"nome": "Cliente 2", "classe": "Cliente Frequente", "ativo": False},
    {"nome": "Cliente 3", "classe": "Cliente Frequente", "ativo": True}
]

def mostra_titulo():
    print("""
    
███████╗██╗░░██╗██████╗░██╗░░██╗██████╗░███████╗██╗██████╗░
██╔════╝██║░░██║██╔══██╗██║░░██║██╔══██╗██╔════╝██║██╔══██╗
█████╗░░███████║██████╔╝███████║██████╔╝█████╗░░██║██████╔╝
██╔══╝░░██╔══██║██╔═══╝░██╔══██║██╔═══╝░██╔══╝░░██║██╔══██╗
███████╗██║░░██║██║░░░░░██║░░██║██║░░░░███████╗██║██║░░██║
╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚═╝░░░░╚══════╝╚═╝╚═╝░░╚═╝

██████╗░██╗░░░░░██╗██╗░░██╗███████╗██╗░░██╗██╗░░██╗██╗██████╗░
██╔══██╗██║░░░░░██║██║░░██║██╔════╝██║░░██║██║░░██║██║██╔══██╗
██████╦╝██║░░░░░██║███████║█████╗░░███████║███████║██║██║░░██║
██╔══██╗██║░░░░░██║██╔══██║██╔══╝░░██╔══██║██╔══██║██║██║░░██║
██████╦╝███████╗██║██║░░██║███████╗██║░░██║██║░░██║██║██████╔╝
╚═════╝░╚══════╝╚═╝╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝╚═════╝░
""")

def mostra_escolhas():
    print("1. Cadastrar Cliente")
    print("2. Listar Clientes")
    print("3. Atualizar Informações do Cliente")
    print("4. Sair")

def escolhe_opcao():

    def exibir_subtitulo(texto):
        os.system("cls" if platform.system() == "Windows" else "clear")
        linha = '-' * 65
        print(linha)
        print(texto)
        print(linha)
        print(" ")

    def retorna_menu():
        input("Digite uma tecla para voltar ao menu principal ")
        main()

    def cadastrar_cliente():
        exibir_subtitulo("Cadastrar Cliente")

        nome_cliente = input("Digite o nome do cliente que deseja cadastrar: ")
        classe_cliente = input("Digite a classe do cliente: ")
        dados_do_cliente = {"nome": nome_cliente, "classe": classe_cliente, "ativo": True}
        clientes.append(dados_do_cliente)
        print(f"O cliente {nome_cliente} foi cadastrado com sucesso\n")

        retorna_menu()

    def listar_clientes():
        exibir_subtitulo("Lista de Clientes Cadastrados")
        for cliente in clientes:
            nome_cliente = cliente["nome"]
            classe_cliente = cliente["classe"]
            ativo = "Ativo" if cliente["ativo"] else "Inativo"
            print(f" - {nome_cliente.ljust(20)} | {classe_cliente.ljust(20)} | {ativo}")
        print()
        retorna_menu()

    def ativar_cliente():
        exibir_subtitulo("Ativar Cliente")
        nome_cliente = input("Digite o nome do cliente que deseja ativar/desativar: ")
        cliente_encontrado = False

        for cliente in clientes:
            if nome_cliente.lower() == cliente["nome"].lower():
                cliente_encontrado = True
                cliente["ativo"] = not cliente["ativo"]
                mensagem = f'O cliente {nome_cliente} foi ativado com sucesso' if cliente["ativo"] else f'O cliente {nome_cliente} foi desativado com sucesso'
                print(mensagem)
                break
        if not cliente_encontrado:
            print("Cliente não encontrado")

        retorna_menu()

    def atualizar_cliente():
        exibir_subtitulo("Atualizar Informações do Cliente")
        listar_clientes()
        if clientes:
            nome_cliente = input("Digite o nome do cliente para atualizar informações: ")
            for cliente in clientes:
                if cliente["nome"].lower() == nome_cliente.lower():
                    nova_classe = input("Digite a nova classe do cliente: ")
                    cliente["classe"] = nova_classe
                    cliente["ativo"] = True
                    print(f"As informações do cliente {nome_cliente} foram atualizadas com sucesso\n")
                    break
            else:
                print("Cliente não encontrado.")
        retorna_menu()

    def finalizar_programa():
        os.system("cls" if platform.system() == "Windows" else "clear")
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
            ativar_cliente()
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
