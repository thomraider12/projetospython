import time

tarefas = []

def adicionar_tarefa(tarefa):
    tarefas.append(tarefa)
    print("\nTarefa adicionada com sucesso!")

def visualizar_tarefas():
    if not tarefas:
        print("\nSem tarefas na lista.")
        time.sleep(2)
    else:
        print("\nTarefas:")
        for indice, tarefa in enumerate(tarefas, start=1):
            print(f"{indice}. {tarefa}")
        time.sleep(2)

def carregar_tarefas():
    try:
        with open("tarefas.txt", "r") as file:
            return file.read().splitlines()
    except FileNotFoundError:
        return print("O ficheiro ainda não existe! Cria um ficheiro chamado 'tarefas.txt', por favor.")
    
def remover_tarefa(numero_tarefa):
    if numero_tarefa > 0 and numero_tarefa <= len(tarefas):
        tarefa_removida = tarefas.pop(numero_tarefa - 1)
        print(f"\nTarefa '{tarefa_removida}' removida com sucesso!")
    else:
        print("\nNúmero de tarefa inválido.")

# Função para salvar tarefas no arquivo
def salvar_tarefas():
    with open("tarefas.txt", "w") as file:
        for tarefa in tarefas:
            file.write(f"{tarefa}\n")

# Alteração na função principal para carregar tarefas no início
def principal():
    global tarefas
    tarefas = carregar_tarefas()

    while True:
        print("\n--- Menu da Lista de Tarefas ---")
        print("1. Adicionar Tarefa")
        print("2. Visualizar Tarefas")
        print("3. Remover Tarefa")
        print("4. Sair")

        escolha = input("\nEscolhe uma opção (1-4): ")

        if escolha == '1':
            tarefa = input("\nInsere a tarefa: ")
            adicionar_tarefa(tarefa)
        elif escolha == '2':
            visualizar_tarefas()
        elif escolha == '3':
            visualizar_tarefas()
            numero_tarefa = int(input("\nInsere o número da tarefa para remover: "))
            remover_tarefa(numero_tarefa)
        elif escolha == '4':
            salvar_tarefas()  # Salva as tarefas antes de sair do programa
            print("\nA sair do programa. Adeus!")
            break
        else:
            print("\nEscolha inválida. Por favor, insere uma opção válida.")

if __name__ == "__main__":
    principal()
