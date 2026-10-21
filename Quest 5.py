def verifica_notas(notas):
    aprovados = []

    for nota in notas:
        if nota >= 7:
            aprovados.append(nota)

    return aprovados


notas = []

while True:
    try:
        quant = int(input("Quantas notas serão verificadas? "))

        if quant <= 0:
            print("Digite uma quantidade maior que zero!")
            continue

        break

    except ValueError:
        print("Digite um número inteiro válido!")


for i in range(quant):
    while True:
        try:
            nota = float(input(f"Digite a {i+1}ª nota: "))

            if 0 <= nota <= 10:
                notas.append(nota)
                break
            else:
                print("A nota deve estar entre 0 e 10!")

        except ValueError:
            print("Digite apenas números!")


aprovados = verifica_notas(notas)
print(f"Notas aprovadas: {aprovados}")