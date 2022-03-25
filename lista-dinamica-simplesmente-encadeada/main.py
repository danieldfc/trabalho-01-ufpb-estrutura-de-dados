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

print('Lista completa A - D: ')
# lista.removerElemento('D')
# lista.removerElemento('C')
lista.inserirPosicao('A', 0)
lista.imprimir()
lista.removerPosicao(3)
print('Lista completa A - C: ')
lista.imprimir()
lista.inserirPosicao('B', 0)
print('Lista completa B - A - B - C: ')
lista.imprimir()
print('Lista completa B - B - C: ')
lista.removerTodas('A')
lista.imprimir()
lista.removerTodas('B')
lista.removerTodas('C')
print('Remove todos os elementos')

print('Adiciona 1 - 2 - 3 - 4')
lista.inserirInicio(3)
lista.inserirInicio(2)
lista.inserirInicio(1)
lista.imprimir()
print('A soma de todos os elementos da lista:', lista.somarElementos())

print('Adiciona 1 - 2 - 3 - 4')
lista.inserirApos(3, 4)
lista.imprimir()
print('A soma de todos os elementos da lista:', lista.somarElementos())
print('Quantidade de números pares da lista:', lista.contarPares())