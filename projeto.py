#Desafio: Análise de Vendas de Produtos Objetivo: 
# Dado um arquivo CSV contendo dados de vendas de produtos, o desafio consiste em ler os dados, 
# processá-los em um dicionário para análise e, por fim, 
# calcular e reportar as vendas totais por categoria de produto.

import csv
from pathlib import Path
caminho_csv: Path = Path("vendas.csv")


def ler_csv(entrada_caminho: Path) -> list[dict]:
    with open(entrada_caminho, newline = '', encoding = "utf-8") as csvfile:
        lista = list()
        dicionario = dict()
        reader = list(csv.reader(csvfile, delimiter = ","))
        for i in range(1,len(reader)):
            dicionario[reader[0][0]] = reader[i][0]
            dicionario[reader[0][1]] = reader[i][1]
            dicionario[reader[0][2]] = reader[i][2]
            dicionario[reader[0][3]] = reader[i][3]
            lista.append(dicionario.copy())
        return lista

lista_saida = ler_csv(caminho_csv)
total_vendas = {}

for j in range(0, len(lista_saida)):
    if lista_saida[j]['Categoria'] not in total_vendas.keys():
        total_vendas[lista_saida[j]['Categoria']] = int(lista_saida[j]['Quantidade']) * int(lista_saida[j]['Venda'])
    else:
        total_vendas[lista_saida[j]['Categoria']] = total_vendas[lista_saida[j]['Categoria']] + int(lista_saida[j]['Quantidade']) * int(lista[j]['Venda'])

print(total_vendas) 
