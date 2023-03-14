##FUNÇÕES DE LIMPEZA DE DADOS
#Referência: https://stackoverflow.com/questions/33404752/removing-emojis-from-a-string-in-python
import re
import string

#Remove os emojis do texto
def remove_emojis(data):
    emoj = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U00002500-\U00002BEF"  # chinese char
        u"\U00002702-\U000027B0"
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        u"\U0001f926-\U0001f937"
        u"\U00010000-\U0010ffff"
        u"\u2640-\u2642" 
        u"\u2600-\u2B55"
        u"\u200d"
        u"\u23cf"
        u"\u23e9"
        u"\u231a"
        u"\ufe0f"  # dingbats
        u"\u3030"
                      "]+", re.UNICODE)
    return re.sub(emoj, '', data)


#Realiza a limpeza da string
def limpa_str(x):
    x = x.lower()
    x = x.encode('utf-8','ignore').decode()
    x = remove_emojis(x)
    x = re.sub(r'https*\S+', ' ', x)
    x = re.sub(r'@\S+', ' ', x)
    x = re.sub(r'#\S+', ' ', x)
    x = re.sub(r'\'\w+', '', x)
    x = re.sub('[%s]' % re.escape(string.punctuation), ' ', x)
    x = re.sub(r'\w*\d+\w*', '', x)
    x = re.sub(r'\s{2,}', ' ', x)
    return x


#Stoplist
stoplist = ['a','á','à','ao','aos','aquela','àquela','aquelas','àquelas','aquele','àquele','aqueles',
'àqueles','aquilo','àquilo','as','às','até','com','como','da','daquela','daquele','das','de','dela',
'delas','dele','deles','depois','do','dos','e','é','ela','elas','ele','eles','em','entre','era',
'era','eram','éramos','essa','essas','esse','esses','esta','está','está','estamos','estão','estão',
'estas','estava','estavam','estávamos','este','esteja','estejam','estejamos','estes','esteve','estive',
'estivemos','estiver','estivera','estiveram','estivéramos','estiverem','estivermos','estivesse','estivessem',
'estivéssemos','estou','eu','foi','foi','fomos','for','fora','foram','foram','fôramos','forem',
'formos','fosse','fosse','fossem','fôssemos','fui','há','há','haja','hajam','hajamos','hão','havemos',
'havia','hei','houve','houvemos','houver','houvera','houverá','houveram','houvéramos','houverão',
'houverei','houverem','houveremos','houveria','houveriam','houveríamos','houvermos','houvesse',
'houvessem','houvéssemos','isso','isto','já','lhe','lhes','mais','mas','me','mesmo','meu','meus',
'minha','minhas','muito','na','não','nas','nem','nessa','nessas','nesse','nesses','nesta','nestas',
'neste','nestes','no','nos','nós','nossa','nossas','nosso','nossos','num','numa','o','os','ou','para',
'pela','pelas','pelo','pelos','por','qual','quando','que','quem','são','se','seja','seja','sejam','sejamos',
'sem','ser','será','será','serão','serei','seremos','seria','seriam','seríamos','seu','seus','só',
'somos','sou','sua','suas','também','te','tem','tem','tém','têm','temos','tenha','tenham','tenhamos',
'tenho','tenho','ter','terá','terão','terei','teremos','teria','teriam','teríamos','teu','teus','teve',
'tinha','tinha','tinham','tínhamos','tive','tivemos','tiver','tivera','tiveram','tivéramos','tiverem',
'tivermos','tivesse','tivessem','tivéssemos','tu','tua','tuas','um','uma','você','vocês','vos',
'vos','lo','la','los','las','ex','vai','vou','vem','tá','ein','ai','aí','ei','ô','q','ex','vc','1',
'2','3','4','5','6','7','8','9','x','10','pra','che','dá','ex1','to','etc','oh','voce','ta','br',
'porque','v','f','faz','eta','ih','po','ne','né','tr','então','após','pô','to','tô','ora','um','dois',
'três','quatro','cinco','seis','sete','oito','nove','dez','duas','in','eita','onze','doze','treze',
'quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte','ex','ir','vc','t','exa',
'desse','dessa','desses','dessas']
