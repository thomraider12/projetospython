from palavras import palavras
import random

def escolher_palavra():
    return random.choice(palavras).lower()  # Escolhe uma palavra aleatoriamente e a converte para minúsculas

def jogar_forca():
    palavra = escolher_palavra()
    letras_certas = []
    letras_erradas = []
    tentativas = 6

    print("Bem-vindo ao Jogo da Forca!")
    print("A palavra tem", len(palavra), "letras.")

    while True:
        palavra_atual = "".join(letra if letra in letras_certas else "_" for letra in palavra)
        print("\nPalavra:", palavra_atual)
        print("Letras Erradas:", letras_erradas)
        print("Tentativas Restantes:", tentativas)
        
        if palavra_atual == palavra:
            print("Parabéns! Você venceu! A palavra era:", palavra)
            break

        if tentativas == 0:
            print("Você perdeu! A palavra era:", palavra)
            break

        palpite = input("Digite uma letra: ").lower()

        if len(palpite) != 1 or not palpite.isalpha():
            print("Por favor, digite apenas uma letra válida.")
            continue

        if palpite in letras_certas or palpite in letras_erradas:
            print("Você já tentou essa letra. Tente outra.")
            continue

        if palpite in palavra:
            letras_certas.append(palpite)
            print("Letra correta!")
        else:
            letras_erradas.append(palpite)
            tentativas -= 1
            print("Letra errada! Você perdeu uma tentativa.")

jogar_forca()
