# Exercício
"""
Você deve criar uma função chamada 'listas_para_dicionario' que recebe duas listas como parâmetros: uma lista de chaves e uma lista de valores. A função deve utilizar a função zip do Python para combinar as duas listas em um dicionário. 

Por exemplo, se as listas forem:
chaves = ['nome', 'idade', 'cidade']
valores = ['Alice', 30, 'São Paulo']

Sua função deve retornar o seguinte dicionário:
{'nome': 'Alice', 'idade': 30, 'cidade': 'São Paulo'}

"""


def listas_para_dicionario(chaves, valores):
    return dict(zip(chaves, valores))

def main():
    chaves = ["nome", "idade", "cidade"]
    valores = ["Alice", 30, "São Paulo"]

    resultado = listas_para_dicionario(chaves, valores)
    print(resultado)  # Esperado: {'nome': 'Alice', 'idade': 30, 'cidade': 'São Paulo'}


if __name__ == "__main__":
    main()
