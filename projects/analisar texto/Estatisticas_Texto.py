def analisar_texto(texto):
    # Contar palavras
    palavras = texto.split()
    num_palavras = len(palavras)

    # Contar letras e caracteres
    num_caracteres = sum(len(palavra) for palavra in palavras)
    num_letras = sum(len(letra) for letra in texto if letra.isalpha())

    # Contar frases
    frases = texto.split('.')
    num_frases = len(frases)

    print("Estatísticas do Texto:")
    print(f"Total de palavras: {num_palavras}")
    print(f"Total de letras: {num_letras}")
    print(f"Total de caracteres: {num_caracteres}")
    print(f"Total de frases: {num_frases}")

def ler_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            return arquivo.read()
    except FileNotFoundError:
        print("Arquivo não encontrado.")
        return None

nome_do_arquivo = input("Qual é o nome do ficheiro que queres analisar?\n")
texto_do_arquivo = ler_arquivo(nome_do_arquivo)

if texto_do_arquivo:
    analisar_texto(texto_do_arquivo)