# Exercicio
"""
Você deve criar uma função chamada salvar_notas que recebe um dicionário contendo nomes de alunos como 
 chaves e suas respectivas notas como valores (exemplo: {'João': 8.5, 'Maria': 9.0}) e o nome de um arquivo de saída (como 'notas.csv'). 
 Sua função deve criar um arquivo CSV com esses dados, formatado corretamente, onde a primeira coluna terá o nome do aluno e a segunda coluna terá a nota.

A estrutura do seu arquivo CSV deve ser a seguinte:

Nome,Nota
João,8.5
Maria,9.0

A função não deve utilizar bibliotecas externas e deve fazer uso apenas das funções built-in do Python.
"""

def salvar_notas(notas, arquivo_saida):
    arquivo = open(arquivo_saida, "w")
    for key in notas:
        arquivo.write(f"{key},{notas[key]}")
    arquivo.close()

def main():
    notas_alunos = {"João": 8.5, "Maria": 9.0, "Carlos": 7.0}
    salvar_notas(notas_alunos, "notas.csv")

if __name__ == "__main__":
    main()
