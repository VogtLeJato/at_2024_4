# Exercicio
"""
Você foi encarregado de escrever uma função chamada escrever_arquivo que deve receber o nome de um arquivo e uma informação, que pode ser um número ou uma string. A função deve calcular o que deve ser escrito no arquivo. 

Os requisitos são:
1) Se a informação recebida for um número, a função deve escrever no arquivo o quadrado desse número.
2) Se a informação for uma string, a função deve escrever no arquivo essa string com todas as letras em maiúsculo.

Implemente a função e em seguida, escreva um bloco de código para testar a função. O arquivo deve ser criado no mesmo diretório que o seu script. 

# Exemplo de uso:
Para usar a função você pode fazer algo como:
escrever_arquivo('resultado.txt', 5)   # Isso deve escrever 25 no arquivo
escrever_arquivo('resultado.txt', 'teste') # Isso deve escrever TESTE no arquivo
"""
def retorna_informacao_gravar(informacao):
    if type(informacao) == str:
        return str(informacao.lower())
    if type(informacao) == int or type(informacao) == float:
        return str(informacao * informacao)
    return None

def escrever_arquivo(nome_arquivo, informacao):
    try:
        informacao_gravar = retorna_informacao_gravar(informacao)
        with open(nome_arquivo, 'w') as arquivo:
            arquivo.write(informacao_gravar)
    except Exception as e:
        print(f"Ocorreu um erro ao escrever, no arquivo, a informação passada {e}")
        return


def main():
    # Testes
    escrever_arquivo("resultado1.txt", 5)  # Deve escrever 25
    escrever_arquivo("resultado2.txt", "teste")  # Deve escrever TESTE


if __name__ == "__main__":
    main()
