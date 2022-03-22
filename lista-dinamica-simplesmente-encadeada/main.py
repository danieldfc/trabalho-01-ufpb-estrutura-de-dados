import Ldse

lista = Ldse.Ldse()

if not lista.estaVazia():
    lista.removerInicio()

lista.inserirInicio('C')
lista.inserirInicio('B')
lista.inserirInicio('A')
lista.inserirFim('D')
lista.inserirFim('E')
lista.inserirFim('F')
print('Lista completa: ')
lista.imprimir()

print('A é o primeiro elemento: ', lista.getFirstElement())
lista.removerInicio()
print('Lista completa B - F: ')
lista.imprimir()

lista.removerFim()
print('Lista completa B - E: ')
lista.imprimir()

lista.removerFim()
print('Lista completa B - D: ')

# lista.removerElemento('D')
# lista.removerElemento('C')
lista.inserirPosicao('A', 3)
lista.imprimir()