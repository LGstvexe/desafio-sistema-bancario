def realizar_deposito(saldo_atual, valor_deposito, extrato_atual, /):
    if valor_deposito > 0:
        saldo_atual += valor_deposito
        extrato_atual += f"Depósito: R$ {valor_deposito:.2f}\n"
        print("Operação concluída com sucesso")
        return saldo_atual, extrato_atual

    print("O valor informado é inválido. Certifique-se de depositar um valor maior que zero.")


def realizar_saque(*, saldo_atual, valor_saque, extrato_atual, limite_atual, numero_saques_atual,
                   limite_saques_permitidos):
    if numero_saques_atual >= limite_saques_permitidos:
        print("Número máximo de saques diários atingido.")
    elif valor_saque > limite_atual:
        print(f"Você possui um limite de saque de R$ {limite_atual}")
    elif valor_saque > saldo_atual:
        print("Você não possui saldo suficiente.")
    elif valor_saque <= 0:
        print("O valor informado é invalido. Certifique-se de sacar um valor maior que 0")
    else:
        saldo_atual -= valor_saque
        extrato_atual += f"Saque: R$ {valor_saque:.2f}\n"
        numero_saques_atual += 1
        print("Operação concluída com sucesso")
        return saldo_atual, extrato_atual, numero_saques_atual


def exibir_extrato(saldo_atual, /, *, extrato_atual):
    print("=============== EXTRATO ===============")
    print("Não foram realizadas movimentações." if not extrato_atual else extrato_atual)
    print(f"Saldo atual: {saldo_atual:.2f}")
    print("=======================================")


def criar_usuario(lista_usuarios):
    cpf = input("Informe o CPF do usuário: ")
    if cpf.isdigit():
        usuario = filtrar_usuario(cpf, lista_usuarios)

        if usuario:
            print("Já existe um usuário com o CPF informado.")
            return
    else:
        print("Formato inserido inválido.")
        return

    nome = input("Informe o nome: ")
    dt_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (Logradouro - Nº - Bairro - Cidade/Sigla Estado): ")

    lista_usuarios.append({"nome": nome, "dt_nascimento": dt_nascimento, "cpf": cpf, "endereco": endereco})
    print("Usuário criado com sucesso!")


def criar_conta(agencia, numero_conta, lista_usuarios):
    cpf = input("Informe o CPF do usuário: ")
    if cpf.isdigit():
        usuario = filtrar_usuario(cpf, lista_usuarios)

        if usuario:
            print("\n=== Conta criada com sucesso! ===")
            return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

        print("Usuário não encontrado, fluxo de criação de conta encerrado!")

    else:
        print("Formato inserido inválido.")


def filtrar_usuario(cpf_usuario, lista_usuarios):
    for usuario in lista_usuarios:
        if usuario.get("cpf") == cpf_usuario:
            return usuario

    return None


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            Nº Conta Corrente:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(linha)


def menu():
    menu = """
        Bem-vindo! Por favor, insira qual operação deseja realizar.

    [D] -> Depositar
    [S] -> Sacar
    [E] -> Extrato
    [NU] -> Criar um novo Usuário
    [NC] -> Criar uma nova Conta
    [LC] -> Listar contas existentes
    [Q] -> Sair
    """
    return input(menu)


def main():
    AGENCIA = "0001"
    SAQUES_DIARIOS = 3

    saldo = 0
    extrato = ""
    numero_saques = 0
    limite_saque = 500.00

    usuarios = []
    contas = []

    while True:
        try:
            match (menu().upper()):
                case "D":
                    valor = float(input("Informe o valor do depósito: \n"))
                    saldo, extrato = realizar_deposito(saldo, valor, extrato)

                case "S":
                    valor = float(input("Informe o valor do saque: \n"))

                    saldo, extrato, numero_saques = realizar_saque(saldo_atual=saldo, valor_saque=valor,
                                                                   extrato_atual=extrato,
                                                                   limite_atual=limite_saque,
                                                                   numero_saques_atual=numero_saques,
                                                                   limite_saques_permitidos=SAQUES_DIARIOS)

                case "E":
                    exibir_extrato(saldo, extrato_atual=extrato)

                case "Q":
                    print("Operações finalizadas, obrigado!")
                    break

                case "NU":
                    criar_usuario(usuarios)

                case "NC":
                    numero_conta = len(contas) + 1
                    conta = criar_conta(AGENCIA, numero_conta, usuarios)

                    if conta:
                        contas.append(conta)

                case "LC":
                    listar_contas(contas)

                case _:
                    print("Operação inválida.")
        except Exception:
            print("Falha na operação, tente novamente.")


main()




