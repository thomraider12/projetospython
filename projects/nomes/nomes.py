print("Qual é o teu nome?")
nome_pessoa = input()

if nome_pessoa == 'Tomás':
    print("Oh meu dono, como estás?")
elif nome_pessoa == "Sandra":
    print("Olá mãe do programador!")
elif nome_pessoa == "Miguel":
    print("Olá pai do programador!")
elif nome_pessoa == "Carmo":
    print("Olá avó do programador!")
elif nome_pessoa == "Joaquim":
    print("Olá avô do programador!")
else:
    print(f"Olá, {nome_pessoa}! Como estás hoje? Adeus.")

input("Carrega no ENTER para sair...")