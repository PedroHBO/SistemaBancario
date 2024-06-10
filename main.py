
from datetime import datetime

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
ultimo_dia = datetime.now().day

while True:

    dia_atual = datetime.now().day

    if dia_atual != ultimo_dia:
        numero_saques = 0
        ultimo_dia = dia_atual

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f} - Data: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n"
            print(f"Depósito: R$ {valor:.2f} - Data: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n")
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f} - Data: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n"
            numero_saques += 1
            print(f"Saque: R$ {valor:.2f} - Data: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')} - Saque número {numero_saques}")

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
