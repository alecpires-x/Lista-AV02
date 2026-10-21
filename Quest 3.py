def verifica_carga_horaria(carga_horaria):
    if carga_horaria >= 40:
        return "Carga horária completa."
    else:
        return "Carga horária incompleta."

while True:
    try:
        carga_horaria = int(input("Digite qual foi sua carga horária: "))
        resultado_carga_horaria = verifica_carga_horaria(carga_horaria)
    except ValueError:
        print("\nDigite apenas números.\n")
    else:
        break

print(resultado_carga_horaria)