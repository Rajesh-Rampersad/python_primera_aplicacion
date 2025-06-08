
# lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# lista_nombres = ['um', 'dois', 'três', 'quatro', 'cinco']
# lista_ano = [1983, 2025]

# # Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.
# for numero in lista_numeros:
#     print(numero)

# # Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.
# IMPARES = 0
# for numero in lista_numeros:
#     if numero % 2 != 0:
#         IMPARES += numero
# print(f"Soma dos números ímpares de 1 a 10: {IMPARES}")

# # Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.
# numero_usuario = int(input("Digite um número para ver sua tabuada: "))
# print(f"Tabuada do {numero_usuario}:")
# for i in range(1, 11):
#     print(f"{numero_usuario} x {i} = {numero_usuario * i}")

# # Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.
# SOMA_TOTAL = 0
# try:
#     for numero in lista_numeros:
#         SOMA_TOTAL += numero
#     print(f"Soma total dos números na lista: {SOMA_TOTAL}")
# except Exception as e:
#     print(f"Ocorreu um erro ao calcular a soma: {e}")

# # Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.
# try:
#     if len(lista_numeros) == 0:
#         raise ValueError(
#             "A lista está vazia, não é possível calcular a média.")
#     media = sum(lista_numeros) / len(lista_numeros)
#     print(f"Média dos valores na lista: {media}")
# except ZeroDivisionError:
#     print("Erro: Divisão por zero. A lista está vazia.")
# except ValueError as ve:
#     print(f"Erro: {ve}")


# Diccionario de info_personal
info_personal = {
    'nome': 'João',
    'idade': 30,
    'cidade': 'São Paulo',
    'profissao': 'Engenheiro',
    'hobbies': ['futebol', 'leitura', 'viagens']
}

# actualizar o dicionário
info_personal['idade'] = 31
info_personal['hobbies'].append('correr')

# adicionar uma nova chave
info_personal['email'] = 'exemplo@gmail.com'
# remover uma chave existente
if 'cidade' in info_personal:
    del info_personal['cidade']

# Crie um dicionário que relacione os números de 1 a 5 aos seus respectivos quadrados.
numeros_quadrados = {i: i**2 for i in range(1, 6)}
# Imprimir o dicionário de números e seus quadrados
print("Números e seus quadrados:")
for numero, quadrado in numeros_quadrados.items():
    print(f"{numero}: {quadrado}")

# Escreva um código que conte a frequência de cada palavra em uma frase utilizando um dicionário.
frase = "Python é uma linguagem de programação poderosa e Python é muito popular"
palavras = frase.lower().split()
frequencia_palavras = {}
for palavra in palavras:
    if palavra in frequencia_palavras:
        frequencia_palavras[palavra] += 1
    else:
        frequencia_palavras[palavra] = 1
# Imprimir a frequência de cada palavra
print("\nFrequência de palavras na frase:")
for palavra, frequencia in frequencia_palavras.items():
    print(f"{palavra}: {frequencia}")

# imprimir o dicionário atualizado
print("Informações pessoais atualizadas:")
for chave, valor in info_personal.items():
    if isinstance(valor, list):
        print(f"{chave.capitalize()}: {', '.join(valor)}")
    else:
        print(f"{chave.capitalize()}: {valor}")
