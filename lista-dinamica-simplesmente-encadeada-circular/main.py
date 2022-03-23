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

lista.inserirFim('E')
lista.trocar(5, 'F')
print('Lista A até F')
lista.imprimir()
lista.removerFim()
lista.removerFim()
lista.removerFim()
lista.removerFim()
lista.removerFim()
lista.removerFim()
print('Remove todos os elementos')

## Somar elementos numéricos

print('Adiciona 1 - 2 - 3')
lista.inserirInicio(3)
lista.inserirInicio(2)
lista.inserirInicio(1)
print('Lista 1 - 2 - 3')
lista.imprimir()
print('A soma de todos os elementos da lista é:', lista.somarElementos())
