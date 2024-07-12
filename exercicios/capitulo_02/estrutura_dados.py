#criação listas
lista_vazia = list()
numeros = [1, 2, 3, 4, 5]
lista_diferentes_tipos = [1, "hello", 3.14, True, [1, 2, 3]]

#checagem de comprimento das listas
comprimento_vazia = len(lista_vazia)
comprimento_numeros = len(numeros)
comprimento_lista_diferentes_tipos = len(lista_diferentes_tipos)

print('o comprimento da lista vazia é: ', comprimento_vazia)
print('o comprimento da lista de numeros é: ', comprimento_numeros)
print('o comprimento da lista de diferentes tipos é: ', comprimento_lista_diferentes_tipos)

#criação da tupla
minha_tupla = (1, 2, 3, 4, 5)

print('\n aqui começa a tupla que criei:\n')
print(minha_tupla[0])
print(minha_tupla[3])

#checagem de comprimento da tupla
comprimento_tupla = len(minha_tupla)

print('\nO comprimento da tuple é:', comprimento_tupla)

#criação de conjunto

meu_conjunto = {1, 2, 3, 4, 5}

#impressão do conjunto na tela
print('\n aqui está meu conjunto: \n', meu_conjunto)

#criação do dicionário
meu_dicionario = {'santos': 'neymar', 'corinthians': 'fenomeno', 'são paulo': 'kaka'}

escolha_dicionario = input('\nEscolha um time para ver seu idolo (santos, corinthians ,são paulo):')

if escolha_dicionario in meu_dicionario :
    valor_dicionario = meu_dicionario[escolha_dicionario]
    print(f"O idolo do time '{escolha_dicionario}'é: '{valor_dicionario}' ")
else:
    print('esse time ainda não foi inserido no dicionario.')