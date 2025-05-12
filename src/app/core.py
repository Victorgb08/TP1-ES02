# src/todo_app/core.py

class TaskManager:
    """Gerencia uma lista de tarefas."""

    def __init__(self):
        """Inicializa com uma lista de tarefas vazia."""
        self._tasks = [] # Formato: {'id': int, 'description': str, 'done': bool}
        self._next_id = 1

    def add_task(self, description: str) -> dict:
        """Adiciona uma nova tarefa à lista.

        Args:
            description: A descrição da tarefa.

        Returns:
            Um dicionário representando a tarefa adicionada.

        Raises:
            ValueError: Se a descrição estiver vazia ou for apenas espaços.
        """
        if not description or description.isspace():
            raise ValueError("A descrição da tarefa não pode ser vazia.")

        task = {
            'id': self._next_id,
            'description': description.strip(), # Remove espaços extras
            'done': False
        }
        self._tasks.append(task)
        self._next_id += 1
        return task

    def list_tasks(self, include_done: bool = True) -> list[dict]:
        """Retorna a lista de tarefas.

        Args:
            include_done: Se True, inclui tarefas concluídas. Se False,
                          retorna apenas tarefas pendentes.

        Returns:
            Uma lista de dicionários, onde cada dicionário é uma tarefa.
        """
        if include_done:
            return self._tasks[:] # Retorna uma cópia
        else:
            return [task for task in self._tasks if not task['done']]

    def mark_task_done(self, task_id: int) -> bool:
        """Marca uma tarefa como concluída pelo seu ID.

        Args:
            task_id: O ID da tarefa a ser marcada como concluída.

        Returns:
            True se a tarefa foi encontrada e marcada, False caso contrário.
        """
        for task in self._tasks:
            if task['id'] == task_id:
                if task['done']:
                    return True # Já estava concluída, considera sucesso
                task['done'] = True
                return True
        return False # Tarefa não encontrada

    def remove_task(self, task_id: int) -> bool:
        """Remove uma tarefa pelo seu ID.

        Args:
            task_id: O ID da tarefa a ser removida.

        Returns:
            True se a tarefa foi encontrada e removida, False caso contrário.
        """
        initial_len = len(self._tasks)
        self._tasks = [task for task in self._tasks if task['id'] != task_id]
        return len(self._tasks) < initial_len

    def get_task_by_id(self, task_id: int) -> dict | None:
         """Busca uma tarefa pelo seu ID.

         Args:
             task_id: O ID da tarefa.

         Returns:
             O dicionário da tarefa se encontrada, None caso contrário.
         """
         for task in self._tasks:
             if task['id'] == task_id:
                 return task
         return None

    def clear_all_tasks(self):
        """Remove todas as tarefas."""
        self._tasks = []
        self._next_id = 1 # Reseta o contador de ID