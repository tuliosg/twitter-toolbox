import tweepy
import pandas as pd
import config

#Autenticação dos tokens/keys
client = tweepy.Client(config.bearer_token)

##FILTROS DE CONSULTA
# Insira palavras-chaves -> É possível utilizar operadores lógicos, com OR sendo "ou" e " " (um espaço em branco) sendo "e"
# Alguns outros filtros podem ser utilizados nessa consulta (query), como idioma, tipo do tweet, elementos presentes e etc...
consulta = "(palavra-chave1 OR palavra-chave2 OR palavra-chave3) lang:pt -is:retweet -has:media"

#Data limite da coleta (Formato ISO 8601/RFC 3339)
#Exemplo de data: ["2022-03-14T23:59:00.00z"]
data_fim = ["AAAA-MM-DDTHH:MM:SS.ssz"]

#Número de resultados (máximo por consulta na conta "Elevated Access" -> 100 tweets)
num_resultados = 100

#Campos -> acessa os dados
fields = ["created_at", "author_id"]

#Expansões dos campos -> acessa os dados relacionados aos campos
exp = ["author_id"]


##BUSCANDO TWEETS
#Busca por tweets recentes (últimos 7 dias) utilizando filtros de consulta
resultados = client.search_recent_tweets(query = consulta, max_results = num_resultados, tweet_fields = fields, expansions = exp, end_time = data_fim)

#Coleta os dados dos usuários (@ e nome)
users = {u["id"]: u for u in resultados.includes["users"]}

#Permite visualizar os dados no terminal
#for tweet in resultados.data:
#    if users[tweet.author_id]:
#        user = users[tweet.author_id]
#        print(tweet.created_at, user.username, user.name, tweet.text)


##GERANDO ARQUIVO .csv COM OS DADOS
#Nome das colunas no dataframe
colunas = ["Data", "Usuário", "Nome", "Tweet"]

#Dados que serão adicionados nas linhas do dataframe
dados = []

#Adiciona os dados coletados na lista "dados"
for tweet in resultados.data:
    if users[tweet.author_id]:
        user = users[tweet.author_id]
        dados.append([tweet.created_at, user.username, user.name, tweet.text])

#Criação do data frame
data_frame = pd.DataFrame(dados, columns = colunas)

#Gerando .csv através do data frame
data_frame.to_csv("Dados-Twitter.csv", encoding="UTF-8")
