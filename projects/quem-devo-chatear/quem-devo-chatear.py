import random
import time

nomes = []

quaisnomes = input("Escreve os nomes pretendidos (separados por espaços):\nR: ")

nomes = quaisnomes.split()

if len(nomes) == 0:
    print("Você não inseriu nenhum nome!")
elif len(nomes) == 1:
    print("Só tens um nome!")
else:
    print("Quem é que eu devia chatear hoje?")
    
    escolha = random.choice(nomes)
    
    print("Hmm.")
    time.sleep(1)
    print(chr(27) + "[2J")
    print("Hmm..")
    time.sleep(1)
    print(chr(27) + "[2J")
    print("Hmm...")
    time.sleep(1)
    print(chr(27) + "[2J")
    
    print(f"Devia chatear o {escolha}!")