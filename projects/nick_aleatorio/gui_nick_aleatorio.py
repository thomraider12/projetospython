import random
import tkinter as tk

def generate_nickname():
    primeiro_nome = primeiro_nome_entry.get()
    ultimo_nome = ultimo_nome_entry.get()
    
    nome_aleatorio = random.choice(opcoes_nome_aleatorio)
    nickname = f"{primeiro_nome} '{nome_aleatorio}' {ultimo_nome}"
    
    nickname_label.config(text=nickname)

opcoes_nome_aleatorio = [
    'Ace', 'Adonis', 'Badboy', 'Bam Bam', 'Bear', 'Beast', 'Beef', 'Biggie',
    'Boner', 'Boss', 'Cowboy', 'Daddy', 'Elmo', 'Gasoline', 'Gangster',
    'Gizmo', 'Godzilla', 'Grandpa', 'Grasshopper', 'Handsome', 'Harvard',
    'Hero', 'Hercules', 'Hollywood', 'Hoss', 'Hunk', 'Jedi', 'Macho',
    'Mayhem', 'Motown', 'Monster', 'Moose', 'Muscle', 'Nemo', 'Pickle',
    'Player', 'Poker', 'Pooh', 'Pops', 'Prince', 'Pup', 'Rockstar', 'Romeo',
    'Scooter', 'Skipper', 'Sparkie', 'Superfly', 'Teddy', 'Tiger', 'Train',
    'Turtle', 'Vegas', 'Waldo', 'Winner', 'Cachorrão', 'AnaChe', 'Gironda',
    'Melissagata', 'Aquidisgraça', 'Martaonde', 'Severinnis',
    'Diegostore', 'Armigoonline', 'Catlucia', 'Tonymarrento', 'Deuonda'
]

root = tk.Tk()
root.title("Gerador de Nicknames")

primeiro_nome_label = tk.Label(root, text="Qual é o teu primeiro nome?")
primeiro_nome_label.pack()

primeiro_nome_entry = tk.Entry(root)
primeiro_nome_entry.pack()

ultimo_nome_label = tk.Label(root, text="Qual é o teu último nome?")
ultimo_nome_label.pack()

ultimo_nome_entry = tk.Entry(root)
ultimo_nome_entry.pack()

generate_button = tk.Button(root, text="Gerar Nickname", command=generate_nickname)
generate_button.pack()

nickname_label = tk.Label(root, text="")
nickname_label.pack()

root.mainloop()
