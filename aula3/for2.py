#Repetição simples: 10 vezes - de 0 a 9
print('Exemplo 1')
for i in range(0, 10):
    print(i, "Vezes")
    
#Repetição com passo <> 1: repete 5 vezes de 2 em dois 
print('\nExemplo 2')
for i in range(0, 10, 2):
    print(i, 'Número')

#Repetição decrescente
print('\nExemplo 3')
for i in range(10, 0, -1):
    print(i, 'Número')

#Repetição com listas
print('\nExemplo 4')
alunos = ['Júlia', 'Kayky', 'Inessa', 'Adriano']
for index, nome in enumerate (alunos):
    print(index, nome)