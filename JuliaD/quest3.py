'''Crie um programa que imprime uma tabuada. O programa deve solicitar
que o usuário informe um número para gerar a tabuada. Utilizando um
laço de repetição, o programa deve gerar a tabuada do número
fornecido de 0 a 100.'''

num = (input ('Informe um número para gerar a tabuada: '))
i = 0
for i in range(0, 100):
    mult = (num * i)
    print(num,"*", i,"=", mult)
    i = i + 1