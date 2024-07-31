import os

#inicia loop
while True:
    nome = input("Informe seu nome: ")
    peso = str(input("Informe seu peso em Kg: ")).replace(",",".")
    altura = str(input("Informe a altura em m: ")).replace(",",".")

    # converter para float
    peso = float(peso)
    altura = float(altura)
    # calcula
    imc = peso / (altura ** 2)

    os.system("cls")

    print(f"IMC de {nome}: {imc:,.2f}")

    # Diagnostico
    if imc <= 16.9:
        print(f"{nome} muito abaixo do peso.")
        print("Favor procurar um médico.")
    elif imc < 18.5:
        print(f"{nome} esta abaixo do peso.")
    elif imc < 25:
        print(f"{nome} esta no seu peso ideal.")
        print("Parabénsss")
    elif imc < 30:
        print(f"{nome} esta acima do seu peso ideal.")
    elif imc < 35:
        print(f"{nome} esta obeso.")
    elif imc < 40:
        print(f"{nome} esta com obesidade nivel II.")
    else:
        print(f"{nome} esta com obesidade morbida.")
        print("Procurar médico para cirurgia.")

    continuar = input("Deseja continuar (s/n)?").lower()
    if continuar == "s":
        continue
    else:
        break
