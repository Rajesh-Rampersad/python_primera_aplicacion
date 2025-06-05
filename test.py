# Exercícios
# 1 - Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else para determinar se o número é par ou ímpar.

def verificar_par_impar():
    try:
        numero = int(input("Digite um número: "))
        if numero % 2 == 0:
            print(f"O número {numero} é par.")
        else:
            print(f"O número {numero} é ímpar.")
    except ValueError:
        print("Entrada inválida. Por favor, insira um número inteiro.")


# 2 - Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para classificar a idade em categorias de acordo com as seguintes condições:

# Criança: 0 a 12 anos;
# Adolescente: 13 a 18 anos;
# Adulto: acima de 18 anos.

def classificar_idade():
    try:
        idade = int(input("Digite sua idade: "))
        if 0 <= idade <= 12:
            print("Você é uma criança.")
        elif 13 <= idade <= 18:
            print("Você é um adolescente.")
        elif idade > 18:
            print("Você é um adulto.")
        else:
            print("Idade inválida. Por favor, insira uma idade não negativa.")
    except ValueError:
        print("Entrada inválida. Por favor, insira um número inteiro para a idade.")


# 3 - Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você.

def verificar_usuario_senha():
    usuario_correto = "admin"
    senha_correta = "12345"

    usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")

    if usuario == usuario_correto and senha == senha_correta:
        print("Acesso concedido.")
    else:
        print("Usuário ou senha incorretos.")


# 4 - Solicite ao usuário as coordenadas (x, y) de um ponto qualquer e utilize uma estrutura if elif else para determinar em qual quadrante do plano cartesiano o ponto se encontra de acordo com as seguintes condições:

# Primeiro Quadrante: os valores de x e y devem ser maiores que zero;
# Segundo Quadrante: o valor de x é menor que zero e o valor de y é maior que zero;
# Terceiro Quadrante: os valores de x e y devem ser menores que zero;
# Quarto Quadrante: o valor de x é maior que zero e o valor de y é menor que zero;
# Caso contrário: o ponto está localizado no eixo ou origem.

def verificar_quadrante():
    try:
        x = float(input("Digite a coordenada x: "))
        y = float(input("Digite a coordenada y: "))

        if x > 0 and y > 0:
            print("O ponto está no Primeiro Quadrante.")
        elif x < 0 and y > 0:
            print("O ponto está no Segundo Quadrante.")
        elif x < 0 and y < 0:
            print("O ponto está no Terceiro Quadrante.")
        elif x > 0 and y < 0:
            print("O ponto está no Quarto Quadrante.")
        else:
            print("O ponto está localizado no eixo ou na origem.")
    except ValueError:
        print("Entrada inválida. Por favor, insira números válidos para as coordenadas.")


def main():
    verificar_par_impar()
    classificar_idade()
    verificar_usuario_senha()
    verificar_quadrante()


if __name__ == "__main__":
    main()
