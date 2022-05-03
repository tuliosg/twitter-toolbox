import csv
import pandas as pd
import cleaning

##LIMPANDO DADOS
#Abre o arquivo contendo os dados coletados e gera um novo .csv após a limpeza
with open('Dados-Twitter.csv', encoding='utf-8') as arquivo:
    dados = csv.reader(arquivo, delimiter=';')

    #O novo arquivo foi organizado contendo uma classificação do tipo de tweet e o texto do tweet.
    #Isso pode ser alterado a depender do objetivo
    colunas = ["Classificacao", "Tweet"]
    linhas = []
    
    #Lê e limpa linha por linha do arquivo
    for i in dados:
        #i[3] -> posição do arquivo "Dados-Twitter.csv" (4ª coluna) onde está o texto do tweet a ser limpo
        tweet = i[3]
        tweet = cleaning.limpa_str(tweet)
        linhas.append(["classificação", tweet])
        #print(tweet)

    data_frame = pd.DataFrame(linhas, columns=colunas)

    #Gerando .csv com os arquivos limpos
    data_frame.to_csv("Dados-Twitter(limpos).csv", encoding="UTF-8")

arquivo.close()
