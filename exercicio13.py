# Exercicio
"""
Você recebeu um arquivo de texto chamado 'entrada13.txt' que contém várias linhas. Seu objetivo é criar um programa que 
remova todas as linhas duplicadas desse arquivo e escreva cada linha única em um novo arquivo chamado 'saida.txt'. 
Siga as instruções abaixo:

1. Leia o conteúdo do arquivo 'entrada.txt'.
2. Remova as linhas duplicadas.
3. Escreva as linhas únicas no arquivo 'saida.txt'.

Certifique-se de que o arquivo 'saida.txt' seja criado e que cada linha única apareça apenas uma vez.
"""

def retorna_lista_sem_repeticoes(linhas_repetidas : list):
    linhas_sem_repeticao = []
    linhas_repetidas = [x.strip() for x in linhas_repetidas]
    [linhas_sem_repeticao.append(x) for x in linhas_repetidas if x not in linhas_sem_repeticao]
    return linhas_sem_repeticao


def remover_linhas_duplicadas(entrada, saida):
    linhas_sem_repeticao = []

    with open(entrada, 'r', encoding="utf-8-sig") as arquivo:
        linhas_repetidas = list(arquivo.readlines())
        linhas_sem_repeticao = retorna_lista_sem_repeticoes(linhas_repetidas)
    
    with open(saida, 'w') as arquivo:
        arquivo.write(str(linhas_sem_repeticao))


def main():
    # Chame a função com os nomes dos arquivos
    remover_linhas_duplicadas("dados/entrada13.txt", "saida_duplicadas.txt")


if __name__ == "__main__":
    main()
