# Exercício
"""
O código abaixo apresenta um problema relacionado ao tratamento de exceções em Python. Analise o seguinte código e responda à pergunta:

"""


def main():
    # Uma função genérica qualquer
    pass


if __name__ == "__main__":
    try:
        main()
    except:
        print("O código não funcionou corretamente")


""""
Por que esse código pode ser considerado uma má prática quando se trata de tratamento de exceções? Que problemas podem surgir ao utilizar um bloco `except` sem especificar o tipo de exceção?
"""

# Resposta:
"""
Quando ocorrer um exceção, não será retornada uma informação relevante de onde está o problema, esta perte do código terá de ser refatorada, para auxiliar na investigação do problema. 
"""
