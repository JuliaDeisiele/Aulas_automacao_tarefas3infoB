#While
'''
repete enquanto uma condição for verdadeira
'''

print ('\nExemplo 1:')
i = 0
while i < 5:
    print(i, 'vezes')
    i= i + 1

print ('\nExemplo 2:')
nomes = []
while True:
    nome = input ('Digite um nome:\n')
    nomes.append(nome) #Pega o nome digitado e adciona na lista nomes
    if (nome == "fim"):
        print(nomes)
        break