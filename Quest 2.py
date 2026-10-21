def media_notas(notas):
    somanotas = 0

    for i in notas:
        somanotas += i

    media = somanotas / len(notas)
    return media


notas = []

for i in range(3):
    while True:
        try:
            nota = float(input(f"Digite a {i+1}ª nota: "))

            if 0 <= nota <= 10:
                notas.append(nota)
                break
            else:
                print("Digite uma nota válida de 0 a 10!")

        except ValueError:
            print("Digite apenas números!")


resultado_media = media_notas(notas)
print(f"{resultado_media:.2f}")