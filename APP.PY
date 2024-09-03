import os

# Lista inicial de serviços e produtos no salão
servicos = [{"nome": "Corte de Cabelo", "categoria": "Serviço", "ativo": True},
            {"nome": "Manicure", "categoria": "Serviço", "ativo": True},
            {"nome": "Shampoo", "categoria": "Produto", "ativo": True}]

def mostra_titulo():
    print("""
███████╗██╗░░░░░███████╗░██████╗░░█████╗░███╗░░██╗░█████╗░███████╗  ██╗░░██╗░█████╗░██╗██████╗░
██╔════╝██║░░░░░██╔════╝██╔════╝░██╔══██╗████╗░██║██╔══██╗██╔════╝  ██║░░██║██╔══██╗██║██╔══██╗
█████╗░░██║░░░░░█████╗░░██║░░██╗░███████║██╔██╗██║██║░░╚═╝█████╗░░  ███████║███████║██║██████╔╝
██╔══╝░░██║░░░░░██╔══╝░░██║░░╚██╗██╔══██║██║╚████║██║░░██╗██╔══╝░░  ██╔══██║██╔══██║██║██╔══██╗
███████╗███████╗███████╗╚██████╔╝██║░░██║██║░╚███║╚█████╔╝███████╗  ██║░░██║██║░░██║██║██║░░██║
╚══════╝╚══════╝╚══════╝░╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝░╚════╝░╚══════╝  ╚═╝░░╚═╝╚═╝░░╚═╝╚═╝╚═╝░░╚═╝
""")

def mostra_escolhas():
    print("1. Cadastrar Serviço ou Produto")
    print("2. Listar Serviços e Produtos")
    print("3. Ativar/Desativar Serviço ou Produto")
    print("4. Sair")

def escolhe_opcao():

    def exibir_subtitulo(texto):
        os.system("cls")
        linha = "_" * 65
        print(linha)
        print(texto)
        print(linha)
        print(" ")

    def retorna_menu():
        input("Digite uma tecla para voltar ao menu principal")
        main()

    def cadastra_servico_produto():
        exibir_subtitulo("Cadastrar Serviço ou Produto")

        nome = input("Digite o nome do serviço ou produto: ")
        categoria = input(f"Digite a categoria (Serviço/Produto) para {nome}: ").capitalize()
        dados = {"nome": nome, "categoria": categoria, "ativo": True}
        servicos.append(dados)
        print(f"O {nome} foi cadastrado com sucesso\n")

        retorna_menu()

    def listar_servicos_produtos():
        exibir_subtitulo("Lista de Serviços e Produtos")
        for item in servicos:
            nome = item["nome"]
            categoria = item["categoria"]
            ativo = "Ativo" if item["ativo"] else "Inativo"
            print(f" - {nome.ljust(25)} | {categoria.ljust(15)} | {ativo}")
        retorna_menu()

    def ativar_desativar():
        exibir_subtitulo("Ativar/Desativar Serviço ou Produto")
        nome = input("Digite o nome do serviço ou produto que deseja ativar/desativar: ")
        encontrado = False

        for item in servicos:
            if nome == item["nome"]:
                encontrado = True
                item["ativo"] = not item["ativo"]
                status = "ativado" if item["ativo"] else "desativado"
                print(f"{nome} foi {status} com sucesso")
        if not encontrado:
            print("Não encontrado")
        retorna_menu()

    def finalizar_programa():
        os.system("cls" if os.name == "nt" else "clear")
        print("Finalizando o programa\n")

    def opcao_invalida():
        print("Essa opção não é válida")
        input("Aperte qualquer tecla para voltar")
        main()

    try:
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            cadastra_servico_produto()
        elif opcao == 2:
            listar_servicos_produtos()
        elif opcao == 3:
            ativar_desativar()
        elif opcao == 4:
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
