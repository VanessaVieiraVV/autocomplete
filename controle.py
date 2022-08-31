from palavra import *
from lista import Lista
''' Você também deve implementar a classe Controle, que é responsável por fornecer as funcionalidades de carregarDados
e find para carregar o arquivo de consultas e ordená-las (OK), e encontrar a lista de sugestões que casam
com o prefixo informado.
Você também deve implementar dois métodos privados, firstIndexOf e lastIndexOf que
retornam as posições da primeira e última consultas que possuem o prefixo desejado. Essas funções devem ser
usadas para encontrar a parte do vetor de consultas que deve ser processado para encontrar as k consultas mais
relevantes. '''

class Controle:
    def __init__(self):
        self.numeroTermos = 0  
        self.termos = list()
        self.dadosCarregados = True
    
    def __apagarTermos(self):
        self.termos = []
        self.numeroTermos = 0
        self.dadosCarregados = False
    

    def __firstIndexOf(self, prefixo):
        inicio = 0
        fim = self.numeroTermos-1 #numeroTermos eh uma variavel gerada em carregarDados(), com a primeira linha do arquivo.txt
        pos = -1
        while inicio <= fim:
            meio = (inicio+fim)//2
            if meio > -1:
                retorno = comparaPorPrefixo(self.termos[meio], prefixo)
            if retorno == 0 : #se palavra tem o prefixo
                if meio > 0 and comparaPorPrefixo(self.termos[meio-1], prefixo) == 0: #se a palavra anterior tambem tem o prefixo
                    fim = meio - 1 # busca binaria vai ser feita na primeira metade
                else : #se palavra anterior nao tem o prefixo,
                    pos = meio #significa que o firstIndex foi encontrado
                    return pos
            elif retorno == -1 : #se palavra for < prefixo
                if inicio < fim : #pra nao ultrapassar o fim da lista
                    inicio = meio + 1 #busca binaria sera feita na segunda metade
                else: #se inicio == fim, entao eh porque a lista chegou ao final
                    return pos #return -1
            elif retorno == 1 : #se palavra > prefixo
                if fim > inicio and meio > 0: #pra nao ultrapassar o começo da lista
                    fim = meio - 1 #busca binaria sera feita na primeira metade
                else: #se fim == inicio, eh porque lista chegou ao começo
                    return pos #return -1
    def __lastIndexOf(self, prefixo):
        inicio = 0
        fim = self.numeroTermos-1 
        pos = -1
        while inicio <= fim:
            meio = (inicio+fim)//2
            retorno = comparaPorPrefixo(self.termos[meio], prefixo)
            if retorno == 0 : #se palavra tem o prefixo
                #pra nao ultrapassar o ultimo elemento da lista
                if meio < self.numeroTermos-2 and comparaPorPrefixo(self.termos[meio+1], prefixo) == 0: #se palavra seguinte tambem tem o prefixo
                    inicio = meio + 1 #busca binaria sera realizad na segunda metada
                else : #se a proxima palavra nao tem o prefixo,
                    pos = meio #significa que o lastIndex foi encontrado
                    return pos
            elif retorno == -1: #se palavra for < prefixo
                if inicio < fim : #pra nao ultrapassar o fim da lista
                    inicio = meio + 1 #busca binaria sera feita na segunda metade
                else: #se inicio == fim, entao eh porque a lista chegou ao final
                    return pos #return -1
            elif retorno == 1 : #se palavra > prefixo
                if fim > inicio and meio > 0: #pra nao ultrapassar o começo da lista
                    fim = meio - 1 #busca binaria sera feita na primeira metade
                else: #se fim == inicio, eh porque lista chegou ao começo
                    return pos #return -1

    def carregarDados(self,filename):
        if self.dadosCarregados:
            self.__apagarTermos()
        arquivo = open(filename,"r", encoding="utf8")
        arquivo = arquivo.readlines()      
        self.numeroTermos = int(arquivo.pop(0).strip("\n")) #guarda o primeiro termo do arquivo, que eh a quantidade de palavras'''
        import string
        numeroTermos = arquivo.pop(0).strip("\n")
        safe_chars = string.ascii_letters + string.digits + ' '
        for item in arquivo:
                item = item.strip().lower()
                item = item.split("\t")
                item[1] = ''.join([char if char in safe_chars else '' for char in item[1]])
                self.termos.append((item[1], (item[0]))) #termos == [ (palavra, peso), (palavra, peso), ... ]
        self.termos.sort() #ordena em ordem lexicografica
        self.dadosCarregados = True
        
    def find(self, prefixo, qtd):
        lista_de_sugestoes = list() #lista simples onde serao guardadas TODAS as ocorrencias que tem o prefixo em ordem lexicografica
        indice = self.__firstIndexOf(prefixo)
        ultimoIndice = self.__lastIndexOf(prefixo)
        if indice != None and ultimoIndice != None:
            if indice > -1 and ultimoIndice > -1:
                while indice <= ultimoIndice :
                    lista_de_sugestoes.append(self.termos[indice])
                    indice = indice + 1 #incrementa a variavel para que o laço possa percorrer a lista completa
                lista_de_sugestoes.append(self.termos[ultimoIndice])
        print("FIRST_INDEX:", self.__firstIndexOf(prefixo)) #TESTE#
        print("LAST_INDEX:", self.__lastIndexOf(prefixo))
        #print("LISTA DE SUGESTOES:")
        lista_ordenada_por_peso = list() #lista simples onde serao guardadas TODAS as ocorrencias que tem o prefixo em ordem de peso
        for item in lista_de_sugestoes :
            lista_ordenada_por_peso.append((item[1], item[0])) # == [ (peso, palavra), (peso, palavra), ... ] 
        lista_ordenada_por_peso.sort(reverse=True) #ordena em ordem descrescente
        ocorrencias_mais_relevantes = list()
        #lista simples onde sera inserida so a quantidade certa de sugestoes, sendo desnecessario o uso da funçao removerFim()na lista duplamente encadeada que sera originada a partir desta
        for item in lista_ordenada_por_peso: 
            if len(ocorrencias_mais_relevantes) < qtd :
                ocorrencias_mais_relevantes.append(item)
        lista_dup_encadeada = Lista() #sera criada de acordo com implementaçao da classe Lista()
        for item in ocorrencias_mais_relevantes: 
            lista_dup_encadeada.inserirOrdenado(item, comparaPorPeso) #vai inserindo cada ocorrencia da lista ordenadamente
            #eh inserido na lista duplamente encadeada TUDO o que esta na lista_de_sugestoes
        if lista_dup_encadeada.ultimo.item == None: 
            return "" #limpa a tela caso seja acrescentado um caractere no prefixo que nao esteja nas palavras apresentadas na tela
        '''if lista_dup_encadeada.ultimo.item != None:
            palavra = lista_dup_encadeada.ultimo.item
            if comparaPorPrefixo(palavra, prefixo) != 0 :
                lista_dup_encadeada.removerFim()
        else:
            palavra = lista_dup_encadeada.ultimo.ant.item
            if comparaPorPrefixo(palavra, prefixo) != 0 :
                lista_dup_encadeada.removerFim()'''
        '''while lista_dup_encadeada.size() > qtd : #vai removendo os itens ate que a lista fique so com as k ocorrencias mais relevantes
            lista_dup_encadeada.removerFim()'''
            
        return lista_dup_encadeada



    

