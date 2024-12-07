# Exercicio
"""
Utilizando a função da questão anterior através do "import exercicio09" ou "from exercicio09 import ler_csv" leia o arquivo dados_anac_2024.csv. Este arquivo contém dados de cancelamentos e atrasos de voos no Brasil.
Crie as funções abaixo para responder as perguntas:

a) Qual o voo que foi percentualmente mais cancelado?
b) Liste as companhias aéreas presentes no arquivo.
c) Qual o número do voo entre Fortaleza (SBFZ) e Galeão (SBGL) que mais teve atrasos maiores que 60 minutos percentualmente?
"""

from exercicio09 import ler_csv

def voo_mais_cancelado(dados : dict):
    try:
        indice_maior_cancelamento = max(range(len(dados["Percentuais_de_Cancelamentos"])), key=lambda i: dados["Percentuais_de_Cancelamentos"][i])
        n_voo_maior_cancelamento = dados["N_Voo"][indice_maior_cancelamento]
        percertual_voo_maior_cancelamento = dados["Percentuais_de_Cancelamentos"][indice_maior_cancelamento]
        return f"Número Voo: {n_voo_maior_cancelamento}", f"Percentual Cancelamento: {percertual_voo_maior_cancelamento}%"
    except Exception as e:
        print(f"Um erro ocorreu ao obter o voo mais cancelado: {e}")
        return None

def listar_companhias(dados : dict):
    try:
        vistos = set()
        lista_empresas_com_duplicatas = list(dados["Empresa_Aerea"])
        lista_empresas = list(filter(lambda x: not (x in vistos or vistos.add(x)), lista_empresas_com_duplicatas))
        string_lista_empresas = ""
        for empresa in lista_empresas: string_lista_empresas += f"{empresa},\n"
        return string_lista_empresas
    except Exception as e:
        print(f"Um erro ocorreu ao lista companhias: {e}")
        return None

def voo_mais_atrasado(dados : dict):
    try:
        indices_voos_galeao_fortaleza = [i for i in range(len(dados["Aeroporto_Origem_Designador_OACI"])) 
                                         if (dados["Aeroporto_Origem_Designador_OACI"][i] == "SBGL" and
                                            dados["Aeroporto_Destino_Designador_OACI"][i] == "SBFZ") or
                                            (dados["Aeroporto_Origem_Designador_OACI"][i] == "SBFZ" and
                                            dados["Aeroporto_Destino_Designador_OACI"][i] == "SBGL")]
        indice_mais_atrasos = max(indices_voos_galeao_fortaleza, key=lambda i: dados["Percentuais_de_Atrasos_superiores_a_30_minutos"][i])
        n_voo_mais_atrasos_fortaleza_galeao = dados["N_Voo"][indice_mais_atrasos]
        percertual_voo_mais_atrasos = dados["Percentuais_de_Atrasos_superiores_a_30_minutos"][indice_mais_atrasos]
        return f"Número Voo: {n_voo_mais_atrasos_fortaleza_galeao}", f"Percentual Atrasos: {percertual_voo_mais_atrasos}%"
    except Exception as e:
        print(f" {e}")
        return None

def main():
    #dados = ler_teste()
    dados = ler_csv("dados/dados_anac_2024.csv",";")
    novo_dicionario = {chave.replace('"','') : [item.replace('"','') for item in valores] for chave, valores in dados.items()}
    print("Voo percentualmente mais cancelado:", voo_mais_cancelado(novo_dicionario))
    print("Companhias aéreas presentes:", listar_companhias(novo_dicionario))
    print("Número do voo entre Fortaleza e Galeão com mais atrasos:", voo_mais_atrasado(novo_dicionario))


if __name__ == "__main__":
    main()
