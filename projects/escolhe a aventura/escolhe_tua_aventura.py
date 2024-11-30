def perdeu_jogo():
    resposta = input("\nTu perdeste! Queres recomeçar o jogo? (sim/não): ").lower()
    if resposta == "sim":
        jogo()
    elif resposta == "não":
        print("\nAté a próxima! Adeus.")
    else:
        print("\nOpção inválida! Por favor, responde 'sim' ou 'não'.")
        perdeu_jogo()

def jogo():
    nome = input("Escreve o teu nome: ")
    print(f"\nBem-vindo, {nome}, a esta aventura!")

    resposta = input("\nEstás numa estrada de terra e chegaste ao fim dela. Podes ir para a esquerda ou para a direita. Qual caminho escolhes? ").lower()

    if resposta == "esquerda":
        resposta = input("\nChegaste a um rio. Queres nadar por ele ou dar a volta? (responde 'nadar' ou 'dar a volta'): ")

        if resposta == "nadar":
            print("\nComeças a nadar e um crocodilo apanha-te. Tu perdeste!")
            perdeu_jogo()
        elif resposta == "dar a volta":
            print("\nDás a volta no rio, mas andaste por muitos quilómetros e ficaste sem água. Tu perdeste!")
            perdeu_jogo()
        else:
            print("\nOpção inválida! Tu perdeste!")
            perdeu_jogo()

    elif resposta == "direita":
        resposta = input("\nChegaste a uma ponte que parece prestes a cair. Queres passar por ela ou voltar? (responde 'passar' ou 'voltar'): ")

        if resposta == "passar":
            resposta = input("\nTu passas pela ponte e encontras uma pessoa. Queres falar com ela? (sim/não): ")

            if resposta == "sim":
                print("\nTu falas com a pessoa e ela dá-te ouro! Parabéns, tu ganhaste o jogo!")
            elif resposta == "não":
                print("\nTu ignoras a pessoa e ela fica ofendida. Tu perdeste!")
                perdeu_jogo()
            else:
                print("\nOpção inválida! Tu perdeste!")
                perdeu_jogo()

        elif resposta == "voltar":
            print("\nTu voltas para trás e perdeste!")
            perdeu_jogo()
        else:
            print("\nOpção inválida! Tu perdeste!")
            perdeu_jogo()

    else:
        print("\nOpção inválida! Tu perdeste!")
        perdeu_jogo()

    print(f"\nObrigado por jogares, {nome}!")

jogo()
