from itertools import count
from sre_constants import CATEGORY_UNI_NOT_SPACE


class No:
    def __init__(self, info, proximo):
        self.info = info
        self.prox = proximo


class Ldse:
    def __init__(self):
        self.prim = self.ult = None
        self.quant = 0

    def getQuant(self):
        return self.quant

    def getFirstElement(self):
        if not self.estaVazia():
            return self.prim.info

    def getLastElement(self):
        if not self.estaVazia():
            return self.ult.info

    def estaVazia(self):
        return self.quant == 0

    def inserirInicio(self, valor):
        if self.quant == 0:
            self.prim = self.ult = No(valor, None)
        else:
            self.prim = No(valor, self.prim)
        self.quant += 1

    def inserirFim(self, valor):
        if self.quant == 0:
            self.prim = self.ult = No(valor, None)
        else:
            self.ult.prox = self.ult = No(valor, None)
        self.quant += 1

    def inserirPosicao(self, valor, posicao):
        if not self.estaVazia():
            aux = ant = self.prim
            for i in range(self.quant+1):
                if posicao == 0:
                    self.inserirInicio(valor)
                    break
                else:
                    if i == posicao:
                        ant.prox = No(valor, aux)
                        self.quant += 1
                        if aux.prox == None:
                            self.ult = aux
                        break
                    ant = aux
                    aux = aux.prox

    def somarElementos(self):
        if not self.estaVazia():
            soma = 0
            aux = self.prim
            for i in range(self.quant):
                soma += aux.info
                aux = aux.prox
            return soma
        return 0

    def inserirApos(self, valor1, valor2):
        if not self.estaVazia():
            if self.quant == 1:
                if self.prim.info == valor1:
                    self.prim.prox = self.ult = No(valor2, None)
                    self.quant += 1
            else:
                print('TODO - Adicionar lógica se a lista tiver mais de 1 item')
                print('Forma de fazer:')
                print('- Criar o anterior e o auxiliar como sendo o primeiro elemento')
                print('- Criar um for sobre a quantidade de elementos')
                print('- Criar verificação de informação do elemento anterior seja igual ao valor1')
                print('  - Se for igual o próximo do anterior deverá receber No novo sendo o próximo o auxiliar')
                print('  - Se não alterar o valor do anterior = auxiliar e o auxiliar = o seu próximo element')

    def removerInicio(self):
        if self.quant == 1:
            self.prim = self.ult = None
        else:
            self.prim = self.prim.prox
        self.quant -= 1

    def removerFim(self):
        if self.quant == 1:
            self.prim = self.ult = None
        else:
            aux = self.prim
            while aux.prox != self.ult:
                aux = aux.prox
            aux.prox = None
            self.ult = aux
        self.quant -= 1

    def removerPosicao(self, posicao):
        if not self.estaVazia():
            aux = ant = self.prim
            if posicao == 0:
                self.removerInicio()
            else:
                for i in range(self.quant):
                    if i == posicao:
                        ant.prox = aux.prox
                        self.quant -= 1
                        break
                    ant = aux
                    aux = aux.prox

    def removerTodas(self, valor):
        if not self.estaVazia():
            if self.quant == 1:
                if self.prim.info == valor:
                    self.prim = self.ult = None
                    self.quant -= 1
            else:
                aux = ant = self.prim
                for i in range(self.quant):
                    if i == 0 and aux.info == valor:
                        self.removerInicio()
                        aux = ant = self.prim
                    else:
                        if aux.info == valor:
                            self.removerElemento(valor)
                        ant = aux
                        aux = aux.prox

    def removerElemento(self, valor):
        if self.quant == 1:
            if self.prim.info == valor:
                self.prim = self.ult = None
                self.quant -= 1
        else:
            aux = ant = self.prim
            while aux.prox != None and aux.info != valor:
                ant = aux
                aux = aux.prox
            if aux.info == valor:
                ant.prox = aux.prox
                if aux == self.prim:
                    self.prim = ant.prox
                if aux == self.ult:
                    self.ult = ant
                self.quant -= 1


    def imprimir(self):
        aux = self.prim
        while aux!= None:
            print(aux.info, end=' ')
            aux = aux.prox
        print()


    def contarPares (self):
        if not self.estaVazia ():
            aux = self.prim
            count = 0
            for i in range (self.quant):
                if aux.info % 2 == 0:
                    count += 1 
                aux = aux.prox
            return count
        else:
            return 0

