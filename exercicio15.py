# Exercicio
"""
Crie uma função chamada adicionar_tarefa que deve receber um nome de arquivo e uma string que representa uma tarefa a ser realizada (uma 'todo-list'). 
Caso o arquivo não exista, crie o arquivo com esse nome. Caso exista, adicione a tarefa no final do arquivo.
"""

import os

def adicionar_tarefa(nome_arquivo, tarefa):
    if os.path.exists(nome_arquivo):
        with open(nome_arquivo, 'a') as arquivo:
            arquivo.write(f"\n{tarefa}")
    else:
        with open(nome_arquivo, 'w') as arquivo:
            arquivo.write(tarefa)

def main():
    # Exemplo de uso
    nome_arquivo = "todo_list.txt"
    tarefa = "Comprar leite"
    adicionar_tarefa(nome_arquivo, tarefa)

    tarefa = "Fazer exercícios"
    adicionar_tarefa(nome_arquivo, tarefa)


if __name__ == "__main__":
    main()
