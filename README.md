### 🔧README em construção...🔧 
# **Twitter toolbox**                                 [![DOI](https://zenodo.org/badge/488197084.svg)](https://zenodo.org/badge/latestdoi/488197084)
Este respositório contém uma série de ferramentas úteis (e relativamente simples para iniciantes) para se trabalhar com dados do Twitter. Os códigos foram escritos para um trabalho de análise de dados do Twitter (nessse caso, tweets), onde foi necessário minerar, organizar e limpar todo o material coletado.<br/>
Esse README está dividido em 4 partes: Mineração, Limpeza, Análise e Referências.<br/>
Cada uma das 3 primeiras partes conta com uma breve explicação dos códigos correspondentes, juntamente com citações das referências utilizadas na construção de cada um. E a última parte, contém todas as referências citadas ao longo do documento, condensadas em uma única seção.
## Mineração
A mineração de dados do Twitter se dá através uma conta de desenvolvedor e as chaves de acesso à API da plataforma. A aplicação para esse tipo de conta pode ser feita no site https://developer.twitter.com/ (use a sua conta do Twitter. E caso não tenha, é preciso criar uma).
Após ter acesso à sua conta de desenvolvedor, é preciso criar um App (dentro do portal do desenvolvedor), é através dele que você vai gerar as chaves e tokens necessários para o acesso aos dados.  <br/>
Irei deixar como recomendação esse vídeo do canal "AI Spectrum", que tem um bom tutorial tanto de como solicitar a conta de desenvolvedor, como também de coletar tweets usando Python: [How to get TWEETS by Python | Twitter API 2022](https://www.youtube.com/watch?v=Lu1nskBkPJU)        <br/><br/>
Existem níveis de acesso à API do Twitter, os quais tem permissões diferentes (como a quantidade de Tweets que você pode coletar, limitação na construção de consultas para a busca de tweets, qual o tipo de arquivo que você terá acesso, entre outros). Todas diferenças entre os níveis de acesso podem ser encontradas na [documentação da API do Twitter](https://developer.twitter.com/en/docs/twitter-api/getting-started/about-twitter-api).     
> OBS.: Todo o material utilizado está referenciado nesse README. Qualquer dúvida é só procurar na seção "Referências"
:)
## Referências
* [**API do Twitter**](https://developer.twitter.com/en/docs/twitter-api)
* [**tweepy**](https://www.tweepy.org/)
* [**NLTK**](https://www.nltk.org/)
* [**pandas**](https://pandas.pydata.org/docs/)
* [**re**](https://docs.python.org/pt-br/3/library/re.html)
* [**csv**](https://docs.python.org/pt-br/3/library/csv.html)
* [**string**](https://docs.python.org/pt-br/3/library/string.html )

