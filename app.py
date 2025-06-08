import os

# Lista para armazenar os restaurantes con  nombres reales
restaurantes_ficticio = [
    'Restaurante A',
    'Restaurante B',
    'Restaurante C',
    'Restaurante D',
    'Restaurante E',
]
# Diccionario de restaureantes con nombres ficticios, categoria y estado: ativo o inativo
restaurantes = [{
    'nome': 'Restaurante Fictício A',
    'categoria': 'Italiana',
    'estado': "Ativo"
}, {
    'nome': 'Restaurante Fictício B',
    'categoria': 'Mexicana',
    'estado': 'Inativo'
}, {
    'nome': 'Restaurante Fictício C',
    'categoria': 'Japonesa',
    'estado': 'Ativo'
}, {
    'nome': 'Restaurante Fictício D',
    'categoria': 'Chinesa',
    'estado': 'Inativo'
}, {
    'nome': 'Restaurante Fictício E',
    'categoria': 'Brasileira',
    'estado': 'Ativo'
}]


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
    categoria = input('Digite a categoria do restaurante: ')

    dados_restaurante = {
        'nome': nome_do_restaurante,
        'categoria': categoria,
        'estado': 'Inativo'
    }

    if nome_do_restaurante:
        restaurantes.append(dados_restaurante)
        print(f'Restaurante "{nome_do_restaurante}" cadastrado com sucesso!')
        voltar_ao_menu()
    else:
        print('Nome do restaurante não pode ser vazio. Tente novamente.')


def listar_restaurantes():
    os.system('cls' if os.name == 'nt' else 'clear')
    if restaurantes:
        print("Restaurantes cadastrados:")
        for i, restaurante in enumerate(restaurantes, start=1):
            estado = restaurante['estado']
            print(
                f"{i}. {restaurante['nome']} - Categoria: {restaurante['categoria']} - Estado: {estado}")

        input('Pressione Enter para voltar ao menu principal...')
        # Call the main function to return to the menu

        voltar_ao_menu()

    else:
        print("Nenhum restaurante cadastrado.")


def ativar_restaurante():
    os.system('cls' if os.name == 'nt' else 'clear')

    # Filtra restaurantes inativos
    inativos = [r for r in restaurantes if r['estado'] == 'Inativo']

    if not inativos:
        print("Todos os restaurantes já estão ativos.")
        voltar_ao_menu()
        return

    print("Restaurantes disponíveis para ativação:")
    for i, restaurante in enumerate(inativos, start=1):
        print(
            f"{i}. {restaurante['nome']} - Categoria: {restaurante['categoria']} - Estado: {restaurante['estado']}")

    try:
        escolha = int(
            input("Digite o número do restaurante que deseja ativar: "))
        if 1 <= escolha <= len(inativos):
            restaurante_escolhido = inativos[escolha - 1]
            restaurante_escolhido['estado'] = 'Ativo'
            print(
                f"Restaurante '{restaurante_escolhido['nome']}' ativado com sucesso!")
            voltar_ao_menu()
        else:
            opcao_invalida()
            voltar_ao_menu()
    except ValueError:
        print("Entrada inválida. Digite um número válido.")
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
