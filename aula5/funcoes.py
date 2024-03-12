'''
As funções são utilizadas para modularizar o código, ou seja, dividi-lo em partes menores, que podem ser reutilizadas.

Estrutura:

def nome_funcao(param1,param2):
    faz algo
    return valor

Exemplos:
'''
#função1
def somar(n1, n2):
    resultado = n1 + n2
    return resultado

#função2
def login(usuario, senha):
    if usuario == "adimin" and senha == '123':
        return True
    else:
        return False 

#função3 
def calcularAreaTriangulo(base, altura):
    area = (base * altura) / 2
    return area

#chamar função
#print (login('ivan', '123'))
#area = calcularAreaTriangulo (100,50) 
#print('A área do triângulo é', area)