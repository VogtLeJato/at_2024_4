# Exercicio
"""
Você está trabalhando em um sistema que gerencia listas de compras de usuários. Abaixo estão duas listas: 
uma contém os itens que um usuário já possui e a outra contém os itens que ele deseja comprar. 

Seu objetivo é encontrar quais itens estão na lista de desejos, mas não na lista de posses (ou seja, os itens que ele ainda não possui). 

Complete a função itens_faltantes que deve retornar a diferença entre os dois conjuntos (sets):
1. items_possuidos: uma lista com os itens que o usuário já possui.
2. items_desejados: uma lista com os itens que o usuário deseja comprar.

Dica: Utilize a operação de diferença entre sets do Python.
"""


def itens_faltantes(items_possuidos, items_desejados):
    diferentes = []
    for desejado in items_desejados:
        if desejado not in items_possuidos:
            diferentes.append(desejado)
    return diferentes

# Versão de teste
def main():
    possuidos = {"maçã", "banana", "laranja"}
    desejados = {"banana", "uva", "melancia", "maçã"}

    faltando = itens_faltantes(possuidos, desejados)
    print(f"Itens faltando na lista de compras: {faltando}")


if __name__ == "__main__":
    main()
