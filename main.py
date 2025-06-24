menu = """
    Bem-vindo! Por favor, insira qual operação deseja realizar.
    
(D) -> Depositar
(S) -> Sacar
(E) -> Extrato
(Q) -> Sair

"""

operacao = True
saldo = 0
extrato = ""
numero_saques = 0
limite_saque = 500.00
SAQUES_DIARIOS = 3

while operacao:
    try:
        match (input(menu).upper()):
            case "D":
                    valor_deposito = float(input("Informe o valor do depósito: \n"))
                    if valor_deposito > 0:
                        saldo += valor_deposito
                        extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
                        print(f"A operação de depósito foi realizada com sucesso.")
                    else:
                        print("Falha na operação. Valor informado é inválido.")

            case "S":
                valor_saque = float(input("Informe o valor do saque: \n"))

                saldo_insuficiente = valor_saque > saldo
                limite_excedido = valor_saque > limite_saque
                saques_excedidos = numero_saques >= SAQUES_DIARIOS

                if saques_excedidos:
                    print("Falha na operação. Número máximo de saques diários atingido.")

                elif limite_excedido:
                    print(f"Falha na operação. Você possui um limite de saque de R$ {limite_saque}")

                elif saldo_insuficiente:
                    print("Falha na operação. Você não possui saldo suificiente")

                elif valor_saque > 0:
                    saldo -= valor_saque
                    extrato += f"Saque: R$ {valor_saque:.2f}\n"
                    numero_saques += 1
                    print("A operação de saque foi realizada com sucesso.")

                else:
                    print("Falha na operação. Valor informado é inválido.")

            case "E":
                print("=============== EXTRATO ===============")
                print("Não foram realizadas movimentações." if not extrato else extrato)
                print(f"Saldo atual: {saldo:.2f}")
                print("=======================================")

            case "Q":
                print("Operações finalizadas, obrigado!")
                operacao = False

            case _:
                print("Operação inválida.")
    except Exception:
        print("Valor de depósito informado é inválido.")





