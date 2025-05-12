# Projeto To-Do List CLI com Testes e CI/CD

Este repositório contém uma aplicação simples de linha de comando (CLI) para gerenciar uma lista de tarefas (To-Do List). O objetivo principal é demonstrar como os testes unitários e a Integração Contínua/Entrega Contínua (CI/CD) com GitHub Actions auxiliam na manutenção e qualidade do software.

## 1. Membros do Grupo

* [Seu Nome Completo Aqui]
* [Nome Completo do Membro 2 (se aplicável)]
* ...

## 2. Explicação do Sistema

A aplicação permite ao usuário:

* Adicionar novas tarefas com uma descrição.
* Listar todas as tarefas cadastradas, indicando seu status (pendente ou concluída).
* Listar apenas as tarefas pendentes.
* Marcar uma tarefa existente como concluída, usando seu ID.
* Remover uma tarefa da lista, usando seu ID.

A aplicação é executada diretamente no terminal e gerencia as tarefas em memória (elas são perdidas quando a aplicação fecha). A interação é feita através de um menu de opções numéricas.

## 3. Tecnologias Utilizadas

* **Linguagem:** Python 3.9+
* **Testes:** Pytest (framework de testes para Python)
* **CI/CD:** GitHub Actions (para execução automática dos testes em diferentes sistemas operacionais a cada commit)
* **Gerenciamento de Pacotes:** Pip e `requirements.txt`
* **Controle de Versão:** Git
* **Hospedagem do Repositório:** GitHub