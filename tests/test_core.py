# tests/test_core.py

import pytest
from todo_app.core import TaskManager

# Fixture para criar uma instância limpa do TaskManager para cada teste
@pytest.fixture
def manager():
    """Retorna uma nova instância de TaskManager."""
    return TaskManager()

# --- Testes para add_task ---

def test_add_task_success(manager):
    """Verifica se adicionar uma tarefa válida funciona."""
    task = manager.add_task("Comprar pão")
    assert task['id'] == 1
    assert task['description'] == "Comprar pão"
    assert not task['done']
    assert len(manager.list_tasks()) == 1
    assert manager.list_tasks()[0] == task

def test_add_multiple_tasks_increment_id(manager):
    """Verifica se IDs são incrementados corretamente."""
    task1 = manager.add_task("Tarefa 1")
    task2 = manager.add_task("Tarefa 2")
    assert task1['id'] == 1
    assert task2['id'] == 2
    assert len(manager.list_tasks()) == 2

def test_add_task_empty_description_raises_error(manager):
    """Verifica se adicionar tarefa com descrição vazia levanta ValueError."""
    with pytest.raises(ValueError, match="A descrição da tarefa não pode ser vazia."):
        manager.add_task("")

def test_add_task_whitespace_description_raises_error(manager):
    """Verifica se adicionar tarefa só com espaços levanta ValueError."""
    with pytest.raises(ValueError, match="A descrição da tarefa não pode ser vazia."):
        manager.add_task("   ")

def test_add_task_strips_whitespace(manager):
    """Verifica se espaços extras na descrição são removidos."""
    task = manager.add_task("  Lavar o carro   ")
    assert task['description'] == "Lavar o carro"

# --- Testes para list_tasks ---

def test_list_tasks_empty(manager):
    """Verifica se listar tarefas retorna lista vazia quando não há tarefas."""
    assert manager.list_tasks() == []
    assert manager.list_tasks(include_done=False) == []

def test_list_tasks_with_items(manager):
    """Verifica se listar tarefas retorna as tarefas adicionadas."""
    task1 = manager.add_task("Tarefa 1")
    task2 = manager.add_task("Tarefa 2")
    tasks = manager.list_tasks()
    assert len(tasks) == 2
    assert task1 in tasks
    assert task2 in tasks

def test_list_tasks_pending_only(manager):
    """Verifica se listar apenas pendentes funciona."""
    task1 = manager.add_task("Tarefa Pendente 1")
    task2 = manager.add_task("Tarefa Concluída 1")
    manager.mark_task_done(task2['id'])
    task3 = manager.add_task("Tarefa Pendente 2")

    pending_tasks = manager.list_tasks(include_done=False)
    all_tasks = manager.list_tasks(include_done=True)

    assert len(pending_tasks) == 2
    assert task1 in pending_tasks
    assert task3 in pending_tasks
    assert task2 not in pending_tasks
    assert len(all_tasks) == 3 # Verifica se a lista completa ainda tem tudo

# --- Testes para mark_task_done ---

def test_mark_task_done_success(manager):
    """Verifica se marcar tarefa como concluída funciona."""
    task = manager.add_task("Estudar Python")
    result = manager.mark_task_done(task['id'])
    assert result is True
    updated_task = manager.get_task_by_id(task['id'])
    assert updated_task is not None
    assert updated_task['done'] is True

def test_mark_task_done_invalid_id(manager):
    """Verifica se marcar tarefa com ID inexistente retorna False."""
    manager.add_task("Tarefa qualquer")
    result = manager.mark_task_done(999) # ID inválido
    assert result is False

def test_mark_task_already_done(manager):
     """Verifica se marcar uma tarefa já concluída não causa erro e retorna True."""
     task = manager.add_task("Tarefa feita")
     manager.mark_task_done(task['id']) # Marca a primeira vez
     result = manager.mark_task_done(task['id']) # Tenta marcar de novo
     assert result is True # Deve retornar sucesso
     updated_task = manager.get_task_by_id(task['id'])
     assert updated_task['done'] is True # Continua concluída

# --- Testes para remove_task ---

def test_remove_task_success(manager):
    """Verifica se remover uma tarefa existente funciona."""
    task1 = manager.add_task("Para remover")
    task2 = manager.add_task("Para manter")
    result = manager.remove_task(task1['id'])
    assert result is True
    remaining_tasks = manager.list_tasks()
    assert len(remaining_tasks) == 1
    assert remaining_tasks[0]['id'] == task2['id']
    assert manager.get_task_by_id(task1['id']) is None

def test_remove_task_invalid_id(manager):
    """Verifica se remover tarefa com ID inexistente retorna False."""
    manager.add_task("Tarefa existente")
    result = manager.remove_task(999) # ID inválido
    assert result is False
    assert len(manager.list_tasks()) == 1 # Nenhuma tarefa foi removida

# --- Testes para get_task_by_id ---

def test_get_task_by_id_success(manager):
    """Verifica se buscar tarefa por ID existente retorna a tarefa correta."""
    task_added = manager.add_task("Buscar esta tarefa")
    task_found = manager.get_task_by_id(task_added['id'])
    assert task_found is not None
    assert task_found['id'] == task_added['id']
    assert task_found['description'] == task_added['description']

def test_get_task_by_id_not_found(manager):
    """Verifica se buscar tarefa por ID inexistente retorna None."""
    manager.add_task("Alguma tarefa")
    task_found = manager.get_task_by_id(999) # ID inválido
    assert task_found is None

# --- Teste Adicional (Clear All) ---
# Embora não pedido explicitamente, é bom ter
def test_clear_all_tasks(manager):
    """Verifica se limpar todas as tarefas funciona e reseta o ID."""
    manager.add_task("Tarefa 1")
    manager.add_task("Tarefa 2")
    manager.clear_all_tasks()
    assert manager.list_tasks() == []
    # Verifica se o ID foi resetado
    new_task = manager.add_task("Nova Tarefa")
    assert new_task['id'] == 1