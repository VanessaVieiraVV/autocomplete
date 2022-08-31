'''1º - Seu trabalho é implementar funções de comparação de termos de consulta
(palavra e peso, cuja estrutura de dados está descrita em Palavra).
Você deve sobrecarregar o operador < para comparar dois objetos
da classe Palavra em ordem lexicográfica dos termos.
Além disso, você deve implementar uma função de comparação por prefixo, e por peso.
Essas funções devem retornar um inteiro negativo, zero,
ou positivo no caso do primeiro
parâmetro ser menor, igual ou maior que o segundo.'''

class Palavra:
    def __init__(self,termo="",peso=-1):
        self.termo = termo
        self.peso = peso
    

    def __lt__(self,other): #determina o comportamento do menor que (<)
        if self < other:
            True

    def __str__(self): #O valor "informal" como uma string.
        return "{0}, {1}".format(self.termo,self.peso)
    
    def __repr__(self): # A representação "oficial" como uma string
        return self.__str__()
   
def comparaPorPrefixo(palavra, prefixo):
    #palavra[0] eh o termo
    if palavra[0].startswith(prefixo):
        return 0
    elif palavra[0] < prefixo :
        return -1
    else :
        return 1    

def comparaPorPeso(palavra1, palavra2):
    #palavra[0] agora e o peso
    if palavra1[0] == palavra2[0] :
        return 0
    elif palavra1[0] < palavra2[0] :
        return -1
    else : #palavra[1] > palavra2[0]
        return 1

