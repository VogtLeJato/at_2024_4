# Exercicio
"""
Crie um programa em Python que imprima na tela a seguinte árvore de natal:

              \ /
            -->*<--
              /o\
             /_\_\
            /_/_0_\
           /_o_\_\_\
          /_/_/_/_/o\
         /@\_\_\@\_\_\
        /_/_/O/_/_/_/_\
       /_\_\_\_\_\o\_\_\
      /_/0/_/_/_0_/_/@/_\
     /_\_\_\_\_\_\_\_\_\_\
    /_/o/_/_/@/_/_/o/_/0/_\
             [___]
    Feliz Natal !! Boas férias
"""


def imprime_arvore():
    mensagem = """\n
              \ /\n
            -->*<--\n
              /o\ \n
             /_\_\ \n
            /_/_0_\ \n
           /_o_\_\_\ \n
          /_/_/_/_/o\ \n
         /@\_\_\@\_\_\ \n
        /_/_/O/_/_/_/_\ \n
       /_\_\_\_\_\o\_\_\ \n
      /_/0/_/_/_0_/_/@/_\ \n
     /_\_\_\_\_\_\_\_\_\_\ \n
    /_/o/_/_/@/_/_/o/_/0/_\ \n
             [___] \n
    Feliz Natal !! Boas férias \n
"""
    print(mensagem)


if __name__ == "__main__":
    imprime_arvore()
