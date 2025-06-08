# maca = input("Digite a quantidade de maçãs vendidas: ")
# banana = input("Digite a quantidade de bananas vendidas: ")

# if maca.isdigit() and banana.isdigit():
#     maca = int(maca)
#     banana = int(banana)

#     if maca > banana:
#         print(
#             f"A quantidade de maçãs vendidas ({maca}) é maior que a quantidade de bananas vendidas ({banana}).")
#     elif maca < banana:
#         print(
#             f"A quantidade de bananas vendidas ({banana}) é maior que a quantidade de maçãs vendidas ({maca}).")
#     else:
#         print(
#             f"A quantidade de maçãs vendidas ({maca}) é igual à quantidade de bananas vendidas ({banana}).")

# """Camila está organizando um projeto e precisa calcular o tempo total necessário para concluir três atividades: A, B e C. No entanto, se alguma atividade tiver um número de dias negativo, o código deve avisar que os valores inseridos são inválidos e não calcular o total.
# Se algum valor for negativo, mostre uma mensagem informando o erro."""
# atividade_a = input("Digite o número de dias para a atividade A: ")
# atividade_b = input("Digite o número de dias para a atividade B: ")
# atividade_c = input("Digite o número de dias para a atividade C: ")

# if atividade_a.isdigit() and atividade_b.isdigit() and atividade_c.isdigit():
#     atividade_a = int(atividade_a)
#     atividade_b = int(atividade_b)
#     atividade_c = int(atividade_c)

#     if atividade_a < 0 or atividade_b < 0 or atividade_c < 0:
#         print("Erro: Os valores inseridos são inválidos. Nenhuma atividade pode ter dias negativos.")
#     else:
#         total_dias = atividade_a + atividade_b + atividade_c
#         print(
#             f"O tempo total necessário para concluir as atividades A, B e C é de {total_dias} dias.")
# else:
#     print("Erro: Por favor, insira números válidos para o número de dias das atividades.")

# temperatura_limite = 25
# temperatura_atual = input("Digite a temperatura atual: ")
# if temperatura_atual.isdigit():
#     temperatura_atual = int(temperatura_atual)

#     if temperatura_atual > temperatura_limite:
#         print(
#             f"A temperatura atual ({temperatura_atual}°C) está acima do limite de {temperatura_limite}°C.")
#     elif temperatura_atual < temperatura_limite:
#         print(
#             f"A temperatura atual ({temperatura_atual}°C) está abaixo do limite de {temperatura_limite}°C.")
#     else:
#         print(f"A temperatura atual é exatamente {temperatura_limite}°C.")
# else:
#     print("Erro: Por favor, insira um número válido para a temperatura atual.")


def calcular_imc():
    try:
        peso = float(input("Digite seu peso atual (kg): ").replace(",", "."))
        altura = float(
            input("Digite sua altura atual (m): ").replace(",", "."))

        if peso <= 0 or altura <= 0:
            print("❌ Erro: Peso e altura devem ser valores positivos.")
            return

        imc = peso / (altura ** 2)
        print(f"\n✅ Seu IMC é: {imc:.2f}")

        # Classificação do IMC
        if imc < 18.5:
            print("🔹 Você está abaixo do peso.")
        elif imc < 25:
            print("✅ Você está com o peso normal.")
        elif imc < 30:
            print("⚠️ Você está com sobrepeso.")
        elif imc < 35:
            print("🔸 Obesidade grau I.")
        elif imc < 40:
            print("🔶 Obesidade grau II.")
        else:
            print("🔴 Obesidade grau III (mórbida).")

    except ValueError:
        print("❌ Erro: Por favor, insira valores numéricos válidos para peso e altura.")


def orcamento():
    try:
        limite_mensal = float(3000.00)
        despesas = float(
            input("Digite o valor total das suas despesas mensais: ").replace(",", "."))
        if despesas < 0:
            print("❌ Erro: O valor das despesas não pode ser negativo.")
            return
        if despesas > limite_mensal:
            print(
                f"⚠️ Atenção! Suas despesas mensais ({despesas:.2f}) ultrapassam o limite de {limite_mensal:.2f}.")
        elif despesas == limite_mensal:
            print(
                f"✅ Suas despesas mensais estão exatamente no limite de {limite_mensal:.2f}.")
        else:
            print(
                f"✅ Suas despesas mensais ({despesas:.2f}) estão dentro do limite de {limite_mensal:.2f}.")
    except ValueError:
        print(
            "❌ Erro: Por favor, insira um valor numérico válido para as despesas mensais.")


# Executa a função
calcular_imc()
orcamento()
