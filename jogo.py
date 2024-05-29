import random

def jogo_adivinhacao():
    numero_secreto = random.randint(1, 100)
    tentativa = 0 

    print("Bem-vindo ao jogo de adivinhação")
    print("Estou pensando em um número entre 1 a 100.")

    while True: 
        try:
            palpite = int(input("Digite o seu palpite:"))
            tentativa += 1

            if palpite < numero_secreto:
                print("Muito baixo!")
            elif palpite > numero_secreto:
                print("MUITO ALTO!")
            else:
                print(f"Parabéns! Você adivinhou o número em {tentativa} tentativas")
                break
        except ValueError: 
            print("Por favor digite um número válido.")

if __name__ == "__main__":
    jogo_adivinhacao()