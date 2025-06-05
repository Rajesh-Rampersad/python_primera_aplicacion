import os

# Lista para armazenar os restaurantes con  nombres reales
restaurantes = [
    'Restaurante A',
    'Restaurante B',
    'Restaurante C',
    'Restaurante D',
    'Restaurante E',
]


def nome_restaurante():
    print(""""

    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░\n
    """)

# menu


def menu():
    print('1, Cadastrar restaurante')
    print('2, Listar restaurantes')
    print('3, Ativar restaurante')
    print('4, Sair\n')


def finalizar():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Obrigado por usar o sistema de restaurantes!')
    exit()


def opcao_invalida():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Opção inválida. Por favor, escolha uma opção válida.')


def voltar_ao_menu():
    input('Pressione Enter para continuar...')
    main()


def cadastrar_novo_restaurante():
    os.system('cls' if os.name == 'nt' else 'clear')
    nome_do_restaurante = input('Digite o nome do restaurante: ')
    if nome_do_restaurante:
        restaurantes.append(nome_do_restaurante)
        print(f'Restaurante "{nome_do_restaurante}" cadastrado com sucesso!')
        voltar_ao_menu()
    else:
        print('Nome do restaurante não pode ser vazio. Tente novamente.')


def listar_restaurantes():
    os.system('cls' if os.name == 'nt' else 'clear')
    if restaurantes:
        print("Restaurantes cadastrados:")
        for i, restaurante in enumerate(restaurantes, start=1):
            print(f"{i}. {restaurante}")

        voltar_ao_menu()

    else:
        print("Nenhum restaurante cadastrado.")


def ativar_restaurante():
    os.system('cls' if os.name == 'nt' else 'clear')
    if restaurantes:
        print("Restaurantes disponíveis para ativação:")
        for i, restaurante in enumerate(restaurantes, start=1):
            print(f"{i}. {restaurante}")
        escolha = input('Digite o número do restaurante que deseja ativar: ')
        try:
            escolha = int(escolha)
            if 1 <= escolha <= len(restaurantes):
                print(
                    f'Restaurante "{restaurantes[escolha - 1]}" ativado com sucesso!')
            else:
                opcao_invalida()
        except ValueError:
            print('Entrada inválida. Por favor, digite um número.')
    else:
        print("Nenhum restaurante cadastrado.")
        voltar_ao_menu()


def escolha_opcao():
    opcao_escolhida = input('Escolha uma opção: ')
    # variable converting to int
    try:
        opcao_escolhida = int(opcao_escolhida)
    except ValueError:
        print("Opção inválida. Por favor, escolha um número entre 1 e 4.")

    # menu options:
    if opcao_escolhida == 1:
        cadastrar_novo_restaurante()
    elif opcao_escolhida == 2:
        listar_restaurantes()
    elif opcao_escolhida == 3:
        ativar_restaurante()

    elif opcao_escolhida == 4:
        finalizar()


def main():
    nome_restaurante()
    menu()
    escolha_opcao()


if __name__ == "__main__":
    main()
