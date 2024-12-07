# Exercício
"""
Crie uma função chamada extrair_informacoes que recebe o nome de um arquivo de texto do 'The Project Gutenberg eBook' e retorna um dicionário com as informações contidas nas primeiras linhas do arquivo, incluindo o título da obra, o autor e a língua. O dicionário deve ter as chaves 'título', 'autor' e 'língua'. 
Não leia o arquivo inteiro para realizar a tarefa, pois o arquivo pode ser muito grande e essa informação está no início do arquivo.
"""


def extrair_informacoes(nome_arquivo):
    #'título', 'autor' e 'língua'
    with open(nome_arquivo,'r',encoding='utf-8-sig') as arquivo:
        informacoes_livro = {"titulo": "", "autor": "", "lingua": ""}
        for linha in arquivo:
            if "" not in informacoes_livro.values():
                return informacoes_livro
            
            if 'title' in linha.lower():
                informacoes_livro["titulo"] = linha[(linha.index(":")+2):-1]

            if 'author' in linha.lower():
                informacoes_livro["autor"] = linha[(linha.index(":")+2):-1]

            if 'language' in linha.lower():
                informacoes_livro["lingua"] = linha[(linha.index(":")+2):-1]
    pass


# Testando a função
def main():
    for nome_arquivo in ["dados/alice.txt", "dados/shakespeare.txt"]:
        informacoes = extrair_informacoes(nome_arquivo)
        print(informacoes)


if __name__ == "__main__":
    main()
