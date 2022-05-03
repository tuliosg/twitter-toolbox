import csv
import pandas as pd
import cleaning

##LIMPANDO DADOS
#Abre o arquivo e gera um novo .csv com os dados limpos
with open('Dados-Fanfic_(romance)(CSV).csv', encoding='utf-8') as arquivo:
    dados = csv.reader(arquivo, delimiter=';')

    colunas = ["Classificacao", "Tweet"]
    linhas = []

    for i in dados:
        tweet = i[3]
        tweet = cleaning.limpa_str(tweet)
        linhas.append(["Romance", tweet])
        #print(tweet)

    data_frame = pd.DataFrame(linhas, columns=colunas)

    data_frame.to_csv("Dados-Fanfic(romance).csv", encoding="UTF-8")

arquivo.close()
