# src/main.py

from app.core import TaskManager

def print_tasks(tasks: list[dict]):
    """Imprime a lista de tarefas formatada."""
    if not tasks:
        print("\nNenhuma tarefa encontrada.")
        return

    print("\n--- Tarefas ---")
    for task in tasks:
        status = "[x]" if task['done'] else "[ ]"
        print(f"{task['id']}: {status} {task['description']}")
    print("---------------")

def main():
    """Função principal da aplicação CLI."""
    manager = TaskManager()
    print("Bem-vindo ao Gerenciador de Tarefas CLI!")

    while True:
        print("\nOpções:")
        print("1. Adicionar Tarefa")
        print("2. Listar Tarefas (Todas)")
        print("3. Listar Tarefas (Pendentes)")
        print("4. Marcar Tarefa como Concluída")
        print("5. Remover Tarefa")
        print("6. Sair")

        choice = input("Escolha uma opção: ")

        try:
            if choice == '1':
                desc = input("Digite a descrição da nova tarefa: ")
                try:
                    added_task = manager.add_task(desc)
                    print(f"Tarefa '{added_task['description']}' adicionada com ID {added_task['id']}.")
                except ValueError as e:
                    print(f"Erro: {e}")
            elif choice == '2':
                print_tasks(manager.list_tasks(include_done=True))
            elif choice == '3':
                 print_tasks(manager.list_tasks(include_done=False))
            elif choice == '4':
                try:
                    task_id_str = input("Digite o ID da tarefa a marcar como concluída: ")
                    task_id = int(task_id_str)
                    if manager.mark_task_done(task_id):
                        print(f"Tarefa {task_id} marcada como concluída.")
                    else:
                        print(f"Erro: Tarefa com ID {task_id} não encontrada.")
                except ValueError:
                     print("Erro: ID inválido. Por favor, insira um número.")
            elif choice == '5':
                try:
                    task_id_str = input("Digite o ID da tarefa a remover: ")
                    task_id = int(task_id_str)
                    if manager.remove_task(task_id):
                        print(f"Tarefa {task_id} removida.")
                    else:
                        print(f"Erro: Tarefa com ID {task_id} não encontrada.")
                except ValueError:
                     print("Erro: ID inválido. Por favor, insira um número.")
            elif choice == '6':
                print("Saindo...")
                break
            else:
                print("Opção inválida. Tente novamente.")
        except Exception as e:
            # Captura genérica para erros inesperados
            print(f"\nOcorreu um erro inesperado: {e}")


if __name__ == "__main__":
    main()