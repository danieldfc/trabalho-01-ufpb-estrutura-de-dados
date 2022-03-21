import Ldsec

lista = Ldsec.Ldsec()

lista.inserirInicio('C')
lista.inserirInicio('B')
lista.inserirInicio('A')
lista.inserirFim('D')
lista.inserirFim('E')

print('Primeiro elemento da lista A: ', lista.getFirstElement())
print('Ultimo elemento da lista E: ', lista.getLastElement())
print('Quantidade de elementos na lista : ', lista.getQuant())

lista.imprimir()

lista.removerInicio()
lista.imprimir()
lista.removerInicio()
lista.imprimir()
lista.removerFim()
lista.imprimir()
lista.removerFim()
lista.imprimir()