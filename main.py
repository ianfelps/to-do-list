import os 

# Crie uma lista vazia para armazenar as tarefas
tarefas = []

# Função para adicionar uma tarefa
def adicionar_tarefa():
    tarefa = input("Digite a tarefa que deseja adicionar: ")
    tarefas.append(tarefa)
    print("Tarefa adicionada com sucesso!")

# Função para listar as tarefas
def listar_tarefas():
    if not tarefas:
        print("\nSua lista de tarefas está vazia.")
    else:
        print("\nLista de tarefas:")
        for i, tarefa in enumerate(tarefas, start=1):
            print(f"{i}. {tarefa}")

# Função para remover uma tarefa
def remover_tarefa():
    listar_tarefas()
    if tarefas:
        try:
            indice = int(input("Digite o número da tarefa que deseja remover: ")) - 1
            if 0 <= indice < len(tarefas):
                tarefa_removida = tarefas.pop(indice)
                print(f"Tarefa '{tarefa_removida}' removida com sucesso!")
            else:
                print("Número de tarefa inválido.")
        except ValueError:
            print("Por favor, insira um número válido.")
    else:
        print("Sua lista de tarefas está vazia.")

# Função para salvar tarefas em um arquivo de bloco de notas
def salvar_tarefas():
    with open('tarefas.txt', 'w') as arquivo:
        for tarefa in tarefas:
            arquivo.write(tarefa + '\n')
    print("Tarefas salvas com sucesso!")

# Função para carregar tarefas de um arquivo de bloco de notas
def carregar_tarefas():
    try:
        with open('tarefas.txt', 'r') as arquivo:
            for linha in arquivo:
                tarefa = linha.strip()
                tarefas.append(tarefa)
        print("Tarefas carregadas com sucesso!\n")
    except FileNotFoundError:
        print("Arquivo de tarefas não encontrado. Criando um novo arquivo.\n")

# Carregando as tarefas do arquivo, se existir
carregar_tarefas()

# Loop principal
while True:
    os.system('cls')
    listar_tarefas()
    print("\nEscolha uma opção:")
    print("1. Adicionar tarefa")
    print("2. Remover tarefa")
    print("3. Salvar e sair")
    
    escolha = input("Digite o número da opção desejada: ")
    
    if escolha == "1":
        adicionar_tarefa()
    elif escolha == "2":
        remover_tarefa()
    elif escolha == "3":
        salvar_tarefas()
        print("Saindo do programa.")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")