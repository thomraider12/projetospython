import random

print("\nAlô alô! Bem-vindo ao Gerador de Nicknames! (Criado por Tomás Afonso)")
print("Nesta aplicação, vais escrever o teu primeiro Nome, e último nome")
print("e depois, esta app, vai te escolher um nickname para ti!")
print("No fim, vais ver o teu nome desta forma:\n")
print("primeiro_nome 'nome_aleatório' ultimo_nome")

primeiro_nome = input('Qual é o teu primeiro nome?\n')
ultimo_nome = input('Qual é o teu último nome?\n')

# Use uma lista para conter as opções de nome aleatório
opcoes_nome_aleatorio = ['Ace', 'Adonis', 'Badboy', 'Bam Bam', 'Bear', 'Beast', 'Beef', 'Biggie',
    'Boner', 'Boss', 'Cowboy', 'Daddy', 'Elmo', 'Gasoline', 'Gangster',
    'Gizmo', 'Godzilla', 'Grandpa', 'Grasshopper', 'Handsome', 'Harvard',
    'Hero', 'Hercules', 'Hollywood', 'Hoss', 'Hunk', 'Jedi', 'Macho',
    'Mayhem', 'Motown', 'Monster', 'Moose', 'Muscle', 'Nemo', 'Pickle',
    'Player', 'Poker', 'Pooh', 'Pops', 'Prince', 'Pup', 'Rockstar', 'Romeo',
    'Scooter', 'Skipper', 'Sparkie', 'Superfly', 'Teddy', 'Tiger', 'Train',
    'Turtle', 'Vegas', 'Waldo', 'Winner', 'Cachorrão', 'Gustavo da 12',
    'AnaChe', 'Gironda', 'Melissagata', 'Aquidisgraça', 'Martaonde', 'Severinnis',
    'Diegostore', 'Armigoonline', 'Catlucia', 'Tonymarrento', 'Deuonda', 'Metira']

# Escolha aleatoriamente um dos itens da lista para o nome aleatório
nome_aleatorio = random.choice(opcoes_nome_aleatorio)

# Combine os nomes e o nome aleatório para criar o nickname
nickname = f"{primeiro_nome} '{nome_aleatorio}' {ultimo_nome}"

print("\nAqui está o teu nickname gerado:")
print(nickname)
