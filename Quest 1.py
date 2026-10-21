while True:
    try:
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))

        divisao = num1 / num2

    except ValueError:
        print("Digite apenas números!")

    except ZeroDivisionError:
        print("Não é possível realizar uma divisão por 0!")
    
    else:
        break
    
print(f"{num1}/{num2} = {divisao:.0f}")