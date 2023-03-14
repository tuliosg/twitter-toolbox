import nltk
import nltk.corpus
from nltk.collocations import *
import cleaning
import csv

#Abre o arquivo a ser lido
with open('Nome_arquivo.csv', encoding='utf-8') as arquivo:
    dados = csv.reader(arquivo, delimiter=',')

    #Variável onde o texto será adicionado
    texto = ""

    #Stop list
    stop_words = cleaning.stoplist

    #Busca apenas os tweets dentro do arquivo e armazena
    #O arquivo contém as colunas: numeração, classificação, texto
    for i in dados:
        tweet = i[3]
        tweet = cleaning.limpa_str(tweet)
        tweet = ' '.join([word for word in tweet.split(' ') if word not in stop_words])
        texto += tweet
        #print(tweet)
        
    tokens = nltk.word_tokenize(texto)

    #Criação dos bigramas
    bigramas = nltk.bigrams(tokens)

    #Calcula a distribuição de frequência dos bigramas
    fdist = nltk.FreqDist(bigramas)
    
    #Ordena os bigramas que mais aparecem
    bigramas_comuns = fdist.most_common(100)
    
    #Mostra os X bigramas mais comuns em ordem decrescente
    #print(bigramas_comuns)

    #Filtro de consulta
    filtro = ['fanfic', 'fic', 'fanficando', 'fanficar', 'fanfiqueiro', 'fanfiqueira']

    #Exibe os bigramas mais comuns que contenham as palavras do filtro
    for texto,qtd in bigramas_comuns:
        for k in texto:
            if k in filtro:
                print((texto, qtd))

    #Exibe todos os bigramas e suas frequências (desordenado)
    #for k, v in fdist.items():
    #    print (k,v)

arquivo.close()