import os

clientes = []

def exibir_nome_do_programa():
    print("""
██████╗░██╗░█████╗░  ██╗░░██╗░█████╗░██╗██████╗░
██╔══██╗██║██╔══██╗  ██║░░██║██╔══██╗██║██╔══██╗
██████╦╝██║███████║  ███████║███████║██║██████╔╝
██╔══██╗██║██╔══██║  ██╔══██║██╔══██║██║██╔══██╗
██████╦╝██║██║░░██║  ██║░░██║██║░░██║██║██║░░██║
╚═════╝░╚═╝╚═╝░░╚═╝  ╚═╝░░╚═╝╚═╝░░╚═╝╚═╝╚═╝░░╚═╝""")

def exibir_opcoes():
    print('1. Cadastrar novo cliente')
    print('2. Listar clientes cadastrados')
    print('3. Consultar detalhes de um cliente')
    print('4. Sair\n')

def finalizar_app():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Finalizando o sistema do Salão de Beleza\n')
    exit()

def opcao_invalida():
    print('Opção inválida!\n')
    input('Digite uma tecla para voltar ao menu principal')

def cadastrar_cliente():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Cadastro de novos clientes\n')
    nome_cliente = input('Digite o nome do cliente que deseja cadastrar: ')
    clientes.append(nome_cliente)
    print(f'O cliente {nome_cliente} foi cadastrado com sucesso\n')
    input('Aperte qualquer tecla para voltar ao menu principal')

def listar_clientes():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Clientes cadastrados:\n')
    if clientes:
        for i, cliente in enumerate(clientes, start=1):
            print(f'{i}. {cliente}')
    else:
        print('Nenhum cliente cadastrado.')
    input('Aperte qualquer tecla para voltar ao menu principal')

def consultar_detalhes():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Consultar detalhes de um cliente\n')
    listar_clientes()
    if clientes:
        try:
            escolha = int(input('Digite o número do cliente para consultar detalhes: '))
            if 1 <= escolha <= len(clientes):
                print(f'Detalhes do cliente {clientes[escolha - 1]}\n')
            else:
                print('Número inválido.')
        except ValueError:
            print('Entrada inválida. Por favor, insira um número.')
    input('Aperte qualquer tecla para voltar ao menu principal')

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        
        if opcao_escolhida == 1:
            cadastrar_cliente()
        elif opcao_escolhida == 2:
            listar_clientes()
        elif opcao_escolhida == 3:
            consultar_detalhes()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except ValueError:
        print('Entrada inválida. Por favor, insira um número.\n')
        input('Digite uma tecla para voltar ao menu principal')

def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        exibir_nome_do_programa()
        exibir_opcoes()
        escolher_opcao()

if __name__ == '__main__':
    main()
