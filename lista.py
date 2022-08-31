''' Finalmente, as k consultas mais relevantes devem ser inseridas numa lista duplamente encadeada (classe Lista).
Você deve implementar as funções inserirOrdenado e removerFim.
O método inserirOrdenado deve inserir os elementos em ordem de acordo com a função de comparação passada como segundo parâmetro.
Você também deve implementar as funções que permitam imprimir uma lista usando as funções de saída disponíveis
(arquivo ou console).'''


    
class No:
    def __init__(self,item=None,ant=None,prox=None):
        self.item = item
        self.ant = ant
        self.prox = prox
class Lista :
    def __init__(self):
        self.primeiro = self.ultimo = No()
        self.tamanho = 0

    def size(self):
        return self.tamanho

    def inserirOrdenado(self, item, cmp):
        novo_no = No(item)
        anterior = self.primeiro 
        atual = self.primeiro.prox 
        while atual != None and cmp(atual.item, item) == 1: #atual > item
            anterior = atual 
            atual = atual.prox
            #lista sera percorrida ate "atual" ser < item
            #se chegar a None, significa que a lista chegou ao fim, e elemtno deve ser inserido na ultima posicao
            #entao o programa vai entrar no if
        if atual == None : #inserirnofim
            anterior.prox = novo_no
            novo_no.ant = anterior
            novo_no.prox= atual 
            self.ultimo = novo_no
            self.tamanho += 1
            return #pra sair da funçao para que nao execute o restante dos comandos
        atual.ant = novo_no
        novo_no.prox = atual
        anterior.prox = novo_no
        novo_no.ant = anterior
        while atual.prox != None : #garante que self.ultimo realmente sera o ultimo elemento
            anterior = atual 
            atual = atual.prox
        self.ultimo = atual 
        self.tamanho += 1 
    def removerFim(self): #fazer que remova até lista duplamente encadeada fique do tamanho de Qtd
        aux = self.ultimo.ant
        aux.prox = self.ultimo.prox
        self.ultimo.ant = None
        self.ultimo = aux
        self.tamanho -= 1
            

    def __str__(self):
        string_gigante = ""
        tmp = self.primeiro.prox 
        while not tmp is None : #enquanto tmp != None
            string_gigante = string_gigante + tmp.item[1] + "\n"
            tmp = tmp.prox 
        return string_gigante
    
    def __repr__(self):
        return str(self)
