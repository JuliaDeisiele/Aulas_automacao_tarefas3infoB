'''
Exercício 3
-------------------------------------------------------------
Crie um programa que execute repetidamente o programa do 
exercício 2. Após a apresentação do resultado o programa deve 
perguntar se o usuário deseja continuar a calcular, se a resposta
for S (Sim) o programa deve continuar se a resposta for N (Não) 
o programa deve terminar.
'''
while True:
    desejo = input("Deseja continuar? [S/N]")
    if desejo == "N":
        break
    else:
        n1 = float(input("digite o primeiro número:"))
        n2 = float(input("digite o segundo número:"))
        operador = input ("digite um operador matemático (+ - * /):")

        if operador =="+":
            resultado_soma = n1 + n2
            print("soma:", resultado_soma)

        elif operador =="-":
            resultado_sub = n1 - n2
            print("subitração:", resultado_sub)

        elif operador =="*":
            resultado_mult = n1 * n2
            print("multiplicação:", resultado_mult)

        else:
            resultado_div = n1 / n2
            print("divisão:", resultado_div)