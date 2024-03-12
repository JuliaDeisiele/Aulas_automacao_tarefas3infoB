'''
Para utilizarmos as funções criadas em outros 
arquivos de código fonte devemos importa-las, para isso 
utilizamos o comando import ou from import 
'''
import funcoes 

base = float(input('Digite a base do triangulo: '))
altura = float(input('Digite a altura do triangulo: '))

area = funcoes.calcularAreaTriangulo(10,50)
print(area)