# SistemaBancario
Desafio DIO 01 - Sistema Bancário em Python

Especificações: Máximo de 3 saques ao dia, não depositar valor negativo, não sacar valor negativo, nem valor maior que saldo.
Segue exemplo: 

Menu:

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> d
Informe o valor do depósito: 100
Depósito: R$ 100.00 - Data: 10/06/2024 09:33:19

=> s
Informe o valor do saque: 10
Saque: R$ 10.00 - Data: 10/06/2024 09:33:26 - Saque número 1

=> s
Informe o valor do saque: 20
Saque: R$ 20.00 - Data: 10/06/2024 09:33:35 - Saque número 2

=> s 
Informe o valor do saque: 10
Saque: R$ 10.00 - Data: 10/06/2024 09:33:41 - Saque número 3

=> s
Informe o valor do saque: 30
Operação falhou! Número máximo de saques excedido.

=> e (Puxando o extrato)

================ EXTRATO ================
Depósito: R$ 100.00 - Data: 10/06/2024 09:33:19
Saque: R$ 10.00 - Data: 10/06/2024 09:33:26
Saque: R$ 20.00 - Data: 10/06/2024 09:33:35
Saque: R$ 10.00 - Data: 10/06/2024 09:33:41


Saldo: R$ 60.00
==========================================



