#!/usr/bin/env python3

def main():
    peso = float(input("Peso (kg): "))
    altura = float(input("Altura (m): "))
    imc = peso / (altura ** 2)
    print(f"\nSeu IMC é {imc:.2f}")

    if imc < 18.5:
        print("Classificação: Abaixo do peso")
    elif imc < 25:
        print("Classificação: Peso normal")
    elif imc < 30:
        print("Classificação: Sobrepeso")
    else:
        print("Classificação: Obesidade")

if __name__ == "__main__":
    main()
