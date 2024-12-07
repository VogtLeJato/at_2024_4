# Exercício
"""
Você deve implementar uma leitura de um arquivo JSON chamado 'dados_ibge_ipca.json'. Este arquivo contém dados sobre o IPCA acumulado. Siga os passos abaixo:

1. Utilize o pacote json para carregar os dados desse arquivo.
2. Filtre os dados onde a chave 'D2C' é igual a 2265, que representa dados do IPCA acumulado para 12 meses.
3. O valor percentual do IPCA acumulado para 12 meses está na chave 'V'.
4. Crie uma função chamada get_maior_ipca que retorna o mês e o ano que tiveram o maior valor de IPCA acumulado para 12 meses.
5. Crie outra função chamada get_menor_ipca que retorna o mês e o ano que tiveram o menor valor de IPCA acumulado para 12 meses.

Certifique-se de que suas funções retornam os valores no formato "Mês/Ano" (por exemplo, "Janeiro/2023").
"""

import json

def get_maior_ipca(dados):
    ipca_12_meses = [dado for dado in dados if dado["D2C"] == "2265"]
    maior_dado = max(ipca_12_meses, key=lambda x: x["V"])
    return maior_dado["D3N"]


def get_menor_ipca(dados):
    ipca_12_meses = [dado for dado in dados if dado.get("D2C") == "2265"]
    menor_dado = min(ipca_12_meses, key=lambda x: x["V"])
    return menor_dado["D3N"]


def main():
    with open("dados/dados_ibge_ipca.json", "r", encoding="utf-8-sig") as file:
        dados = json.load(file)
        maior = get_maior_ipca(dados)
        menor = get_menor_ipca(dados)
        print(f"Maior IPCA acumulado para 12 meses: {maior}")
        print(f"Menor IPCA acumulado para 12 meses: {menor}")


if __name__ == "__main__":
    main()
