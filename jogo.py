import random

numero_secreto = random.randint(1, 100)
tentativas = 7


print("=== JOGO DE ADIVINHAÇÃO ===")
print("Tente adivinhar o número de 1 a 100!")
print("Você tem 7 tentativas.")

for tentativa in range(1, tentativas + 1):
    numero = int(input(f"\nTentativa {tentativa}: Digite um número: "))

    if numero == numero_secreto:
        print("🎉 Parabéns! Você acertou o número!")
        print(f"Você acertou na tentativa {tentativa}.")
        break

    elif numero < numero_secreto:
        print("O número secreto é MAIOR.")

    else:
        print("O número secreto é MENOR.")

else:
    print("\n😢 Suas tentativas acabaram!")
    print(f"O número secreto era: {numero_secreto}")