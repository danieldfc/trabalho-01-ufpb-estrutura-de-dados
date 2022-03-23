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
print('Lista 1 até 3')
lista.inserirInicio(3)
lista.inserirInicio(2)
lista.inserirInicio(1)
lista.imprimir()
print("O elemento anterior do 2 é:", lista.consultarAnterior(2))
