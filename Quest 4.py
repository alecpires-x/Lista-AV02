saldo_atual = 1000.0

def calcular_saldo(saldo, valor, operacao):
    
    if valor <= 0:
        print("\nO valor deve ser maior que zero!\n")
        return saldo
    
    match operacao:
        case "deposito":
            novo_saldo = saldo+valor
        case "saque":
            if valor>saldo:
                print("\nSaldo insuficiente.\n")
                return saldo
            novo_saldo = saldo-valor
    print("\nOperação realizada com sucesso.")
    print(f"Saldo atual: R${novo_saldo:.2f}\n")
    return novo_saldo

print("Seja bem_vindo!\n")
while True:
    print("1- Depósito\n2- Saque\n3- Sair")
    try:
        opc=int(input("Digite uma das opções: "))
            
    except ValueError:
        print("\nDigite apenas números!\n")
        continue
    
    match opc:
        case 1:
            operacao="deposito"
        case 2:
            operacao="saque"
        case 3:
            break
        case _:
                print("\nOpção inválida.\n")
                continue
    try:
        valor=float(input("Digite o valor da operação: "))
    except ValueError:
        print("\nDigite apenas números!\n")
        continue
        
        saldo_atual=calcular_saldo(saldo_atual, valor, operacao)